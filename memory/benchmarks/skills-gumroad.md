# Benchmark exp-03 : packs de skills / agents Claude Code (Gumroad ~29 €)

Date : 2026-11-22. Recherche lecture seule, rien créé. Chiffres GitHub = API le 22/11/2026. Tout le reste = lu sur les pages (WebFetch), sauf mention "non vérifié".

## Constat principal (à lire d'abord)
- **Aucun produit payant trouvé n'affiche de ventes ou d'avis chiffrés** (Gumroad, Selar, Payhip, Leanpub, Agensi : 0 avis ou rien). On ne peut PAS classer les payants par résultats mesurables. Seule preuve de demande : les concurrents gratuits (stars/installs) et le fait que ~10 vendeurs listent des packs à 9–99 $.
- Offre payante saturée en "généraliste dev" (review/test/debug/CLAUDE.md Next.js). Le gratuit couvre déjà ce terrain avec des centaines de milliers de stars.
- Le prix 29 $ est dans la fourchette basse-médiane des packs (9 $, 12 $, 19 $, 29 $, 39 $, 69 $, 99 $), mais sans preuve que quelqu'un l'achète.

## A. Concurrents gratuits (mesurables)
| Repo | Stars | Dernier push | Note |
|---|---|---|---|
| mattpocock/skills | 329 959 | 19/11/26 | skills.sh : 6,3 M installs cumulés (6 skills dans le top 15) |
| obra/superpowers | 323 926 | 03/11/26 | méthodo dev complète |
| anthropics/skills | 198 662 | 16/11/26 | officiel |
| ComposioHQ/awesome-claude-skills | 80 030 | 18/09/26 | liste |
| hesreallyhim/awesome-claude-code | 58 558 | 22/11/26 | liste de référence |
| wshobson/agents | 42 781 | 21/11/26 | agents/skills/plugins |
| alirezarezvani/claude-skills | 30 261 | 21/11/26 | 410 skills, 120+ agents |
| VoltAgent/awesome-claude-code-subagents | 26 721 | 02/11/26 | 100+ subagents |
| czlonkowski/n8n-mcp | 23 293 | 19/11/26 | MCP n8n |
| czlonkowski/n8n-skills | 6 691 | 18/11/26 | 7 skills n8n, ~25 K installs (skills.sh) |
| supabase/agent-skills | 3 121 | 12/11/26 | officiel Supabase (skills.sh : supabase-postgres-best-practices 494 K installs, supabase 372 K) |
URLs : https://github.com/<repo> ; https://skills.sh (installs).

## B. Produits payants ouverts (7 pages réellement lues)
Ordre = force du signal (faible partout) puis pertinence.

1. **Claude Code Mastery (claudecodeguides.com)** — https://claudecodeguides.com/mastery/
   - 99 $ à vie (fondateurs, 500 places) ou 19 $/mois. **Mesure : "47/500 places prises", "Join 50+ builders"** (auto-déclaré, non vérifié ; incohérences relevées : 16 vs 108 extensions, 2 500 vs 2 600 articles).
   - 16 CLAUDE.md (1/framework, 300+ lignes), 3 configs multi-agents, 80+ prompts. Public : devs multi-stack.
   - Page : hero + crédentiels, "version courte", contenu, bonus, prix, FAQ 5 q., bio auteur. Longue. Ton fondateur perso, urgence (places). Remboursement : "écris-moi", sans délai.
2. **Claude Code Skills Pack (protodex / Gumroad manja8)** — https://dev.to/manja316/claude-code-skills-pack-15-production-skills-5-hooks-7-slash-commands-99-lifetime-5fd0 ; Gumroad https://manja8.gumroad.com/l/dhnzd (page Gumroad illisible côté fetch : titre seul)
   - 99 $ à vie, licence 1 dev. Mesure : aucune.
   - 15 skills, 5 hooks, 7 slash commands, 1 CLAUDE.md, 32 fichiers/60 Ko, INSTALL.md (4 étapes). Public : devs rigoureux (commit, PR, secret-scanner).
   - Structure : article dev.to (liste, installation en 4 étapes, licence). Remboursement 7 jours "sans question". Ton technique sobre.
3. **Claude Code Power User Kit (popularaitools.ai)** — https://popularaitools.ai/store/claude-code-power-user
   - 39 $+ unique, Gumroad. Mesure : aucune. 7 slash commands (scaffold, review, test-gen, doc-gen, git-flow, refactor, debug).
   - Structure la plus complète : hero + achat, pain points, checklist "pour qui", "How it works" 3 étapes, prix, FAQ 3 q., image de preview pleine page, CTA. Remboursement 30 j (Gumroad). Ton promotionnel ("3x plus vite", sans preuve).
4. **Claude Code Starter Kit (Selar)** — https://selar.com/9237gl2p20
   - 29 $ (notre prix exact). Mesure : **0 avis**, un "1" non étiqueté (vente ?). 6 CLAUDE.md (web, SaaS, WordPress/Woo, Shopify, Python auto, statique SEO), 5 slash skills, 4 subagents, hooks de sécurité, 30 prompts, guide PDF 15 p.
   - Page courte (~250 mots), 1 bannière, aucune capture, pas de FAQ, pas de remboursement visible, disclaimer "non affilié Anthropic". Ton direct.
5. **Septim Claude Code Mastery Bundle** — https://septimlabs.vercel.app/claude-bundle (HTTP 402 à l'ouverture : NON LU, infos via snippet de recherche, non vérifié)
   - 69 $ (87 $ séparés) : 25 skills, 10 subagents, 24 prompts ; pack agents aussi gratuit en open source.
6. **Agentic Coding Starter Kit (Gumroad)** — https://dev.to/jovan_chan_9500711396d4e6/agentic-coding-starter-kit-review-2026-is-9-worth-it-for-claude-code-and-cursor-users-8ap (page Gumroad non ouverte)
   - 9 $ (19 $ selon un répertoire, incohérent). Mesure : aucune ; auteur compte récent (mai 2026). 6 CLAUDE.md (Next, Python, Go, Rust, monorepo), 4 subagents, 4 hooks, 2 configs MCP.
   - Article structuré : problème "setup tax", contenu, pour qui / pas pour qui, calcul du prix, limites honnêtes. Seul à dire qui ne doit PAS acheter.
7. **Agent Skill Pack Payhip** — https://payhip.com/b/S3RJk
   - 12 $ (promo). Mesure : aucune. 24 skills SKILL.md (planif, review, test, release, docs, git), install.py avec dry-run, lint_skills.py, versions Cursor, tests unitaires, Quick-Start PDF. Compatible Claude Code / Cursor / Codex.
   - Page : liste de contenu + limites explicites. Pas de remboursement affiché (page EU TVA/RGPD seulement).
8. **Claude Code Operator's Library (Leanpub)** — https://leanpub.com/b/cc-operators-library
   - 29 $ min / 39 $ suggéré (4 livres, 462 p.). Mesure : aucune (pas de compteur). Thèmes : coût tokens, sécurité/hooks, migration, AGENTS.md. Remboursement 60 j (Leanpub). Ton technique, "données mesurées". Format livre, pas des fichiers.
9. **Marketplace Agensi** — https://www.agensi.io/claude-marketplace/digital-products
   - 672 skills "digital products" ; prix 5–39 $ (majorité 8,99–19 $) ; compteurs non étiquetés (0–7, notes ex. "(1)(2)" => 1–3 avis max). Scan sécurité 8 points affiché. Aucun skill n8n/logistique/Supabase sur la page 1 ; un snippet cite n8n Workflow QA Linter et Supabase RLS checker à ~8–11 $ (non vérifié, non ouvert).
10. Contre-exemple de preuve : article "skill qui se vend sur Gumroad" (https://dev.to/manja316/how-to-build-a-claude-code-skill-that-actually-sells-on-gumroad-4kdm) : skills à 7–10 $, "objectif 25 ventes/mois = 200 $", **aucun chiffre de ventes réel**. Source intéressée, non fiable.

## C. Motifs communs des pages
- Contenu = nombres explicites (N skills, N agents, N templates). Installation en ≤4 étapes. Licence + mise à jour à vie. Disclaimer non-affilié Anthropic.
- Les 2 meilleures pages (Power User, Mastery) ont : pain points, "pour qui", FAQ, aperçu visuel, remboursement. Les plus faibles (Selar, Payhip) : texte seul, pas de capture.
- Presque aucune preuve sociale vérifiable chez personne. Un vendeur qui montre de vraies captures + preuve d'usage réel serait en tête sur ce point.
- Généraliste dev = prix 9–19 $ en pratique ; 39–99 $ seulement avec marque/bundle (non démontré que ça se vend).

## D. Trous de marché et 3 niches candidates
Gratuit déjà saturé : review/test/debug/git, design front, Supabase officiel, n8n de base (6,7 K stars gratuits : ne pas vendre "n8n générique").
Aucun produit payant ni gratuit trouvé en français ni en logistique (recherche GitHub "logistics/français" : rien de pertinent ; absence de preuve, pas preuve d'absence de demande).

1. **n8n avancé orienté métier FR (factures, relances, e-commerce, entrepôt)** : n8n-skills gratuit prouve la demande (6,7 K stars, 25 K installs) mais couvre la technique, pas les workflows métier ; Agensi n'a pas de n8n sur page 1. Force de Baptiste : n8n. Risque : le gratuit peut absorber.
2. **Logistique / supply chain (suivi colis, stocks, transporteurs, WMS/ERP, reporting)** : zéro concurrent trouvé ; expérience pro de Baptiste = avantage réel. Preuve de demande payante : AUCUNE (non vérifié) -> à tester par une page d'attente / pré-vente avant de produire.
3. **Pack en français pour indépendants / micro-entrepreneurs FR (devis, facturation Factur-X, URSSAF, TVA) pilotés par Claude Code** : audience non-dev France, hors portée des listes anglophones ; demande inférée seulement (non vérifié). Réforme facturation électronique FR : à vérifier avant d'argumenter.
Recommandation provisoire : tester 1 et 2 en page de pré-vente (coût 0 €) avant de produire ; ne pas construire un généraliste.

## E. Grille de score (produit + page), seuil critique >= 4/5 partout
1. **Précision de niche** : 5 = un public nommé en 1 phrase, un seul problème résolu ; 1 = "pour tous les devs".
2. **Utilité immédiate** : 5 = chaque skill testé sur un vrai cas, résultat visible en <5 min après installation ; 1 = prompts génériques.
3. **Qualité technique** : 5 = format SKILL.md valide (lint passé), noms/descriptions qui déclenchent bien, testé sur la version actuelle de Claude Code, 0 chemin en dur ; 1 = non testé.
4. **Différenciation vs gratuit** : 5 = comparaison explicite avec 2+ équivalents gratuits et raison claire de payer (gain de temps chiffré, contenu absent du gratuit) ; 1 = copie du gratuit.
5. **Preuve** : 5 = démo réelle (GIF/vidéo avant-après), captures du contenu, extrait gratuit téléchargeable ; 1 = affirmations seules.
6. **Clarté de la page** : 5 = titre-promesse + pour qui/pas pour qui + liste chiffrée + installation en <=4 étapes + FAQ >=5 q. + remboursement daté (>=14 j) + licence ; lisible en 60 s ; 1 = bloc de texte.
7. **Honnêteté/confiance** : 5 = limites dites, disclaimer non-affilié, aucun chiffre inventé, mises à jour datées ; 1 = promesses "3x plus vite" sans source.
8. **Installation et support** : 5 = un script/zip, install.py ou INSTALL.md vérifié sur Windows et macOS, contact et changelog ; 1 = copier-coller manuel.

## Non vérifié / limites
- Aucune vente réelle confirmée pour aucun produit payant ; les "50+ builders" et "47/500" sont auto-déclarés.
- Septim, Gumroad manja8 et Agentic Kit : pages Gumroad/Septim non lues directement.
- Compteurs Agensi non étiquetés : interprétation incertaine.
- Pas d'accès aux classements Gumroad Discover (page vide au fetch) ni à Lemon Squeezy / Polar.
