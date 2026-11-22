# Légendes des visuels ComeUp (toutes les captures portent « Exemple – données fictives »)

## Ce qui est réel / illustré (état au 22/11/2026)
- RÉEL : exécution du workflow S1 avec la CLI n8n 2.48.7 (import + `execute`, statut success, 7 nœuds, 4 colis détectés = résultat du script Python de référence). Journal brut : demos/S1/n8n/out/n8n-execution.log.
- RÉEL : détection de retards, extraction de PDF par règles, recherche FAQ avec citation de la source, hors périmètre sans fausse réponse.
- NON RÉALISÉ : génération par Claude (S2) et extraction par Claude (S3). La CLI `claude` locale est déconnectée (« OAuth session expired », 22/11) : le code est écrit (demos/llm.py, `S2_LLM=1 python app.py`, `python extract.py --ai`) mais jamais exécuté avec succès. Aucune capture n'est présentée comme une réponse IA. À débloquer : Baptiste lance `claude` une fois pour se reconnecter, puis relancer les deux commandes et les shots.
- Ne pas écrire « IA » ni « Claude » dans les légendes S2/S3 tant que ce n'est pas fait.

## S1 – Logistique e-commerce
- S1-couverture.png : couverture 1280x720 (le nom « n8n » y figure : cohérent, un workflow n8n réel existe).
- S1-1-donnees-entree.png : « Entrée : export commandes et statuts transporteur (données fictives). »
- S1-2-execution.png : « Exécution réelle du workflow avec n8n : 7 nœuds, 4 expéditions à risque sur 10 détectées. »
- S1-3-sorties.png : « Sortie : messages clients prêts à envoyer et résumé d'alerte (retard, incident, absence de scan). » (généré par le script Python de référence, mêmes 4 colis que n8n)
- S1-4-workflow-n8n.png : « Schéma généré depuis le workflow n8n réel (pas une capture de l'éditeur). » Les nombres d'éléments viennent de l'exécution.
- Limite honnête : pas d'envoi d'e-mail dans la démo (messages rédigés seulement) ; pas d'étape IA dans S1.

## S2 – Assistant sur documents
Démo actuelle = recherche pondérée dans une FAQ fictive, réponse = passage cité (pas de texte généré).
- S2-couverture.png : couverture 1280x720.
- S2-1-reponse-sourcee.png : « Question sur la livraison : l'assistant répond avec le passage de la FAQ et cite sa source. »
- S2-2-hors-perimetre.png : « Deux questions hors FAQ (cartes cadeaux, magasin à Lyon) : il dit qu'il ne sait pas et transmet à l'équipe. » (faux positif « cartes cadeaux » corrigé)
- S2-3-questions-sans-reponse.png : « Journal des questions sans réponse, pour compléter la FAQ. »

## S3 – Extraction de documents
Extraction déterministe (texte du PDF + règles), sans IA. L'étape IA (documents scannés ou mal structurés) n'est pas illustrée.
- S3-couverture.png : couverture 1280x720 (« par IA » dans le titre : à retirer ou à réécrire tant que l'étape IA n'est pas démontrée).
- S3-1-pdf-entree.png : « Entrée : facture PDF fictive et champs lus. »
- S3-2-tableau-extrait.png : « Sortie : 8 factures converties en tableau, 4 marquées à vérifier. »
- S3-3-incoherence.png : « Cas douteux signalé : HT + TVA (648,00 €) ne correspond pas au TTC (612,00 €). Aucune correction automatique. »
