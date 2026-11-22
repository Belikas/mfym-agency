# S2 - Chatbot IA qui répond aux clients depuis vos documents

Les blocs entre les lignes ==== sont à coller tels quels dans ComeUp : texte brut, sans Markdown (pas de ** ni de ->), listes avec "- " et numéros "1.".
Prix = prix affiché acheteur (benchmark). À la création, saisir le prix vendeur qui donne ce prix affiché (~ prix / 1,102) et contrôler au checkout. Limite de titre ComeUp non vérifiée : titre gardé nettement sous 80 caractères.
À confirmer par Baptiste avant publication : les ordres de grandeur de coûts tiers (n8n, serveur, Supabase, API IA) sont à revérifier sur les sites des fournisseurs ; le délai de réponse "sous 48 h ouvrées".

## Titre (73 caractères)
Je vais créer un chatbot IA qui répond à vos clients depuis vos documents
(ComeUp impose "Je vais" : saisir "créer un chatbot IA qui répond à vos clients depuis vos documents")

## Catégorie
Programmation & Tech > Automatisation (alternative : Chatbot / IA si une catégorie dédiée existe, à voir à la création)

## Paliers

| | Essentiel | Standard | Premium |
|---|---|---|---|
| Prix | 59 € | 249 € | 549 € |
| Délai | 4 jours | 10 jours | 18 jours |
| Révisions | 1 | 2 | 3 + 14 jours de réglages |
| Chatbot sur votre site (widget) | 1 | 1 | 1 |
| Documents / FAQ intégrés | jusqu'à 10 | jusqu'à 50 | jusqu'à 100 |
| Règles de ton et de contenu | oui | oui | oui |
| Test avec 20 questions | oui | oui | oui |
| "Je ne sais pas" paramétré | oui | oui | oui |
| Transfert à un humain par email | non (option +49 €) | oui | oui |
| Historique des conversations | non (option +39 €) | oui | oui |
| Limite de coût API réglée | non | oui | oui |
| 1 intégration (agenda ou CRM) | non | non | oui |
| Tableau des questions sans réponse | non | non | oui |
| Documentation | 1 page | doc d'exploitation + guide de mise à jour | doc d'exploitation + guide de mise à jour |
| Hébergement | voir bloc "Où tourne votre chatbot" | idem | idem |

Où tourne votre chatbot (identique à tous les paliers) : le widget se colle sur votre site (une ligne de code). Le "cerveau" du chatbot tourne sur un compte n8n (cloud ou petit serveur) et une base Supabase, tous deux ouverts à votre nom ; l'IA est appelée via un compte API à votre nom. Je ne vous héberge rien et ne garde aucun accès après livraison.
Coûts mensuels payés par vous directement aux fournisseurs (ordre de grandeur pour une petite boutique, estimation chiffrée avant commande) : n8n cloud ou serveur environ 5 à 25 € / mois, Supabase 0 € à l'offre gratuite, API IA quelques euros selon le nombre de conversations. Total courant : environ 5 à 30 € / mois.

Logique de prix : l'Essentiel à 59 € (10 documents) se place en haut de la médiane marché d'un nouveau vendeur (33-55 €) pour obtenir les premiers avis ; les chatbots déjà notés démarrent à 110-220 €, donc 59 € reste très accessible tout en couvrant un vrai travail (base de connaissances, widget, test de 20 questions). Standard et Premium portent le panier. Options alignées sur l'écart de palier : transfert humain (49) + historique (39) + 40 documents (58) + guide de mise à jour ≈ écart Essentiel-Standard (190 €). WhatsApp n'est pas dans les paliers : voir exclusions. Tarif de lancement à relever après les premiers avis (Baptiste décide).

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
Essentiel (59 € / 4 jours) :
1 chatbot IA en widget sur votre site, basé sur jusqu'à 10 de vos documents ou FAQ, avec règles de ton, réponse "je ne sais pas" quand l'information manque, test avec 20 questions, documentation d'1 page. 1 correction.
====
Standard (249 € / 10 jours) :
Essentiel + jusqu'à 50 documents, transfert à un humain par email, historique des conversations, limite de coût API réglée, documentation d'exploitation + guide de mise à jour de vos documents. 2 corrections.
====
Premium (549 € / 18 jours) :
Standard + jusqu'à 100 documents, 1 intégration (agenda ou CRM), tableau des questions sans réponse, 14 jours de réglages. 3 corrections.
====

## Description (à coller)
====
Vos clients posent chaque jour les mêmes questions (délais, retours, tarifs, fonctionnement) et vous y répondez à la main. Je crée un chatbot IA pour votre boutique en ligne ou votre site : il répond à partir de VOS documents et vous passe le relais quand il ne sait pas.

Je suis développeur avec une expérience professionnelle de la logistique, donc habitué aux questions de livraison, de retour et de suivi. Je crée un chatbot sur mesure, intégré à votre site, qui répond uniquement à partir des documents que vous me fournissez.

CE QUE VOUS RECEVEZ
- Un chatbot en widget à intégrer sur votre site (une ligne de code à coller).
- Une base de connaissances construite à partir de vos documents (FAQ, CGV, fiches produits, procédures).
- Un ton réglé selon vos consignes (vouvoiement, style, ce qu'il ne doit jamais dire).
- Un test avec 20 questions réelles, avec les réponses relues ensemble.
- Selon le palier : transfert à un humain par email, historique des conversations, limite de coût, tableau des questions sans réponse, guide de mise à jour.

Les captures de la galerie montrent la logique (réponse sourcée, "je ne sais pas", journal des questions) sur un prototype avec une FAQ fictive ; chez vous, elle est construite dans n8n avec une étape IA.

EXEMPLE (illustratif, pas un résultat client)
Une cliente écrit sur votre boutique : "Je peux retourner une robe achetée il y a trois semaines ?" Le chatbot retrouve la règle dans vos conditions de retour et répond avec cette règle, en citant votre politique. Si la réponse n'est pas dans vos documents, il répond "Je n'ai pas cette information" et vous envoie la question par email, avec les coordonnées laissées par la cliente (palier Standard et au-dessus).
Côté technique, pour les curieux : n8n, base Supabase et API Claude (Anthropic).

OÙ TOURNE VOTRE CHATBOT ET CE QUE ÇA COÛTE
- Le widget se colle sur votre site (WordPress, Shopify, Wix, site sur mesure).
- Le chatbot tourne sur un compte n8n (cloud ou petit serveur) et une base Supabase, ouverts à votre nom. L'IA est appelée via un compte API à votre nom. Je ne vous héberge rien et ne conserve aucun accès après la livraison.
- Coûts payés directement aux fournisseurs, ordre de grandeur pour une petite boutique : n8n cloud ou serveur environ 5 à 25 € par mois, Supabase 0 € à l'offre gratuite, API IA quelques euros selon le nombre de conversations. Soit environ 5 à 30 € par mois. Je vous donne une estimation chiffrée avant que vous commandiez.

COMMENT ÇA SE PASSE
1. Vous répondez aux questions de commande et m'envoyez vos documents.
2. Je prépare la base de connaissances et définis avec vous les règles de ton et de contenu.
3. Je construis le chatbot et le widget.
4. Test avec 20 questions : nous relisons les réponses, j'ajuste.
5. Je livre le code, la documentation et vos accès. Corrections selon les révisions du palier.

CE QUI N'EST PAS INCLUS
- Les coûts d'API IA (usage) et les abonnements tiers (n8n, serveur, base de données au-delà de l'offre gratuite), à votre charge.
- WhatsApp, Messenger, téléphone : non compris. WhatsApp est possible en option après vérification des contraintes Meta.
- Un service client 100 % autonome : un chatbot IA peut se tromper. Je mets en place des garde-fous (réponse basée sur vos documents, "je ne sais pas", transfert à un humain), pas une garantie d'exactitude.
- La rédaction de vos documents (je travaille sur ce que vous avez).
- La conformité juridique de votre site (mention d'information RGPD, conditions) : à votre charge.

FAQ
Le chatbot peut-il inventer des réponses ?
Il est limité à vos documents et paramétré pour dire "je ne sais pas" quand l'information manque. Le risque d'erreur n'est pas nul : c'est pourquoi on teste avec 20 questions avant la livraison.

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

Écrivez-moi avant de commander avec l'adresse de votre site et 3 questions que vos clients posent souvent : je vous dis si c'est adapté et quel palier choisir (réponse sous 48 h ouvrées).
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
chatbot IA, chatbot site web, assistant IA, base de connaissances, service client

## Brief image de couverture
- Format : paysage 16:9, vignette claire type YouTube, même gabarit que S1 et S3.
- Texte sur l'image (5 mots) : "Chatbot IA pour votre site", en gros, 2 lignes, police grasse sans empattement, lisible à 200 px.
- Fond : dégradé violet sombre (#2E1065) vers violet (#6D28D9) ; texte blanc, "Chatbot" en jaune (#FACC15).
- Visuel : à droite, une bulle de chat avec question courte fictive ("Délai de retour ?") et une réponse ; à gauche, une pile de documents qui alimente la bulle (flèche). Pas de vraie donnée client.
- Pas de visage, pas de logos de tiers, pas de faux avis, de notes en étoiles ni de badge.
- À tester à 200 px de large avant publication.

## Preuves (à joindre)
Galerie ComeUp, dans cet ordre. Toutes les images portent la mention "Exemple - données fictives". Les captures montrent la logique sur un prototype en Python local (code réel, données fictives) : elles ne montrent ni n8n ni IA générative. Chez le client, la logique est construite dans n8n avec l'IA (API Claude) pour formuler la réponse à partir de vos documents. Ne jamais présenter ces captures comme un workflow n8n livré.
Le prototype est une recherche par mots-clés dans une FAQ fictive, avec sources et "je ne sais pas" ; il ne montre pas de génération de réponse par IA.
- livrables/comeup/assets/S2-couverture.png : couverture 1280x720 (le mot "IA" désigne l'offre, pas la démo).
- livrables/comeup/assets/S2-1-reponse-sourcee.png. Légende : "L'assistant répond à partir de votre document et cite la section source."
- livrables/comeup/assets/S2-2-hors-perimetre.png. Légende : "Hors périmètre : il dit qu'il ne sait pas et transmet la question à l'équipe."
- livrables/comeup/assets/S2-3-questions-sans-reponse.png. Légende : "Journal des questions sans réponse, pour compléter la FAQ."
- Vidéo de démo 60-90 s + lien public vers une page de test du widget (version réelle avec IA) : à produire par Baptiste, hors atelier.
