"""Chatbot FAQ local : recherche par mots-clés (TF-IDF simplifié) dans faq.md, cite la section source, dit « je ne sais pas » sous le seuil.
Lancer : python app.py  puis http://localhost:8765  (aucune API, aucune dépendance)"""
import re, math, json, unicodedata, pathlib, datetime, html
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
here = pathlib.Path(__file__).parent
THRESHOLD = 1.0
STOP = set("le la les un une des de du d l et ou en a au aux je tu il on nous vous ce ca que qui quoi quel quels quelle est sont ai as avez avons puis peut pour par sur dans mon ma mes votre vos y".split())
def toks(s):
    s = unicodedata.normalize("NFD", s.lower()); s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return [w[:5] for w in re.findall(r"[a-z0-9]+", s) if w not in STOP and len(w) > 1]
docs = [(m.group(1), m.group(2).strip()) for m in re.finditer(r"## ([^\n]+)\n(.+?)(?=\n## |\Z)", (here/"faq.md").read_text(encoding="utf-8"), re.S)]
N = len(docs); df = {}
for t, b in docs:
    for w in set(toks(t + " " + b)): df[w] = df.get(w, 0) + 1
def ask(q):
    qt = set(toks(q)); best = (0, None)
    for t, b in docs:
        dt = set(toks(t + " " + b)); sc = sum(math.log(1 + N/df[w]) for w in qt & dt)
        if sc > best[0]: best = (sc, (t, b))
    if best[0] < THRESHOLD:
        with open(here/"unanswered.log", "a", encoding="utf-8") as f: f.write(f"{datetime.datetime.now():%Y-%m-%d %H:%M}\t{q}\n")
        return {"answer": "Je ne sais pas : cette information n'est pas dans la FAQ. Je transmets votre question à l'équipe, qui vous répondra par e-mail sous 24 h ouvrées.", "source": None, "score": round(best[0], 2)}
    t, b = best[1]; return {"answer": b, "source": f"FAQ Boutique Démo > {t}", "score": round(best[0], 2)}
PAGE = (here/"widget.html").read_text(encoding="utf-8")
class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def send(self, body, ct="text/html"):
        self.send_response(200); self.send_header("Content-Type", ct + "; charset=utf-8"); self.end_headers(); self.wfile.write(body.encode())
    def do_GET(self):
        u = urlparse(self.path)
        if u.path == "/ask": self.send(json.dumps(ask(parse_qs(u.query).get("q", [""])[0]), ensure_ascii=False), "application/json")
        elif u.path == "/log":
            p = here/"unanswered.log"; rows = p.read_text(encoding="utf-8").splitlines() if p.exists() else []
            self.send("<meta charset=utf-8><body style='font:16px Segoe UI;margin:0'><div style='background:#2E1065;color:#fff;padding:10px 24px;display:flex;justify-content:space-between'><span>Questions sans réponse</span><b style='background:#FACC15;color:#0f172a;padding:2px 10px;border-radius:4px'>Exemple – données fictives</b></div><div style='padding:22px 28px'><h2>Questions à compléter dans la FAQ</h2><table border=0 cellpadding=8 style='border-collapse:collapse;width:100%'><tr style='background:#6D28D9;color:#fff'><th align=left>Date</th><th align=left>Question</th></tr>" + "".join(f"<tr style='border-bottom:1px solid #ddd'><td>{html.escape(r.split(chr(9))[0])}</td><td>{html.escape(r.split(chr(9))[1])}</td></tr>" for r in rows) + "</table></div>")
        else: self.send(PAGE)
if __name__ == "__main__": HTTPServer(("127.0.0.1", 8765), H).serve_forever()
