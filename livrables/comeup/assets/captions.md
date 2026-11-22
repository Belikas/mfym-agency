# Légendes des visuels ComeUp (données fictives ; badge « Exemple – données fictives » selon image, voir S1)

## Ce qui est réel / illustré (état au 22/11/2026)
- RÉEL : exécution du workflow S1 avec la CLI n8n 2.48.7 (import + `execute`, statut success, 7 nœuds, 4 colis détectés = résultat du script Python de référence). Journal brut : demos/S1/n8n/out/n8n-execution.log.
- RÉEL : détection de retards, extraction de PDF par règles, recherche FAQ avec citation de la source, hors périmètre sans fausse réponse.
- RÉEL (22/11, après reconnexion) : génération Claude dans le prototype S2 (`S2_LLM=1`, réponse rédigée à partir du seul passage retrouvé) et extraction Claude dans S3 (`extract.py --ai`, 8/8 factures identiques aux règles). Prototypes en Python, PAS en n8n ; données fictives ; aucun test sur de vrais documents, ni scans/photos.

## S1 – Logistique e-commerce
- S1-couverture.png : couverture 1280x720 (le nom « n8n » y figure : cohérent, un workflow n8n réel existe).
- S1-1-donnees-entree.png : « Entrée : export commandes et statuts transporteur (données fictives). »
- S1-2-execution.png : « Exécution réelle du workflow avec n8n : 7 nœuds, 4 expéditions à risque sur 10 détectées. »
- S1-3-sorties.png : « Sortie : messages clients prêts à envoyer et résumé d'alerte (retard, incident, absence de scan). » (généré par le script Python de référence, mêmes 4 colis que n8n)
- S1-4-workflow-n8n.png : RETIRÉE de la galerie (elle montre un autre workflow, 8 nœuds dont une étape IA, jamais exécuté). Ne pas la publier ni la décrire comme la démo.
- Badge « Exemple – données fictives » : présent sur la couverture, S1-1 et S1-3 ; absent de S1-2 (le titre du workflow indique « données fictives »).
- Limite honnête : pas d'envoi d'e-mail dans la démo (messages rédigés seulement) ; pas d'étape IA exécutée (démo n8n de 7 nœuds sans IA).

## S2 – Assistant sur documents
Démo = recherche pondérée dans une FAQ fictive, puis réponse rédigée par Claude à partir du passage retrouvé (la source est citée).
- S2-couverture.png : couverture 1280x720.
- S2-1-reponse-sourcee.png : « Réponses rédigées par Claude à partir du passage de la FAQ, avec la source citée (données fictives). »
- S2-2-hors-perimetre.png : « Hors périmètre : il dit qu'il ne sait pas ; la question est enregistrée dans le journal de l'équipe (aucun e-mail envoyé dans la démo). Le transfert humain par e-mail est inclus à partir du palier Standard, non démontré ici. »
- S2-3-questions-sans-reponse.png : « Journal des questions sans réponse, pour compléter la FAQ. »
- Limite : prototype Python, pas n8n ; FAQ de 5 sections.

## S3 – Extraction de documents
Règles + relecture Claude sur 8 factures PDF fictives (accord 8/8 ; 4 factures piégées volontairement). Seules des factures sont démontrées : bons de livraison / CMR sur devis après test. Pas de scans ni de photos, pas de taux de lecture sur documents réels.
- S3-couverture.png : couverture 1280x720 (« par IA » désormais fondé sur l'étape Claude du prototype ; n8n désigne l'offre).
- S3-1-pdf-entree.png : « Entrée : facture PDF fictive, champs lus par les règles et relus par Claude. »
- S3-2-tableau-extrait.png : « Sortie : 8 factures fictives converties en tableau ; 4 d'entre elles contiennent volontairement une erreur ou un doublon pour montrer les contrôles (4 à vérifier). Colonne Claude (IA) : mêmes valeurs que les règles sur 8/8, ce qui ne mesure pas la précision réelle. »
- S3-3-incoherence.png : « Cas douteux signalé : HT + TVA (648,00 €) ne correspond pas au TTC (612,00 €). Aucune correction automatique. »
