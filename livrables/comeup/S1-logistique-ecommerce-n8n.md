# S1 - Automatisation logistique et e-commerce (n8n + IA)

Les blocs entre les lignes ==== sont à coller tels quels dans ComeUp : texte brut, sans Markdown (pas de ** ni de ->), listes avec "- " et numéros "1.".
Prix = prix affiché acheteur (benchmark). À la création, saisir le prix vendeur qui donne ce prix affiché (~ prix / 1,102) et contrôler au checkout. Limite de titre ComeUp non vérifiée : titre gardé nettement sous 80 caractères.
À confirmer par Baptiste avant publication : (1) le délai de réponse "sous 48 h ouvrées" est tenable avec son emploi ; (2) la charge réelle du Premium (4 workflows + Supabase + installation en 14 jours).

## Titre (71 caractères)
Je vais automatiser vos flux logistiques et e-commerce avec n8n et l'IA
(ComeUp impose "Je vais" : saisir seulement "automatiser vos flux logistiques et e-commerce avec n8n et l'IA")

## Catégorie
Programmation & Tech > Automatisation (à confirmer dans le menu à la création)

## Paliers

| | Essentiel | Standard | Premium |
|---|---|---|---|
| Prix | 49 € | 149 € | 349 € |
| Délai | 3 jours | 7 jours | 14 jours |
| Révisions | 1 | 2 | 3 + 7 jours de support |
| Workflows | 1 (1 déclencheur, 2 outils, 5 nœuds max) | 2 | jusqu'à 4, liés entre eux |
| Canaux de notification | 1 au choix (mail, Slack ou Telegram) | 2 au choix (mail, Slack, Telegram) | les 3 (mail, Slack, Telegram) |
| Étape IA (classement, résumé, rédaction du message) | non | 1 | 2 |
| Journal des erreurs | non | oui | oui |
| Base Supabase + tableau de suivi | non | non | oui |
| Installation de n8n à votre nom (cloud ou serveur) | non (option +49 €) | non (option +49 €) | oui, comprise |
| Test sur vos données ("testé" = 3 exécutions réussies de suite sur vos données ou un extrait) | oui | oui | oui |
| Documentation | 1 page | 2 à 3 pages | complète + schéma des flux |
| Vidéo de démonstration (écran) | option | incluse | incluse |

Logique de prix : Essentiel sous la médiane marché (33-55 €) pour obtenir les premiers avis ; Standard = palier visé ; Premium = vrai petit projet. Les options sont alignées sur l'écart Standard-Premium (200 €) : 2 workflows en plus (78 €) + Supabase (59 €) + installation (49 €) + 1 étape IA (29 €) = 215 €. Tarif de lancement à relever après les premiers avis (Baptiste décide).

## Options (extras)
- Workflow supplémentaire : +39 € (+2 jours)
- Étape IA supplémentaire (classement, extraction, rédaction) : +29 €
- Connecteur supplémentaire (Shopify, WooCommerce, Google Sheets, Airtable, API transporteur) : +19 €
- Base Supabase + tableau de suivi (Standard) : +59 €
- Installation de n8n à votre nom, cloud ou serveur (Essentiel, Standard) : +49 €
- Vidéo de démonstration (Essentiel) : +15 €
- Visio de prise en main 30 min : +35 €
- Livraison express 48 h (Essentiel) : +39 €
- Support 30 jours après livraison : +69 €

## Texte à coller par palier
====
Essentiel (49 € / 3 jours) :
1 workflow n8n sur mesure (1 déclencheur, 2 outils connectés, 5 nœuds maximum), 1 canal de notification au choix (mail, Slack ou Telegram), testé sur vos données (3 exécutions réussies de suite), livré en fichier JSON importable + 1 page de documentation. 1 correction incluse.
====
Standard (149 € / 7 jours) :
2 workflows, notifications sur 2 canaux au choix (mail, Slack, Telegram), journal des erreurs, 1 étape IA (classement ou résumé), documentation de 2 à 3 pages, vidéo de démonstration. 2 corrections incluses.
====
Premium (349 € / 14 jours) :
Jusqu'à 4 workflows liés, notifications mail + Slack + Telegram, base Supabase et tableau de suivi, installation de n8n à votre nom (cloud ou serveur), 2 étapes IA, documentation complète avec schéma, 7 jours de support après livraison. 3 corrections incluses.
====

## Description (à coller)
====
Un colis en retard, un client qui écrit "Où est ma commande ?", et vous qui recopiez des numéros de suivi dans un tableur. Avec n8n, une alerte Telegram peut vous prévenir dès qu'un colis reste 48 h sans mouvement : ces tâches de suivi de colis se font toutes seules.

Je suis développeur et je connais la logistique de l'intérieur (préparation, expéditions, retards, litiges). Je construis des automatisations n8n qui font ce travail répétitif à votre place : vous êtes prévenu quand un colis est bloqué, le client reçoit son suivi sans que vous touchiez à rien, et vos commandes arrivent dans un tableau propre.

Les captures de la galerie montrent la logique sur un prototype avec des données fictives ; chez vous, elle est construite dans n8n, avec une étape IA selon le palier.

CE QUE VOUS RECEVEZ
- Des workflows n8n prêts à importer (fichier JSON), connectés à vos outils, testés sur vos données (3 exécutions réussies de suite).
- Une documentation claire : ce que fait chaque étape, où modifier un réglage, que faire si une alerte tombe.
- Les accès et les clés API à votre nom : rien ne dépend de moi après la livraison.
- Selon le palier : un journal des erreurs, une étape IA, une base Supabase avec tableau de suivi, une vidéo de démonstration.

EXEMPLES DE FLUX QUE JE PEUX CONSTRUIRE (exemples illustratifs, pas des réalisations passées)
- Alerte retard transporteur : une commande Shopify est expédiée, n8n enregistre son numéro de suivi, vérifie le statut toutes les heures et, sans mouvement depuis 48 h, vous envoie un message (mail, Slack ou Telegram) avec le numéro de commande et le client concerné, puis met à jour votre tableau de suivi.
- Suivi automatique au client : à l'expédition, le client reçoit un mail avec son lien de suivi. En cas de retard, un message d'excuse est préparé par l'IA ; vous le validez, ou il part automatiquement, au choix.
- Rapprochement commandes et stock : les commandes Shopify ou WooCommerce sont écrites dans Google Sheets ou Supabase, avec une alerte quand le stock passe sous un seuil.
- Relance de réclamations : les mails "colis non reçu" sont classés par l'IA (retard, perdu, abîmé) et un ticket est créé dans votre tableau.

COMMENT ÇA SE PASSE
1. Vous répondez à mes questions (outils, volumes, règles de gestion). Je vous confirme par écrit ce qui est faisable avant de démarrer.
2. Je construis le workflow sur une copie, avec des données de test.
3. Je teste sur vos vraies données (ou un extrait) et je corrige.
4. Je livre : fichier JSON, documentation, vidéo selon palier.
5. Vous validez ; je corrige ce qui ne correspond pas au périmètre convenu, dans la limite des révisions du palier.

CE QUI N'EST PAS INCLUS
- Les abonnements tiers : n8n cloud ou serveur, outils connectés, transporteurs. Ils restent à votre charge.
- Les crédits d'API IA : le coût est faible mais réel ; je vous donne une estimation avant de commencer.
- L'accès à l'API d'un transporteur si votre contrat ne l'ouvre pas : dans ce cas je passe par votre outil de suivi existant ou un export mail, et je vous le dis avant.
- Le développement d'une application ou d'un site complet, la formation de votre équipe.
- Aucune promesse de gain de temps ou d'argent chiffré : cela dépend de vos volumes.

FAQ
Quels outils connectez-vous ?
n8n, Shopify, WooCommerce, Google Sheets, Airtable, Gmail/Outlook, Slack, Telegram, Supabase et toute application ayant une API ou un webhook. Dites-moi votre outil avant de commander si vous hésitez.

Faut-il déjà avoir n8n ?
Non. L'installation de n8n à votre nom (cloud ou serveur) est comprise dans le Premium, et disponible en option (+49 €) pour les autres paliers.

Mon transporteur est-il compatible ?
Si une API de suivi existe pour votre compte (ou via un agrégateur de suivi), oui. Sinon je vous propose une alternative avant que vous ne commandiez.

L'IA peut-elle se tromper ?
Oui. Pour les messages clients, je recommande une validation humaine au début ; je règle le niveau d'autonomie avec vous.

À qui appartiennent les workflows ?
À vous. Livrés en JSON, avec vos accès et vos clés API.

Et si ça ne marche pas ?
Je corrige jusqu'à ce que le workflow fonctionne conformément au périmètre écrit, dans les révisions du palier. Un changement de périmètre fait l'objet d'une option.

Je ne suis pas sûr de mon besoin, que faire ?
Écrivez-moi avant de commander : je réponds sous 48 h ouvrées et je vous dis honnêtement si je suis la bonne personne.

Écrivez-moi avant de commander en décrivant votre flux en 3 lignes : je vous dis le palier adapté et ce qui est faisable.
====

## Consignes à l'acheteur (questions à la commande)
1. Quel est le flux à automatiser, en 3 lignes (de quel événement à quel résultat) ?
2. Quels outils utilisez-vous (boutique, transporteur, tableur, messagerie, ERP) ?
3. Volume approximatif : commandes ou colis par jour ?
4. Utilisez-vous déjà n8n ? Si non, préférez-vous le cloud ou un serveur à vous ?
5. Qui doit être alerté, et par quel canal (mail, Slack, Telegram) ?
6. Pouvez-vous fournir un extrait de données (anonymisé si besoin) pour les tests ?
7. Les accès API sont-ils disponibles (Shopify, transporteur) ? Sinon, je vous guide.

## Tags (5)
n8n, automatisation logistique, e-commerce, suivi colis, alerte retard colis

## Brief image de couverture
- Format : paysage 16:9, style vignette claire type YouTube.
- Texte sur l'image (3 mots) : "Automatisez votre logistique", en gros, 2 lignes, police grasse sans empattement, lisible à 200 px de large.
- Fond : dégradé bleu nuit (#0F172A) vers bleu (#1D4ED8) ; texte blanc, "logistique" en jaune (#FACC15).
- Visuel : à gauche, schéma de 3 blocs reliés par des flèches (icône colis, puis nom "n8n", puis icône alerte). Capture réelle de l'éditeur n8n en arrière-plan flouté à 20 % d'opacité, SANS données de tiers.
- Pas de visage, pas de logos de transporteurs, pas de faux chiffres ni badge.
- Même gabarit, même police et mêmes couleurs que S2 et S3 (seule la couleur d'accent change).
- À tester à 200 px de large avant publication.

## Preuves (à joindre)
Galerie ComeUp, dans cet ordre. Toutes les images portent la mention "Exemple - données fictives". Les captures montrent la logique sur un prototype en Python local (code réel, données fictives) : elles ne montrent ni n8n ni IA générative. Chez le client, la logique est construite dans n8n avec, selon le palier, une étape IA. Ne jamais présenter ces captures comme un workflow n8n livré.
- livrables/comeup/assets/S1-couverture.png : couverture 1280x720 (le texte "n8n" désigne l'offre, pas la démo).
- livrables/comeup/assets/S1-1-donnees-entree.png. Légende : "Entrée : export commandes et statuts transporteur (données fictives)."
- livrables/comeup/assets/S1-2-execution.png. Légende : "Le script lit les deux fichiers et détecte 4 expéditions à risque sur 10."
- livrables/comeup/assets/S1-3-sorties.png. Légende : "Sortie : messages clients prêts à envoyer et résumé d'alerte (retard, incident, absence de scan)."
- Vidéo de démo 60-90 s (workflow n8n réel sur données fictives) : à enregistrer par Baptiste, hors atelier. Seule cette vidéo pourra montrer n8n.
