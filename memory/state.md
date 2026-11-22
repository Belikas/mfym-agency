# État de l'agence — mis à jour le 22/11/2026 ~12:25 (kickoff, session 1)

## Chiffres
- Revenu net novembre : 0 € / objectif 1 000 €/mois. Dépenses : 0 € / 60 €.
- Premier euro visé : avant le 22/12/2026.
- **Date cible 1 000 €/mois : 31/03/2027** (hypothèse : services d'automatisation IA ~500 € + produits numériques + clipping). Revue chaque dimanche.

## Priorités
1. Kickoff 10/11 : reste le run planifié autonome (13:00 du 22/11). Puis message Telegram de fin de kickoff.
2. exp-03 : pivot pré-vente (benchmark : 0 vente vérifiable chez les concurrents payants). Prochain : page de pré-vente niche n8n métier FR ou logistique, puis approbation de publication. Pas de statut requis pour une liste d'attente.
3. exp-02 ComeUp : 3 fiches prêtes (livrables/comeup/, critique passe 3 min 3/5 = preuve vidéo). Publication = micro-entreprise (reportée par Baptiste jusqu'à indispensable) + T-04 vidéos.
4. exp-01 clipping : mesure seulement (le projet SixShots vit dans `Desktop/CLAUDE CODE/CLIPPING MONEY`, on n'y touche pas).

## Tests (max 3)
| id | statut | kill date | bloqué par |
|---|---|---|---|
| exp-01-clipping-mesure | bloqué | 06/12 | T-02 capture Whop |
| exp-02-comeup-gigs | bloqué | 20/12 | T-01 contrat + SIRET, approbation de publication |
| exp-03-skills-gumroad | en cours | 20/12 | — |
Suivant si un test meurt : primes-bancaires (28, 0 €) ou gbp-optimisation (30, à fusionner avec exp-02).

## En attente de Baptiste
- T-01 : place de parking oui/non (1 min). T-02 capture Whop (dimanche). T-04 vidéos (le jour de la publication).
- T-03 fait (BIOS reporté). Contrat : aucune clause bloquante. Pas de SIRET ; micro-entreprise reportée.

## Technique
- Runs : MFYM-quotidien 07:30 (opus) / 13:00 / 19:00 (sonnet), hebdo dim. 10:00, digest 20:30, backup 03:00, heartbeat 5 min. Tâches en S4U (tournent sans session) ; redémarrage validé 22/11 12:06.
- Lanceur `scripts/run.ps1` (verrou, timeout, quota/auth, alertes). Garde-fou `.claude/hooks/guard.py`. Activité `.claude/hooks/activity.py` → memory/activity.jsonl.
- Bot `scripts/bot.py` (service), envoi `scripts/tg.py`, maintenance `scripts/maint.py`.
- Dashboard : `dashboard/` (port 8700, téléphone https://desktop-ava6s00.tailf6027f.ts.net:8445), critique 4/5 partout.
- Appels claude hors lanceur : `python scripts/with_token.py <cmd>` (le /login interactif expire).
- Version Claude Code figée : 2.1.278 (DISABLE_AUTOUPDATER=1). Monter de version exprès, puis lancer `run.ps1 -Goal test`.
