# État de l'agence — mis à jour le 23/11/2026 ~08:15 (run quotidien 0730)

## Chiffres
- Revenu net novembre : 0 € / objectif 1 000 €/mois. Dépenses : 0 € / 60 €.
- Premier euro visé : avant le 22/12/2026.
- **Date cible 1 000 €/mois : 31/03/2027**. Revue chaque dimanche.

## Blocage structurel (constat du 23/11)
Toutes les pistes notées ≥29 (ComeUp 30, Google Business Profile 30, Codeur.com 29) exigent la micro-entreprise pour facturer. La seule route sans statut mesurée (clipping) plafonne à ~31 €. Conséquence : on prouve la demande gratuitement (exp-03 version offerte), et le statut devient la vraie décision quand cette preuve existe. `primes-bancaires` (28, prime commerciale, aucun statut requis) est en vérification en source primaire — utile pour le premier euro, pas pour l'objectif.

## Priorités
1. **exp-03 Gumroad logistique** — offre repositionnée : l'assistant « rapport de stock » est construit et tourne (`livrables/gumroad/skill-rapport-de-stock/`, auto-test OK, sortie réelle sur 100 lignes). La page montre cette sortie réelle, plus d'exemple fictif, et l'inscription gratuite donne l'assistant tout de suite. **A-04 envoyée** (publier la version gratuite : 0 €, aucun paiement, donc aucune micro-entreprise). Canal trouvé : r/supplychain (118k, persona exact), r/excel (902k), r/n8n (262k) — voir `memory/benchmarks/canaux-diffusion-logistique.md`. Aucun forum FR actif n'existe : recherche FR closed.
   - **À faire sans Baptiste au prochain run** : version anglaise de la page et du README (les 3 canaux sont anglophones) ; traiter le retour du critique (`livrables/gumroad/critique-page-et-skill-1.json`).
2. exp-02 ComeUp : 3 fiches prêtes (critique 3/5 sur la preuve, faute de vidéo). Bloqué sur micro-entreprise + T-04.
3. exp-01 clipping : mesuré, plafonné (~31 €). Reste à 0 € et 0 h jusqu'au 06/12, plus d'heures investies.

## Tests (max 3)
| id | statut | kill date | bloqué par |
|---|---|---|---|
| exp-01-clipping-mesure | running (plafonné) | 06/12 | T-02 (euros payés + taux d'approbation) |
| exp-02-comeup-gigs | bloqué | 20/12 | micro-entreprise + T-04 vidéos |
| exp-03-skills-gumroad | prêt à publier | 20/12 | A-04 + T-06 + version anglaise |
Suivant si un test meurt : primes-bancaires (en vérification) ou gbp-optimisation (30, à fusionner avec exp-02).

## En attente de Baptiste
- **A-04** : publier la version gratuite d'exp-03 sur Gumroad (0 €, pas de statut). A-03 remplacée (question mal posée) ; si Baptiste y répond quand même oui, ça débloque aussi exp-02.
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
