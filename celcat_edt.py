#!/usr/bin/env python3
"""
celcat_edt.py — Récupère l'emploi du temps d'un groupe sur CELCAT (Université de
Bordeaux) et l'écrit dans un fichier .ics importable dans Calendrier Apple.

CELCAT Bordeaux ne publie pas de flux ICS par groupe : seul le flux personnel
(https://celcat.u-bordeaux.fr/ICalFeed/) existe. Ce script interroge la même API
que la page web du planning et fabrique le .ics lui-même.

Prérequis :  python3 -m pip install requests

Usage :

  1) Chercher l'identifiant de ton groupe :
       python3 celcat_edt.py --chercher "MI"
       python3 celcat_edt.py --chercher "L3"

  2) Générer le calendrier (les dates sont optionnelles) :
       python3 celcat_edt.py --groupe "L3 MI - Groupe A" \
                             --debut 2026-09-01 --fin 2027-07-31 \
                             --sortie edt.ics

  3) Ouvrir edt.ics (double-clic sur Mac) et l'importer dans Calendrier.
     Crée d'abord un calendrier dédié "Cours" pour pouvoir tout effacer
     d'un coup à la prochaine génération.

Le fichier produit est un instantané, pas un abonnement : relance le script
quand l'emploi du temps change (typiquement au changement de semestre).
"""

import argparse
import html
import re
import sys
import time
import unicodedata
from datetime import datetime, date, timedelta

try:
    import requests
except ImportError:
    sys.exit("Il manque la librairie requests :  python3 -m pip install requests")

BASE = "https://celcat.u-bordeaux.fr/calendar"

# CELCAT numérote ses types de ressources. Le type « Groupes » n'est pas le même
# selon les déploiements, donc on les essaie tous et on garde ce qui répond.
RES_TYPES = [103, 104, 100, 101, 102, 105, 106]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": f"{BASE}/",
}


def _session():
    s = requests.Session()
    s.headers.update(HEADERS)
    s.get(f"{BASE}/", timeout=30)  # récupère les cookies de session
    return s


def _norm(s):
    """minuscule sans accents, pour comparer des noms de groupes."""
    s = unicodedata.normalize("NFD", s or "")
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", s).strip().lower()


def chercher(sess, terme, types=None):
    """Renvoie [(res_type, id, dept), ...] pour les ressources qui matchent."""
    cible = _norm(terme)
    trouve, vus = [], set()
    for rt in types or [103]:
        page, lus, total = 1, 0, None
        while page <= 300:  # garde-fou
            r = sess.post(
                f"{BASE}/Home/ReadResourceListItems",
                data={
                    "myResources": "false",
                    "searchTerm": "%",
                    "pageSize": "200",
                    "pageNumber": str(page),
                    "resType": str(rt),
                },
                timeout=30,
            )
            if r.status_code != 200:
                break
            try:
                payload = r.json()
            except ValueError:
                break
            if isinstance(payload, dict):
                items = payload.get("results") or []
                total = payload.get("total", total)
            else:
                items = payload or []
            if not items:
                break
            lus += len(items)
            for it in items:
                rid = (it.get("id") or "").strip()
                if not rid or cible not in _norm(rid):
                    continue
                cle = (rt, rid)
                if cle in vus:
                    continue
                vus.add(cle)
                trouve.append((rt, rid, it.get("dept")))
            print(f"  ... {lus} ressources parcourues", end="\r", file=sys.stderr)
            # le serveur peut renvoyer moins que pageSize : on compte ce qu'on a lu.
            if total is not None and lus >= total:
                break
            page += 1
        print(" " * 40, end="\r", file=sys.stderr)
    return trouve


class SourceInjoignable(Exception):
    """CELCAT n'a pas repondu : panne passagere, pas une erreur de configuration."""


def _tranche(sess, res_type, fid, debut, fin, essais=4):
    """Une requete, reessayee avec attente croissante en cas de timeout."""
    derniere = None
    for n in range(essais):
        try:
            r = sess.post(
                f"{BASE}/Home/GetCalendarData",
                data={
                    "start": debut,
                    "end": fin,
                    "resType": str(res_type),
                    "calView": "month",
                    "federationIds[]": fid,
                    "colourScheme": "3",
                },
                timeout=120,
            )
            r.raise_for_status()
            return r.json()
        except Exception as exc:
            derniere = exc
            if n < essais - 1:
                attente = 10 * 2 ** n  # 10 s, 20 s, 40 s
                print(f"    {debut} -> {fin} : {type(exc).__name__}, "
                      f"nouvel essai dans {attente} s", file=sys.stderr)
                time.sleep(attente)
    raise SourceInjoignable(f"{debut} -> {fin} : {derniere}")


def evenements(sess, res_type, fid, debut, fin, jours=45):
    """Recupere l'annee par tranches : une grosse requete fait tomber CELCAT."""
    d0 = date.fromisoformat(debut)
    d1 = date.fromisoformat(fin)
    tout, vus = [], set()
    d = d0
    while d <= d1:
        f = min(d + timedelta(days=jours - 1), d1)
        for e in _tranche(sess, res_type, fid, d.isoformat(), f.isoformat()):
            cle = (e.get("id"), e.get("start"))
            if cle in vus:
                continue
            vus.add(cle)
            tout.append(e)
        print(f"  {d} -> {f} : {len(tout)} evenements cumules", file=sys.stderr)
        d = f + timedelta(days=1)
    return tout


# --- fabrication du .ics -----------------------------------------------------

VTIMEZONE = """BEGIN:VTIMEZONE
TZID:Europe/Paris
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE"""


def esc(t):
    return (
        (t or "")
        .replace("\\", "\\\\")
        .replace(";", "\\;")
        .replace(",", "\\,")
        .replace("\n", "\\n")
    )


def plier(ligne):
    """RFC 5545 : 75 octets par ligne max."""
    out, courant = [], ""
    for ch in ligne:
        if len((courant + ch).encode("utf-8")) > 73:
            out.append(courant)
            courant = " " + ch
        else:
            courant += ch
    out.append(courant)
    return "\r\n".join(out)


def depiler_description(brut):
    """La description CELCAT est du HTML : <br /> sépare module, prof, salle, groupe."""
    txt = re.sub(r"<br\s*/?>", "\n", brut or "", flags=re.I)
    txt = re.sub(r"<[^>]+>", "", txt)
    lignes = [html.unescape(l).strip() for l in txt.split("\n")]
    return [l for l in lignes if l]


def horodatage(s):
    """'2026-09-01T08:00:00' -> '20260901T080000'"""
    return datetime.fromisoformat(s[:19]).strftime("%Y%m%dT%H%M%S")


def construire_ics(events, nom_groupe):
    stamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    L = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//celcat_edt.py//FR",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        f"X-WR-CALNAME:{esc(nom_groupe)}",
        "X-WR-TIMEZONE:Europe/Paris",
        VTIMEZONE,
    ]
    n = 0
    for i, e in enumerate(events):
        if not e.get("start"):
            continue
        lignes = depiler_description(e.get("description"))
        categorie = (e.get("eventCategory") or "").strip()
        modules = e.get("modules") or []
        sites = e.get("sites") or []

        titre = (modules[0] if modules else (lignes[0] if lignes else "Cours")).strip()
        if categorie:
            titre = f"{titre} — {categorie}"
        salle = ", ".join(s.strip() for s in sites if s) or ""

        uid = e.get("id") or f"{i}-{e['start']}"
        L += [
            "BEGIN:VEVENT",
            plier(f"UID:{esc(str(uid))}@celcat.u-bordeaux.fr"),
            f"DTSTAMP:{stamp}",
            f"DTSTART;TZID=Europe/Paris:{horodatage(e['start'])}",
            f"DTEND;TZID=Europe/Paris:{horodatage(e.get('end') or e['start'])}",
            plier(f"SUMMARY:{esc(titre)}"),
        ]
        if salle:
            L.append(plier(f"LOCATION:{esc(salle)}"))
        if lignes:
            L.append(plier(f"DESCRIPTION:{esc(chr(10).join(lignes))}"))
        L.append("END:VEVENT")
        n += 1
    L.append("END:VCALENDAR")
    return "\r\n".join(L) + "\r\n", n


def main():
    p = argparse.ArgumentParser(description="CELCAT Bordeaux -> fichier .ics")
    p.add_argument("--chercher", help="chercher un groupe par nom, puis s'arrêter")
    p.add_argument("--groupe", help="identifiant exact du groupe (federation id)")
    p.add_argument("--type", type=int, help="resType CELCAT, si tu le connais déjà")
    p.add_argument(
        "--tous-types",
        action="store_true",
        help="chercher dans tous les types de ressources (plus lent)",
    )
    p.add_argument("--debut", default=f"{date.today().year}-09-01")
    p.add_argument("--fin", default=f"{date.today().year + 1}-07-31")
    p.add_argument("--sortie", default="edt.ics")
    a = p.parse_args()

    sess = _session()

    if a.chercher:
        types = [a.type] if a.type else (RES_TYPES if a.tous_types else [103])
        res = chercher(sess, a.chercher, types)
        if not res:
            sys.exit(
                f"Aucune ressource ne contient « {a.chercher} ». "
                "Essaie un terme plus court, ou ajoute --tous-types."
            )
        print(f"{len(res)} correspondance(s) :\n")
        for rt, rid, dept in res:
            print(f'  --type {rt}  --groupe "{rid}"' + (f"   [{dept}]" if dept else ""))
        return

    if not a.groupe:
        p.error("donne --chercher pour explorer, ou --groupe pour générer le .ics")

    types = [a.type] if a.type else RES_TYPES
    events, injoignable = [], None
    for rt in types:
        try:
            events = evenements(sess, rt, a.groupe, a.debut, a.fin)
        except SourceInjoignable as exc:
            injoignable = exc
            print(f"  resType {rt} : {exc}", file=sys.stderr)
            continue
        except Exception as exc:
            print(f"  resType {rt} : {exc}", file=sys.stderr)
            continue
        if events:
            print(f"resType {rt} : {len(events)} évènements.")
            break

    if not events:
        if injoignable:
            # Code 2 : CELCAT n'a pas repondu. Le workflow le traite comme un
            # incident passager et garde le fichier precedent, sans echouer.
            print(f"CELCAT injoignable : {injoignable}", file=sys.stderr)
            sys.exit(2)
        sys.exit(
            "Aucun évènement. Vérifie l'identifiant du groupe (--chercher) "
            "et la plage de dates."
        )

    ics, n = construire_ics(events, a.groupe)
    with open(a.sortie, "w", encoding="utf-8", newline="") as f:
        f.write(ics)
    print(f"{n} cours écrits dans {a.sortie}")


if __name__ == "__main__":
    main()
