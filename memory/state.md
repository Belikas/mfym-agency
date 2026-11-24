# État de l'agence — mis à jour le 24/11/2026 ~19:05 (run quotidien 1900)

## Chiffres
- Revenu net novembre : 0 € / objectif 1 000 €/mois. Dépenses : 0 € / 60 €.
- Premier euro visé : avant le 22/12/2026.
- **Date cible 1 000 €/mois : 31/03/2027**. Revue chaque dimanche.

## Le blocage est réel, mais il se lève pour 0 € (24/11)
Tout vérifié en source primaire aujourd'hui. Les 3 voies de contournement sont fermées, la micro-entreprise est la seule porte — et elle est quasi gratuite.
- **Aucune exonération pour vente occasionnelle** : pas de seuil chiffré, critère qualitatif (« profession habituelle », C. com. L121-1). Les chiffres qui circulent sont d'une autre nature : 305 € = seuil d'imposition, 2 000 €/30 transactions = dispense de *reporting* de la plateforme. Défaut d'immatriculation au RNE = délit, 7 500 € (L123-38-1), requalifiable en travail dissimulé (3 ans / 45 000 €, redressement +35 %).
- **ComeUp autorise un vendeur particulier sans statut** (CGU art. 7.12.1, FAQ « aucun statut n'est imposé ») et édite le document de vente à sa place. Mais c'est la barrière de la **plateforme**, pas celle de la loi — ne pas reconfondre les deux.
- **Codeur.com** : CGU exigent un statut → parkée. **CAE** (Coopaname, Oxalis, Smart) : fermée, le CAPE exclut les salariés à temps plein. **Portage salarial** : minimum conventionnel ~2 800-3 400 €/mois → inutilisable.
- **Micro-entreprise, vrai coût** : création gratuite (guichet INPI), **0 € de cotisations à CA nul** (déclaration « néant » obligatoire, 60,10 € par oubli), CFE exonérée 1re année puis si CA N-2 > 5 000 €, cumul CDI autorisé, paie et couverture santé inchangées, fermeture 30 jours. Baptiste n'a jamais refusé : « on la crée quand ce sera indispensable » — c'est maintenant. → **A-07**.
- **Droits d'auteur exclus de la micro-entreprise par la loi** (high) : redevances KDP/Gumroad = régime artiste-auteur BNC, auto-édition couverte. Un SIRET d'artiste-auteur resterait nécessaire (med, pages URSSAF inaccessibles). Sujet séparé, à poser après T-07.
- Détails : `memory/benchmarks/facturer-sans-statut.md`, `statut-artiste-auteur.md`, `canaux-hors-reddit-exp03.md`.

## Priorités
1. **exp-02 ComeUp** — la mieux notée (30/35, confiance high). 3 fiches prêtes mais plafonnées à 3/5 sur la preuve sans vidéos. Bloque sur **A-07** (micro-entreprise — remplace A-06, mal posée) puis **T-04** (3 vidéos, 45 min, script exact prêt dans `memory/drafts/script-video-T-04-comeup.md`).
2. **exp-03 Gumroad logistique** — publiable techniquement depuis le 23/11 (FR + EN, critique `publiable=true`). Diffusion prête : post pour community.n8n.io (« Help me Build my Workflow ») validé par le critique en 3 passes le 24/11 (`memory/drafts/post-n8n-community-exp03.md`). Bloque sur **A-04** et la création par Baptiste d'un compte community.n8n.io (gratuit). T-06 (règles Reddit) devenu secondaire. Plan de mesure : le seuil (≥30 inscrits) n'est pas mesurable sans une capture hebdo du tableau de bord Gumroad → à greffer sur T-02 le jour de la publication.
3. **exp-04 primes bancaires** — bloqué sur A-05. One-off qui finance le budget, pas une route vers l'objectif.
4. exp-01 clipping : remesuré 24/11 (111 clips, plafond ~39 €, inchangé). 0 € et 0 h jusqu'au 06/12.

## Tests (3 running, 1 bloqué)
| id | statut | kill date | bloqué par |
|---|---|---|---|
| exp-01-clipping-mesure | running (plafonné) | 06/12 | T-02 (euros payés) |
| exp-02-comeup-gigs | running (débloqué le 24/11) | 20/12 | A-07 + T-04 |
| exp-03-skills-gumroad | running (publiable, diffusion prête) | 20/12 | A-04 + compte community.n8n.io |
| exp-04-primes-bancaires | bloqué | 31/01 | A-05 |
Suivant si un test meurt : gbp-optimisation (30, à fusionner avec exp-02). codeur-n8n (29) parkée jusqu'à la micro-entreprise.

## En attente de Baptiste (3 approbations + 4 tâches)
- **A-07** (24/11) : créer la micro-entreprise maintenant. 0 €. Débloque exp-02, Google Business Profile, Codeur.com d'un coup.
- **A-04** (23/11) : publier la version gratuite d'exp-03 sur Gumroad. 0 €. Pas-à-pas prêt : `memory/drafts/pas-a-pas-A-04-gumroad.md`.
- **A-05** (23/11) : ouvrir un compte Fortuneo (FTNSEA, 250 €). Pas-à-pas prêt : `memory/drafts/pas-a-pas-A-05-fortuneo.md`.
- **T-07** (12 min) : inventaire des romans KDP/Gumroad et du compte manga+Patreon — ils ne sont dans aucune des 35 pistes, donc invisibles.
- T-06 (8 min) : règles Reddit + ancienneté du compte. **Secondaire** depuis qu'un canal hors Reddit existe.
- T-04 (45 min, script prêt) : 3 vidéos ComeUp, le jour où A-07 passe.
- T-02 (5 min, hebdo) : capture des gains Whop. T-01 : place de parking oui/non (1 min).
- Total ouvert : ~1,2 h.

## Technique
- Runs : MFYM-quotidien 07:30 (opus) / 13:00 / 19:00 (sonnet), hebdo dim. 10:00, digest 20:30, backup 03:00, heartbeat 5 min. Tâches en S4U.
- **La revue hebdo du 22/11 n'a jamais eu lieu** : run `skipped_locked` sortant en code 0, donc aucun réessai du planificateur et revue perdue. Vérifier dimanche 29/11 qu'elle tourne (`grep hebdo logs/runs.jsonl`).
- **À faire en session surveillée** : ajouter à `.claude/agents/chercheur.md` « si tu délègues, c'est en avant-plan ; un livrable annoncé mais non écrit ne compte pas » — l'édition de `.claude/` est refusée aux runs. Le chercheur s'est arrêté 3 fois en attendant ses sous-agents aujourd'hui.
- Lanceur `scripts/run.ps1` (verrou, timeout, quota/auth, alertes). Garde-fou `.claude/hooks/guard.py`. Activité `.claude/hooks/activity.py`.
- Bot `scripts/bot.py` (service), envoi `scripts/tg.py`, maintenance `scripts/maint.py`. Le bot n'envoie que ce qui a `telegram_message_id` vide : modifier une tâche déjà envoyée ne la renvoie pas.
- Digest : exclut désormais les approbations déjà traitées et liste les identifiants.
- Mesure exp-01 : `python scripts/clipping_stats.py`.
- Dashboard : `dashboard/` (port 8700, téléphone https://desktop-ava6s00.tailf6027f.ts.net:8445).
- Appels claude hors lanceur : `python scripts/with_token.py <cmd>`. Version Claude Code figée : 2.1.278 (DISABLE_AUTOUPDATER=1).
- Reddit bloque les outils web de l'agence (domaine entier) ; urssaf.fr, impots.gouv.fr, inpi.fr et hellobank.fr aussi (anti-bot) — passer par service-public.gouv.fr ou par Baptiste.
