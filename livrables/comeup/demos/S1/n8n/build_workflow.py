"""Génère workflow.json (7 nœuds, exécuté par run_n8n.sh) et workflow-standard.json (+ étape IA, palier
Standard : non exécuté ici, voir README — sert uniquement à une capture de l'éditeur). Lancer : python build_workflow.py"""
import json, pathlib
here = pathlib.Path(__file__).parent
D = (here.parent).as_posix()   # dossier contenant orders.csv / tracking.csv
LATE = r"""
const TODAY = new Date('2026-11-20'), STALE = 3, day = 86400000;
const track = Object.fromEntries($input.all().map(i => [i.json.tracking, i.json]));
const out = [];
for (const {json: o} of $('Lire orders').all()) {
  const t = track[o.tracking]; let reason = null;
  const late = Math.round((TODAY - new Date(o.promised)) / day);
  if (!t) reason = 'aucun statut de suivi';
  else if (t.status === 'delivered') continue;
  else if (t.status === 'exception') reason = 'incident transporteur';
  else if (late > 0) reason = `${late} j de retard sur la date promise`;
  else if ((TODAY - new Date(t.last_scan)) / day >= STALE) reason = `aucun scan depuis ${Math.round((TODAY - new Date(t.last_scan)) / day)} j`;
  if (reason) out.push({json: {...o, reason}});
}
return out;
"""
MSG = r"""
return $input.all().map(({json: o}) => {
  const [y, m, d] = o.promised.split('-');
  return {json: {to: o.email, order: o.order_id, reason: o.reason,
    subject: `Votre commande ${o.order_id} – point sur la livraison`,
    body: `Bonjour ${o.customer.split(' ')[0]},\nvotre colis (${o.carrier}, suivi ${o.tracking}) devait arriver le ${d}/${m}. Il connaît un retard (${o.reason}). Nous suivons le dossier auprès du transporteur et revenons vers vous sous 24 h.\nL'équipe boutique`}};
});
"""
# Étape IA (palier Standard) : un Code node shell-out vers classify_ai.py (CLI Claude headless, pas d'API payante).
# Nécessite NODE_FUNCTION_ALLOW_BUILTIN=child_process au démarrage de n8n (voir run_n8n.sh).
SCRIPT = json.dumps(str(here/"classify_ai.py"))
AI = (
 "const { execFileSync } = require('child_process');\n"
 "return $input.all().map(({json: o}) => {\n"
 "  const urgence = execFileSync('python', [" + SCRIPT + "], "
 "{input: JSON.stringify({order: o.order_id, reason: o.reason}), encoding: 'utf8', timeout: 60000}).trim();\n"
 "  return {json: {...o, urgence}};\n"
 "});\n"
)
N = lambda name, typ, v, x, params: {"parameters": params, "name": name, "type": typ, "typeVersion": v, "position": [x, 0], "id": name.lower().replace(" ", "-").replace("'", "")}

def build(id_, name, nodes):
    nodes[3]["executeOnce"] = True  # une seule lecture du fichier tracking, pas une par commande
    names = [n["name"] for n in nodes]
    conn = {a: {"main": [[{"node": b, "type": "main", "index": 0}]]} for a, b in zip(names, names[1:])}
    return {"id": id_, "name": name, "nodes": nodes, "connections": conn, "settings": {}}

base = lambda: [
 N("Démarrer", "n8n-nodes-base.manualTrigger", 1, 0, {}),
 N("Fichier orders", "n8n-nodes-base.readWriteFile", 1, 220, {"fileSelector": f"{D}/orders.csv"}),
 N("Lire orders", "n8n-nodes-base.extractFromFile", 1, 440, {"operation": "csv"}),
 N("Fichier tracking", "n8n-nodes-base.readWriteFile", 1, 660, {"fileSelector": f"{D}/tracking.csv"}),
 N("Lire tracking", "n8n-nodes-base.extractFromFile", 1, 880, {"operation": "csv"}),
 N("Détecter les retards", "n8n-nodes-base.code", 2, 1100, {"jsCode": LATE}),
]
nodes7 = base() + [N("Rédiger les messages", "n8n-nodes-base.code", 2, 1320, {"jsCode": MSG})]
nodes8 = base() + [N("Classer l'urgence (IA)", "n8n-nodes-base.code", 2, 1320, {"jsCode": AI}),
                    N("Rédiger les messages", "n8n-nodes-base.code", 2, 1540, {"jsCode": MSG})]
(here/"workflow.json").write_text(json.dumps(build("colisRetard01", "Détection des colis en retard (démo, données fictives)", nodes7), ensure_ascii=False, indent=1), encoding="utf-8")
(here/"workflow-standard.json").write_text(json.dumps(build("colisRetard01Standard", "Détection des colis en retard + étape IA (palier Standard, démo)", nodes8), ensure_ascii=False, indent=1), encoding="utf-8")
print("workflow.json (7 nœuds) et workflow-standard.json (8 nœuds, + IA) écrits")
