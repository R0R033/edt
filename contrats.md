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

CONTRAT DU JOUR - revision espacee J+1 sur la seance d'hier
Fin de seance = les 4 resultats d'hier ressortis sans notes + l'exercice rate refait.

15 min  -  RESTITUTION A FROID
Feuille blanche, rien d'ouvert. Reecris R1 a R4 d'hier (inegalite triangulaire, inegalite triangulaire inverse, Bernoulli, caracterisation du sup) avec les demonstrations. Coche ce qui sort seul.
Ce qui ne sort pas aujourd'hui alors que tu l'avais hier : c'est exactement ca qu'il faut revoir. Note-le au carnet, ce n'est pas un echec, c'est l'information que tu es venu chercher.

20 min  -  L'EXERCICE QUE TU N'AS PAS TROUVE HIER
Refais-le de zero, sans relire le corrige. Si tu l'avais tous trouves, prends celui-ci :
  Montrer que pour tout n >= 1 : sum(k = 1 a n) k C(n, k) = n 2^(n-1).
  Deux voies : deriver (1 + x)^n, ou la formule dite du capitaine k C(n, k) = n C(n-1, k-1). Fais les deux.

15 min  -  ORAL DU JOUR
Debout, chronometre : R4, la caracterisation du sup, enoncee et demontree. Puis l'illustrer sur A = { 1 - 1/n, n >= 1 }.

METHODE
Tu lis d'abord, c'est ton choix, mais la lecture est CHRONOMETREE et le livre se referme au signal. Ce qui compte n'est pas d'avoir lu, c'est ce qui ressort livre ferme.
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
Fin de seance = la dichotomie entierement specifiee, prouvee (terminaison ET correction) et son cout etabli, le tout sans le livre.
Aucune ligne de Python n'est exigee aujourd'hui. Ton oral porte sur du raisonnement, pas sur la syntaxe.

30 min  -  LECTURE, chronometree (Beury ch. 3)
Tu cherches quatre mots et leur definition exacte : precondition, postcondition, variant, invariant. Le reste se lira en le pratiquant.

50 min  -  LA DICHOTOMIE, LIVRE FERME
Sur la recherche dichotomique d'une valeur v dans un tableau trie T de taille n :
  1. Ecris la specification complete : ce qu'on suppose en entree (precondition), ce qu'on garantit en sortie (postcondition). Sois precis sur 'trie'.
  2. Donne un VARIANT de boucle et prouve la terminaison. Un variant est un entier naturel qui decroit strictement a chaque tour : dis lequel, et montre-le.
  3. Donne l'INVARIANT de boucle et prouve la correction PARTIELLE. L'invariant a dire : si v est dans T, alors v est dans la tranche encore consideree.
  4. Conclus a la correction TOTALE, et explique pourquoi ce mot exige les deux preuves precedentes et pas une seule.
  5. Complexite au pire : pose la recurrence C(n) = C(n/2) + O(1), resous-la, et dis pourquoi c'est un ordre de grandeur et non un nombre d'operations.

30 min  -  EXERCICE AUTOSUFFISANT (enonce complet, rien a connaitre d'avance)
  Soit T un tableau de n entiers, STRICTEMENT croissant, indice de 0 a n-1.
  On cherche s'il existe un indice i tel que T[i] = i.
  a. Montrer que la suite g(i) = T[i] - i est croissante au sens large.
  b. En deduire un algorithme en O(log n). L'ecrire en pseudo-code.
  c. En donner l'invariant de boucle, prouver la terminaison et la correction.
  d. Pourquoi l'hypothese STRICTEMENT croissant est-elle indispensable ? Donner un tableau croissant au sens large pour lequel la methode echoue.
  La question d est la vraie question. Une hypothese qu'on ne sait pas casser est une hypothese qu'on n'a pas comprise.

CLOTURE  -  une seule tentative, pas de rattrapage
Debout, a voix haute, chronometre 5 min : enonce l'invariant de la dichotomie et explique en une phrase la difference entre correction partielle et correction totale.

METHODE
Tu lis d'abord, c'est ton choix, mais la lecture est CHRONOMETREE et le livre se referme au signal. Ce qui compte n'est pas d'avoir lu, c'est ce qui ressort livre ferme.
Un exercice se cherche 20 min maximum. Passe ce delai : corrige, comprends, et le lendemain refais-le de zero.
Toute erreur va au carnet, avec la date. Elle se refait a J+2.

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

