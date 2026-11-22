# État de l'agence — mis à jour le 22/11/2026 ~09:30 (kickoff, session 1)

## Chiffres
- Revenu net novembre : 0 € / objectif 1 000 €/mois. Dépenses : 0 € / 60 €.
- Premier euro visé : avant le 22/12/2026.
- **Date cible 1 000 €/mois : 31/03/2027** (hypothèse : services d'automatisation IA ~500 € + produits numériques + clipping). Revue chaque dimanche.

## Priorités
1. Finir le kickoff (memory/kickoff.md) : 6/11 cochés ; le reste attend surtout T-03 (Baptiste).
2. exp-03 skills Gumroad : seul test débloqué → benchmark, construction, critique, puis approbation de publication.
3. exp-02 ComeUp : préparer les 3 fiches (benchmark + rédacteur + critique) pendant qu'on attend T-01, pour publier dès le feu vert.
4. exp-01 clipping : mesure seulement (le projet SixShots vit dans `Desktop/CLAUDE CODE/CLIPPING MONEY`, on n'y touche pas).

## Tests (max 3)
| id | statut | kill date | bloqué par |
|---|---|---|---|
| exp-01-clipping-mesure | bloqué | 06/12 | T-02 capture Whop |
| exp-02-comeup-gigs | bloqué | 20/12 | T-01 contrat + SIRET, approbation de publication |
| exp-03-skills-gumroad | en cours | 20/12 | — |
Suivant si un test meurt : primes-bancaires (28, 0 €) ou gbp-optimisation (30, à fusionner avec exp-02).

## En attente de Baptiste
- T-03 mise en route (45 min) : bot, token, Windows/BIOS, GitHub, healthchecks, + `schedule.ps1` en admin.
- T-01 contrat/SIRET (15 min). T-02 capture Whop (5 min/sem).

## Technique
- Runs : MFYM-quotidien 07:30 (opus) / 13:00 / 19:00 (sonnet), hebdo dim. 10:00, digest 20:30, backup 03:00, heartbeat 5 min. Tâches en mode session (sans admin) tant que T-03 n'est pas fait.
- Lanceur `scripts/run.ps1` (verrou, timeout, quota/auth, alertes). Garde-fou `.claude/hooks/guard.py`. Activité `.claude/hooks/activity.py` → memory/activity.jsonl.
- Bot `scripts/bot.py` (service), envoi `scripts/tg.py`, maintenance `scripts/maint.py`.
- Dashboard : `dashboard/` (port 8700 local, téléphone via tailscale serve 8445) — en construction.
- Version Claude Code figée : 2.1.278 (DISABLE_AUTOUPDATER=1). Monter de version exprès, puis lancer `run.ps1 -Goal test`.
