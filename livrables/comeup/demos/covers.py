"""Génère les 3 couvertures ComeUp 1280x720 (HTML/CSS -> PNG via Chrome headless). Même gabarit, accent différent."""
import pathlib, tempfile
from common import shot, ASSETS
Y = "#FACC15"
ARROW = '<svg width="110" height="60" viewBox="0 0 110 60"><path d="M5 30h88M70 8l28 22-28 22" fill="none" stroke="#fff" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/></svg>'
box = lambda inner, c="#fff": f'<div style="width:190px;height:190px;border-radius:26px;background:{c};display:flex;align-items:center;justify-content:center;flex-direction:column;font-weight:800">{inner}</div>'
def svg(p, c): return f'<svg width="100" height="100" viewBox="0 0 100 100" fill="none" stroke="{c}" stroke-width="7" stroke-linejoin="round" stroke-linecap="round">{p}</svg>'
colis = svg('<path d="M50 10L88 30V70L50 90L12 70V30Z"/><path d="M12 30L50 50L88 30M50 50V90"/>', "#1D4ED8")
alerte = svg('<path d="M50 12L92 86H8Z"/><path d="M50 40V60M50 73V74"/>', "#DC2626")
lines = lambda c: "".join(f'<div style="height:12px;border-radius:6px;background:{c};margin:11px 0;width:{w}%"></div>' for w in (90, 70, 85, 55, 78))
docs = '<div style="position:relative;width:170px;height:200px">' + "".join(f'<div style="position:absolute;left:{i*16}px;top:{i*14}px;width:150px;height:185px;background:#fff;border-radius:10px;border:3px solid #c4b5fd;padding:18px 16px">{lines("#cbd5e1")}</div>' for i in range(3)) + '</div>'
bubble = lambda t, bg, fg, al: f'<div style="align-self:{al};background:{bg};color:{fg};font-weight:700;font-size:34px;padding:16px 26px;border-radius:26px;max-width:460px">{t}</div>'
pdf = f'<div style="width:150px;height:200px;background:#fff;border-radius:8px;padding:22px 18px;clip-path:polygon(0 0,75% 0,100% 22%,100% 100%,0 100%)">{lines("#cbd5e1")}</div>'
grid = '<div style="display:grid;grid-template-columns:repeat(3,100px);gap:6px;background:#fff;padding:8px;border-radius:10px">' + "".join(f'<div style="height:38px;border-radius:4px;background:{"#0F766E" if i < 3 else "#d1fae5"};{"" if i < 3 else "color:#065f46"};font:700 20px Segoe UI;display:flex;align-items:center;padding-left:10px;color:{"#fff" if i < 3 else "#065f46"}">{["Date","N°","TTC","05/11","0187","195,84","10/11","064","612,00","12/11","5520","281,40"][i]}</div>' for i in range(12)) + '</div>'
C = {
 "S1-couverture": ("#0F172A", "#1D4ED8", ["Automatisez votre", f'<span style="color:{Y}">logistique</span>'],
   f'{box(colis)}{ARROW}{box("<span style=\'font-size:58px;color:#0F172A\'>n8n</span>")}{ARROW}{box(alerte)}'),
 "S2-couverture": ("#2E1065", "#6D28D9", ["Votre assistant IA", f'<span style="color:{Y}">répond</span>'],
   f'{docs}{ARROW}<div style="display:flex;flex-direction:column;gap:16px;width:520px">{bubble("Délai de retour ?", "#fff", "#2E1065", "flex-end")}{bubble("30 jours après réception.", "#FACC15", "#2E1065", "flex-start")}</div>'),
 "S3-couverture": ("#052E2B", "#0F766E", ["PDF vers", f'<span style="color:{Y}">tableur</span>, par IA'],
   f'{pdf}{ARROW}{grid}<div style="position:absolute;right:50px;bottom:24px;font:700 28px Segoe UI;color:#fff;opacity:.85">n8n</div>'),
}
for name, (c1, c2, title, visual) in C.items():
    h = f"""<!doctype html><meta charset=utf-8><style>*{{margin:0;box-sizing:border-box}}
body{{width:1280px;height:720px;background:linear-gradient(135deg,{c1},{c2});font-family:'Segoe UI Black','Arial Black',Arial,sans-serif;color:#fff;position:relative;overflow:hidden}}
h1{{position:absolute;left:60px;top:50px;font-size:118px;line-height:1.05;font-weight:900;letter-spacing:-2px}}
.v{{position:absolute;left:60px;right:60px;bottom:50px;height:230px;display:flex;align-items:center;gap:28px}}</style>
<h1>{title[0]}<br>{title[1]}</h1><div class=v>{visual}</div>"""
    p = pathlib.Path(tempfile.mkdtemp())/"c.html"; p.write_text(h, encoding="utf-8"); shot(p, ASSETS/f"{name}.png", 1280, 720)
