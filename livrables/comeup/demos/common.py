"""Helpers partagés : page HTML avec bandeau 'Exemple – données fictives' + capture via Chrome headless."""
import subprocess, pathlib, html
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
ASSETS = pathlib.Path(__file__).resolve().parent.parent / "assets"

CSS = """
*{box-sizing:border-box}body{margin:0;font:16px/1.45 'Segoe UI',Arial,sans-serif;background:#f1f5f9;color:#0f172a}
.bar{background:#0f172a;color:#fff;padding:10px 24px;display:flex;justify-content:space-between;font-size:15px}
.tag{background:#facc15;color:#0f172a;font-weight:700;padding:2px 10px;border-radius:4px}
main{padding:22px 28px}h1{font-size:24px;margin:0 0 14px}
table{border-collapse:collapse;width:100%;background:#fff;font-size:14px}
th{background:var(--a);color:#fff;text-align:left;padding:7px 9px}td{padding:6px 9px;border-bottom:1px solid #e2e8f0}
.bad{background:#fee2e2;color:#991b1b;font-weight:600}.ok{color:#166534}.warn{background:#fef9c3}
pre{background:#0f172a;color:#e2e8f0;padding:16px;border-radius:8px;font:14px/1.5 Consolas,monospace;white-space:pre-wrap}
.card{background:#fff;border-left:6px solid var(--a);border-radius:6px;padding:10px 14px;margin:0 0 10px;font-size:14px}
"""

def page(title, body, accent, label="Exemple – données fictives", extra_css=""):
    return f"""<!doctype html><meta charset=utf-8><style>:root{{--a:{accent}}}{CSS}{extra_css}</style>
<div class=bar><span>{html.escape(title)}</span><span class=tag>{label}</span></div><main>{body}</main>"""

def shot(html_path, png, w, h):
    url = html_path if str(html_path).startswith("http") else pathlib.Path(html_path).resolve().as_uri()
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={w},{h}",
                    f"--screenshot={png}", "--virtual-time-budget=3000", url], check=True, capture_output=True)
