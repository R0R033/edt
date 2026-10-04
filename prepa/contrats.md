# Contrats de seance
#
# Un bloc par seance. En-tete : @@ AAAA-MM-JJ UID
# Ligne !titre: juste apres l'en-tete = remplace aussi le titre de l'evenement.
# Tout le reste jusqu'au prochain @@ devient le commentaire de l'evenement.
# Publie par .github/workflows/prepa.yml des que le fichier change, puis chaque matin.
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
  - resultats du ch. 3 que tu sais redemontrer seul, livre ferme : ___
  - exercices cherches 20 min : ___
  - oraux debout chronometres : ___
  - lignes ajoutees au carnet d'erreurs : ___
Un carnet vide n'est pas une bonne semaine, c'est une semaine trop facile.

CE QUI DEVAIT ETRE ACQUIS
  Ch. 3, section I : inegalite triangulaire et sa forme inverse, Bernoulli, caracterisation du sup, derivee positive sur un INTERVALLE donne croissance.
  Info : specification, variant, invariant, correction partielle et totale, complexite au pire.

SEMAINE PROCHAINE : profond ch. 3, sections II a IV et cloture samedi | outil ch. 4, sommes, binome, pivot. Info : recherche et dichotomie. Francais : nouvelle methode, premier resume vendredi.

@@ 2026-09-27 51fc27a2433c7e7425483e93642348e5@fuf-romain
RAPPEL DU SOIR - 15 min, sans notes
Se retester a distance de la seance, c'est ce qui fait tenir un resultat jusqu'en mai. C'est court expres.

1. 5 min - Demain 8 h, outil ch. 4 : ecris de tete ce que tu sais deja des sommes (geometrique, sum k, telescopage). C'est ton point de depart.
2. 5 min - Info : relis la correction de la dichotomie de cet apres-midi, ferme-la, puis reecris le variant et l'invariant.
3. 5 min - Carnet d'erreurs : relis a voix haute les lignes de la semaine.

Si un point ne sort pas ce soir, tu ne le revois pas maintenant : tu le notes, et il ouvre la seance de demain.

@@ 2026-09-28 df5234b893605b867089706f1710a6a5@fuf-romain
!titre: Maths - Outil ch. 4 (I) : sommes, changement d'indice, telescopage
THEME DE LA SEMAINE : profond ch. 3 (sections II a IV, cloture samedi) | outil ch. 4 (sections I a III)

OUTIL - Deschamps ch. 4, section I 'Symboles somme et produit', p. 102-115.
Un chapitre OUTIL ne se redemontre pas : il s'automatise. Peu de lecture, beaucoup de calculs courts, justes du premier coup.
Fin de seance = 6 calculs justes. Chaque faute va au carnet avec sa cause : indice, borne ou signe.

08h00-08h10 SURVOL p. 102-115, crayon en main. Note seulement les formules que tu ne saurais pas ecrire de tete.

08h10-08h45 SIX CALCULS, livre ferme, 5 a 6 min chacun
  S1. sum(k = 0 a n) q^k pour q different de 1. Puis sum(k = 3 a n) q^k : la somme geometrique qui ne commence pas en 0, une faiblesse que le jury de l'X releve chez les candidats.
  S2. sum(k = 1 a n) 1 / (k (k + 1)) par telescopage. C'etait le bonus de mardi dernier.
  S3. Retrouve sum(k = 1 a n) k^2 en telescopant (k + 1)^3 - k^3.
  S4. prod(k = 2 a n) (1 - 1/k^2). Factorise chaque facteur, puis telescope le produit.
  S5. Somme double : sum(1 <= i <= j <= n) i. Somme d'abord en i, a j fixe.
  S6. Avec le changement d'indice j = n - k, montre que sum(k = 0 a n) k = sum(k = 0 a n) (n - k), et deduis-en la formule de Gauss sans recurrence.

08h45-08h50 CLOTURE, debout : la formule de sum(k = p a n) q^k, et comment tu la retrouves en 20 secondes.

A ne regarder qu'apres : S2 = n / (n + 1) ; S4 = (n + 1) / (2n) ; S5 = n (n + 1) (n + 2) / 6.

@@ 2026-09-29 dcd7a674adb05b82b870c9fb33d8aefc@fuf-romain
!titre: Maths - Profond ch. 3 (II) : fonctions reelles de la variable reelle
THEME DE LA SEMAINE : profond ch. 3 (sections II a IV, cloture samedi) | outil ch. 4 (sections I a III)

PROFOND - Deschamps ch. 3, section II 'Fonctions reelles de la variable reelle', p. 72-79. En fin de seance, lecture de la section III.
Fin de seance = section II lue, 3 resultats reecrits livre ferme avec leur preuve, 3 exercices cherches, 1 oral de 5 min.

14h00-14h10 REPRISE, 10 min max. De tete : 'f' >= 0 sur un intervalle implique f croissante', hypotheses comprises, preuve par les accroissements finis en 5 lignes. Ce qui ne sort pas va au carnet et revient a J+2.

14h10-14h40 LECTURE CHRONOMETREE p. 72-79. En lisant, dresse la liste des enonces encadres : c'est ta liste de reconstruction.

14h40-15h05 LIVRE FERME, avec preuve
  R1. La composee de deux fonctions decroissantes est croissante. Pour les trois autres cas, 'de meme' suffit, mais sache dire lequel donne quoi.
  R2. Une fonction strictement monotone est injective.
  R3. f est bornee si et seulement si |f| est majoree. Les DEUX sens.
  Plus les autres enonces encadres de ta liste.

15h05-15h15 PAUSE

15h15-16h15 TROIS EXERCICES, 20 min max chacun
  E1. (analyse-synthese) Montrer que toute fonction f : R -> R s'ecrit de maniere UNIQUE comme somme d'une fonction paire et d'une fonction impaire. Commence par l'analyse : si f = p + i, que valent p(x) et i(x) en fonction de f(x) et f(-x) ?
  E2. (la reciproque de R2) Une fonction injective de R dans R est-elle forcement monotone ? Preuve ou contre-exemple. Puis ecris, sans le demontrer, quel theoreme deviendrait necessaire si l'on imposait en plus la continuite sur un intervalle.
  E3. Soit f : R -> R periodique et monotone. Montrer que f est constante.

16h15-16h40 LECTURE p. 80-85 (section III, rappels de derivation). Note seulement ce que tu ne saurais pas demontrer : c'est le programme de demain.

16h40-16h50 CLOTURE, une seule tentative : debout, chronometre, 5 min. Enonce et demontre R2, puis donne ton contre-exemple de E2.

METHODE
Lecture chronometree, livre ferme au signal. Un exercice se cherche 20 min maximum ; passe ce delai, corrige, comprends, et refais-le de zero a J+2. Avant la premiere ligne d'un exercice, ecris 'OUTIL :' et le resultat que tu comptes utiliser.
Deux controles sur chaque preuve : chaque hypothese a-t-elle servi ? Ai-je ecrit quelque chose qui contredit ce que je sais deja ?

@@ 2026-09-30 293b89d2436fd38b81d37a30558ae8d8@fuf-romain
!titre: Maths - Profond ch. 3 (III) : derivation, les preuves a savoir faire
THEME DE LA SEMAINE : profond ch. 3 (sections II a IV, cloture samedi) | outil ch. 4 (sections I a III)

PROFOND - Deschamps ch. 3, section III 'Derivation - rappels du secondaire', p. 80-85, lue hier en fin de seance.
Fin de seance = 3 resultats enonces avec leurs hypotheses exactes, dont 1 redemontre, 1 exercice, 1 oral.

09h40-09h55 REPRISE, 15 min max : ce qui a casse hier (carnet).

09h55-10h20 LIVRE FERME
  R1. Derivee d'un produit, a partir du taux d'accroissement. L'astuce tient en une ligne : ajouter et retrancher f(a) g(x). Preuve complete.
  R2. Derivee d'une composee : (g o f)'(a) = f'(a) g'(f(a)). Enonce exact : ou f doit-elle etre derivable, et ou g ?
  R3. Derivee de la reciproque : f bijection de l'intervalle I sur J, derivable en a avec f'(a) non nul ; alors f^-1 est derivable en b = f(a), et (f^-1)'(b) = 1 / f'(a). Dis pourquoi f'(a) non nul est indispensable : regarde x -> x^3 en 0.
  Si le livre admet R2 et R3 dans cette section, retiens l'enonce exact et le role de chaque hypothese : la preuve viendra au ch. 11.

10h20-10h40 EXERCICE, 20 min max
  E1. Montrer que arctan est derivable sur R et calculer sa derivee par la formule de la reciproque. L'etape que presque tout le monde saute : tan est une bijection DE QUOI SUR QUOI ?

10h40-10h50 CLOTURE : debout, 5 min, R3 et le contre-exemple x^3. Puis 5 min de carnet.

METHODE
Lecture chronometree, livre ferme au signal. Un exercice se cherche 20 min maximum ; passe ce delai, corrige, comprends, et refais-le de zero a J+2. Avant la premiere ligne d'un exercice, ecris 'OUTIL :' et le resultat que tu comptes utiliser.
Deux controles sur chaque preuve : chaque hypothese a-t-elle servi ? Ai-je ecrit quelque chose qui contredit ce que je sais deja ?

@@ 2026-10-01 464ec5adfbd495308d03d609e444285c@fuf-romain
!titre: Maths - Profond ch. 3 (IV) : variations d'une fonction sur un intervalle
THEME DE LA SEMAINE : profond ch. 3 (sections II a IV, cloture samedi) | outil ch. 4 (sections I a III)

PROFOND - Deschamps ch. 3, section IV 'Variations d'une fonction sur un intervalle', p. 86-94.
Fin de seance = section IV lue, 2 resultats reecrits, 1 exercice, 1 oral de 3 min.

09h40-09h55 REPRISE, 15 min max : carnet de mardi et de mercredi.

09h55-10h25 LECTURE CHRONOMETREE p. 86-94. Liste les enonces encadres.
  A verifier livre en main, et a me dire ce soir : le theoreme de la bijection (fonction continue et strictement monotone sur un intervalle) est-il enonce ici, ou seulement au ch. 10 ?

10h25-10h50 LIVRE FERME
  R1. f' >= 0 sur un intervalle implique f croissante. Tu l'as deja : 3 min, pas plus.
  R2. Si f' > 0 sur l'intervalle sauf en un nombre fini de points, alors f est strictement croissante. Indice : f est croissante par R1 ; si f(a) = f(b) avec a < b, que vaut f sur [a, b], et donc f' sur ]a, b[ ?
  Plus les autres enonces encadres de ta liste.

10h50-11h05 EXERCICE, 15 min
  E1. Montrer que pour tout x de [0, pi/2] : (2/pi) x <= sin x <= x.
  La majoration est immediate. Pour la minoration, etudie h(x) = sin x - 2x/pi : h' change de signe une seule fois. Qu'en deduis-tu sur h, sachant que h(0) = h(pi/2) = 0 ?

11h05-11h10 CLOTURE : debout, 3 min, R2.

METHODE
Lecture chronometree, livre ferme au signal. Un exercice se cherche 20 min maximum ; passe ce delai, corrige, comprends, et refais-le de zero a J+2. Avant la premiere ligne d'un exercice, ecris 'OUTIL :' et le resultat que tu comptes utiliser.
Deux controles sur chaque preuve : chaque hypothese a-t-elle servi ? Ai-je ecrit quelque chose qui contredit ce que je sais deja ?

@@ 2026-10-02 1af70f9607aee0dd1c9f49df6cf147ef@fuf-romain
!titre: Maths - Oral blanc format jury (2 exercices) + outil ch. 4 (II-III)
THEME DE LA SEMAINE : profond ch. 3 (sections II a IV, cloture samedi) | outil ch. 4 (sections I a III)

FORMAT DU JURY FUF : deux exercices tires de deux parties distinctes du programme, environ 25 min chacun, debout, a voix haute, sans preparation. Tu parles pendant que tu cherches.

14h00-14h25 EXERCICE 1
  Soit f definie sur R par f(x) = x / (1 + |x|).
  1. Montrer que f est strictement croissante et impaire.
  2. Montrer que f est une bijection de R sur ]-1, 1[ et expliciter sa reciproque.
  3. f est-elle derivable en 0 ? Et f^-1 ?
  Question d'examinateur a anticiper : comment prouves-tu la surjectivite SANS le theoreme des valeurs intermediaires ?

14h25-14h30 Trois observations sur ta prestation, ecrites.

14h30-14h55 EXERCICE 2
  Pour n >= 1, calculer S = sum(k = 0 a n) k binom(n, k).
  Deux methodes exigees : (a) la relation k binom(n, k) = n binom(n - 1, k - 1), a justifier ; (b) deriver x -> (1 + x)^n.
  Relance possible : et sum(k = 0 a n) k^2 binom(n, k) ?

14h55-15h00 Trois observations de plus.

15h00-16h00 OUTIL ch. 4, sections II et III (binome p. 116-118, pivot p. 119-123). Survol 10 min, puis livre ferme :
  B1. Formule de Pascal : une preuve par le calcul, une preuve par le denombrement.
  B2. sum(k = 0 a n) binom(n, k) 2^k.
  B3. La somme des binom(n, k) pour k pair, n >= 1. Combine (1 + 1)^n et (1 - 1)^n.
  B4. Resoudre par le pivot, en discutant selon le reel m :
      x + y + z = 1 ; x + 2y + 3z = 2 ; x + 4y + m z = 3.
  Critere : 4 resultats justes. Chaque faute au carnet avec sa cause.

LES SIX OBSERVATIONS : le moment exact ou tu t'es tu ; un tic de langage ; une etape ecrite sans etre dite ; ton temps reel sur chaque exercice. Le jury annonce deux exercices en 50 min : l'ecart entre ton temps et 25 min est ce qu'il te reste a gagner.

@@ 2026-10-03 d51198d372f67224b817ce51b7783909@fuf-romain
!titre: Maths - Cloture du ch. 3 : l'enseigner, puis deux exercices
THEME DE LA SEMAINE : profond ch. 3 (sections II a IV, cloture samedi) | outil ch. 4 (sections I a III)

CLOTURE DU CHAPITRE 3. Un chapitre est fini quand tu l'as enseigne a voix haute, pas quand tu as lu sa derniere page.
Fin de seance = plan de memoire + cours de 20 min donne debout + 2 exercices + le compte des sections.

10h00-10h15 REPRISE, 15 min max : carnet de la semaine.

10h15-10h20 PLAN DE MEMOIRE : les 4 sections du ch. 3 en 4 lignes, chacune avec son resultat phare.

10h20-10h45 ENSEIGNE, debout, 20 min, sans notes. Impose-toi 3 theoremes avec leurs hypotheses exactes, 1 exemple et 2 contre-exemples : derivee positive sans croissance sur R*, fonction injective non monotone.

10h45-10h55 LA OU TU AS HESITE : reprends ce point seul, puis reenseigne-le une fois.

10h55-11h05 PAUSE

11h05-11h25 EXERCICE 1, 20 min max
  Montrer que ln x <= x - 1 pour tout x > 0, avec egalite si et seulement si x = 1.
  En deduire, pour a1, ..., an > 0 de moyenne arithmetique m : a1 a2 ... an <= m^n. Indice : applique l'inegalite a chaque ai / m, puis somme.

11h25-11h45 EXERCICE 2, 20 min max
  Soit f(x) = x^3 + x sur R. Montrer que f est une bijection de R sur R, que f^-1 est derivable sur R, et calculer (f^-1)'(2).
  Pour la surjectivite, tu peux invoquer le theoreme de la bijection : dis precisement ce qu'il demande.

11h45-12h10 LE COMPTE, ecrit :
  sections du ch. 3 faites / prevues : ___ / 4 (II, III, IV, cloture)
  sections du ch. 4 faites / prevues : ___ / 3 (I, II, III)
  resultats redemontrables livre ferme : ___ ; exercices cherches : ___ ; oraux debout : ___
Ces chiffres ouvrent le bilan de dimanche.

12h10-12h20 Marge.

METHODE
Lecture chronometree, livre ferme au signal. Un exercice se cherche 20 min maximum ; passe ce delai, corrige, comprends, et refais-le de zero a J+2. Avant la premiere ligne d'un exercice, ecris 'OUTIL :' et le resultat que tu comptes utiliser.
Deux controles sur chaque preuve : chaque hypothese a-t-elle servi ? Ai-je ecrit quelque chose qui contredit ce que je sais deja ?

@@ 2026-09-28 18c72e6bc0532d66e4fea37347571573@fuf-romain
SEMAINE 3 - Recherche et dichotomie. Beury ch. 4, p. 51-58. Le rattrapage de la semaine Python est integre ici.
Fin de seance = la dichotomie reprise au propre + 4 algorithmes ecrits en vrai Python et testes, chacun avec sa specification et sa complexite justifiee.

17h10-17h25 REPRISE DE LA CORRECTION DE DIMANCHE, 15 min max, livre ferme
  - Le variant est UN entier naturel qui decroit strictement a chaque tour : fin - debut + 1, la taille de la tranche. 'Les indices debut et fin' n'est pas un variant.
  - L'invariant : si v est dans T, alors v est dans T[debut..fin].
  - La correction partielle se lit a la SORTIE de la boucle : ou bien T[m] = v et on renvoie m ; ou bien la tranche est vide, et l'invariant donne 'v n'est pas dans T'. 'On finira par tomber sur T[m] = v' n'est pas une preuve.
  - Au pire (v absent), la taille est au moins divisee par 2 a chaque tour : au plus floor(log2 n) + 1 tours. C'est un ordre de grandeur parce qu'on compte des tours de boucle, a une constante pres. Et le pire cas ne depend pas de v : c'est le maximum sur toutes les entrees de taille n.

17h25-17h50 LECTURE CHRONOMETREE Beury ch. 4, p. 51-58.

17h50-18h30 QUATRE ALGORITHMES EN VRAI PYTHON, 10 min chacun. Pour chacun : precondition, postcondition, complexite au pire justifiee en une phrase.
  A1. Maximum d'une liste non vide ET son indice, en un seul parcours.
  A2. Second maximum en un seul parcours. Decide ce que tu renvoies pour [5, 5, 3] et ecris-le dans la specification.
  A3. Nombre d'occurrences de chaque element, avec un dictionnaire. Puis la meme chose avec une liste de couples (element, compte) a la place du dictionnaire : quelle complexite, et pourquoi ?
  A4. Exponentiation rapide : son invariant, et pourquoi O(log n) multiplications.

18h30-18h40 CLOTURE : debout, 5 min, la preuve complete de la dichotomie, dite. Puis carnet.

LE RATTRAPAGE PYTHON est dans A1 a A4 : les fondamentaux du langage s'ecrivent en vrai Python (listes, boucles, fonctions, dictionnaires). Le jury prefere le raisonnement a la syntaxe : la specification et la complexite comptent plus que le code.

Socle officiel : programme d'informatique commune MP PC PSI PT (2021), plus le programme que tu declares.

@@ 2026-10-01 81e729abce0493eb18d0596c1aea0fb0@fuf-romain
ORAL BLANC D'INFO - format jour J, debout, a voix haute. 50 min de questions, 10 min de bilan.
Tout doit etre DIT : ce qui est seulement ecrit n'existe pas pour l'examinateur.

11h20-11h35 Q1. La recherche dichotomique de bout en bout : specification, algorithme, terminaison par le variant, correction par l'invariant, complexite au pire. Sans notes.

11h35-11h55 Q2. T est un tableau STRICTEMENT croissant de n entiers, indices de 0 a n-1. Existe-t-il i tel que T[i] = i ?
  a. Montrer que g(i) = T[i] - i est croissante au sens large. C'est ici que servent 'strictement' ET 'entiers'.
  b. En deduire un algorithme en O(log n), avec son invariant.
  c. Question d'examinateur : pourquoi 'strictement' ? Donne un tableau croissant au sens large qui met ta methode en defaut.

11h55-12h10 Q3. Deux valeurs les plus proches dans une liste de n reels. L'algorithme naif et sa complexite. Puis l'amelioration par un tri prealable : pourquoi suffit-il alors de comparer des voisins ? Quelle complexite totale ?

12h10-12h20 BILAN : trois observations. Le moment ou tu t'es tu, un tic de langage, une etape ecrite sans etre dite.

@@ 2026-10-02 e1a2d74976ca75a44c2fe1de6cfeadae@fuf-romain
Futur et hypothese. Coefficient 3.

CONTRAT DU JOUR
Fin de seance = deux minutes d'anglais parle enregistrees, reecoutees, et le compte exact de tes fautes de futur et de conditionnel.

15 min - LES REGLES, EN PAIRES : une phrase juste et une phrase fausse par regle. C'est le contraste qui fixe la regle.
  1. Will = decision prise sur le moment, ou prediction. Be going to = intention deja formee, ou indice present. Present continu = arrangement deja fixe : 'I'm meeting my tutor tomorrow' quand le rendez-vous est pris.
  2. Jamais de will apres if ou when dans la subordonnee : 'When I arrive in Bristol, I will call you', jamais 'When I will arrive'. C'est LA faute du francophone, calquee sur 'quand j'arriverai'.
  3. Hypothese sur le present : if + preterit, would. 'If I had more time, I would read more.' Jamais 'if I would have'.
  4. Irreel du passe : if + past perfect, would have + participe. 'If I had known, I would have applied earlier.'

25 min - PRODUCTION. C'est le coeur de la seance.
Sujet : 'Your semester in Bristol: what you expect, what you have planned, and what you would do differently if you could start your degree again.' Il force les quatre regles.
Deux minutes a voix haute, sans t'arreter pour te corriger. ENREGISTRE-TOI.
Reecoute et COMPTE : fautes de futur, fautes de conditionnel. Ce nombre est ta note du jour.

10 min - REFAIRE : les memes deux minutes, une seule fois, en corrigeant ce que tu as entendu. L'ecart entre les deux prises est ce que tu as reellement appris aujourd'hui.

@@ 2026-10-02 db110acf5f63fe7508f977401e3c11a8@fuf-romain
!titre: Francais - Le resume (1) : methode, inventaire honnete, premier resume
CE QUI CHANGE EN FRANCAIS, a partir d'aujourd'hui
Deux chantiers, et seulement deux :
  - L'EXERCICE. Le jury le dit : il 'ne s'improvise pas'. On l'entraine au format reel, chronometre, enregistre.
  - LE CORPUS. Uniquement des oeuvres que tu as lues ou vues. Moins nombreuses, mais tenues.

FORMAT DE L'EPREUVE (rapports du jury FUF 2020-2025) : 45 min de preparation sur un texte d'une bonne page (litterature, philosophie, esthetique, sciences humaines, de l'Antiquite a aujourd'hui). Puis 30 min : resume en 2-3 min ; expose d'une douzaine de minutes (introduction avec problematique et plan, trois parties qui progressent, breve conclusion, un exemple culturel precis et maitrise par partie) ; entretien d'une quinzaine de minutes.
REGLE DU CORPUS : aucune oeuvre citee sans l'avoir lue ou vue. Le jury l'ecrit, et l'entretien le verifie.

CONTRAT DU JOUR
Fin de seance = ton inventaire honnete + un resume ecrit en entier, dit debout en 2 a 3 min, enregistre et passe a la grille.

15 min - INVENTAIRE HONNETE
Liste ce que tu as REELLEMENT lu ou vu, en entier ou le passage precis : livres, poemes, films, series, tableaux, pieces, expositions, concerts. Cinq cases par ligne : titre, auteur, date, un detail precis que tu saurais raconter, 'je tiens 2 min dessus' oui ou non.
Marque d'une croix les oeuvres que le jury dit voir revenir tous les ans : 1984, Le Meilleur des mondes, Candide, L'Etranger, Germinal, Rhinoceros, Bel-Ami, Guernica, la science-fiction, les mangas, l'heroic fantasy. Il ne les accepte que si tu les connais PARFAITEMENT.
Les lignes a 'oui' sans croix forment ton vrai corpus de depart. Tes fiches sur Camus n'y entrent que si tu as lu les textes.

45 min - PREMIER RESUME, SUR UN AUTEUR DE CONCOURS
Texte : Baudelaire, la lettre-dedicace 'A Arsene Houssaye', en tete du Spleen de Paris (Petits poemes en prose). Une page, sur Wikisource. Le Spleen de Paris figurait parmi les textes donnes en 2024.
  1. Lis-la deux fois. A la deuxieme, marque dans la marge chaque articulation : ton resume les garde toutes, dans l'ordre.
  2. Redige le resume EN ENTIER au brouillon, comme le jour J. Le jury conseille de le rediger integralement, et tu as le droit de le lire, 'avec le ton'.
  3. Debout, chronometre, enregistre-toi. Cible : entre 2 et 3 min.

LA GRILLE - chaque 'non' va au carnet
  - Enonciation : Baudelaire ecrit 'je' a un ami, ton resume garde ce 'je'. Deux interdits explicites du jury : commencer par 'ce texte parle de', et passer a la troisieme personne ('Baudelaire explique que') quand l'auteur parle en son nom.
  - Aucun jugement, aucun commentaire personnel.
  - Reformulation forte : aucune phrase du texte recopiee.
  - Toutes les articulations, dans l'ordre.
  - Entre 2 et 3 min. Le jury deplore les resumes expedies en moins d'une minute : 'trop de candidats', ecrivait-il en 2024.

20 min - APERCU DE L'EXPOSE, sans le faire
Le sujet se choisit sur un aspect MAJEUR du texte, a partir d'une de ses phrases. 'Le texte n'est pas un pretexte.'
Choisis ta phrase. Ecris une problematique en une question, puis trois titres de parties qui PROGRESSENT, pas trois exemples juxtaposes.
Pas d'exemples aujourd'hui. Pour chaque partie, regarde seulement si ton inventaire contient une oeuvre qui la nourrirait. Une case vide, c'est ton prochain chantier de corpus.

10 min - CARNET
La duree de ton resume, le nombre de 'non' a la grille, et les mots familiers entendus a la reecoute. Le jury cite 'au final', 'positionner', 'au jour d'aujourd'hui', 'ceci dit', 'solutionner', et les anglicismes.

@@ 2026-10-04 475df1e728b11319a2c742398aa72cd7@fuf-romain
LE COMPTE DE LA SEMAINE - ecris les chiffres, ne les estime pas.

MATHS - sections faites / prevues
  ch. 3 : II, III, IV, cloture -> ___ / 4
  ch. 4 : I, II, III -> ___ / 3
  resultats redemontrables livre ferme : ___ ; exercices cherches 20 min : ___ ; oraux debout : ___
INFO - la dichotomie dite sans notes, de bout en bout : oui / non. Algorithmes ecrits et testes : ___ / 4.
FRANCAIS - inventaire fait : oui / non. Duree de ton resume : ___ min ___ s. 'Non' a la grille : ___.
ANGLAIS - fautes de futur et de conditionnel : prise 1 ___, prise 2 ___.
CARNET - lignes ajoutees : ___ ; erreurs refaites a J+2 : ___.

Une section non faite ne se rattrape pas en force : elle decale le plan. Donne-moi ces chiffres ce soir, je recale la suite sur ton rythme reel.

SEMAINE PROCHAINE : profond ch. 9, nombres reels et suites | outil ch. 4 (trigonometrie) puis ch. 5 (complexes). Info : recursivite.

@@ 2026-10-05 303b88192dbd7cefdfb81ffa333d012b@fuf-romain
!titre: Maths - Cloture du ch. 3 (1) : l'enseigner, puis ln x <= x - 1
THEME DE LA SEMAINE : reports d'abord (cloture du ch. 3, oral blanc, ch. 4 II-III), puis profond ch. 9 (I a III) | outil ch. 4 (IV)

REPRISE APRES LA COUPURE. Ce qui n'a pas ete fait vendredi et samedi passe avant le chapitre 9 : on ne rattrape pas en force, on decale.
Fin de seance = plan de memoire + cours de 20 min donne debout + 1 exercice.

08h00-08h05 PLAN DE MEMOIRE : les 4 sections du ch. 3 en 4 lignes, chacune avec son resultat phare.

08h05-08h25 ENSEIGNE, debout, 20 min, sans notes. Impose-toi 3 theoremes avec leurs hypotheses exactes, 1 exemple et 2 contre-exemples : derivee positive sans croissance sur R*, fonction injective non monotone. Pour le second, deux couples temoins, un par sens.

08h25-08h45 EXERCICE, 20 min max
  Montrer que ln x <= x - 1 pour tout x > 0, avec egalite si et seulement si x = 1.
  En deduire, pour a1, ..., an > 0 de moyenne arithmetique m : a1 a2 ... an <= m^n. Indice : applique l'inegalite a chaque ai / m, puis somme.

08h45-08h50 CARNET : le point ou tu as hesite en enseignant. C'est le vrai resultat de la seance.

@@ 2026-10-05 d5fdc441d3b8aa1c7c808439031df2b2@fuf-romain
SEMAINE 4 - Recursivite. Beury ch. 7, p. 79-96. Deux reports y sont absorbes : l'exponentiation rapide (le A4) et la dichotomie, en version recursive.
Fin de seance = 3 fonctions recursives ecrites en vrai Python et testees, chacune avec terminaison, correction et complexite.

17h10-17h35 LECTURE CHRONOMETREE Beury ch. 7 : p. 79-81, puis survol des exemples.

17h35-17h45 LIVRE FERME, quatre phrases a savoir dire :
  1. Le cas de base, et pourquoi sans lui la fonction ne termine pas.
  2. L'appel recursif porte sur une instance strictement plus petite : cette taille est le variant.
  3. La correction se prouve par recurrence (forte) sur la taille.
  4. La complexite se lit sur une relation de recurrence : C(n) = C(n/2) + O(1) donne O(log n).

17h45-18h30 TROIS FONCTIONS, 15 min chacune
  R1. Exponentiation rapide recursive, de zero, sans relire ma correction.
  R2. Recherche dichotomique recursive dans T[g..d] : terminaison par la taille d - g + 1, correction par recurrence forte sur cette taille.
  R3. Tours de Hanoi : la fonction qui affiche les deplacements pour n disques. Montre que le nombre de deplacements verifie u(n) = 2 u(n-1) + 1, puis u(n) = 2^n - 1. Mercredi, tu retrouveras la meme structure en maths.

18h30-18h40 CLOTURE : debout, 5 min, la correction de l'exponentiation rapide par recurrence forte. Puis carnet.

Le jury prefere le raisonnement a la syntaxe : la terminaison et la correction comptent plus que le code.

@@ 2026-10-06 58c1b4be060ac1127fa24f0b381d97b7@fuf-romain
!titre: Maths - Cloture du ch. 3 (2) + profond ch. 9 (I) : l'ensemble des nombres reels
THEME DE LA SEMAINE : reports d'abord (cloture du ch. 3, oral blanc, ch. 4 II-III), puis profond ch. 9 (I a III) | outil ch. 4 (IV)

Fin de seance = l'exercice de cloture du ch. 3 + section I du ch. 9 lue, 3 resultats reecrits, 2 exercices, 1 oral.
L'essentiel est place en premier. Le dernier bloc est un BONUS : s'il saute, rien n'est en retard.

14h00-14h20 CLOTURE DU CH. 3, exercice 2, 20 min max
  Soit f(x) = x^3 + x sur R. Montrer que f est une bijection de R sur R, que f^-1 est derivable sur R, et calculer (f^-1)'(2).
  Pour la surjectivite, tu peux invoquer le theoreme de la bijection : dis precisement ce qu'il demande.

14h20-14h50 LECTURE CHRONOMETREE ch. 9, section I 'L'ensemble des nombres reels', p. 310-313. Liste les enonces encadres.

14h50-15h15 LIVRE FERME, avec preuve
  R1. R est archimedien : pour tout a > 0 et tout reel b, il existe n entier avec n a > b.
  R2. Partie entiere : pour tout reel x, il existe un UNIQUE entier n tel que n <= x < n + 1. Existence ET unicite.
  R3. Q est dense dans R : entre deux reels a < b, il y a un rationnel. Indice : choisis n avec 1/n < b - a, puis regarde (floor(n a) + 1) / n.
  LEMME DU PLANCHER, deja vu cet ete : pour k entier, k <= y equivaut a k <= floor(y). Invoque-le par son nom, ne le redemontre pas.

15h15-15h25 PAUSE

15h25-16h05 DEUX EXERCICES, 20 min max chacun
  E1. Montrer que pour tout reel x : floor(2x) = floor(x) + floor(x + 1/2). Ecris x = n + t avec n entier et t dans [0, 1[, puis distingue t < 1/2 et t >= 1/2.
  E2. Montrer que l'ensemble des irrationnels est dense dans R. Indice : applique R3 entre a - racine(2) et b - racine(2).

16h05-16h10 CLOTURE, une seule tentative : debout, 5 min, R2 (existence et unicite de la partie entiere).

16h10-16h50 BONUS : lecture du ch. 9, section II, p. 314-316. Si tu la fais, mercredi commence directement au livre ferme.

METHODE
Lecture chronometree, livre ferme au signal. Un exercice se cherche 20 min maximum ; passe ce delai, corrige, comprends, et refais-le de zero a J+2. Avant la premiere ligne d'un exercice, ecris 'OUTIL :' et le resultat que tu comptes utiliser.
Deux controles sur chaque preuve : chaque hypothese a-t-elle servi ? Ai-je ecrit quelque chose qui contredit ce que je sais deja ?

@@ 2026-10-07 d65850b67a4607ec1a94e5c1ffa732cc@fuf-romain
!titre: Maths - Profond ch. 9 (II) : generalites sur les suites reelles
THEME DE LA SEMAINE : reports d'abord (cloture du ch. 3, oral blanc, ch. 4 II-III), puis profond ch. 9 (I a III) | outil ch. 4 (IV)

PROFOND - Deschamps ch. 9, section II, p. 314-316.
Fin de seance = 1 resultat reecrit avec sa preuve + 1 exercice + 1 oral de 3 min.

08h00-08h10 REPRISE, 10 min max : ce qui a casse mardi (carnet).

08h10-08h25 LECTURE p. 314-316. Si tu l'as faite mardi en bonus, relis 5 min et garde 10 min pour l'exercice.

08h25-08h35 LIVRE FERME
  R1. Suite arithmetico-geometrique u(n+1) = a u(n) + b, avec a different de 1. Pose l = b / (1 - a), le point fixe. Montre que u(n) - l = a^n (u(0) - l) en trois lignes. Que le livre la traite ici ou non, c'est un incontournable d'oral.

08h35-08h45 EXERCICE, 10 min
  u(0) = 0 et u(n+1) = 2 u(n) + 3. Expliciter u(n). Tu retrouveras exactement cette structure lundi soir en info, avec les tours de Hanoi.

08h45-08h50 CLOTURE : debout, 3 min, R1 et sa preuve.

@@ 2026-10-08 4cfe4ed8e75f34f068cf07d638b726e4@fuf-romain
!titre: Maths - Profond ch. 9 (III) : la limite d'une suite, la definition
THEME DE LA SEMAINE : reports d'abord (cloture du ch. 3, oral blanc, ch. 4 II-III), puis profond ch. 9 (I a III) | outil ch. 4 (IV)

PROFOND - Deschamps ch. 9, section III 'Limite d'une suite reelle', p. 317-322. La fin de la section passe samedi.
Fin de seance = section III lue + 2 resultats reecrits + 1 oral.

08h55-09h20 LECTURE CHRONOMETREE p. 317-322. Liste les enonces encadres.

09h20-09h35 LIVRE FERME
  R1. La definition de 'u(n) tend vers l', avec ses quantificateurs dans le bon ordre. Puis sa NEGATION, ecrite proprement. C'est le chapitre 1 en situation : la negation est la que les candidats tombent.
  R2. Unicite de la limite, par l'absurde, avec epsilon = |l - l'| / 3.
      Question d'examinateur : si la definition est ecrite avec |u(n) - l| <= epsilon, pourquoi epsilon = |l - l'| / 2 ne suffirait-il pas ? Et avec une inegalite stricte ?

09h35-09h40 CLOTURE : debout, 3 min, R2.

@@ 2026-10-08 0de4b4a087ef0e000a1eac31a34d9062@fuf-romain
ORAL BLANC D'INFO - 2 h, debout, a voix haute. Les questions de l'oral manque jeudi dernier y sont reprises.
Tout doit etre DIT : ce qui est seulement ecrit n'existe pas pour l'examinateur.

09h50-10h05 Q1. L'exponentiation rapide recursive : algorithme, terminaison, correction, complexite.

10h05-10h25 Q2 (report). T est un tableau STRICTEMENT croissant de n entiers. Existe-t-il i tel que T[i] = i ?
  Montre que g(i) = T[i] - i est croissante, deduis-en un algorithme en O(log n), puis dis pourquoi 'strictement' est indispensable, avec un tableau qui casse la methode.

10h25-10h45 Q3. Fibonacci recursif naif. Montre que le nombre d'appels A(n) verifie A(n) = A(n-1) + A(n-2) + 1, puis que A(n) >= 2^floor(n/2) : le nombre d'appels est exponentiel. Donne ensuite une version en O(n).

10h45-11h00 Q4 (report). Deux valeurs les plus proches dans une liste de n reels : naif et sa complexite, puis tri prealable. Pourquoi suffit-il alors de comparer des voisins ?

11h00-11h20 Q5. Tours de Hanoi a l'oral : la recurrence et sa resolution. Question d'examinateur : peut-on faire moins de 2^n - 1 deplacements ? Indice : au moment ou le plus grand disque bouge, ou sont les n - 1 autres ?

11h20-11h35 BILAN : trois observations. Le moment ou tu t'es tu, un tic de langage, une etape ecrite sans etre dite.

11h35-11h50 Marge et carnet.

@@ 2026-10-08 5942f8261794449014c8ae11d1231c05@fuf-romain
Qu'est-ce qu'un ingenieur ? Science, technique, societe. Coefficient 4.
Le sujet le plus proche de l'X elle-meme : il servira aussi a l'entretien de motivation.

CONTRAT DU JOUR
Fin de seance = une fiche en cinq blocs + un expose de 10 min tenu debout, sans notes, enregistre.

35 min - LA FICHE, cinq blocs, pas un de plus
  1. LES DISTINCTIONS, une phrase chacune : science (comprendre), technique (faire), technologie (une technique fondee sur la science), ingenierie (concevoir sous contraintes : cout, securite, delais, normes).
  2. L'INGENIEUR EN FRANCE : la creation de l'Ecole polytechnique en 1794, sous le nom d'Ecole centrale des travaux publics, et ce que l'X dit former aujourd'hui. Verifie chaque date dans une source avant de l'ecrire.
  3. DEUX THESES OPPOSEES. La technique est neutre, tout depend de l'usage. Ou bien elle ne l'est pas : elle impose ses propres fins. Cherche ce que soutient Jacques Ellul (La Technique ou l'enjeu du siecle, 1954) et resume-le en deux phrases.
  4. LA RESPONSABILITE. Hans Jonas, Le Principe responsabilite (1979), et son imperatif : 'Agis de facon que les effets de ton action soient compatibles avec la permanence d'une vie authentiquement humaine sur terre.' Puis le principe de precaution, inscrit dans la Charte de l'environnement de 2005.
  5. UN CAS. Challenger, 1986 : des joints dont la defaillance par temps froid etait connue, et une decision de lancement. Feynman conclut son annexe au rapport d'enquete : 'For a successful technology, reality must take precedence over public relations, for nature cannot be fooled.' Puis un cas a toi : ton stage a l'Inria, et la question de ce qu'on choisit d'optimiser.

REGLE : tu cites une idee au niveau ou tu la connais. 'Jonas soutient que...' oui. 'Au chapitre tant de son livre...' seulement si tu l'as lu.

15 min - PREPARATION, montre en main
  Sujet : 'L'ingenieur doit-il se demander a quoi servira ce qu'il construit ?'

10 min - EXPOSE debout, sans notes, chronometre, ENREGISTRE. Exigence : un exemple pris dans ton propre domaine.

10 min - REECOUTE ET CARNET : ce que tu n'as pas su DIRE, pas ce que tu n'as pas su lire.

Preparation et expose sont raccourcis ici : la seance vise le contenu. Le format complet viendra dans les seances de repetition.

@@ 2026-10-09 5fe08f461e3a0ed1a8a3661ccbf5399f@fuf-romain
!titre: Anglais - Futur et hypothese (report de vendredi dernier)
REPORT DE VENDREDI DERNIER, a l'identique. Les modaux passent a vendredi prochain.

Futur et hypothese. Coefficient 3.

CONTRAT DU JOUR
Fin de seance = deux minutes d'anglais parle enregistrees, reecoutees, et le compte exact de tes fautes de futur et de conditionnel.

15 min - LES REGLES, EN PAIRES : une phrase juste et une phrase fausse par regle. C'est le contraste qui fixe la regle.
  1. Will = decision prise sur le moment, ou prediction. Be going to = intention deja formee, ou indice present. Present continu = arrangement deja fixe : 'I'm meeting my tutor tomorrow' quand le rendez-vous est pris.
  2. Jamais de will apres if ou when dans la subordonnee : 'When I arrive in Bristol, I will call you', jamais 'When I will arrive'. C'est LA faute du francophone, calquee sur 'quand j'arriverai'.
  3. Hypothese sur le present : if + preterit, would. 'If I had more time, I would read more.' Jamais 'if I would have'.
  4. Irreel du passe : if + past perfect, would have + participe. 'If I had known, I would have applied earlier.'

25 min - PRODUCTION. C'est le coeur de la seance.
Sujet : 'Your semester in Bristol: what you expect, what you have planned, and what you would do differently if you could start your degree again.' Il force les quatre regles.
Deux minutes a voix haute, sans t'arreter pour te corriger. ENREGISTRE-TOI.
Reecoute et COMPTE : fautes de futur, fautes de conditionnel. Ce nombre est ta note du jour.

10 min - REFAIRE : les memes deux minutes, une seule fois, en corrigeant ce que tu as entendu. L'ecart entre les deux prises est ce que tu as reellement appris aujourd'hui.

@@ 2026-10-09 52b9ce28382b7b1db141eb969b220c2c@fuf-romain
!titre: Maths - Oral blanc format jury (2 exercices) + outil ch. 4 (II-III)
THEME DE LA SEMAINE : reports d'abord (cloture du ch. 3, oral blanc, ch. 4 II-III), puis profond ch. 9 (I a III) | outil ch. 4 (IV)

REPORT DE VENDREDI DERNIER, a l'identique.

FORMAT DU JURY FUF : deux exercices tires de deux parties distinctes du programme, environ 25 min chacun, debout, a voix haute, sans preparation. Tu parles pendant que tu cherches.

14h00-14h25 EXERCICE 1
  Soit f definie sur R par f(x) = x / (1 + |x|).
  1. Montrer que f est strictement croissante et impaire.
  2. Montrer que f est une bijection de R sur ]-1, 1[ et expliciter sa reciproque.
  3. f est-elle derivable en 0 ? Et f^-1 ?
  Question d'examinateur a anticiper : comment prouves-tu la surjectivite SANS le theoreme des valeurs intermediaires ?

14h25-14h30 Trois observations sur ta prestation, ecrites.

14h30-14h55 EXERCICE 2
  Pour n >= 1, calculer S = sum(k = 0 a n) k binom(n, k).
  Deux methodes exigees : (a) la relation k binom(n, k) = n binom(n - 1, k - 1), a justifier ; (b) deriver x -> (1 + x)^n.
  Relance possible : et sum(k = 0 a n) k^2 binom(n, k) ?

14h55-15h00 Trois observations de plus.

15h00-16h00 OUTIL ch. 4, sections II et III (binome p. 116-118, pivot p. 119-123). Survol 10 min, puis livre ferme :
  B1. Formule de Pascal : une preuve par le calcul, une preuve par le denombrement.
  B2. sum(k = 0 a n) binom(n, k) 2^k.
  B3. La somme des binom(n, k) pour k pair, n >= 1. Combine (1 + 1)^n et (1 - 1)^n.
  B4. Resoudre par le pivot, en discutant selon le reel m :
      x + y + z = 1 ; x + 2y + 3z = 2 ; x + 4y + m z = 3.
  Critere : 4 resultats justes. Chaque faute au carnet avec sa cause.

LES SIX OBSERVATIONS : le moment exact ou tu t'es tu ; un tic de langage ; une etape ecrite sans etre dite ; ton temps reel sur chaque exercice. Le jury annonce deux exercices en 50 min : l'ecart entre ton temps et 25 min est ce qu'il te reste a gagner.

@@ 2026-10-09 bec6df8b8149be80096c7d78921f705c@fuf-romain
!titre: Francais - Le resume (1) : methode, inventaire honnete, premier resume
REPORT DE VENDREDI DERNIER. Tout le programme de francais glisse d'une seance ; la seance de bilan du 04/12 disparait, son compte passera au bilan du dimanche.

CE QUI CHANGE EN FRANCAIS, a partir d'aujourd'hui
Deux chantiers, et seulement deux :
  - L'EXERCICE. Le jury le dit : il 'ne s'improvise pas'. On l'entraine au format reel, chronometre, enregistre.
  - LE CORPUS. Uniquement des oeuvres que tu as lues ou vues. Moins nombreuses, mais tenues.

FORMAT DE L'EPREUVE (rapports du jury FUF 2020-2025) : 45 min de preparation sur un texte d'une bonne page (litterature, philosophie, esthetique, sciences humaines, de l'Antiquite a aujourd'hui). Puis 30 min : resume en 2-3 min ; expose d'une douzaine de minutes (introduction avec problematique et plan, trois parties qui progressent, breve conclusion, un exemple culturel precis et maitrise par partie) ; entretien d'une quinzaine de minutes.
REGLE DU CORPUS : aucune oeuvre citee sans l'avoir lue ou vue. Le jury l'ecrit, et l'entretien le verifie.

CONTRAT DU JOUR
Fin de seance = ton inventaire honnete + un resume ecrit en entier, dit debout en 2 a 3 min, enregistre et passe a la grille.

15 min - INVENTAIRE HONNETE
Liste ce que tu as REELLEMENT lu ou vu, en entier ou le passage precis : livres, poemes, films, series, tableaux, pieces, expositions, concerts. Cinq cases par ligne : titre, auteur, date, un detail precis que tu saurais raconter, 'je tiens 2 min dessus' oui ou non.
Marque d'une croix les oeuvres que le jury dit voir revenir tous les ans : 1984, Le Meilleur des mondes, Candide, L'Etranger, Germinal, Rhinoceros, Bel-Ami, Guernica, la science-fiction, les mangas, l'heroic fantasy. Il ne les accepte que si tu les connais PARFAITEMENT.
Les lignes a 'oui' sans croix forment ton vrai corpus de depart. Tes fiches sur Camus n'y entrent que si tu as lu les textes.

45 min - PREMIER RESUME, SUR UN AUTEUR DE CONCOURS
Texte : Baudelaire, la lettre-dedicace 'A Arsene Houssaye', en tete du Spleen de Paris (Petits poemes en prose). Une page, sur Wikisource. Le Spleen de Paris figurait parmi les textes donnes en 2024.
  1. Lis-la deux fois. A la deuxieme, marque dans la marge chaque articulation : ton resume les garde toutes, dans l'ordre.
  2. Redige le resume EN ENTIER au brouillon, comme le jour J. Le jury conseille de le rediger integralement, et tu as le droit de le lire, 'avec le ton'.
  3. Debout, chronometre, enregistre-toi. Cible : entre 2 et 3 min.

LA GRILLE - chaque 'non' va au carnet
  - Enonciation : Baudelaire ecrit 'je' a un ami, ton resume garde ce 'je'. Deux interdits explicites du jury : commencer par 'ce texte parle de', et passer a la troisieme personne ('Baudelaire explique que') quand l'auteur parle en son nom.
  - Aucun jugement, aucun commentaire personnel.
  - Reformulation forte : aucune phrase du texte recopiee.
  - Toutes les articulations, dans l'ordre.
  - Entre 2 et 3 min. Le jury deplore les resumes expedies en moins d'une minute : 'trop de candidats', ecrivait-il en 2024.

20 min - APERCU DE L'EXPOSE, sans le faire
Le sujet se choisit sur un aspect MAJEUR du texte, a partir d'une de ses phrases. 'Le texte n'est pas un pretexte.'
Choisis ta phrase. Ecris une problematique en une question, puis trois titres de parties qui PROGRESSENT, pas trois exemples juxtaposes.
Pas d'exemples aujourd'hui. Pour chaque partie, regarde seulement si ton inventaire contient une oeuvre qui la nourrirait. Une case vide, c'est ton prochain chantier de corpus.

10 min - CARNET
La duree de ton resume, le nombre de 'non' a la grille, et les mots familiers entendus a la reecoute. Le jury cite 'au final', 'positionner', 'au jour d'aujourd'hui', 'ceci dit', 'solutionner', et les anglicismes.

@@ 2026-10-10 a8019d9311e5f4e7f06bfca50369e23e@fuf-romain
!titre: Maths - Profond ch. 9 (III, fin) + outil ch. 4 (IV) : trigonometrie
THEME DE LA SEMAINE : reports d'abord (cloture du ch. 3, oral blanc, ch. 4 II-III), puis profond ch. 9 (I a III) | outil ch. 4 (IV)

Fin de seance = 3 resultats reecrits, 2 exercices, 5 calculs de trigonometrie justes, et le compte de la semaine.

10h00-10h15 REPRISE, 15 min max : carnet de la semaine.

10h15-10h40 LIVRE FERME, ch. 9 section III
  R3. Toute suite convergente est bornee.
  R4. Passage a la limite dans les inegalites LARGES. Puis le contre-exemple pour les strictes : u(n) = 1/n est > 0, et sa limite ne l'est pas.
  R5. La definition de 'u(n) tend vers + l'infini'.

10h40-11h20 DEUX EXERCICES, 20 min max chacun
  E1. En revenant a la definition, montrer que u(n) = (2n + 1) / (n + 3) tend vers 2. Exhibe le N, explicitement, en fonction d'epsilon.
  E2. Une suite d'entiers relatifs converge. Montrer qu'elle est constante a partir d'un certain rang. Indice : epsilon = 1/3, et demande-toi pourquoi pas 1/2.

11h20-11h30 PAUSE

11h30-12h10 OUTIL ch. 4, section IV 'Trigonometrie', p. 124-140. Survol 10 min, puis livre ferme, 5 calculs :
  T1. cos(a + b) et sin(a + b) de tete ; en deduire cos(2a), puis cos^2(a) en fonction de cos(2a).
  T2. Resoudre cos x = sin(2x) sur R.
  T3. Lineariser cos^3(x).
  T4. tan(a + b) en fonction de tan a et tan b, avec les conditions d'existence.
  T5. cos p + cos q en produit.
  Critere : 5 justes. Chaque faute au carnet, avec sa cause.

12h10-12h20 LE COMPTE, ecrit, pour le bilan de demain :
  cloture du ch. 3 faite : oui / non ; oral blanc fait : oui / non
  ch. 4 : sections II, III, IV faites -> ___ / 3
  ch. 9 : sections I, II, III faites -> ___ / 3

METHODE
Lecture chronometree, livre ferme au signal. Un exercice se cherche 20 min maximum ; passe ce delai, corrige, comprends, et refais-le de zero a J+2. Avant la premiere ligne d'un exercice, ecris 'OUTIL :' et le resultat que tu comptes utiliser.
Deux controles sur chaque preuve : chaque hypothese a-t-elle servi ? Ai-je ecrit quelque chose qui contredit ce que je sais deja ?

@@ 2026-10-11 af0df3ef191cc1ff93d882a2a4767754@fuf-romain
LE COMPTE DE LA SEMAINE - ecris les chiffres, ne les estime pas.

REPORTS DE LA SEMAINE DERNIERE
  cloture du ch. 3 (enseigner + 2 exercices) : oui / non
  oral blanc de maths a deux exercices : oui / non
  francais, premier resume : duree ___ min ___ s ; 'non' a la grille : ___
  anglais, futur et hypothese : fautes prise 1 ___, prise 2 ___

MATHS - sections faites / prevues
  ch. 4 : II, III, IV -> ___ / 3
  ch. 9 : I, II, III -> ___ / 3
  resultats redemontrables livre ferme : ___ ; exercices cherches 20 min : ___ ; oraux debout : ___
INFO - fonctions recursives ecrites et prouvees : ___ / 3. Questions tenues a l'oral blanc : ___ / 5.
CULTURE GENERALE - expose de 10 min tenu : oui / non.
CARNET - lignes ajoutees : ___ ; erreurs refaites a J+2 : ___.

Deux semaines de compteur, c'est assez pour mesurer ton rythme reel. Donne-moi ces chiffres ce soir : je recale la suite du plan dessus.
