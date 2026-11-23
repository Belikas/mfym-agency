# Benchmark : primes de bienvenue bancaires — vérification en source primaire

Date : 2026-11-23. Objectif : vérifier sur les pages officielles des banques (pas les comparateurs) les offres en cours, leurs conditions mot pour mot, et si elles peuvent produire le premier euro avant le 22/12 sans statut juridique. Pages officielles réellement ouvertes (WebFetch) : monabanq.com, fortuneo.fr, boursobank.com, bforbank.com. Hello bank! (hellobank.fr, y compris le PDF tarifaire sur m-webservices.hellobank.fr) renvoie un **403 systématique** à toute requête automatisée — impossible à vérifier en direct ; repose sur 2 sources secondaires concordantes (moneyvox + detective-banque), à confirmer par Baptiste en ouvrant la page lui-même avant le 08/12.

## Constat principal
- **Fortuneo et BoursoBank sont les deux offres les plus sûres** : montants confirmés en source primaire, compte et carte **100 % gratuits** (donc la prime n'est quasi pas rognée par un abonnement), et la tranche "mobilité" n'exige **pas** de domicilier le salaire principal — juste "au moins un" prélèvement ou virement récurrent (texte exact BoursoBank ; Fortuneo parle de transférer "l'ensemble ou une partie" des opérations).
- **Monabanq** est solide aussi mais la prime maximale (280 €) exige une carte payante (Pratiq+ à 3,90 €/mois minimum) et d'attendre le 13ᵉ mois pour la dernière tranche de 60 €.
- **BforBank** affiche le montant le plus élevé vérifié en primaire (330 €) mais la fenêtre se ferme le **09/12/2026** (12 jours) et la clause de reprise n'est documentée que pour l'assurance-vie BforLife, pas pour le compte courant — zone grise à vérifier par téléphone avant de compter dessus.
- **Hello bank! (330 €)** est la seule offre non vérifiable en primaire (403 partout) ; sur les 330 €, 200 € sont un **bon d'achat**, pas du cash — moins liquide que les autres offres.
- **N26** n'a aucune offre de bienvenue active en France en 2026 (confirmé par recherche) ; **Orange Bank** a cessé toute activité bancaire le 15/12/2025 (licence retirée) — à retirer définitivement du pipeline. **Ma French Bank** n'existe plus depuis juillet 2025 (absorbée par La Banque Postale, offre résiduelle 20 €, hors cible). **Helios** ne propose pas de prime de bienvenue à l'ouverture, seulement un parrainage (18 €/3 mois d'abonnement chacun) sur un compte déjà payant (4-15 €/mois) — pas pertinent seul.
- **Revolut** : 20 € de bienvenue confirmés (texte officiel), montant faible mais coût nul et rapide.
- **Trade Republic** (courtier, pas une banque) : action/ETF gratuite 5-200 € (tirage aléatoire) en ouvrant par parrainage + 50-100 € investis ; cumulable car compte-titres, pas compte courant.

## A. Tableau comparatif (montants vérifiés)

| Banque | Montant brut max | Coût mensuel réel | Domiciliation salaire exigée ? | Date de fin | Reprise si clôture | Verdict |
|---|---|---|---|---|---|---|
| **Fortuneo** | 250 € (Gold, offre FTNSEA) + 20 € Livret+ possible | 0 €/mois (compte et carte Gold gratuits si ≥1 paiement/mois) | Non (mobilité = "tout ou partie" des opérations, pas obligatoirement le salaire) | 31/12/2026 (offre FTNSEA) | Non documenté précisément sur cette page ; pratique du secteur = 12 mois, à vérifier au "voir conditions" avant de clôturer tôt | **RENTABLE** |
| **BoursoBank** | 180 € (code BBKOPE180) | 0 €/mois (compte et carte Welcome gratuits sans condition depuis le 27/02/2026) | Non — texte exact : "domicilier au moins un émetteur de prélèvement ou virement récurrent" | Pas de date de fin affichée (offre permanente depuis 06/10/2026) | Oui, 24 mois sur la tranche EasyMove (80 €) seulement ; clôture anticipée = reprise possible de l'intégralité | **RENTABLE** |
| **Monabanq** | 280 € | Pratiq+ 3,90 €/mois (carte Visa Classic) — formule "Pratiq" de base non confirmée gratuite | Non précisé explicitement pour la tranche mobilité (80 €) — zone grise, à demander au conseiller avant de l'activer | Offre depuis 01/07/2026, pas de fin affichée | Oui, 12 mois : clôture anticipée = Monabanq reprend l'intégralité des primes versées | **RENTABLE mais plus lent** (dernière tranche au 13ᵉ mois) |
| **BforBank** | 330 € (80 € paiements + 250 € mobilité) | 5 €/mois après le 1ᵉʳ mois gratuit (carte BforZEN) | Non précisé — "domicilier au moins 1 émetteur de prélèvement ou virement récurrent" (comme BoursoBank) | **09/12/2026** — fenêtre très courte | Clause de reprise documentée uniquement pour BforLife (assurance-vie) ; rien trouvé pour le compte courant | **RENTABLE si délai tenu**, confiance moyenne (texte incomplet) |
| **Hello bank!** | 330 € (80 € + 50 € + 200 € en bon d'achat) | 0 €/mois si ≥1 500 €/mois déposés, sinon 6 €/mois (carte Hello Prime) | Hello Prime : carte gratuite seulement si ≥1 500 €/mois d'entrées — pousse de fait vers une quasi-domiciliation si on veut éviter les frais | Validation avant **08/12/2026**, ouverture confirmée avant 08/01/2027 | Non vérifié (site inaccessible) | **FAUSSE BONNE AFFAIRE partielle** : 130 € cash nets, 200 € en bon d'achat (moins liquide) ; non vérifié en primaire |
| **Revolut** | 20 € | 0 €/mois (plan gratuit) | Non | Non précisé | Non documenté | RENTABLE mais marginal |
| **N26** | 0 € (aucune offre active) | — | — | — | — | **OFFRE MORTE** |
| **Orange Bank** | — | — | — | Banque fermée depuis le 15/12/2025 | — | **OFFRE MORTE** (banque n'existe plus) |
| **Helios** | 0 € à l'ouverture (18 €/3 mois seulement en parrainage, compte déjà payant) | 4-15 €/mois selon formule | — | — | — | **FAUSSE BONNE AFFAIRE** |
| **Ma French Bank** | — | — | — | N'existe plus depuis 07/2025 | — | **OFFRE MORTE** |

## B. Détail par banque

### Fortuneo — https://www.fortuneo.fr/offres-speciales-fortuneo et https://www.fortuneo.fr/compte-bancaire/offre-exclusive-mobilite-sea
- Deux pages officielles, deux offres actives simultanément : la page "offres spéciales" affiche **80 €** (code BIENVENUEFTO, carte Gold, 5 paiements en 90 jours, sans mobilité) ; la page mobilité affiche **250 €** (code FTNSEA = 160 € ouverture + 90 € mobilité bancaire), valable **01/07/2026 au 31/12/2026**.
- Carte Fosfo (sans condition de revenu) : 30 €. Carte Gold CB Mastercard (nécessite ≥2 200 €/mois de revenus pour l'éligibilité, pas pour la prime) : 80 à 160 € selon la page, + 90 € de mobilité.
- Carte Gold gratuite à vie si ≥1 paiement/mois ; compte sans frais de tenue.
- Mobilité : "transfère l'ensemble ou une partie des opérations bancaires" — pas de mention d'obligation de domicilier le salaire précisément.
- Versement : prime de bienvenue classique sous 30 jours max après les 5 paiements. Délai de versement de la tranche mobilité non précisé sur la page lue.
- Clause de reprise : non trouvée sur les pages ouvertes (seules les offres d'assurance-vie/PER Fortuneo affichent une clause de reprise explicite en cas de rachat <12 mois).
- **Coût réel 12 mois : 0 €. Net ≈ 250 € (voire 270 € avec le Livret+).**

### BoursoBank — https://www.boursobank.com/banque/compte-bancaire (+ carte Welcome)
- **180 € max**, code BBKOPE180 : 20 € ouverture, jusqu'à 40 € premier versement (10/20/40 € selon 1-49 €, 50-299 €, ≥300 €), jusqu'à 40 € opérations carte (20 € mois 1, 10 € mois 2, 10 € mois 3), 80 € mobilité EasyMove.
- Condition exacte EasyMove : "domicilier au moins un émetteur de prélèvement ou virement récurrent" — explicitement pas limité au salaire.
- Compte et carte Welcome 100 % gratuits sans condition depuis le 27/02/2026 (confirmé officiel + secondaire).
- Versement : échelonné, max 60 jours après chaque étape.
- Reprise : si la domiciliation EasyMove n'est pas maintenue 24 mois, BoursoBank peut reprendre la prime correspondante ; clôture anticipée du compte = reprise possible de l'intégralité.
- **Coût réel 12 mois : 0 €. Net = 180 € si EasyMove tenu 24 mois (ou 100 € nets et sans risque si on laisse tomber la tranche mobilité).**

### Monabanq — https://www.monabanq.com/fr/ma-prime.html
- **280 € max** : 20 € à l'ouverture, 60 € si dépôt ≥300 € dans le mois, 60 € après 30 paiements carte en 2 mois, 80 € pour l'aide à la mobilité bancaire, 60 € de fidélité au 13ᵉ mois (compte conservé + 2 autres produits Monabanq dont un produit d'épargne).
- Carte requise : Visa Classic (formule Pratiq+, 3,90 €/mois depuis le 01/10/2026) ou Uniq (6 €/mois) ou Uniq+ (12 €/mois) ; la formule de base "Pratiq" sans "+" n'a pas de prix confirmé en source primaire pour cette offre.
- Reprise : "en cas de clôture du compte dans les 12 mois suivant son ouverture effective, Monabanq se réserve le droit de prélever... l'ensemble des primes" (clause explicite, texte officiel).
- Offre active depuis le 01/07/2026, pas de date de fin affichée.
- **Coût réel 12-13 mois (Pratiq+) : ~47-51 €. Net ≈ 229 € en attendant le 13ᵉ mois, ou 132 € nets en 2 mois si on s'arrête aux 3 premières tranches (20+60+60=140 € brut, moins ~8 € de cotisation).**

### BforBank — https://www.bforbank.com/
- **330 € max** : 80 € après 15 paiements carte (≥150 € cumulés) en 90 jours + 250 € pour mobilité bancaire (mandat de mobilité + domiciliation d'au moins un prélèvement ou virement récurrent).
- Carte BforZEN : 1ᵉʳ mois gratuit, puis **5 €/mois**.
- Fenêtre très courte : **du 12/11/2026 au 09/12/2026 inclus**.
- Versement : max 2 mois après chaque étape validée.
- Clause de reprise trouvée uniquement pour l'assurance-vie BforLife ("rachat total ou partiel dans les 12 premiers mois") ; rien d'explicite pour le compte courant dans les pages ouvertes — zone grise, pas une garantie qu'il n'y a pas de clause ailleurs (brochure tarifaire complète non accessible, 403).
- **Coût réel 12 mois : ~55 € (11 × 5 €). Net ≈ 275 € si la fenêtre est tenue et si aucune clause de reprise cachée ne s'applique — à confirmer par téléphone avant de considérer ce chiffre comme acquis.**

### Hello bank! — hellobank.fr (403 sur toutes les pages testées, y compris le PDF tarifaire) ; via moneyvox.fr (éditorial) et detective-banque.fr (comparateur, intérêt financier)
- **330 € max** : 80 € à l'ouverture (Hello One ou Hello Prime) + 50 € pour Hello Prime (5 paiements/retraits par mois pendant 12 mois) + **200 € en bon d'achat** via Hello Start+ (mobilité).
- Hello Prime : carte gratuite seulement si ≥1 500 €/mois déposés, sinon 6 €/mois.
- Validation de la demande avant le **08/12/2026**, ouverture confirmée avant le 08/01/2027. Bon d'achat valable 6 mois.
- **Coût réel 12 mois : 0 € si ≥1 500 €/mois déposés (pousse vers une quasi-domiciliation), sinon 72 €.**
- **Net réel en cash : 130 € (ou 58 € si carte payante) + 200 € en bon d'achat non liquide.** Non vérifiable en primaire → traité avec prudence, à confirmer par Baptiste en ouvrant la page lui-même avant le 08/12 si retenu.

### Revolut — citation directe du texte officiel via recherche (revolut.com/fr-FR/legal, page bloquée au fetch direct mais contenu confirmé par le moteur de recherche)
- 20 € de bonus de bienvenue pour tout nouveau client Particuliers résidant en France, premier paiement carte ≥0,01 €. Plan gratuit, 0 €/mois.
- **Net ≈ 20 €, quasi immédiat.** Pas de date de fin précisée.

### N26 — confirmé : aucune offre de bienvenue active en France en 2026, seulement un parrainage variable affiché dans l'app. **OFFRE MORTE** pour un nouveau client sans parrain.

### Orange Bank — activité bancaire cessée le 15/12/2025, licence retirée, renommée Orange OBK. Impossible d'ouvrir un compte. **OFFRE MORTE**, à retirer du radar.

### Helios — blog.helios.do/programme-parrainage : parrainage = 18 € (3 mois d'abonnement offerts) pour le parrain ET le filleul, mais le compte lui-même coûte 4 à 15 €/mois selon la formule — pas de prime à l'ouverture seule, nécessite déjà d'être client payant. **FAUSSE BONNE AFFAIRE** comme lead autonome.

### Ma French Bank — n'existe plus depuis le 01/07/2025 (licence ACPR retirée). Les clients ont été transférés chez La Banque Postale (offre résiduelle 20 €, hors périmètre "sans statut"). **OFFRE MORTE**.

## C. Fiscalité — ce que dit une source officielle
- Échange officiel sur **plus.transformation.gouv.fr** (service des impôts, non commercial) : ces gains ("primes commerciales, applications de marche ou réponses à des sondages") **doivent être déclarés dans la plupart des cas comme revenu imposable**.
- Cohérence avec plusieurs sources indépendantes (non vérifié mot pour mot sur un texte BOFIP identifié précisément, mais convergent) : un abattement annuel de **305 €** s'applique aux "gains divers" occasionnels ; au-delà, le total (moins 305 €) se déclare en "autres revenus imposables" (case 1AO/1BO, formulaire 2042), imposé au barème de l'impôt sur le revenu selon la tranche marginale de Baptiste — pas de confiscation à 70 % par défaut comme l'ancienne note du pipeline le supposait ; la perte réelle dépend de sa TMI (ex. TMI 30 % → ~30 % de l'excédent au-delà de 305 €, pas plus).
- **Conséquence concrète** : Fortuneo (250 €) seul reste sous le seuil. Fortuneo + BoursoBank (250+180=430 €) dépasse 305 € : l'excédent (125 €) devient imposable au barème. À déclarer l'année suivante, pas au moment du versement.
- Aucune retenue à la source par les banques observée dans les sources consultées : c'est à Baptiste de déclarer.

## D. Risque de fichage / multi-comptes
- **Aucune limite légale** au nombre de comptes qu'une personne peut détenir (confirmé via lafinancepourtous.com et banque-france.fr, sources sans intérêt financier) : ouvrir 4-5 comptes en quelques semaines n'est pas en soi interdit ni signalé.
- Le fichage à la Banque de France (FICP/FCC) concerne les **incidents de paiement** (chèques sans provision, interdits bancaires), pas le nombre d'ouvertures de comptes. Le risque réel documenté est opérationnel : oublier un petit solde sur un compte secondaire peut entraîner un rejet de prélèvement puis des frais, dans de rares cas un fichage pour incident — pas pour avoir ouvert plusieurs comptes.
- Aucune source ne documente un refus systématique des banques en ligne pour "trop de comptes ouverts récemment" ; reste un risque théorique si les scores anti-fraude internes des banques (non publics) détectent un pattern de "chasse aux primes" répété — aucune preuve trouvée que cela arrive en pratique pour 4-5 ouvertures espacées.

## E. Domiciliation du salaire principal
- Les tranches "mobilité bancaire" (BoursoBank EasyMove, Fortuneo, BforBank) sont formulées comme "au moins un émetteur de prélèvement **ou** virement récurrent" — **pas explicitement le salaire**. Un abonnement (téléphone, streaming) suffit dans le texte lu pour BoursoBank, ce qui permet en principe de répéter l'opération à plusieurs banques sans toucher au vrai virement de salaire.
- Monabanq et Hello bank! : le texte exact disponible ne confirme pas si "au moins un" prélèvement suffit ou si le salaire est explicitement requis — zone grise, à clarifier avec le conseiller avant d'activer la tranche mobilité sur ces deux-là.
- Hello Prime pousse de fait vers un dépôt mensuel régulier de ≥1 500 € pour éviter les frais de carte — proche d'une domiciliation de fait même si ce n'est pas écrit comme une obligation contractuelle.
- **Classement selon l'exigence de domiciliation du salaire principal** :
  - Pas d'exigence claire : BoursoBank (confirmé), Fortuneo (probable), BforBank (probable), Revolut.
  - Zone grise à vérifier avant d'activer : Monabanq, Hello bank!.
  - Aucune banque testée n'exige explicitement et par écrit "le salaire principal, exclusivement, pendant X mois" — mais plusieurs poussent vers un usage régulier qui s'en approche.

## F. Classement final — 3 meilleures offres par euros nets sur 12 mois

| Rang | Offre | Net réel sur 12 mois | Temps Baptiste | Ce qu'il doit faire exactement |
|---|---|---|---|---|
| **1** | **Fortuneo**, compte + carte Gold CB Mastercard, code **FTNSEA** | **≈ 250 €** (270 € avec le Livret+) | ~1h au total | Ouvrir en ligne (fortuneo.fr/compte-bancaire/souscrire, code FTNSEA), carte Gold (revenu net ≥2 200 €/mois à déclarer). Faire 5 paiements carte dans les 90 jours (dépenses du quotidien). Activer la mobilité bancaire en ne transférant qu'un abonnement non-salarial. Garder le compte 12 mois par prudence. Ouvrir en plus un Livret+ gratuit pour les 20 € additionnels. |
| **2** | **BoursoBank**, compte + carte Welcome, code **BBKOPE180** | **≈ 180 €** (100 € nets et sans risque si on laisse tomber EasyMove) | ~45 min | Ouvrir en ligne (boursobank.com, code BBKOPE180 dès la 1ère page). Verser ≥300 € (argent récupérable, pas une dépense). Faire ≥1 paiement carte/mois pendant 3 mois. Activer EasyMove en y mettant un seul prélèvement non-salarial, et le maintenir 24 mois pour ne pas risquer la reprise des 80 €. |
| **3** | **Monabanq**, formule Pratiq+ (3,90 €/mois) | **≈ 132 € nets en 2 mois** (jusqu'à 229 € nets en attendant le 13ᵉ mois, avec 2 autres produits dont un livret) | ~1h + 1 rappel au mois 13 | Ouvrir en ligne (monabanq.com/fr/ma-prime.html). Déposer ≥300 € le mois 1. Faire 30 paiements carte en 2 mois (facile si c'est la carte du quotidien). Décider ensuite : s'arrêter là (132 € nets, zéro engagement long) ou viser les 229 € en gardant le compte 13 mois et en ouvrant un livret d'épargne gratuit chez Monabanq. |

**Mention à part (non classée dans le top 3, confiance moyenne)** : **BforBank** afficherait un net plus élevé (≈275 €) mais la fenêtre ferme le **09/12/2026** (12 jours) et la clause de reprise du compte courant n'a pas pu être confirmée en texte intégral — si Baptiste veut tenter, il doit faire vite et idéalement appeler le service client pour confirmer qu'aucune clause de reprise ne s'applique au-delà des paiements/90 jours.

**Hello bank! (330 €, dont 200 € en bon d'achat)** n'est pas classée dans le top 3 : impossible de vérifier ses conditions en source primaire (403 systématique) malgré 2 sources secondaires concordantes, et une partie significative n'est pas du cash. Si retenue, Baptiste doit l'ouvrir et la lire lui-même avant le 08/12/2026, et considérer le bon d'achat de 200 € comme un bonus annexe, pas comme du cash garanti.

## G. Cumul
- Toutes les offres bancaires ci-dessus sont **cumulables entre elles** : ce sont des établissements différents, et rien n'interdit légalement de détenir plusieurs comptes. La seule vraie limite pratique est le temps de gestion et le risque de petits frais oubliés sur un compte secondaire (voir D).
- **Trade Republic** (courtier, pas une banque) est cumulable en plus des banques ci-dessus : ouverture par parrainage, dépôt ~50-100 €, 3 investissements sous 21 jours → action/ETF gratuite entre 5 et 200 € (tirage aléatoire, donc non garanti au montant maximum). Mécanisme différent (compte-titres), zéro conflit avec les comptes courants.
- **Revolut** (20 €) se cumule aussi sans difficulté, coût et effort quasi nuls.
- Attention fiscale au cumul : au-delà de 305 €/an tous gains occasionnels confondus, l'excédent devient imposable (voir C). Ça reste un gain net, juste pas 100 % net.

## Non vérifié / limites
- Hello bank! : aucune page officielle accessible (403 systématique, y compris le PDF tarifaire sur un sous-domaine différent). Les 330 € reposent sur 2 sources secondaires concordantes, pas sur une lecture directe.
- BforBank : clause de reprise du compte courant non trouvée explicitement (seulement pour l'assurance-vie) — absence de preuve n'est pas preuve d'absence ; la brochure tarifaire complète n'a pas pu être ouverte (403).
- Monabanq : prix de la formule "Pratiq" de base (sans "+") non confirmé en source primaire pour cette offre précise ; l'estimation de coût utilise Pratiq+ (3,90 €/mois) par prudence.
- Fiscalité : le seuil de 305 € et la case de déclaration (1AO/1BO, formulaire 2042) sont cohérents sur plusieurs sources indépendantes mais n'ont pas été confirmés mot pour mot sur un texte BOFIP identifié précisément ni sur impots.gouv.fr/service-public.fr directement (ces deux domaines n'ont pas livré de page dédiée aux primes bancaires lors des recherches).
- La question de savoir si Monabanq et Hello bank! exigent de facto le salaire principal pour la tranche "mobilité" reste ouverte — à clarifier par téléphone avant d'activer cette tranche chez ces deux banques si retenues.
