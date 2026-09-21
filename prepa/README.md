# prepa/ - contrats de seance

## A quoi ca sert

Le calendrier `X_FUF_2027_complet.ics` porte les horaires. Ce dossier porte le
CONTENU de chaque seance : quoi reconstruire, quels exercices, quel critere de
fin. Le contrat du jour arrive dans le commentaire de l'evenement, sur le
telephone, sans rien faire.

## Les trois fichiers

| Fichier | Role |
|---|---|
| `contrats.md` | le plan : un bloc par seance, en-tete `@@ AAAA-MM-JJ UID` |
| `etat.md` | texte libre, ou tu notes le soir ou tu en es |
| `appliquer.py` | injecte les contrats echus dans le `.ics` |

## Quand ca tourne

`.github/workflows/prepa.yml` s'execute chaque matin vers 6h10, juste apres la
mise a jour CELCAT. Il publie les blocs dont la date est <= demain : le contrat
du jour est en place au reveil, celui du lendemain est visible des le soir.

Il tourne aussi a chaque modification de `prepa/`, donc un contrat corrige est
en ligne dans la minute.

Aucun token, aucun secret : GitHub fournit le droit d'ecriture au job le temps
de son execution, comme pour `edt.yml`.

## Modifier un contrat a la main

Ouvre `contrats.md`, edite le bloc, commit. C'est tout. Contraintes :

- l'en-tete d'un bloc est exactement `@@ AAAA-MM-JJ UID`, sans rien d'autre ;
- l'UID doit exister dans le `.ics` (sinon le job echoue en le disant) ;
- une ligne `!titre:` juste apres l'en-tete remplace aussi le titre de
  l'evenement ;
- pas d'accents : tout le calendrier est en ASCII.

## Essayer sans rien casser

    python prepa/appliquer.py --verifier            # dit ce qui changerait
    python prepa/appliquer.py --date 2026-10-05     # simule une autre date
    python prepa/appliquer.py --tout                # publie tout le plan

Le script est idempotent : deux executions de suite ne produisent aucun second
changement, et `SEQUENCE` n'est incremente que si le texte change vraiment.
Les UID ne bougent jamais, donc l'agenda met a jour au lieu de dupliquer.
