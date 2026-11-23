# État de l'agence — mis à jour le 23/11/2026 ~19:05 (run quotidien 1900)

## Chiffres
- Revenu net novembre : 0 € / objectif 1 000 €/mois. Dépenses : 0 € / 60 €.
- Premier euro visé : avant le 22/12/2026.
- **Date cible 1 000 €/mois : 31/03/2027**. Revue chaque dimanche.

## Blocage structurel (constat du 23/11)
Toutes les pistes notées ≥29 (ComeUp 30, Google Business Profile 30, Codeur.com 29) exigent la micro-entreprise pour facturer. La seule route sans statut mesurée (clipping) plafonne à ~31 €. Conséquence : on prouve la demande gratuitement (exp-03 version offerte), et le statut devient la vraie décision quand cette preuve existe.
`primes-bancaires` est passée **31/35, confiance high** après vérification en source primaire (`memory/benchmarks/primes-bancaires.md`) : Fortuneo FTNSEA 250 € nets, 0 €/mois, sans déplacer le salaire, jusqu'au 31/12/2026 → **exp-04**, A-05 envoyée. C'est un one-off qui finance le budget, pas une route vers l'objectif. Offres mortes retirées : Orange Bank, N26, Ma French Bank, Helios.

## Priorités
1. **exp-03 Gumroad logistique** — **publiable techniquement depuis le 23/11 13h** (4 passes de critique + 1 correctif direct) : page + assistant « rapport de stock » réel (`livrables/gumroad/skill-rapport-de-stock/`), verdict final du critique `publiable=true`, zéro régression. Dernier défaut bloquant trouvé (seuil d'écart d'inventaire absolu, faux métier sur petites et grosses références) corrigé directement par le directeur (seuil relatif) et revérifié par le critique. Canal trouvé : r/supplychain (118k, persona exact), r/excel (902k), r/n8n (262k) — voir `memory/benchmarks/canaux-diffusion-logistique.md`. Aucun forum FR actif n'existe : recherche FR closed. Version anglaise de la page+README livrée et validée par le critique (publiable=true, aucune dérive de fait) pour les canaux anglophones.
   - **Ne bloque plus que sur Baptiste** : A-04 (publier) et T-06 (règles Reddit). Run 19h : textes de diffusion prêts à l'emploi écrits d'avance (modmail r/supplychain, réponse-type r/excel, post r/n8n) dans `memory/drafts/reddit-diffusion-exp03.md`, et pas-à-pas de publication Gumroad dans `memory/drafts/pas-a-pas-A-04-gumroad.md` — pour publier/diffuser dès la réponse, sans round de rédaction supplémentaire.
2. exp-02 ComeUp : 3 fiches prêtes (critique 3/5 sur la preuve, faute de vidéo). Bloqué sur micro-entreprise + T-04.
3. exp-01 clipping : mesuré, plafonné (~31 €). Reste à 0 € et 0 h jusqu'au 06/12, plus d'heures investies.

## Tests (2 en cours, 2 bloqués sur Baptiste)
| id | statut | kill date | bloqué par |
|---|---|---|---|
| exp-01-clipping-mesure | running (plafonné) | 06/12 | T-02 (euros payés + taux d'approbation) |
| exp-02-comeup-gigs | bloqué | 20/12 | micro-entreprise + T-04 vidéos |
| exp-03-skills-gumroad | running (publiable, en attente A-04) | 20/12 | A-04 + T-06 |
| exp-04-primes-bancaires | bloqué | 31/01 | A-05 (ouverture du compte) |
Suivant si un test meurt : gbp-optimisation (30, à fusionner avec exp-02) ou codeur-n8n (29).

## En attente de Baptiste
- **A-04** : publier la version gratuite d'exp-03 sur Gumroad (0 €, pas de statut). Verdict `publiable=true` obtenu le 23/11 (FR et EN) : le garde-fou de séquencement est levé, il ne manque plus que la réponse de Baptiste. Si oui → envoyer le pas-à-pas de publication.
- **A-05** : ouvrir un compte Fortuneo (code FTNSEA, 0 €, ~40 min, 250 € de prime). Si oui → envoyer le pas-à-pas (déjà écrit : `memory/drafts/pas-a-pas-A-05-fortuneo.md`).
- T-06 (8 min) : règles d'autopromo de r/supplychain + ancienneté de son compte Reddit + activité de r/InventoryManagement et r/Warehousing. Remplace T-05 (annulée).
- T-02 (5 min, hebdo) : capture des gains Whop — seul chiffre absent de la base clipping.
- T-04 (45 min) : vidéos ComeUp, le jour de la publication seulement.
- T-01 : reste la place de parking oui/non (1 min). Total ouvert : ~1 h.

## Technique
- Runs : MFYM-quotidien 07:30 (opus) / 13:00 / 19:00 (sonnet), hebdo dim. 10:00, digest 20:30, backup 03:00, heartbeat 5 min. Tâches en S4U.
- Lanceur `scripts/run.ps1` (verrou, timeout, quota/auth, alertes). Garde-fou `.claude/hooks/guard.py`. Activité `.claude/hooks/activity.py`.
- Bot `scripts/bot.py` (service), envoi `scripts/tg.py`, maintenance `scripts/maint.py`. Le bot n'envoie que ce qui a `telegram_message_id` vide : modifier une tâche déjà envoyée ne la renvoie pas.
- Mesure exp-01 : `python scripts/clipping_stats.py` (seule lecture de la base du projet clipping).
- Dashboard : `dashboard/` (port 8700, téléphone https://desktop-ava6s00.tailf6027f.ts.net:8445).
- Appels claude hors lanceur : `python scripts/with_token.py <cmd>`.
- Version Claude Code figée : 2.1.278 (DISABLE_AUTOUPDATER=1).
- Reddit bloque les outils web de l'agence (domaine entier, y compris old./.json) : passer par Baptiste ou un agrégateur tiers.
