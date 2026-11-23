# Canaux de diffusion pour la pré-vente logistique (exp-03)

Date : 2026-11-23. Recherche lecture seule. Contexte : page de pré-vente prête (`livrables/gumroad/presell-logistique.md`), aucun canal touchant le persona gestionnaire d'entrepôt/stocks/transport n'a survécu à vérification (forum.gestconseil.com mort, forum.logistiqueconseil.org en erreur, FNTR hors-sujet, LinkedIn/Facebook invérifiables sans compte).

**Limite technique à noter honnêtement : reddit.com est bloqué pour l'outil de récupération web utilisé (domaine entier refusé, y compris old.reddit.com, .json, et les miroirs type redlib/top.gg/disboard qui renvoient 403/429).** Les chiffres Reddit ci-dessous viennent donc d'un agrégateur tiers sans intérêt financier (`reddapi.dev`, qui lit l'API Reddit) + recoupement avec des sites "règles d'auto-promo" tiers (threadotter, rankhog, mediafa.st — eux aussi sans intérêt financier dans notre pack, mais de fiabilité éditoriale inégale). Je le signale sur chaque ligne concernée plutôt que de prétendre avoir ouvert reddit.com moi-même.

## Tableau récapitulatif

| Canal | Membres | Dernière activité vérifiée | Autopromo | Verdict | Persona (1-5) |
|---|---|---|---|---|---|
| r/supplychain (Reddit) | 118 356 (reddapi.dev) | posts du 04-05/11/26, plusieurs/semaine | Besoin accord modmail préalable (source tierce, non confirmée mot pour mot) | ACTIF, autopromo sous condition | 5 |
| r/logistics (Reddit) | 76 201 (reddapi.dev) | posts du 02-04/11/26, mais 3-7 upvotes seulement | Interdite explicitement ("no advertising or promotion... blogspam will be removed") | ACTIF MAIS AUTOPROMO INTERDITE | 5 |
| r/n8n (Reddit) | 261 988 (reddapi.dev) | posts quotidiens 06-07/11/26 | Interdite pour vente/agence/client ; workflow réel toléré avec flair "Workflow – GitHub Included" | ACTIF MAIS AUTOPROMO INTERDITE (sauf partage gratuit du workflow) | 2 |
| r/excel (Reddit) | 901 829 (reddapi.dev) | plusieurs posts/jour, 06-07/11/26 | Tolérée si la réponse apporte déjà toute la valeur sans le lien (règle non officielle, sources tierces) | ACTIF, autopromo soft tolérée | 2 |
| r/ClaudeAI (Reddit) | 1 248 760 (reddapi.dev) | posts quotidiens, 1,3 M membres | Pas de règle claire trouvée | ACTIF, autopromo floue | 1 |
| r/InventoryManagement (Reddit) | 3 177 (reddapi.dev) | non disponible ("awaiting first crawl") | Inconnue | NON VÉRIFIÉ (activité) | 4 |
| r/Warehousing (Reddit) | 3 409 (reddapi.dev) | non disponible ("awaiting first crawl") | Inconnue | NON VÉRIFIÉ (activité) | 5 |
| cc-france.org (Discord) | 931 (déjà vérifié exp-03) | — | Canal #showcase dédié | ACTIF+UTILISABLE mais mauvais persona | 1 |
| devw.ai (Slack) | 3 236 (déjà vérifié exp-03) | — | Canal #showcase dédié | ACTIF+UTILISABLE mais mauvais persona | 1 |
| WizOps (Slack) | ~9 000 (thehiveindex, tiers) | inconnue | Inconnue | MORT/NON VÉRIFIABLE — domaine wizops.org ne résout pas (ENOTFOUND) | 2 (ops business, pas entrepôt) |
| "Logistics Network" / "Warehouse Operations Community" / "Last-Mile Delivery Community" (Slack) | non affiché | aucune preuve d'existence réelle ouverte | inconnue | NON VÉRIFIÉ — fiches d'annuaire sans lien de join confirmé | n/a |
| Discord "Supply Chain" (top.gg) | 711 (snippet de recherche seul) | "top 12% actifs" (snippet seul) | inconnue | NON VÉRIFIÉ — page bloquée en 403, jamais réellement ouverte | n/a |
| Indie Hackers (groupes logistique/supply chain) | — | posts récents mais majorité ressemble à du contenu SEO/backlink ("Why Leading Companies Rely on shipping companies in UAE") | — | ÉCARTÉ — communauté diluée par du spam, pages bloquées en 403 | 2 |
| faq-logistique.com | — | — | — | PAS DE FORUM — site éditorial, aucune fonction de forum trouvée | n/a |
| actu-transport-logistique.fr | — | commentaires d'articles existants (ex. 6 commentaires sur un article DFDS) | Réactif seulement, pas de sujet ouvert par un tiers | NON UTILISABLE comme canal de post — seulement des commentaires réactifs sur articles existants | n/a |
| Forums FR transport/logistique génériques | — | rien trouvé au-delà des salons physiques (Forum Transport-Logistique Aix, Montbartier...) | — | AUCUN FORUM EN LIGNE ACTIF TROUVÉ | n/a |

## Preuves par canal

### r/supplychain — ACTIF, persona 5/5
- Source 1 (sans intérêt financier) : `reddapi.dev/subreddits/supplychain/insights` ouvert directement — 118 356 membres, 1 083 posts indexés (communauté depuis 2012-01-11). Posts récents datés et titrés : "Procurement Job Offer" (04/11/26), "Simple best practices that made a difference in your Sourcing / Procurement job?" (04/11/26), "Graduated May and still haven't found a job" (04/11/26) — audience de praticiens supply chain réels (recherche d'emploi, achats, opérations).
- Source 2 (sans intérêt financier, qualité éditoriale moyenne) : recherche croisée (threadotter.com) citant une règle "promotion seulement avec accord modérateur via modmail" — non confirmée mot pour mot sur le wiki du sub lui-même (reddit.com inaccessible à cet outil), donc à vérifier par Baptiste en ouvrant manuellement `reddit.com/r/supplychain/wiki/rules` avant de poster.
- Pas de preuve financière biaisée : aucune des deux sources ne vend quoi que ce soit lié à notre pack.

### r/logistics — ACTIF MAIS AUTOPROMO INTERDITE, persona 5/5
- Source 1 : `reddapi.dev/subreddits/logistics/insights` — 76 201 membres, 645 posts indexés depuis 2009 (≈38 posts/an sur la base indexée, donc faible densité malgré les posts datés de la semaine du 02-04/11/26). Exemples : "NYC to Fed Ex" (04/11/26, 3 upvotes), "Sea Cargo from UK to Multan Pakistan" (02/11/26, 3 upvotes) — faible engagement par post.
- Règle citée verbatim par la même source : *"there is no advertising or promotion allowed on this subreddit. Logistics blogspam will also be removed."* — règle explicite et sans ambiguïté, contrairement à r/supplychain.
- Conclusion : poster un lien ou même un "retour d'expérience" qui mentionne le produit = suppression quasi certaine. Seule option : répondre à de vraies questions sans lien, en pure aide.

### r/n8n — ACTIF MAIS AUTOPROMO INTERDITE (sauf partage gratuit), persona 2/5
- Source 1 : `reddapi.dev/subreddits/n8n/insights` — 261 988 membres, posts quotidiens le 06-07/11/26 ("How have you been using AI while building in n8n?", "My AI agent kept reading giant n8n JSON exports, so I built an MCP server...") — communauté de builders n8n très active techniquement.
- Source 2 : recherche croisée (rankhog.com + recoupement multiple) citant la règle explicite "No Self-Promotion or Advertising" qui bannit SaaS/services payants/cours, ET bannit spécifiquement les posts "agence/clients/pricing/business model" — donc même un post honnête façon "voici comment j'ai trouvé un client logistique" serait hors-sujet. Exception documentée : un workflow réellement partagé avec le flair "Workflow – Github Included" (code inclus, gratuit) est toléré.
- Persona : ce sub cible des développeurs d'automatisation, pas des gestionnaires d'entrepôt — mais une partie de ces builders construisent pour des clients PME logistiques, donc l'audience peut *relayer* vers le vrai persona sans y être elle-même.

### r/excel — ACTIF, autopromo soft tolérée, persona 2/5
- Source 1 : `reddapi.dev/subreddits/excel/insights` — 901 829 membres, plusieurs posts/jour le 06-07/11/26, dont "Power Query – Large 1-Year Inventory Transaction File" (07/11/26) — preuve directe que des gens y postent déjà sur des problèmes de suivi de stock en Excel, proche de notre persona.
- Source 2 : recoupement (replyhey.com) : règle non officielle mais cohérente sur plusieurs sources — répondre complètement à une question sans le lien, puis mentionner ce qu'on a construit avec une ligne de disclosure ; sinon suppression comme spam.
- Persona : généraliste Excel, pas logistique nommément, mais le sujet "inventaire/stock en Excel" y apparaît organiquement — angle utilisable : répondre à une vraie question d'automatisation de suivi de stock.

### r/ClaudeAI — ACTIF, persona 1/5
- Source : `reddapi.dev/subreddits/claudeai/insights` — 1 248 760 membres, fil très actif (posts du 07/11, 02/11, 25/10/26). Aucune règle d'autopromo claire trouvée dans le contenu récupéré.
- Déjà écarté dans la logique de exp-03 : audience devs/enthousiastes IA, pas de gestionnaires d'entrepôt. Utile seulement pour valider l'intérêt générique pour le format "pack de skills", pas pour le persona logistique.

### r/InventoryManagement et r/Warehousing — NON VÉRIFIÉ (activité), persona 4-5/5
- `reddapi.dev` confirme leur existence (3 177 et 3 409 membres respectivement) mais affiche "awaiting first crawl" / données de posts indisponibles : impossible de dire s'ils sont vivants ou quasi-morts comme forum.gestconseil.com. À vérifier manuellement par Baptiste (ouverture directe sur reddit.com, impossible depuis cet outil) avant tout post — ne pas les traiter comme actifs sans cette vérification.

### Discord "Supply Chain" (top.gg) et tag "logistics" (disboard.org) — NON VÉRIFIÉ
- Un snippet de recherche indique un serveur "Supply Chain" à 711 membres, "top 12% most active servers" — mais `top.gg/servers/695813821591322644` et `disboard.org/servers/tag/logistics` renvoient tous deux une erreur 403 à l'ouverture directe. Je n'ai jamais réellement vu la page : classé non vérifié, pas actif, conformément à la consigne de ne pas confondre un extrait de recherche avec une preuve ouverte.

### Slack WizOps / "Logistics Network" / "Warehouse Operations Community" / "Last-Mile Delivery Community" — MORT ou NON VÉRIFIÉ
- `thehiveindex.com/topics/operations-logistics/platform/slack/` (annuaire tiers, sans intérêt financier) liste ces 4 communautés mais sans compteur de membres pour 3 d'entre elles et sans lien de join vérifiable directement.
- Tentative d'ouverture du site officiel `wizops.org` : **échec DNS (ENOTFOUND)** — le domaine ne résout pas. Soit le site a changé d'adresse, soit la communauté est morte. Dans les deux cas, pas utilisable en l'état, et son thème réel ("sales ops, marketing ops, revenue ops" selon la description elle-même) ne correspond pas au persona entrepôt/transport.
- "Logistics Network", "Warehouse Operations Community", "Last-Mile Delivery Community" : aucune preuve d'existence trouvée au-delà de la fiche d'annuaire elle-même (pas de site propre retrouvé, pas de lien de join). Traités comme non vérifiés, pas comme actifs.

### Indie Hackers — ÉCARTÉ (persona 2/5, qualité dégradée)
- Les posts remontés sous les mots-clés "supply chain"/"logistics"/"warehouse" sont majoritairement des contenus qui ressemblent à du SEO/backlink spam plutôt qu'à de vrais retours d'expérience de fondateurs ("Why Leading Companies Rely on shipping companies in UAE for Scalable Global Trade Growth", "Modernizing Supply Chain Management: How Enterprise Integration is Powering the Future of Retail") — pas le ton habituel d'un vrai post Indie Hackers.
- Tentative d'ouverture directe de plusieurs posts et de la page groupes : 403 systématique, donc impossible de confirmer dates/commentaires réels.
- Même la réussite citée dans exp-03 ("$57 en 48h") décrit du trafic venu de Reddit, pas d'Indie Hackers lui-même.
- Conclusion : canal à écarter pour cette diffusion, pas assez fiable ni pertinent pour le persona.

### faq-logistique.com — PAS DE FORUM
- Page d'accueil et pages "Actualités"/"Dossiers Thématiques" explorées via les résultats de recherche : portail éditorial B2B (créé en 2002, ~26-100 k visites/mois selon les pages), mais aucune fonctionnalité de forum ou d'espace communautaire identifiée. Pas un canal de diffusion candidat.

### actu-transport-logistique.fr — NON UTILISABLE comme canal de post
- Média B2B (ProMedia Group / ex-Info6tm) avec commentaires sur certains articles (ex. 6 commentaires sur un article DFDS) — mais c'est un espace de réaction à l'actualité du média, pas un lieu où l'on peut ouvrir un sujet ou poster un retour d'expérience produit. Pas retenu.

### Forums professionnels FR transport/logistique — AUCUN TROUVÉ ACTIF EN LIGNE
- La recherche ne remonte que des forums métiers *physiques* (salons de l'emploi : Forum Transport-Logistique Aix-en-Provence, Montbartier, Florange, Mérignac — tous organisés par France Travail/AFT en 2026), pas de forum en ligne. Confirme et élargit le constat déjà posé dans exp-03 (gestconseil mort, logistiqueconseil en erreur) : il n'existe pas de forum francophone en ligne actif et ouvert pour ce persona, au moins pas trouvé en deux sessions de recherche.

## Classement des 5 meilleurs canaux

Score = persona × activité confirmée × publication possible (sur le réel, pas sur l'espoir).

1. **r/supplychain** (118k membres, persona 5/5, activité confirmée, autopromo possible sous accord modmail) — meilleur compromis : vrai public cible, actif, règle contournable légalement en demandant l'autorisation.
2. **r/excel** (902k membres, persona 2/5 mais trafic massif et sujet "inventaire Excel" qui existe déjà organiquement, autopromo soft tolérée) — volume très supérieur, angle "j'ai automatisé mon suivi de stock Excel avec Claude" répond à une vraie douleur visible dans les posts.
3. **r/n8n** (262k membres, persona 2/5, activité quotidienne, partage gratuit de workflow toléré) — ne permet pas de vendre, mais permet de prouver l'utilité réelle (poster le workflow n8n logistique gratuit, mesurer l'intérêt, convertir en message privé si quelqu'un demande plus).
4. **r/logistics** (76k membres, persona 5/5, activité faible/engagement faible, autopromo interdite) — meilleur persona en théorie, mais le règlement explicite et le faible engagement en font un canal d'écoute (répondre à des questions) plutôt que de diffusion.
5. **r/InventoryManagement / r/Warehousing** (persona 4-5/5, activité non vérifiée) — à vérifier manuellement avant d'y compter ; potentiellement le meilleur fit persona si vivant, mais aujourd'hui ce n'est qu'une hypothèse.

## Recommandation

**Tester dans cet ordre, à coût 0 :**

1. **r/supplychain** : envoyer un modmail honnête (qui es-tu, ce que tu as construit, pourquoi, demander l'autorisation de poster un retour d'expérience) avant tout post — c'est le seul canal qui combine vrai persona et activité confirmée.
2. **r/excel** : répondre à une question réelle de suivi de stock/inventaire (il y en a cette semaine, ex. le fil "Power Query – Large 1-Year Inventory Transaction File" du 07/11/26) avec une réponse complète et utile, puis une ligne honnête sur l'outil construit — pas un post dédié, un commentaire qui apporte toute la valeur même sans le lien.
3. **r/n8n** : poster le workflow n8n gratuit (pas le pack payant) avec le flair "Workflow – GitHub Included", mesurer les réactions ; si quelqu'un demande "ça marche pour la logistique ?", répondre en DM avec le lien de pré-vente.

**Ne pas utiliser maintenant** (non vérifiés ou morts) : WizOps, "Logistics Network"/"Warehouse Operations Community"/"Last-Mile Delivery Community", Discord top.gg/disboard, Indie Hackers, tout forum FR en ligne (aucun trouvé actif).

**Reste à vérifier par Baptiste manuellement** (reddit.com bloqué pour cet outil) avant tout post : la règle exacte de r/supplychain sur le wiki du sub, et l'activité réelle de r/InventoryManagement et r/Warehousing.
