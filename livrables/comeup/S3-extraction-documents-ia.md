# S3 - Automatisation de l'extraction de documents (factures, bons de livraison, PDF vers Excel)

Les blocs entre les lignes ==== sont à coller tels quels dans ComeUp : texte brut, sans Markdown (pas de ** ni de ->), listes avec "- " et numéros "1.".
Prix = prix affiché acheteur (benchmark). À la création, saisir le prix vendeur qui donne ce prix affiché (~ prix / 1,102) et contrôler au checkout. Limite de titre ComeUp non vérifiée : titre gardé nettement sous 80 caractères.
À confirmer par Baptiste avant publication : la niche (recherche ComeUp "saisie de factures" / "extraction de données") et la catégorie Saisie/Data si elle existe.

## Titre (73 caractères)
Je vais créer votre automatisation factures PDF vers Excel avec n8n et IA
(ComeUp impose "Je vais" : saisir "créer votre automatisation factures PDF vers Excel avec n8n et IA")

## Catégorie
Programmation & Tech > Automatisation (à confirmer à la création ; alternative : Saisie / Data si la catégorie existe)

## Définitions (valables pour toute la fiche)
- Type de document : une famille de documents ayant les mêmes champs à extraire, quel que soit le fournisseur. Exemples : factures fournisseurs = 1 type ; bons de livraison = 1 autre type ; CMR = 1 autre type. Si vos fournisseurs ont des mises en page très différentes, on le constate au test et je vous propose un ajustement en option.
- Cas douteux : un document marqué "à relire" quand au moins une de ces règles est déclenchée : un champ obligatoire manque ou est illisible, la somme des lignes ne correspond pas au total (Standard et Premium), le numéro de facture existe déjà (Standard et Premium), ou l'IA signale qu'elle n'est pas sûre d'une valeur. Les règles exactes sont écrites avec vous à l'étape 2.
- Taux de lecture : part des champs lus correctement sur vos documents de test, comparés à votre lecture, champ par champ.

## Paliers

| | Essentiel | Standard | Premium |
|---|---|---|---|
| Prix | 49 € | 169 € | 429 € |
| Délai | 3 jours | 7 jours | 14 jours |
| Révisions | 1 | 2 | 3 + 14 jours de support |
| Types de documents | 1 | 3 | jusqu'à 5 |
| Destination | 1 (Google Sheets, Excel ou CSV) | 1 | Google Sheets/Excel + base Supabase + export |
| Test sur vos documents | 10 documents | 20 par type | 20 par type |
| Taux de lecture mesuré et communiqué | oui | oui | oui |
| Contrôles de cohérence (totaux, doublons) | non | oui | oui |
| Alerte sur les cas douteux | non (champs manquants seulement signalés) | oui | oui |
| Flux complet (boîte mail ou dossier, extraction, base, export) | non | non | oui |
| Validation humaine intégrée (écran de relecture) | non | non | oui |
| Documentation | 1 page | 2-3 pages | complète |

Logique de prix : Essentiel à 49 €, dans la médiane marché (33-55 €), avec un test de 10 documents pour rester tenable en temps ; niche sans concurrent vu ; upsell naturel vers les contrôles de cohérence puis le flux complet. Tarif de lancement à relever après les premiers avis (Baptiste décide). Le coût API par document n'est pas dans le prix : estimation donnée avant commande.

## Options (extras)
- Type de document supplémentaire : +39 €
- Destination supplémentaire (Sheets, Excel, Supabase, email récapitulatif) : +25 €
- Contrôle de cohérence supplémentaire sur mesure (ex. TVA, IBAN, bon de commande) : +19 €
- 10 documents de test supplémentaires (Essentiel) : +15 €
- Contrôles de cohérence et alerte sur les cas douteux (Essentiel) : +59 €
- Écran de validation humaine (Standard) : +69 €
- Photos et scans de mauvaise qualité (prétraitement) : +29 €
- Visio 30 min : +35 €
- Livraison express 48 h (Essentiel) : +39 €
- Support 30 jours après livraison : +69 €

## Texte à coller par palier
====
Essentiel (49 € / 3 jours) :
Extraction de 1 type de document (ex. factures fournisseurs) vers 1 destination (Google Sheets, Excel ou CSV), avec n8n et l'IA. Test sur 10 de vos documents, taux de lecture correcte mesuré champ par champ et communiqué, documentation d'1 page. 1 correction.
====
Standard (169 € / 7 jours) :
3 types de documents, contrôles de cohérence (totaux, doublons), alerte sur les cas douteux, test sur 20 documents par type, documentation de 2 à 3 pages. 2 corrections.
====
Premium (429 € / 14 jours) :
Flux complet : boîte mail ou dossier surveillé, extraction, base Supabase, export. Jusqu'à 5 types de documents, écran de validation humaine, test sur 20 documents par type, 14 jours de support. 3 corrections.
====

## Description (à coller)
====
Vous retapez à la main des factures, des bons de livraison ou des CMR dans un tableur : c'est long, ennuyeux et une faute de frappe passe vite. J'automatise cette saisie de factures et de documents PDF vers Excel ou Google Sheets avec n8n et l'IA, avec vos règles de contrôle.

Je suis développeur avec une expérience professionnelle de la logistique : je connais ces documents (références, quantités, dates, numéros de commande, totaux) et leurs pièges. Je mets en place un flux n8n + IA qui lit vos PDF et photos, en extrait les champs utiles et les range dans Google Sheets, Excel ou une base de données.

CE QUE VOUS RECEVEZ
- Un workflow n8n prêt à l'emploi pour le ou les types de document du palier. Un type = une famille de documents aux mêmes champs (par exemple "factures fournisseurs"), quel que soit le fournisseur.
- Un test sur vos vrais documents (10 en Essentiel, 20 par type en Standard et Premium), avec le taux de lecture correcte mesuré champ par champ et communiqué : vous voyez ce qui marche et ce qui ne marche pas.
- Selon le palier : contrôles de cohérence (le total correspond-il aux lignes ? doublon ?), alerte sur les cas douteux, base Supabase, écran de validation humaine.
- Une documentation et vos accès à votre nom.

Cas douteux : un document est marqué "à relire" si un champ obligatoire manque ou est illisible, si la somme des lignes ne correspond pas au total, si le numéro existe déjà, ou si l'IA signale qu'elle n'est pas sûre d'une valeur. Les règles sont écrites avec vous avant de construire.

Les captures de la galerie montrent la logique (lecture de PDF, tableau, cas douteux signalé) sur un prototype avec des factures fictives ; chez vous, elle est construite dans n8n avec une étape IA pour les documents scannés ou mal structurés.

EXEMPLE (illustratif, pas un résultat client)
Une facture PDF arrive dans une boîte Gmail ou un dossier Drive. n8n la récupère, l'IA (API Claude) lit le document et renvoie les champs : fournisseur, numéro de facture, date, lignes, total HT, TVA, total TTC. n8n vérifie que la somme des lignes égale le total et que le numéro n'existe pas déjà, puis ajoute la ligne dans Google Sheets. Si une vérification échoue, la ligne est marquée "à relire" et vous recevez un message.

COMMENT ÇA SE PASSE
1. Vous répondez aux questions et m'envoyez 10 à 20 documents représentatifs selon le palier (anonymisés si nécessaire).
2. Je définis avec vous les champs à extraire et les règles de contrôle, par écrit.
3. Je construis le workflow et je le teste sur vos documents.
4. Je vous remets le taux de lecture correcte mesuré, champ par champ, avec les erreurs relevées, et j'ajuste.
5. Je livre : workflow, documentation, accès. Corrections selon les révisions du palier.

CE QUI N'EST PAS INCLUS
- Le coût API IA par document : à votre charge, estimé sur vos documents avant que vous ne commandiez.
- Les abonnements tiers (n8n, Google Workspace, Supabase au-delà de l'offre gratuite).
- Une précision de 100 % : aucune lecture automatique ne l'est. Je ne promets aucun pourcentage à l'avance : le taux se mesure sur vos documents de test.
- Les documents manuscrits très dégradés ou illisibles à l'oeil nu.
- L'intégration dans un ERP ou logiciel comptable sans API (sur devis).

FAQ
Quels documents sont lus ?
Factures, bons de livraison, bons de commande, CMR, tickets, relevés, PDF texte ou scannés, photos nettes.

Quelle précision ?
Elle dépend de vos documents. On mesure ensemble le taux de lecture sur vos documents de test avant de valider ; pas de promesse chiffrée avant ce test. À l'issue du test, vous décidez de continuer ou non.

Que se passe-t-il quand l'IA hésite ?
Le document est marqué "à relire" (voir la définition des cas douteux plus haut) et vous êtes alerté, plutôt que d'écrire une valeur douteuse sans le dire.

Mes documents sont-ils confidentiels ?
Ils sont envoyés à l'API de l'IA pour être lus, selon les conditions de son fournisseur. Pour des documents sensibles (données de santé, bancaires), dites-le avant de commander : je vous indique si je peux m'en charger.

Combien coûte la lecture ?
Chaque document consomme un peu de crédit API, à votre charge. Je vous donne une estimation chiffrée sur vos documents avant la commande.

Faut-il avoir n8n ?
Non, je vous guide pour l'installation (cloud ou serveur) ; le flux vous appartient.

Et si le résultat ne me convient pas ?
Je corrige dans les révisions du palier jusqu'à ce que le flux fonctionne conformément au périmètre écrit. Si, à l'issue du test, le taux de lecture n'est pas acceptable pour vous, nous arrêtons là d'un commun accord : l'annulation passe par la procédure d'annulation de commande de ComeUp.

Écrivez-moi avant de commander avec un exemple de document (anonymisé) : je vous dis ce qui est lisible, le palier adapté et le coût API estimé (réponse sous 48 h ouvrées).
====

## Consignes à l'acheteur (questions à la commande)
1. Quel(s) type(s) de document (factures, BL, CMR...) et en quel volume par mois ?
2. Format : PDF texte, scans, photos de téléphone ?
3. Quels champs voulez-vous extraire (liste précise) ?
4. Où doivent aller les données (Google Sheets, Excel, base) et quelles colonnes ?
5. Comment arrivent vos documents (mail, dossier, upload) ?
6. Quelles vérifications voulez-vous (total = somme des lignes, doublons, fournisseur connu) ?
7. Pouvez-vous m'envoyer 10 à 20 documents représentatifs, anonymisés si besoin ? Y a-t-il des contraintes de confidentialité ?

## Tags (5)
extraction de données, saisie de factures, OCR IA, n8n, automatisation

## Brief image de couverture
- Format : paysage 16:9, vignette claire type YouTube, même gabarit que S1 et S2.
- Texte sur l'image (5 mots) : "PDF vers tableur, par IA", en gros, 2 lignes, police grasse sans empattement, lisible à 200 px.
- Fond : dégradé vert sombre (#052E2B) vers vert (#0F766E) ; texte blanc, "tableur" en jaune (#FACC15).
- Visuel : à gauche, un document PDF stylisé (lignes grises, coin plié, aucune donnée réelle) ; une flèche ; à droite, une grille de tableur avec colonnes vertes remplies de valeurs fictives. Petit nom "n8n" en texte en bas.
- Pas de visage, pas de logos de marques tierces, pas de faux chiffres ni badge.
- À tester à 200 px de large avant publication.

## Preuves (à joindre)
Galerie ComeUp, dans cet ordre. Toutes les images portent la mention "Exemple - données fictives". Les captures montrent la logique sur un prototype en Python local (code réel, données fictives) : elles ne montrent ni n8n ni IA générative. Chez le client, la logique est construite dans n8n avec une étape IA pour les documents scannés ou mal structurés. Ne jamais présenter ces captures comme un workflow n8n livré.
Le prototype lit le texte de PDF fictifs avec des règles fixes (extraction déterministe) ; l'étape IA n'est pas illustrée.
- livrables/comeup/assets/S3-couverture.png : couverture 1280x720 (les mots "par IA" et "n8n" désignent l'offre, pas la démo).
- livrables/comeup/assets/S3-1-pdf-entree.png. Légende : "Entrée : facture PDF fictive et champs lus."
- livrables/comeup/assets/S3-2-tableau-extrait.png. Légende : "Sortie : 8 factures converties en tableau, 4 marquées à vérifier."
- livrables/comeup/assets/S3-3-incoherence.png. Légende : "Cas douteux signalé : HT + TVA ne correspond pas au TTC. Aucune correction automatique."
- Vidéo de démo 60-90 s (flux n8n réel, facture fictive vers ligne Sheets, cas douteux marqué) : à enregistrer par Baptiste, hors atelier.
