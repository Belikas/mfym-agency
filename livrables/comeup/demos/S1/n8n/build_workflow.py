"""Génère workflow.json (importable dans n8n). Lancer : python build_workflow.py"""
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
N = lambda name, typ, v, x, params: {"parameters": params, "name": name, "type": typ, "typeVersion": v, "position": [x, 0], "id": name.lower().replace(" ", "-")}
nodes = [
 N("Démarrer", "n8n-nodes-base.manualTrigger", 1, 0, {}),
 N("Fichier orders", "n8n-nodes-base.readWriteFile", 1, 220, {"fileSelector": f"{D}/orders.csv"}),
 N("Lire orders", "n8n-nodes-base.extractFromFile", 1, 440, {"operation": "csv"}),
 N("Fichier tracking", "n8n-nodes-base.readWriteFile", 1, 660, {"fileSelector": f"{D}/tracking.csv"}),
 N("Lire tracking", "n8n-nodes-base.extractFromFile", 1, 880, {"operation": "csv"}),
 N("Détecter les retards", "n8n-nodes-base.code", 2, 1100, {"jsCode": LATE}),
 N("Rédiger les messages", "n8n-nodes-base.code", 2, 1320, {"jsCode": MSG}),
]
names = [n["name"] for n in nodes]
conn = {a: {"main": [[{"node": b, "type": "main", "index": 0}]]} for a, b in zip(names, names[1:])}
(here/"workflow.json").write_text(json.dumps({"name": "Détection des colis en retard (démo, données fictives)", "nodes": nodes, "connections": conn, "settings": {}}, ensure_ascii=False, indent=1), encoding="utf-8")
print("workflow.json écrit,", len(nodes), "nœuds")
