À remplir avant publication : [LIEN GITHUB] (dépôt public du skill, pas encore créé) ; [LIEN GUMROAD] (page presale, decision le 20/12/2026 — si le projet est abandonné à cette date, retirer ce lien ou le remplacer avant de publier) ; vérifier à la publication que le compte Discourse utilisé a bien atteint trust level 1 (liens débloqués).

Catégorie retenue : **Help me Build my Workflow** (`community.n8n.io/c/help-me-build-my-workflow/36`), pas « Built with n8n ». Règle citée : *« Need help creating an n8n workflow? Stuck on a tricky automation? This is the place to collaborate with other community members and build your workflows in public! »* — ça correspond au post (je n'ai pas encore branché le script sur n8n, je demande comment le faire), contrairement à « Built with n8n » qui exige un projet déjà construit *avec* n8n.

---

## Looking for the cleanest way to run this stock-report script from n8n

I keep seeing the same manual task at small warehouses: export inventory from the WMS (or an Excel sheet acting as one), then build a pivot table by hand to find stockouts, overstocks, and counts that don't match the system. Every week, same file, same copy-paste.

I built a small tool for this — a **Claude Code skill** (plain Python, standard library only) that reads a CSV export and flags stockouts, overstocks, and inventory-count discrepancies, free to use: [LIEN GITHUB].

Real output on a 100-SKU sample file:
> 8 réf. en rupture (REF-1064, REF-1065, REF-1067…) · 8 surstocks à écouler (REF-1092, REF-1091…) · 6 écart(s) d'inventaire à vérifier (REF-1097, REF-1095…)

*(translation: 8 SKUs out of stock · 8 overstocks to clear · 6 inventory discrepancies to check — the tool's interface is French-only right now, see below)*

Two honest limits:
- The interface is French-only right now (error messages, expected column headers). No English version yet.
- The inventory-discrepancy check uses a relative threshold: the larger of 5 units or 10% of theoretical stock. Under ~50 units of theoretical stock, the 5-unit floor dominates, so a discrepancy needs to reach roughly 40-50% before it's flagged on small SKUs. Not fixed yet, just disclosed.

I'd like to turn this into a scheduled n8n workflow — drop the weekly export in, get the report back — but I haven't wired it up myself. Right now my plan is just a schedule trigger feeding an **Execute Command** node that calls `python run.py export.csv` on demand.

Is Execute Command the right tool for this kind of "run an external script, get a file back" step, or is there a cleaner pattern people use instead — a Code node, a reusable sub-workflow, something else?
