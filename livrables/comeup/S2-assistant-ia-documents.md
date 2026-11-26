# S2 - Chatbot IA qui répond aux clients depuis vos documents

Les blocs entre les lignes ==== sont à coller tels quels dans ComeUp : texte brut, sans Markdown (pas de ** ni de ->), listes avec "- " et numéros "1.".
Prix = prix affiché acheteur (benchmark). À la création, saisir le prix vendeur qui donne ce prix affiché (~ prix / 1,102) et contrôler au checkout. Limite de titre ComeUp non vérifiée : titre gardé nettement sous 80 caractères.
À confirmer par Baptiste avant publication : les ordres de grandeur de coûts tiers (n8n, serveur, Supabase, API IA) sont à revérifier sur les sites des fournisseurs ; le délai de réponse "sous 48 h ouvrées".

## Titre (78 caractères)
Je vais créer un chatbot IA pour votre boutique en ligne, depuis vos documents
(ComeUp impose "Je vais" : saisir "créer un chatbot IA pour votre boutique en ligne, depuis vos documents")

## Catégorie
Programmation & Tech > Automatisation (alternative : Chatbot / IA si une catégorie dédiée existe, à voir à la création)

## Paliers

| | Essentiel | Standard | Premium |
|---|---|---|---|
| Prix | 55 € | 249 € | 549 € |
| Délai | 5 jours | 10 jours | 18 jours |
| Révisions | 1 | 2 | 3 + 14 jours de réglages |
| Chatbot sur votre site (widget) | 1 | 1 | 1 |
| Documents / FAQ intégrés (1 document = 1 PDF ou page de 20 pages maximum) | jusqu'à 10 | jusqu'à 50 | jusqu'à 100 |
| Règles de ton et de contenu | oui | oui | oui |
| Test avec des questions réelles | 10 questions | 20 questions | 20 questions |
| "Je ne sais pas" paramétré | oui | oui | oui |
| Transfert à un humain par email | non (option +49 €) | oui | oui |
| Historique des conversations (nécessite une base Supabase) | non (option +39 €) | oui | oui |
| Limite de coût API réglée (plafond mensuel : alerte ou coupure au-delà du montant choisi) | non | oui | oui |
| 1 intégration au choix (Google Calendar/Calendly pour un agenda, ou un CRM avec API comme HubSpot) | non | non | oui |
| Tableau des questions sans réponse | non | non | oui |
| Documentation | 1 page | doc d'exploitation + guide de mise à jour | doc d'exploitation + guide de mise à jour |
| Hébergement et coûts tiers | voir description | idem | idem |

Logique de prix : l'Essentiel à 55 € (10 documents, sans base Supabase) reste dans la médiane marché d'un nouveau vendeur (33-55 €) pour obtenir les premiers avis ; les chatbots déjà notés démarrent à 110-220 €. Standard et Premium portent le panier. Les options (transfert humain 49 € + historique 39 € + 40 documents 58 € + guide de mise à jour 25 €, soit 171 €) couvrent l'essentiel de l'écart Essentiel-Standard (194 €) ; le reste correspond au temps de mise en place plus complexe du Standard (base Supabase, limite de coût API). WhatsApp n'est pas dans les paliers : voir exclusions. Tarif de lancement à relever après les premiers avis (Baptiste décide).

## Options (extras)
- 20 documents supplémentaires : +29 €
- Langue supplémentaire : +25 €
- Transfert à un humain par email (Essentiel) : +49 €
- Historique des conversations (Essentiel) : +39 €
- Guide de mise à jour de vos documents (Essentiel) : +25 €
- Mise à jour de la base par mes soins à partir de vos nouveaux documents (par mise à jour) : +25 €
- Intégration supplémentaire (agenda, CRM, Google Sheets) : +79 €
- Version email : le chatbot prépare un brouillon de réponse à vos emails entrants : +99 €
- WhatsApp : sur devis, après vérification des contraintes Meta (compte Business, coûts) : +149 € de mise en place si faisable
- Visio 30 min : +35 €
- Support 30 jours après livraison : +69 €

## Texte à coller par palier
====
Essentiel (55 € / 5 jours) :
1 chatbot IA en widget sur votre site, basé sur jusqu'à 10 de vos documents ou FAQ (1 document = 1 PDF ou page de 20 pages maximum), avec règles de ton, réponse "je ne sais pas" quand l'information manque, test avec 10 questions, documentation d'1 page. 1 correction.
====
Standard (249 € / 10 jours) :
Essentiel + test porté à 20 questions, jusqu'à 50 documents, transfert à un humain par email, historique des conversations (base Supabase à votre nom), un plafond mensuel de dépense API réglé pour vous, documentation d'exploitation + guide de mise à jour de vos documents. 2 corrections.
====
Premium (549 € / 18 jours) :
Standard + jusqu'à 100 documents, 1 intégration au choix (Google Calendar/Calendly pour un agenda, ou un CRM avec API comme HubSpot), tableau des questions sans réponse, 14 jours de réglages. 3 corrections.
====

## Description (à coller)
====
Vos clients posent chaque jour les mêmes questions (délais, retours, tarifs, fonctionnement) et vous y répondez à la main. Je crée un chatbot IA pour votre boutique en ligne ou votre site : il répond à partir de VOS documents (il peut se tromper : voir les limites plus bas) et, à partir du palier Standard, vous passe le relais quand il ne sait pas.

Je suis développeur avec une expérience professionnelle de la logistique, donc habitué aux questions de livraison, de retour et de suivi. Le chatbot est intégré à votre site et s'appuie sur les documents que vous me fournissez.

CE QUE VOUS RECEVEZ
- Un chatbot en widget à intégrer sur votre site (une ligne de code à coller).
- Une base de connaissances construite à partir de vos documents (FAQ, CGV, fiches produits, procédures) : un document compte pour 1 PDF ou 1 page de 20 pages maximum ; au-delà, il compte pour plusieurs, au prorata.
- Un ton réglé selon vos consignes (vouvoiement, style, ce qu'il ne doit jamais dire).
- Un test avec vos questions réelles (10 en Essentiel, 20 en Standard et Premium), avec les réponses relues ensemble.
- Selon le palier : transfert à un humain par email, historique des conversations, plafond de dépense API réglé, tableau des questions sans réponse, guide de mise à jour.

Les captures de la galerie viennent d'un prototype en Python sur une FAQ fictive : il retrouve le passage utile, puis Claude (IA) rédige la réponse à partir de ce seul passage, en citant la source, et répond "je ne sais pas" hors périmètre ; la question sans réponse est seulement enregistrée dans un journal (pas d'e-mail envoyé dans la démo). Ce prototype n'est pas un workflow n8n ; chez vous, le chatbot est construit dans n8n avec l'API Claude.

EXEMPLE (illustratif, pas un résultat client)
Une cliente écrit sur votre boutique : "Je peux retourner une robe achetée il y a trois semaines ?" Le chatbot retrouve la règle dans vos conditions de retour et répond avec cette règle, en citant votre politique. Si la réponse n'est pas dans vos documents, il répond "Je n'ai pas cette information" et, à partir du Standard, vous envoie la question par email, avec les coordonnées laissées par la cliente (palier Standard et au-dessus).
Côté technique, pour les curieux : n8n, base Supabase et API Claude (Anthropic).

OÙ TOURNE VOTRE CHATBOT ET CE QUE ÇA COÛTE
- Le widget se colle sur votre site (WordPress, Shopify, Wix, site sur mesure).
- Le chatbot tourne sur un compte n8n (cloud ou petit serveur), ouvert à votre nom. L'IA est appelée via un compte API à votre nom. À partir du Standard, une base Supabase à votre nom stocke l'historique des conversations et facilite la mise à jour de vos documents ; en Essentiel, la base de connaissances reste directement dans n8n. Je ne vous héberge rien et ne conserve aucun accès après la livraison.
- Coûts payés directement aux fournisseurs, ordre de grandeur pour une petite boutique : n8n cloud ou serveur environ 5 à 25 € par mois, Supabase 0 € à l'offre gratuite (à partir du Standard), API IA quelques euros selon le nombre de conversations. Soit environ 5 à 30 € par mois. Je vous donne une estimation chiffrée avant que vous commandiez.

COMMENT ÇA SE PASSE
1. Vous répondez aux questions de commande et m'envoyez vos documents.
2. Je prépare la base de connaissances et définis avec vous les règles de ton et de contenu.
3. Je construis le chatbot et le widget.
4. Test avec vos questions (10 ou 20 selon le palier) : nous relisons les réponses, j'ajuste.
5. Je livre le code, la documentation et vos accès. Corrections selon les révisions du palier.

CE QUI N'EST PAS INCLUS
- Les coûts d'API IA (usage) et les abonnements tiers (n8n, serveur, base de données au-delà de l'offre gratuite), à votre charge.
- WhatsApp, Messenger, téléphone : non compris. WhatsApp est possible en option après vérification des contraintes Meta.
- Un service client 100 % autonome : un chatbot IA peut se tromper. Je mets en place des garde-fous (réponse basée sur vos documents, "je ne sais pas", transfert à un humain), pas une garantie d'exactitude.
- La rédaction de vos documents (je travaille sur ce que vous avez).
- La conformité juridique de votre site (mention d'information RGPD, conditions) : à votre charge.

FAQ
Le chatbot peut-il inventer des réponses ?
Il est limité à vos documents et paramétré pour dire "je ne sais pas" quand l'information manque. Le risque d'erreur n'est pas nul : c'est pourquoi on teste avec vos questions réelles avant la livraison.

Quels documents puis-je fournir ?
PDF, Word, pages web, FAQ en texte, tableaux simples.

Sur quels sites marche-t-il ?
Tout site où vous pouvez ajouter un script (WordPress, Shopify, Wix, site sur mesure). Je vérifie avec vous avant de démarrer.

Que coûte son fonctionnement ?
Environ 5 à 30 € par mois pour une petite boutique (n8n, base de données, usage de l'IA), payés directement aux fournisseurs. Je vous donne une estimation chiffrée avant commande et, dans le Standard, je règle une limite de dépense.

Et si mes documents changent ?
À partir du Standard, vous recevez un guide de mise à jour pour recharger vos documents vous-même. Dans l'Essentiel, le guide est en option (+25 €). Je peux aussi faire la mise à jour pour vous (option).

Que deviennent les conversations de mes clients ?
Les questions sont envoyées au fournisseur d'IA (Anthropic) pour générer la réponse, selon ses conditions d'utilisation. Avec l'historique (Standard et Premium), elles sont conservées dans votre base Supabase, à votre nom. Informer vos visiteurs (RGPD) reste à votre charge.

Qui est propriétaire du chatbot ?
Vous : code, base et clés API à votre nom.

Et si ça ne me convient pas ?
Je corrige jusqu'à ce que le chatbot fonctionne conformément au périmètre écrit, dans les révisions du palier. Un changement de périmètre passe par une option.

Écrivez-moi avant de commander avec l'adresse de votre site et une question que vos clients posent souvent : je vous dis si c'est adapté et quel palier choisir (réponse sous 48 h ouvrées).
====

## Consignes à l'acheteur (questions à la commande)
1. Adresse de votre site et outil utilisé (WordPress, Shopify, autre).
2. Les 10 questions que vos clients posent le plus.
3. Quels documents me fournissez-vous (liste, formats, nombre approximatif) ?
4. Ton souhaité (tutoiement ou vouvoiement, style) et sujets que le chatbot ne doit jamais aborder.
5. Que doit-il faire quand il ne sait pas (transmettre par email, à quelle adresse) ?
6. Nombre de visiteurs par mois (pour estimer le coût API) ?
7. Langue(s) de réponse ?

## Tags (5)
chatbot IA, chatbot site web, assistant IA, e-commerce, service client

## Brief image de couverture
- Format : paysage 16:9, vignette claire type YouTube, même gabarit que S1 et S3.
- Texte sur l'image, aligné sur la couverture livrée : "Votre assistant IA répond", en gros, 2 lignes, police grasse sans empattement, lisible à 200 px (le mot "chatbot" reste dans le titre de l'annonce).
- Fond : dégradé violet sombre (#2E1065) vers violet (#6D28D9) ; texte blanc, accent jaune (#FACC15).
- Visuel : à droite, une bulle de chat avec une question fictive et une réponse (la bulle "30 jours après réception" n'apparaît dans aucune capture de la galerie : illustration, pas une réponse démontrée) ; à gauche, une pile de documents qui alimente la bulle (flèche). Pas de vraie donnée client.
- Pas de visage, pas de logos de tiers, pas de faux avis, de notes en étoiles ni de badge.
- À tester à 200 px de large avant publication.

## Preuves (à joindre)
Galerie ComeUp, dans cet ordre. Toutes les images portent la mention "Exemple - données fictives". Les captures viennent d'un prototype en Python local (code réel, FAQ fictive) avec une vraie étape IA : la recherche retrouve le passage, puis Claude rédige la réponse à partir de ce seul passage ; la source est citée et, hors périmètre, la réponse est "je ne sais pas" et la question est enregistrée dans un journal (aucun e-mail envoyé). Le prototype n'est pas un workflow n8n (chez le client, la logique est construite dans n8n avec l'API Claude) et n'a pas été testé sur de vrais documents clients. Ne jamais présenter ces captures comme un chatbot livré.
- livrables/comeup/assets/S2-couverture.png : couverture 1280x720.
- livrables/comeup/assets/S2-1-reponse-sourcee.png. Légende : "Réponses rédigées par Claude à partir du passage de la FAQ, avec la source citée (données fictives)."
- livrables/comeup/assets/S2-2-hors-perimetre.png. Légende : "Hors périmètre : il dit qu'il ne sait pas ; la question est enregistrée dans le journal de l'équipe (aucun e-mail envoyé dans cette démo). Le transfert à un humain par e-mail est inclus à partir du palier Standard, non démontré ici."
- livrables/comeup/assets/S2-3-questions-sans-reponse.png. Légende : "Journal des questions sans réponse, pour compléter la FAQ."
- Vidéo de démonstration (63 s) livrée avec la fiche : livrables/comeup/videos/S2.mp4 (prototype Python réel sur FAQ fictive, réponses rédigées par Claude, question hors périmètre journalisée, aucun e-mail envoyé). Démo sur données fictives, pas un résultat client.
