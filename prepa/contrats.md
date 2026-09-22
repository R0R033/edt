# Contrats de seance
#
# Un bloc par seance. En-tete : @@ AAAA-MM-JJ UID
# Ligne !titre: juste apres l'en-tete = remplace aussi le titre de l'evenement.
# Tout le reste jusqu'au prochain @@ devient le commentaire de l'evenement.
# Publie par .github/workflows/prepa.yml le jour meme (et la veille au soir).
# Fichier ASCII : pas d'accents, comme le reste du calendrier.

@@ 2026-09-22 abcd143f2ebe5f00c7cbdd3a0adc1817@fuf-romain
Fonctions numeriques | Calculs algebriques et trigonometrie

CONTRAT DU JOUR - Deschamps ch. 3, puis debut du ch. 4
Fin de seance = 4 resultats reecrits sans notes + 3 exercices cherches + 1 oral de 5 min.
C'est ce compte qui dit si la seance est faite, pas le nombre de pages tournees.

SEGMENT 1  14h00-14h50  -  inegalites et valeur absolue
Lecture 25 min, montre en main, crayon a la main (ch. 3, la partie sur les inegalites dans R). Tu as deja lu une dizaine de pages : reprends la ou tu t'es arrete, ne recommence pas au debut.
Puis LIVRE FERME, tu reecris ces quatre enonces AVEC leur demonstration :
  R1. |x + y| <= |x| + |y|, et le cas d'egalite.
  R2. | |x| - |y| | <= |x - y|.
  R3. Bernoulli : (1 + x)^n >= 1 + n x pour tout x >= -1 et tout n de N.
  R4. Caracterisation de la borne superieure : M = sup A ssi M majore A et, pour tout epsilon > 0, il existe a dans A avec a > M - epsilon.
Ce qui ne sort pas : tu relis CE point seul, puis tu reecris. Pas le chapitre entier.

SEGMENT 2  15h00-15h50  -  deux exercices
  E1. Montrer que pour tout x > 0 : x / (1 + x) < ln(1 + x) < x.
  E2. Soit f derivable sur un intervalle I avec f' >= 0. Montrer que f est croissante sur I. Puis expliquer pourquoi x -> -1/x, de derivee positive, n'est pas croissante sur R*. Quelle hypothese saute ?
E2 est le coeur du chapitre : l'intervalle n'est pas un detail d'enonce.

SEGMENT 3  16h00-16h40  -  ch. 4, sommes
Lecture 20 min (sommes, changement d'indice, telescopage, binome). Puis livre ferme :
  E3 - SANS ETIQUETTE. Soient a, b, c trois reels strictement positifs. Montrer que
      (a + b + c) (1/a + 1/b + 1/c) >= 9.
      Trouve DEUX preuves. Aucune ne demande le cours du jour : c'est justement l'idee.

CLOTURE  16h40-16h50  -  une seule tentative, pas de rattrapage
Debout, a voix haute, chronometre 5 min : enonce et demontre R3 (Bernoulli).

BONUS si tout est fait : sum(k = 1 a n) 1 / (k (k+1)) par telescopage.

METHODE
Tu lis d'abord, c'est ton choix, mais la lecture est CHRONOMETREE et le livre se referme au signal. Ce qui compte n'est pas d'avoir lu, c'est ce qui ressort livre ferme.
Un exercice se cherche 20 min maximum. Passe ce delai : corrige, comprends, et le lendemain refais-le de zero.
Toute erreur va au carnet, avec la date. Elle se refait a J+2.

@@ 2026-09-23 8e05670b992eaff7bc30089ddb47252a@fuf-romain
Fonctions numeriques | Calculs algebriques et trigonometrie

CONTRAT DU JOUR - reparer la preuve d'hier
Fin de seance = le theoreme redemontre par les accroissements finis, le contre-exemple exhibe avec un couple, et un oral de 10 min.

25 min  -  LA PREUVE CORRECTE
Soient a < b dans I.
  1. Pourquoi [a, b] est-il inclus dans I ? Ecris-le noir sur blanc. C'est ici, et nulle part ailleurs, que sert l'hypothese d'intervalle.
  2. Verifie les hypotheses du theoreme des accroissements finis : f continue sur [a, b], derivable sur ]a, b[. D'ou viennent-elles ?
  3. Applique le TAF et conclus.
Rappel du passage interdit d'hier : de 'la limite du taux est >= 0' tu as deduit 'le taux est >= 0'. Faux. Contre-exemple a garder : f : x -> x^2 en x0 = 0, ou f'(0) = 0 >= 0 alors que le taux vaut x, negatif des que x < 0.

15 min  -  DEUX CHOSES A FAIRE VITE
  a. Le contre-exemple, correctement : f : x -> -1/x sur R*. Ne dis pas 'pas croissante car R* n'est pas un intervalle' : l'echec d'une hypothese ne prouve jamais que la conclusion est fausse. EXHIBE un couple.
  b. Chronometre-toi sur | |x| - |y| | <= |x - y|. Objectif : deux lignes. Idee unique : ecris x = (x - y) + y, applique l'inegalite triangulaire, puis 'par symetrie des roles de x et y' au lieu de tout refaire.

10 min  -  ORAL DU JOUR
Debout, chronometre : enonce et demontre que f' >= 0 sur un intervalle entraine f croissante. A la fin, dis a voix haute : 'l'hypothese d'intervalle sert a garantir que [a, b] est inclus dans I'. Si tu ne l'as pas dite, l'oral ne compte pas.

LES DEUX CONTROLES A FAIRE SUR CHAQUE PREUVE, desormais :
  - Ai-je utilise CHAQUE hypothese ? Si l'une ne sert nulle part, la preuve est fausse.
  - Ce que je viens d'ecrire contredit-il quelque chose que je sais deja ?

METHODE
Nomme l'OUTIL avant d'ecrire la premiere ligne : quel theoreme du cours s'applique ici ? Si aucun ne vient, c'est deja une information.
Un exercice se cherche 20 min maximum. Passe ce delai : corrige, comprends, et le lendemain refais-le de zero.
Toute erreur va au carnet, avec la date. Elle se refait a J+2.

@@ 2026-09-24 c84fd76a2b2d5473c58aa5aca2127db1@fuf-romain
Fonctions numeriques | Calculs algebriques et trigonometrie

CONTRAT DU JOUR - passe 3, enseigner le ch. 3
Fin de seance = un cours de 20 min donne a voix haute, sans notes, avec un contre-exemple que tu sais justifier.

5 min   -  Ecris le PLAN du chapitre 3 en 5 lignes, de memoire. C'est le test le plus dur du chapitre : si le plan ne vient pas, la structure n'est pas la.

20 min  -  ENSEIGNE, debout, a voix haute, comme si tu faisais cours
  Impose-toi : 3 theoremes enonces proprement, 1 exemple, 1 CONTRE-EXEMPLE.
  Le contre-exemple impose : derivee positive sans croissance, sur R*. Tu dois pouvoir dire en une phrase pourquoi l'hypothese d'intervalle est indispensable, et ou exactement elle sert dans la preuve.

20 min  -  LA OU TU AS BUTE
Tu as forcement hesite quelque part en parlant. C'est le vrai resultat de la seance. Reprends ce point seul, puis reenseigne-le, une seule fois.

Enseigner est le seul test qui attrape ce que relire ne montre jamais : les endroits ou tu comprends sans savoir dire.

METHODE
Tu lis d'abord, c'est ton choix, mais la lecture est CHRONOMETREE et le livre se referme au signal. Ce qui compte n'est pas d'avoir lu, c'est ce qui ressort livre ferme.
Un exercice se cherche 20 min maximum. Passe ce delai : corrige, comprends, et le lendemain refais-le de zero.
Toute erreur va au carnet, avec la date. Elle se refait a J+2.

@@ 2026-09-24 75176cadb2a573831f7d0bea7ffe07d8@fuf-romain
!titre: Info mineure - Specification, terminaison, correction, complexite (1re seance : cours + preuves)
SEMAINE 2 - Specification, terminaison, correction, complexite
DANS LE LIVRE : Beury ch. 3

SEANCE REQUALIFIEE : c'est ta PREMIERE seance d'informatique, pas un oral blanc. Un oral blanc sur un chapitre jamais ouvert ne mesure rien. L'oral blanc d'info passe a jeudi prochain, sur ce chapitre-ci.

CONTRAT DU JOUR
Fin de seance = 7 definitions recitees sans notes + la dichotomie entierement specifiee, prouvee et chiffree + 1 exercice + 1 oral de 5 min.
Aucune ligne de Python n'est exigee aujourd'hui. Ton oral porte sur du raisonnement, pas sur la syntaxe.

25 min  -  LECTURE CHRONOMETREE (Beury ch. 3)
Tu ne lis pas pour tout retenir, tu lis pour remplir les sept cases ci-dessous. Referme le livre au signal.

20 min  -  LES 7 DEFINITIONS, LIVRE FERME
Ecris chacune en UNE phrase, de memoire. Ce sont elles qu'un examinateur demande en premier, et elles doivent sortir mot pour mot.
  D1. Precondition.
  D2. Postcondition.
  D3. Variant de boucle.
  D4. Invariant de boucle.
  D5. Correction partielle.
  D6. Correction totale.
  D7. Complexite au pire, en ordre de grandeur.
Celles qui ne sortent pas : relis CE point seul, puis reecris.

45 min  -  LA DICHOTOMIE, DE BOUT EN BOUT
Recherche d'une valeur v dans un tableau trie T de taille n.
  1. Specification complete : precondition, postcondition. Sois precis sur le mot 'trie'.
  2. VARIANT et preuve de terminaison. Un variant est un entier naturel qui decroit strictement a chaque tour : dis lequel, et montre-le.
  3. INVARIANT et preuve de correction partielle. L'invariant a dire : si v figure dans T, alors v figure dans la tranche encore consideree.
  4. Conclus a la correction TOTALE, et explique pourquoi ce mot exige les deux preuves precedentes et pas une seule.
  5. Complexite au pire : pose la recurrence, resous-la, et dis pourquoi c'est un ordre de grandeur et non un nombre d'operations.

25 min  -  EXERCICE AUTOSUFFISANT (enonce complet, rien a savoir d'avance)
  Soit T un tableau de n entiers, STRICTEMENT croissant, indice de 0 a n-1.
  On cherche s'il existe un indice i tel que T[i] = i.
  a. Montrer que g(i) = T[i] - i est croissante au sens large.
  b. En deduire un algorithme en O(log n). L'ecrire en pseudo-code.
  c. En donner l'invariant, prouver terminaison et correction.
  d. Pourquoi STRICTEMENT croissant est-il indispensable ? Donner un tableau croissant au sens large qui met la methode en defaut.
  La question d est la vraie question. Une hypothese qu'on ne sait pas casser est une hypothese qu'on n'a pas comprise.

5 min  -  CLOTURE, une seule tentative
Debout, chronometre : l'invariant de la dichotomie, puis la difference entre correction partielle et totale, en une phrase chacune.

LE REFLEXE DU JOUR, le meme qu'en maths : avant d'ecrire le moindre algorithme, ecris sa SPECIFICATION. C'est l'equivalent informatique de nommer l'outil avant de commencer.

METHODE
Tu lis d'abord, c'est ton choix, mais la lecture est CHRONOMETREE et le livre se referme au signal. Ce qui compte n'est pas d'avoir lu, c'est ce qui ressort livre ferme.
Un exercice se cherche 20 min maximum. Passe ce delai : corrige, comprends, et le lendemain refais-le de zero.
Toute erreur va au carnet, avec la date. Elle se refait a J+2.

@@ 2026-09-24 893e62d6fe850c1ec0dd627bf6313951@fuf-romain
La methode scientifique : Popper et la refutabilite
Theme le plus frequent de l'epreuve. Coefficient 4.

CONTRAT DU JOUR
Fin de seance = une fiche en cinq blocs + un expose de 15 min tenu debout, sans notes.

35 min  -  CONSTRUIRE LA FICHE. Cinq blocs, pas un de plus.
  1. LE PROBLEME. Hume et l'induction : aucune quantite d'observations ne demontre une loi universelle. Ecris pourquoi, en deux phrases.
  2. LA REPONSE DE POPPER. L'asymetrie logique : un enonce universel n'est jamais definitivement verifiable, mais un seul contre-exemple le refute. D'ou le critere : est scientifique ce qui INTERDIT quelque chose.
  3. DEUX EXEMPLES OPPOSES, avec dates. D'un cote l'eclipse de 1919 et la deviation de la lumiere : une prediction risquee, qui pouvait echouer. De l'autre, les theories que Popper juge irrefutables parce que tout les confirme. Cherche toi-meme lesquelles il vise, et ce qu'il leur reproche exactement.
  4. LES OBJECTIONS. Duhem-Quine : on ne teste jamais une hypothese seule mais un bloc (hypothese + hypotheses auxiliaires + conditions experimentales), donc un echec ne dit pas QUOI abandonner. Kuhn : la science normale ne cherche pas a refuter, elle resout des enigmes ; les ruptures sont des revolutions. Lakatos : un noyau dur protege par une ceinture d'hypotheses ajustables.
  5. TROIS CONFUSIONS A NE PAS FAIRE.
     - Refutable n'est pas faux. Un enonce refutable peut etre vrai, et c'est le cas de toutes les bonnes theories.
     - Refutable n'est pas verifiable. Le Cercle de Vienne demandait la verification ; Popper se construit contre eux.
     - Non scientifique n'est pas denue de sens. Popper ne condamne pas la metaphysique, il la place hors du champ de la science.
     C'est ici que se gagne le demi-point : la plupart des candidats confondent au moins une de ces trois paires.

35 min  -  MISE EN CONDITION, une seule tentative, pas de rattrapage
  Sujet : "Une theorie qui explique tout explique-t-elle quelque chose ?"
  15 min de preparation montre en main, puis 15 min debout, a voix haute, sans notes. Puis 5 min pour ecrire ce qui a manque.
  EXIGENCE : un exemple pris dans TON domaine. Une borne de complexite se refute par un seul contre-exemple. Une conjecture comme P different de NP est-elle refutable, et en quel sens ? Personne d'autre dans la salle n'aura cette carte : joue-la.

10 min  -  CARNET
Note ce que tu n'as pas su DIRE, pas ce que tu n'as pas su lire. A cette epreuve, ce qui n'est pas prononce n'existe pas.

@@ 2026-09-24 c6737c15a0aa89946c7705eb5357c915@fuf-romain
Fonctions numeriques | Calculs algebriques et trigonometrie

ORAL BLANC DU SOIR - format jour J, une seule tentative
50 min, sans preparation, debout, tu parles pendant que tu cherches. Pas de retour en arriere, pas de deuxieme essai : c'est la regle de l'epreuve et c'est ton ecart connu entre controle continu et examen.

PLANCHE
  Soit x un reel et n un entier naturel. Calculer
      C = sum(k = 0 a n) cos(k x).
  1. Traiter d'abord le cas x congru a 0 modulo 2 pi, separement.
  2. Dans le cas general, passer par l'exponentielle complexe et factoriser par l'angle moitie.
  3. En deduire sum(k = 0 a n) sin(k x).
  4. Question de l'examinateur, a preparer : pourquoi le cas x congru a 0 doit-il etre ecarte AVANT le calcul, et non discute apres ?

APRES, 10 min, note trois choses :
  - le moment exact ou tu t'es tu ;
  - un tic de langage ('du coup', 'en fait', 'voila') ;
  - une etape que tu as ecrite sans la dire.
Aux oraux, ce qui n'est pas dit n'existe pas.

METHODE
Tu lis d'abord, c'est ton choix, mais la lecture est CHRONOMETREE et le livre se referme au signal. Ce qui compte n'est pas d'avoir lu, c'est ce qui ressort livre ferme.
Un exercice se cherche 20 min maximum. Passe ce delai : corrige, comprends, et le lendemain refais-le de zero.
Toute erreur va au carnet, avec la date. Elle se refait a J+2.

@@ 2026-09-25 4f29f2fcfb4dcf9e112ae86ae3e689c0@fuf-romain
Temps du passe. Coefficient 3.

CONTRAT DU JOUR
Fin de seance = deux minutes d'anglais parle enregistrees, reecoutees, et le compte exact de tes fautes de temps.

15 min  -  LES TROIS FAUTES DE FRANCOPHONE
Pour chacune, ecris UNE phrase juste et UNE phrase fausse. C'est le contraste qui fixe la regle, pas la regle seule.
  1. Action datee = preterit, toujours. "I saw him yesterday", jamais "I have seen him yesterday". Des qu'une date, une heure ou un "ago" apparait, le present perfect est exclu.
  2. "Depuis" se coupe en deux : since + point de depart, for + duree, et le verbe va au present perfect. "I have lived here for three years" / "since 2023". Le francais dit "je vis ici depuis" au present : d'ou la faute, systematique.
  3. Anteriorite dans un recit deja au passe = past perfect. "When I arrived, he had already left." Le francais s'en passe souvent, l'anglais non.

25 min  -  PRODUCTION. C'est le coeur de la seance.
Choisis un fait scientifique recent. Raconte-le a voix haute, en anglais, au passe, pendant 2 minutes. ENREGISTRE-TOI avec ton telephone.
Ne t'arrete pas pour te corriger : au concours tu ne pourras pas.
Puis reecoute, et COMPTE. Le nombre de fautes de temps est ta note du jour.

10 min  -  REFAIRE
Reprends les memes 2 minutes, une seule fois, en corrigeant ce que tu as entendu. L'ecart entre les deux prises est ce que tu as reellement appris aujourd'hui.

POURQUOI T'ENREGISTRER : a l'ecrit tu vois tes fautes, a l'oral tu ne les entends pas. C'est le seul moyen de te relire en anglais parle, et c'est en anglais parle que tu seras note.

@@ 2026-09-25 7e1bd15afd12e7e4a662ab72c01ed3d6@fuf-romain
Fonctions numeriques | Calculs algebriques et trigonometrie

DEUX PLANCHES CHRONOMETREES - 2 h, format concours
Fin de seance = 2 planches traitees debout + 6 observations ecrites sur ta prestation.

PLANCHE 1  14h00-14h50
  Montrer que arctan(1/2) + arctan(1/3) = pi/4.
  Exige de toi DEUX preuves : par la tangente d'une somme, et par les nombres complexes (produit de (2 + i) et (3 + i)).
  Le piege est le meme dans les deux : la formule donne la tangente, pas l'angle. Tu dois justifier l'intervalle avant de conclure. Un examinateur t'arretera la.

PAUSE + AUTO-EVALUATION  14h50-15h05 (note tes 3 observations)

PLANCHE 2  15h05-15h55
  Soit f une application de [0, 1] dans [0, 1].
  1. On suppose f continue. Montrer que f admet un point fixe.
  2. On suppose seulement f croissante, sans aucune hypothese de continuite. Montrer qu'elle admet encore un point fixe.
  Indication pour 2, a n'ouvrir qu'apres 20 min de recherche : poser A = { x de [0,1] : f(x) >= x } et regarder sup A.
  La question 2 est exactement le chapitre 3 en situation : c'est la caracterisation du sup qui fait tout le travail.

AUTO-EVALUATION FINALE  15h55-16h00 (3 observations de plus)

METHODE
Tu lis d'abord, c'est ton choix, mais la lecture est CHRONOMETREE et le livre se referme au signal. Ce qui compte n'est pas d'avoir lu, c'est ce qui ressort livre ferme.
Un exercice se cherche 20 min maximum. Passe ce delai : corrige, comprends, et le lendemain refais-le de zero.
Toute erreur va au carnet, avec la date. Elle se refait a J+2.

@@ 2026-09-25 dd3094bc057004fed7fe4d23f93f737f@fuf-romain
Baroque et classicisme. Coefficient 3.
Deux esthetiques opposees, tres rentables a l'oral.

CONTRAT DU JOUR
Fin de seance = une fiche-munition complete, au format habituel en cinq sections, avec au moins six citations sues mot pour mot.

Format impose, le meme que tes autres fiches-munitions :
  1. idees et themes majeurs
  2. citations a memoriser mot pour mot
  3. applications en dissertation
  4. contexte auteur et dates precises
  5. categories thematiques

40 min  -  LES DEUX ESTHETIQUES, EN TABLEAU
  Baroque : instabilite, metamorphose, illusion, mouvement, ostentation, le theatre dans le theatre. Motifs a retenir : l'eau, le miroir, la bulle, les ruines, le songe, la vanite.
  Classicisme : ordre, mesure, raison, bienseance, vraisemblance, les trois unites, l'imitation des Anciens, plaire et instruire.

  AUTEURS : pas ceux du lycee. Cote baroque, va voir Sponde, Chassignet, Saint-Amant, et le proces de Theophile de Viau. Cote classique, prends La Rochefoucauld, La Bruyere, Madame de La Fayette plutot que Racine et Moliere, que tout le monde citera.
  Verifie CHAQUE date dans une source. N'en invente aucune : une date fausse a l'oral coute plus cher qu'une date absente.

30 min  -  CITATIONS
Six au minimum, trois par esthetique, apprises mot pour mot. Courtes. Une citation de six mots placee au bon endroit vaut mieux qu'un paragraphe recite.

20 min  -  LE PIEGE, et c'est la que tu prends de l'avance
L'opposition baroque / classicisme est trop propre pour etre vraie. Trois choses a savoir dire :
  - Corneille appartient aux deux, et L'Illusion comique (1636) en est la preuve. Cherche pourquoi.
  - Le classicisme ne s'est pas pense comme une reaction au baroque. Le mot 'baroque' applique a la litterature francaise est une construction critique tardive, pas une etiquette que ces auteurs revendiquaient.
  - Les bornes chronologiques usuelles sont commodes, pas etanches.
Un candidat qui oppose proprement recite un cours. Un candidat qui montre que la frontiere est construite a lu.

@@ 2026-09-27 bf530fdb2538c92cc660d4f5f0f9496b@fuf-romain
Trois questions : oral quotidien fait 5 fois ? chapitre-cible tenu ? carnet relu et erreurs retravaillees ? Trois oui = tu es a jour.

LE COMPTE DE LA SEMAINE - ecris les chiffres, ne les estime pas
  - resultats du ch. 3 et du ch. 4 que tu sais redemontrer seul, livre ferme : ___
  - exercices cherches 20 min : ___
  - oraux debout chronometres : ___
  - lignes ajoutees au carnet d'erreurs : ___
Un carnet vide n'est pas une bonne semaine, c'est une semaine trop facile.

CE QUI DEVAIT ETRE ACQUIS CETTE SEMAINE
  Ch. 3 : inegalite triangulaire et sa forme inverse, Bernoulli, caracterisation du sup, derivee positive sur un INTERVALLE donne croissance, theoreme de la bijection monotone.
  Ch. 4 : telescopage, sommes geometriques, binome de Newton, formule du capitaine, factorisation par l'angle moitie.
  Info : specification, variant, invariant, correction partielle et totale, complexite au pire.
Coche. Ce qui n'est pas coche passe en tete de la semaine prochaine, avant le nouveau chapitre.

SEMAINE PROCHAINE : ch. 5 nombres complexes, ch. 6 fonctions usuelles. Info : recherche et dichotomie.
