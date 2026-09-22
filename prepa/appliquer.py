#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Injecte les contrats de seance de prepa/contrats.md dans le calendrier FUF.

Publie TOUS les blocs du fichier. Ce qui est dans contrats.md est dans le
calendrier : pas de fenetre, pas de surprise. Une semaine de contrats devient
visible des que tu la deposes, et tu vois venir les seances suivantes.

Le fichier est modifie chirurgicalement : les UID sont conserves a l'identique,
SEQUENCE n'est incremente que si le texte change reellement, et l'encodage
(ASCII, CRLF, pliage a 75 octets) est celui du calendrier d'origine.

Idempotent : deux executions de suite ne produisent aucun second changement.

Usage :  python prepa/appliquer.py [--fenetre N] [--date AAAA-MM-JJ] [--verifier]
"""

import argparse
import datetime
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTRATS = os.path.join(RACINE, 'prepa', 'contrats.md')
CALENDRIER = os.path.join(RACINE, 'X_FUF_2027_complet.ics')

EN_TETE = re.compile(r'^@@\s+(\d{4}-\d{2}-\d{2})\s+(\S+)\s*$')


# --------------------------------------------------------------- lecture du plan
def lire_contrats(chemin):
    """Retourne [(date, uid, titre ou None, corps)] dans l'ordre du fichier."""
    blocs, courant = [], None
    with open(chemin, encoding='utf-8') as f:
        for brute in f:
            ligne = brute.rstrip('\n')
            m = EN_TETE.match(ligne)
            if m:
                if courant:
                    blocs.append(courant)
                courant = {'date': datetime.date.fromisoformat(m.group(1)),
                           'uid': m.group(2), 'titre': None, 'lignes': []}
            elif courant is None:
                continue                      # commentaires d'en-tete du fichier
            elif ligne.startswith('!titre:') and not courant['lignes']:
                courant['titre'] = ligne[len('!titre:'):].strip()
            else:
                courant['lignes'].append(ligne)
    if courant:
        blocs.append(courant)

    sortie = []
    for b in blocs:
        corps = '\n'.join(b['lignes']).strip('\n')
        if not corps:
            raise SystemExit('Bloc vide pour %s (%s)' % (b['uid'], b['date']))
        sortie.append((b['date'], b['uid'], b['titre'], corps))
    return sortie


# ------------------------------------------------------------------ iCalendar
def deplier(texte):
    lignes = []
    for ligne in texte.split('\r\n'):
        if ligne[:1] in (' ', '\t') and lignes:
            lignes[-1] += ligne[1:]
        else:
            lignes.append(ligne)
    return lignes


def plier(ligne):
    b = ligne.encode('utf-8')
    if len(b) <= 73:
        return [ligne]
    morceaux, cur, reste = [], b[:73], b[73:]
    while cur and (cur[-1] & 0xC0) == 0x80:
        reste = bytes([cur[-1]]) + reste
        cur = cur[:-1]
    morceaux.append(cur.decode('utf-8'))
    while reste:
        bout, reste = reste[:72], reste[72:]
        while bout and (bout[-1] & 0xC0) == 0x80:
            reste = bytes([bout[-1]]) + reste
            bout = bout[:-1]
        morceaux.append(' ' + bout.decode('utf-8'))
    return morceaux


def echapper(t):
    return (t.replace('\\', '\\\\').replace(';', '\\;')
             .replace(',', '\\,').replace('\n', '\\n'))


# ----------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--date', help='simuler une autre date du jour')
    ap.add_argument('--fenetre', type=int, metavar='N',
                    help="ne publier que les blocs dont la date est <= aujourd'hui + N "
                         "(par defaut : tout est publie)")
    ap.add_argument('--tout', action='store_true',
                    help='conserve pour compatibilite ; publier tout est deja le defaut')
    ap.add_argument('--verifier', action='store_true',
                    help="n'ecrit rien, signale seulement ce qui changerait")
    args = ap.parse_args()

    aujourdhui = (datetime.date.fromisoformat(args.date) if args.date
                  else datetime.date.today())

    plan = lire_contrats(CONTRATS)
    if args.fenetre is None:
        a_publier = {uid: (titre, corps) for _, uid, titre, corps in plan}
    else:
        limite = aujourdhui + datetime.timedelta(days=args.fenetre)
        a_publier = {uid: (titre, corps) for d, uid, titre, corps in plan
                     if d <= limite}
    if not a_publier:
        print('Rien a publier au %s.' % aujourdhui)
        return 0

    with open(CALENDRIER, encoding='utf-8', newline='') as f:
        lignes = deplier(f.read())

    sortie, bloc, dans_ev = [], [], False
    vus, modifies = set(), []

    for ligne in lignes:
        if ligne == 'BEGIN:VEVENT':
            dans_ev, bloc = True, [ligne]
            continue
        if not dans_ev:
            sortie.append(ligne)
            continue
        bloc.append(ligne)
        if ligne != 'END:VEVENT':
            continue

        dans_ev = False
        uid = next((l[4:] for l in bloc if l.startswith('UID:')), None)
        if uid not in a_publier:
            sortie.extend(bloc)
            continue

        vus.add(uid)
        titre, corps = a_publier[uid]
        desc_voulue = 'DESCRIPTION:' + echapper(corps)
        titre_voulu = 'SUMMARY:' + echapper(titre) if titre else None

        change = any(
            (l.startswith('DESCRIPTION:') and l != desc_voulue) or
            (titre_voulu and l.startswith('SUMMARY:') and l != titre_voulu)
            for l in bloc)
        if not any(l.startswith('DESCRIPTION:') for l in bloc):
            change = True

        if not change:
            sortie.extend(bloc)
            continue

        modifies.append(uid)
        neuf, a_desc = [], False
        for l in bloc:
            if l.startswith('DESCRIPTION:'):
                neuf.append(desc_voulue)
                a_desc = True
            elif titre_voulu and l.startswith('SUMMARY:'):
                neuf.append(titre_voulu)
            elif l.startswith('SEQUENCE:'):
                neuf.append('SEQUENCE:%d' % (int(l.split(':', 1)[1]) + 1))
            elif l == 'END:VEVENT':
                if not a_desc:
                    neuf.append(desc_voulue)
                neuf.append(l)
            else:
                neuf.append(l)
        if not any(l.startswith('SEQUENCE:') for l in neuf):
            neuf.insert(1, 'SEQUENCE:1')
        sortie.extend(neuf)

    introuvables = sorted(set(a_publier) - vus)
    if introuvables:
        sys.stderr.write('UID absents du calendrier : %s\n' % ', '.join(introuvables))
        return 1

    if args.verifier:
        print('%d seance(s) seraient mises a jour.' % len(modifies))
        return 0

    if not modifies:
        print('Calendrier deja a jour au %s.' % aujourdhui)
        return 0

    pliees = []
    for l in sortie:
        if l:
            pliees.extend(plier(l))
    with open(CALENDRIER, 'w', encoding='utf-8', newline='') as f:
        f.write('\r\n'.join(pliees) + '\r\n')

    print('%d seance(s) mises a jour au %s.' % (len(modifies), aujourdhui))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
