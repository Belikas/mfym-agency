import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent/"demos"))
from common import shot
here = pathlib.Path(__file__).parent
for n, h in [("S1-2-execution.png", 188), ("S1-4-workflow-n8n.png", 188)]:
    p = here/"_t.html"
    p.write_text(f"<body style=margin:0><img src={n} style=width:300px;display:block></body>", encoding="utf-8")
    out = here/("_small_" + n)
    shot(p, out, 300, h)
    print(n, "->", out, out.exists(), out.stat().st_size)
p.unlink()
