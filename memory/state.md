# État de l'agence — mis à jour le 22/11/2026 ~13:25 (run quotidien 1300)

## Chiffres
- Revenu net novembre : 0 € / objectif 1 000 €/mois. Dépenses : 0 € / 60 €.
- Premier euro visé : avant le 22/12/2026.
- **Date cible 1 000 €/mois : 31/03/2027** (hypothèse : services d'automatisation IA ~500 € + produits numériques + clipping). Revue chaque dimanche.

## Priorités
1. exp-03 Gumroad logistique : page de pré-vente prête (livrables/gumroad/presell-logistique.md), critique 4-5/5 sur les 8 critères (2 passes). **Approbation A-03 envoyée** : publier = créer la micro-entreprise maintenant (le moment "indispensable"). 4 communautés de diffusion trouvées (chartes vérifiées) : forum.gestconseil.com (seule à toucher le persona logistique, activité à vérifier), cc-france.org, devw.ai, rucheia.fr (ces 3 dernières = audience dev/Claude Code, pas logistique — bon pour feedback produit, pas pour le persona cible).
2. exp-02 ComeUp : 3 fiches prêtes (livrables/comeup/, critique passe 3 min 3/5 = preuve vidéo). Publication = même décision micro-entreprise + T-04 vidéos.
3. exp-01 clipping : mesure seulement (le projet SixShots vit dans `Desktop/CLAUDE CODE/CLIPPING MONEY`, on n'y touche pas).
4. Kickoff terminé (11/11, 22/11 13:20) : runs en mode business normal.

## Tests (max 3)
| id | statut | kill date | bloqué par |
|---|---|---|---|
| exp-01-clipping-mesure | bloqué | 06/12 | T-02 capture Whop |
| exp-02-comeup-gigs | bloqué | 20/12 | décision micro-entreprise (A-03) + T-04 vidéos |
| exp-03-skills-gumroad | prêt à publier | 20/12 | décision micro-entreprise (A-03) |
Suivant si un test meurt : primes-bancaires (28, 0 €) ou gbp-optimisation (30, à fusionner avec exp-02).

## En attente de Baptiste
- **A-03** (Telegram) : publier exp-03 maintenant (= créer la micro-entreprise) ?
- T-01 : place de parking oui/non (1 min). T-02 capture Whop (dimanche). T-04 vidéos (le jour de la publication).
- T-03 fait (BIOS reporté). Contrat : aucune clause bloquante. Pas de SIRET ; micro-entreprise reportée jusqu'à A-03.

## Technique
- Runs : MFYM-quotidien 07:30 (opus) / 13:00 / 19:00 (sonnet), hebdo dim. 10:00, digest 20:30, backup 03:00, heartbeat 5 min. Tâches en S4U (tournent sans session) ; redémarrage validé 22/11 12:06.
- Lanceur `scripts/run.ps1` (verrou, timeout, quota/auth, alertes). Garde-fou `.claude/hooks/guard.py`. Activité `.claude/hooks/activity.py` → memory/activity.jsonl.
- Bot `scripts/bot.py` (service), envoi `scripts/tg.py`, maintenance `scripts/maint.py`.
- Dashboard : `dashboard/` (port 8700, téléphone https://desktop-ava6s00.tailf6027f.ts.net:8445), critique 4/5 partout.
- Appels claude hors lanceur : `python scripts/with_token.py <cmd>` (le /login interactif expire).
- Version Claude Code figée : 2.1.278 (DISABLE_AUTOUPDATER=1). Monter de version exprès, puis lancer `run.ps1 -Goal test`.
