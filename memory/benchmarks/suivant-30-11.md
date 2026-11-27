# Test suivant (après exp-03/exp-04 bloqués) — 2026-11-27

Recherche faite en avant-plan, 8 requêtes web. Limites : Gumroad/Notion Marketplace n'exposent pas de compteurs lisibles par fetch (marché FR de templates NON MESURÉ) ; fiscalité cashback = source secondaire seulement (BOFiP non trouvé). Toutes les pistes restent en confiance low.

| | notion-templates-fr | cashback | chrome-extension-niche |
|---|---|---|---|
| Micro-entreprise pour encaisser | OUI (vente répétée, A-07) | NON (remise conso, non imposable selon Previssima, à confirmer) | OUI (Stripe/ExtensionPay récurrent) |
| Heures Baptiste avant 1er euro | ~6 h (templates, compte, A-07) | ~2 h (inscriptions + 1 achat prévu) | ~10 h (compte CWS, Stripe, A-07, tests) |
| Coût de démarrage | 0 EUR | 0 EUR | 5 EUR (CWS) + frais Stripe |
| Preuve (sans intérêt financier) | IH : 1 cas 15 000 EUR, non représentatif ; pas de compteur FR | Culture-financiere : 100-200 EUR/an (surtout primes bancaires) | IH : 36 $ MRR/2 ans ; 52 installs/0 EUR en 6 sem. |
| Revenu réaliste | ~0-80 EUR/mois | ~5-12 EUR/mois | 0 EUR typique ; 300+ EUR rare |
| Délai 1er euro | ~30 j | ~45 j (validation marchand) | ~60 j |
| Scores délai/preuve/revenu/coût/heures/auto/risque | 2/2/1/5/3/3/3 | 4/2/1/5/3/1/4 | 2/2/2/4/2/4/3 |
| **Total /45** | **23** | **26** | **23** |

Anciens totaux (28 chacun) sur-estimaient : la micro-entreprise n'était pas prise en compte, ni le fait que CWS ne gère plus les paiements.

## Recommandation : cashback (26), seule piste lançable sans A-07

Honnêtement : gain plafonné ~10 EUR/mois, ne rapproche pas des 1000 EUR. Elle gagne au total et au critère décisif (aucune micro-entreprise, ~2 h de Baptiste, 0 EUR). Son rôle est de produire un premier euro réel et un test mesuré pendant que A-07 est en attente.

- Hypothèse : sur des achats déjà prévus, un cashback (iGraal ou équivalent) donne >= 10 EUR de gains confirmés (statut « validé ») en 28 jours.
- Métrique : euros de cashback au statut validé/payable.
- Seuil : >= 10 EUR validés = continuer (puis chaîner avec exp-04) ; < 3 EUR = tuer.
- Kill date proposée : 2026-12-30 (au lieu de 4 semaines glissantes depuis le démarrage, car la validation marchand prend 30-60 j ; le statut « en attente » ne compte pas).
- Condition de départ : Baptiste crée 1 compte (tâche ~20 min) et déclare 1 achat prévu >= 100 EUR.

## Ce que l'agence construit seule avant toute action de Baptiste

1. Liste des achats récurrents/prévus à décider avec lui en 1 question oui/non (Noël, abonnements, courses).
2. Fiche comparative des taux publics des plateformes pour les marchands visés et du seuil de retrait.
3. Tâche Telegram pré-rédigée (étapes, temps, retour attendu : capture du statut « en attente »).
4. Confirmer la position fiscale dans le BOFiP / service-public avant paiement.

## Piste à fort potentiel à préparer en parallèle (après A-07) : extension Chrome

Plafond plus haut mais 57 % des extensions font 0 EUR. Niches où l'avantage de Baptiste (React/TS, logistique, n8n) est réel mais demande NON vérifiée : (a) ouvrir/suivre en masse des numéros de suivi multi-transporteurs ; (b) validateur SSCC/EAN/GS1 dans la page ; (c) copier/coller de nodes n8n entre instances. L'agence peut prototyper (a) seule en gratuit avant tout compte payant ; vérifier la demande (recherches CWS, forums logistique) avant d'y investir des heures.

Notion templates : rejetée pour l'instant (marché FR non mesurable, attente d'approbation Notion, exp-03 Gumroad déjà bloqué).

## Correction du directeur (27/11 07:50)
La règle du pipeline prend le meilleur total parmi les pistes `scored`, pas parmi les 3 pistes à 28. Après la re-notation : primes-bancaires 31 (déjà exp-04), gbp-optimisation 30 (micro-entreprise, à fusionner avec exp-02), puis 27 pour superprof-code, prolific et n8n-productized-service. Cashback n'arrive qu'à 26.
- superprof-code et n8n-productized : micro-entreprise nécessaire (cours de programmation pour adultes = hors services à la personne, pas de CESU) → même blocage A-07.
- **prolific (27)** : seule pistes à 27 lançable sans A-07, 0 €, premier euro sous ~7 jours, ~80 €/mois. Prolific recrute activement en France (offres par ville, Paris inclus, 27/11). Inconnue : Prolific demande de déclarer les gains en « self-employed » → vérifier si un BNC non professionnel sans RNE suffit, avant de lancer.
- **Proposition pour le 30/11** : test suivant = prolific (cashback en repli). Il ne remplace un test que si l'un des 3 tests en cours est tué ou mis en pause (maximum 3 tests à la fois).
