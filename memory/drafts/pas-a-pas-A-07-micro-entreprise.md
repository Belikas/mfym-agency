# Pas-à-pas micro-entreprise (A-07) — à envoyer comme tâche dès que Baptiste répond "oui"

Source : memory/benchmarks/facturer-sans-statut.md (section 4). Ne pas renvoyer sur Telegram tant que A-07 n'a pas reçu "oui" — ce fichier n'est qu'un brouillon prêt à copier dans tasks.json.

## Étapes (≈30 min en ligne, gratuit)
1. Aller sur **formalites.entreprises.gouv.fr** (guichet unique INPI), créer un compte, choisir « Créer une entreprise » > personne physique > micro-entreprise.
2. Activité principale à déclarer : **prestations de services (BNC)** — régime qui s'applique à ComeUp (automatisations n8n/IA) et à Codeur.com le jour où ils redeviennent utiles. Si Baptiste vend aussi des biens (peu probable ici), ajouter une activité secondaire BIC — sinon, ne pas compliquer.
3. Renseigner identité, adresse, date de début d'activité (peut être déclarée jusqu'à 15 jours après le vrai démarrage, donc pas besoin d'attendre le SIRET pour préparer les 3 fiches ComeUp).
4. Pas de capital, pas de local professionnel à déclarer (domicile personnel suffit pour une activité de service en ligne).
5. Valider et transmettre : **gratuit**, confirmation immédiate par email, SIRET sous ~15 jours en moyenne.
6. Dès réception du SIRET, créer un compte **Urssaf Autoentrepreneur** (autoentrepreneur.urssaf.fr) pour les déclarations de chiffre d'affaires.

## Ce qui ne change rien pour Baptiste
- CDI : aucune autorisation à demander (sauf clause d'exclusivité du contrat — neutralisée automatiquement 1 an par la loi, Code du travail L1222-5). Paie, mutuelle, retraite salarié : inchangés.
- CFE (taxe locale) : exonérée la 1ère année, puis seulement due si le CA dépasse 5 000 €/an.

## Point de vigilance — à ne jamais oublier
- **Déclaration trimestrielle obligatoire même à 0 €** (case "néant" si aucune vente) sur autoentrepreneur.urssaf.fr. Oubli = pénalité de 60,10 €. Si le CA reste nul pendant 24 mois consécutifs (8 déclarations), radiation automatique — sans gravité si c'est voulu, mais à savoir.
- Taux de cotisation si CA > 0 : ~25,6 % du chiffre d'affaires en prestations de services/BNC (ex. 100 € encaissés → ~74 € nets avant impôt sur le revenu). À annoncer clairement dans toute fiche ComeUp pour calculer la vraie marge.

## Deliverable attendu
- Confirmation "fait" + date de la déclaration.
- Dès que le SIRET arrive (email INPI) : transférer le numéro pour qu'il soit noté dans pipeline.json (débloque formellement ComeUp/Codeur/GBP) et que les fiches ComeUp passent en publication.

## Fermeture (si jamais ça ne marche pas)
Déclaration de cessation gratuite sur le même guichet, radiation en 7-15 jours ouvrés.
