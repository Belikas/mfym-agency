# Pack Claude Code pour la logistique — liste d'attente / précommande

*(Page de pré-vente — produit en construction, pas encore livrable. Voir section "C'est une pré-vente, pas un achat classique" avant de vous engager.)*

## Claude Code pour la logistique : un rapport de stock lisible en quelques minutes, pas une ressaisie à la main

Vous gérez un entrepôt, un flux transport ou des stocks, et une bonne partie de votre semaine part dans des tâches répétitives : lire un export Excel/CSV pour en sortir un résumé, rédiger la même relance transporteur pour la dixième fois, recopier un retard de livraison dans un mail client, croiser deux fichiers pour retrouver une référence introuvable.

Je construis un pack d'assistants (« skills ») pour **Claude Code**, l'outil d'IA en ligne de commande d'Anthropic, pensé spécifiquement pour ces tâches de logistique — pas pour des développeurs. L'idée : vous donnez un fichier ou une consigne en français, l'assistant fait le travail de mise en forme et de rédaction, vous gardez la décision.

Je viens de la logistique avant de coder : ce pack part de problèmes que j'ai vus de l'intérieur, pas d'une liste générique de prompts.

## Pour qui

Gestionnaires d'entrepôt et responsables stocks qui traitent un export Excel/CSV (WMS, inventaire, ruptures) chaque jour, à l'aise pour installer un outil en suivant une notice pas à pas même sans savoir coder. (Les métiers transport et reporting sont aussi visés — voir "Et aussi" plus bas.)

## Pas pour qui

- Vous cherchez un WMS ou un ERP complet : ce pack ne remplace pas votre logiciel métier, il travaille à côté (exports, mails, synthèses).
- Vous voulez un produit livré aujourd'hui : il n'existe pas encore, voir plus bas.
- Vous n'avez jamais ouvert Claude Code et ne voulez pas installer un outil en ligne de commande (même simple) : ce pack ne sera pas pour vous dans cette première version.

## Pourquoi pas un pack gratuit ?

Il existe déjà des packs de skills gratuits et massifs pour Claude Code (par exemple mattpocock/skills ou le pack officiel anthropics/skills, plusieurs centaines de milliers d'installations à eux deux). Ils couvrent très bien le générique dev : revue de code, tests, debug, structure de projet. Ce qu'ils n'ont pas : rien de spécifique à la logistique, aucun vocabulaire métier transport/stock (rupture, surstock, litige transporteur, taux de service), aucun cas d'usage prêt à l'emploi pour ce secteur. Recopier un prompt générique gratuit ne vous fera pas gagner le temps que ce pack vise à vous faire gagner sur vos exports et vos mails de relance — c'est la vraie différence entre payer 19 € et piocher dans le gratuit. Estimation non vérifiée, à confirmer avec les premiers inscrits : viser à passer d'un rapport de stock qui prend aujourd'hui 20-30 min en recopiant à la main, à quelques minutes.

## Cas d'usage visés (exemples concrets, pas une liste de fonctionnalités figée)

Le contenu exact n'est pas arrêté, il sera construit avec les premiers inscrits — à titre indicatif, entre 4 et 6 assistants sont visés pour cette première version, pas plus pour rester testable sérieusement. Le cas d'usage le plus universel, visé en priorité :

**Rapport de stock** : à partir d'un export Excel/CSV de votre WMS, produire un résumé lisible (ruptures, surstocks, références à surveiller) sans reconstruire un tableau croisé à la main.

À quoi ça pourrait ressembler (extrait fictif, à titre d'illustration — le pack n'existe pas encore, aucune sortie réelle n'a été générée) :
> Stock au 20/11 : 3 réf. en rupture (REF-1042, REF-2210, REF-3387) · 2 surstocks à écouler (REF-5501, REF-5598) · 1 écart à vérifier (REF-4120, -40 unités vs dernier inventaire).

**Et aussi**, dans la même logique :
- **Relance transporteur** : mail de relance clair et factuel à partir d'un numéro de colis et d'un motif de retard.
- **Analyse de retard de livraison** : explication structurée à partir d'une date prévue et d'une date réelle, utilisable pour un client ou votre hiérarchie.
- **Synthèse de reporting** : un export de livraison ou de stock transformé en quelques lignes exploitables pour une réunion.

Ces exemples orientent le travail à venir ; ils ne constituent pas une liste de livraison garantie poste par poste.

## Comment ça marchera, une fois livré

1. Vous recevez un fichier ZIP + une notice d'installation en français.
2. Vous l'installez dans Claude Code en suivant 4 étapes maximum (copie des fichiers, une commande à lancer, vérification).
3. Vous ouvrez un de vos fichiers réels (export, mail) et vous testez un cas d'usage.
4. Vous gardez un contact direct avec moi (email) pour signaler un bug ou demander un ajustement : réponse sous 48h ouvrées, mises à jour gratuites incluses pendant 6 mois après la livraison.

Testé avant livraison sur Windows et macOS, sur la version de Claude Code en vigueur au moment de la livraison (pas une version figée aujourd'hui qui serait obsolète d'ici la sortie), avec une notice vérifiée pas à pas — pas un simple copier-coller à l'aveugle. Chaque assistant passera le format SKILL.md standard (vérifié, sans chemin codé en dur) avant livraison. Licence : usage personnel ou professionnel au sein de votre structure, pas de redistribution du pack. Chaque mise à jour pendant les 6 mois inclus arrive avec une note de version datée (ce qui a changé).

## C'est une pré-vente, pas un achat classique

Dites-le-vous clairement avant de vous engager :

- **Le pack n'existe pas encore.** Cette page sert à vérifier qu'il y a assez de monde intéressé avant que je passe du temps à le construire.
- **Date limite de décision : 20 décembre 2026.** Si trop peu de monde s'est inscrit ou a précommandé à cette date, je ne construis pas le pack, je vous le dis, et je rembourse intégralement toute précommande, sans délai de carence.
- **Si le seuil est atteint**, je m'engage à livrer le pack dans les 4 semaines suivant le 20 décembre 2026.
- **Remboursement garanti 14 jours** après la livraison si le pack ne correspond pas à ce qui est décrit ici, aucune question posée.
- **Aucun avis, aucune vente ni aucun compteur de places affiché sur cette page n'est inventé.** À ce stade, il n'y en a pas : c'est la première version de cette offre.

## Deux façons de manifester votre intérêt

- **Liste d'attente gratuite** : laissez votre email, vous êtes prévenu dès que la décision est prise (construction ou abandon), sans engagement.
- **Précommande à tarif de lancement** : 19 € au lieu des 29 € prévus au tarif normal une fois le pack livré. Vous ne payez que si vous choisissez de précommander maintenant ; remboursement intégral automatique si le projet ne se fait pas.

[Je m'inscris à la liste d'attente] — [Je précommande à 19 €]

## FAQ

**Le pack existe déjà, je peux l'avoir tout de suite ?**
Non. C'est une pré-vente : rien n'est livré aujourd'hui. Si vous avez besoin d'un outil immédiatement, attendez la décision du 20 décembre ou ne précommandez pas.

**Qu'est-ce qui se passe si le projet est abandonné ?**
Vous êtes remboursé intégralement, automatiquement, sans démarche de votre part si vous avez précommandé. Si vous étiez seulement inscrit sur la liste d'attente, vous êtes simplement informé.

**Ce pack est-il affilié ou soutenu par Anthropic ?**
Non. Ce pack n'est pas un produit officiel Anthropic. Claude Code et Claude sont des outils d'Anthropic ; ce pack est un ensemble d'assistants tiers conçus pour les utiliser, vendu indépendamment.

**Dois-je savoir coder pour l'utiliser ?**
Non, mais vous devez savoir installer un outil en suivant une notice pas à pas (copier des fichiers, lancer une commande). Si l'idée d'ouvrir une ligne de commande vous bloque complètement, ce pack n'est pas encore pour vous.

**Le contenu final sera-t-il exactement celui décrit plus haut ?**
Les cas d'usage listés sont ceux visés en priorité, construits à partir de vrais problèmes de logistique. Le nombre exact d'assistants et leur forme finale seront précisés aux inscrits avant la livraison, pas improvisés après coup.

## Pour résumer

Pack d'assistants Claude Code pour la logistique (stock, transport, reporting), en construction, livré sous 4 semaines si assez de monde se manifeste avant le 20 décembre 2026, remboursement intégral sinon. Pas affilié à Anthropic. Deux options sans risque : liste d'attente gratuite ou précommande à 19 € remboursable.
