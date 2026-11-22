# Légendes des visuels ComeUp (toutes les captures portent « Exemple – données fictives »)

Règle : les démos S1 et S3 sont des scripts Python locaux, PAS des workflows n8n. Ne pas écrire « n8n » dans les légendes des captures. La couverture montre le nom « n8n » (texte seul) comme le prévoit le brief : à retirer si la page ne propose pas n8n.

## S1 – Logistique e-commerce
- S1-couverture.png : couverture 1280x720.
- S1-1-donnees-entree.png : « Entrée : export commandes et statuts transporteur (données fictives). »
- S1-2-execution.png : « Le script lit les deux fichiers et détecte 4 expéditions à risque sur 10. »
- S1-3-sorties.png : « Sortie : messages clients prêts à envoyer et résumé d'alerte (retard, incident, absence de scan). »

## S2 – Assistant IA sur documents
Aucune IA générative ici : recherche par mots-clés dans une FAQ fictive. Ne pas écrire « IA » ou « Claude » dans les légendes des captures.
- S2-couverture.png : couverture 1280x720.
- S2-1-reponse-sourcee.png : « L'assistant répond à partir de votre document et cite la section source. »
- S2-2-hors-perimetre.png : « Hors périmètre : il dit qu'il ne sait pas et transmet la question à l'équipe. »
- S2-3-questions-sans-reponse.png : « Journal des questions sans réponse, pour compléter la FAQ. »

## S3 – Extraction de documents
Extraction déterministe (texte du PDF + règles), sans IA. L'étape IA, utile pour les documents scannés ou mal structurés, n'est pas illustrée : ne pas la suggérer par ces captures.
- S3-couverture.png : couverture 1280x720.
- S3-1-pdf-entree.png : « Entrée : facture PDF fictive et champs lus. »
- S3-2-tableau-extrait.png : « Sortie : 8 factures converties en tableau, 4 marquées à vérifier. »
- S3-3-incoherence.png : « Cas douteux signalé : HT + TVA ne correspond pas au TTC. Aucune correction automatique. »
