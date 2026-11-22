"use strict";
// Dashboard de l'agence : bureau pixel (canvas) + cartes business. Données : api/state, live : api/events (SSE).

const WORKING_S = 90, INFLIGHT_S = 900, TERMINAL = ["Stop", "SessionEnd", "SubagentStop"];
const REDUCED = matchMedia("(prefers-reduced-motion: reduce)").matches;
const $ = (id) => document.getElementById(id);
const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const eur = (n) => (Math.round((+n || 0) * 100) / 100).toLocaleString("fr-FR", { maximumFractionDigits: 2 }) + " €";

let S = null;            // dernier état serveur
let skew = 0;            // horloge serveur - horloge locale (s)
const live = {};         // agent -> état live (mis à jour par SSE)
let lastMsg = 0, es = null;

const now = () => Date.now() / 1000 + skew;
const tsOf = (s) => { const t = Date.parse(s); return isNaN(t) ? null : t / 1000; };
function ago(t) {
  if (t == null) return "jamais";
  const d = Math.max(0, now() - t);
  if (d < 10) return "à l'instant";
  if (d < 60) return `il y a ${Math.floor(d)} s`;
  if (d < 3600) return `il y a ${Math.floor(d / 60)} min`;
  if (d < 86400) return `il y a ${Math.floor(d / 3600)} h`;
  return `il y a ${Math.floor(d / 86400)} j`;
}
const fmtDate = (s) => { const t = Date.parse(s); return isNaN(t) ? (s || "") : new Date(t).toLocaleDateString("fr-FR", { day: "2-digit", month: "2-digit" }); };
const fmtTime = (s) => { const t = Date.parse(s); return isNaN(t) ? "" : new Date(t).toLocaleTimeString("fr-FR", { hour: "2-digit", minute: "2-digit" }); };
const hours = (h) => { const m = Math.round(h * 60); return m < 60 ? `${m} min` : `${Math.floor(m / 60)} h${m % 60 ? String(m % 60).padStart(2, "0") : ""}`; };

function status(l) {
  if (!l || !l.last_event || TERMINAL.includes(l.last_event)) return "idle";
  const t = tsOf(l.last_active);
  if (t == null) return "idle";
  const lim = (l.last_event === "PreToolUse" || l.last_event === "SubagentStart") ? INFLIGHT_S : WORKING_S;
  return now() - t < lim ? "working" : "idle";
}

const TOOL_COLORS = [
  [/^(Edit|Write|MultiEdit|NotebookEdit)$/, "#6b96ff"],
  [/^(Bash|PowerShell)$/, "#ff9a3c"],
  [/^(Read|Grep|Glob|LS)$/, "#46d9e6"],
  [/^(WebSearch|WebFetch)$/, "#5fd38d"],
  [/^(Agent|Task)$/, "#b18cff"],
];
const toolColor = (t) => (TOOL_COLORS.find(([re]) => re.test(t || "")) || [0, "#e8dcb8"])[1];

// ---------- Prochain passage planifié (depuis le champ schedule) ----------
const DAYS = ["dim", "lun", "mar", "mer", "jeu", "ven", "sam"];
function nextRun(a) {
  if (a.next_run && tsOf(a.next_run)) return new Date(tsOf(a.next_run) * 1000);
  const sched = String(a.schedule || "");
  let best = null;
  const ref = new Date((now()) * 1000);
  for (const seg of sched.split(/[,+;]/)) {
    const m = seg.match(/(\d{1,2})\s*[:h]\s*(\d{2})/);
    if (!m) continue;
    const dm = seg.toLowerCase().match(/\b(dim|lun|mar|mer|jeu|ven|sam)/);
    for (let d = 0; d < 8; d++) {
      const c = new Date(ref); c.setDate(c.getDate() + d); c.setHours(+m[1], +m[2], 0, 0);
      if (c <= ref || (dm && DAYS[c.getDay()] !== dm[1])) continue;
      if (!best || c < best) best = c;
      break;
    }
  }
  return best;
}
function nextLabel(a) {
  const n = nextRun(a);
  if (!n) return /demande/i.test(a.schedule || "") ? "à la demande" : (a.schedule || "");
  const ref = new Date(now() * 1000), hm = n.toLocaleTimeString("fr-FR", { hour: "2-digit", minute: "2-digit" });
  const dd = Math.round((new Date(n).setHours(0, 0, 0, 0) - new Date(ref).setHours(0, 0, 0, 0)) / 864e5);
  return "prochain " + (dd === 0 ? hm : dd === 1 ? "demain " + hm : DAYS[n.getDay()] + ". " + hm);
}

// ---------- Sprites pixel (dessinés ici, pas d'image externe) ----------
const BODY = [
  "..........",
  "...hhhh...",
  "..hhhhhh..",
  ".hhhhhhhh.",
  ".hssssssh.",
  ".sesssses.",
  ".ssssssss.",
  "..ssmmss..",
  "....ss....",
  "..tttttt..",
  ".tttttttt.",
  "tttttttttt",
  "tttttttttt",
];
const SHIRTS = ["#e0574f", "#3f8efc", "#f2b838", "#4fbf7a", "#a970ff", "#ff8c42", "#2ec4c4", "#e86fb0", "#9ccc50", "#c9cfd8"];
const HAIRS = ["#2a1a12", "#d9a441", "#b5462e", "#1c1c2a", "#e8e4da", "#6b3a1e", "#5b4bb0"];
const SKINS = ["#f1c7a3", "#a86e4a", "#d9a07a", "#7a4b2f", "#f6d5b8"];
const ACC = [0, 1, 2, 0, 2, 1, 0, 1, 2, 0];   // 0 rien, 1 lunettes, 2 casque

function look(i) {
  return { shirt: SHIRTS[i % 10], hair: HAIRS[(i * 3) % 7], skin: SKINS[(i * 2) % 5], style: i % 4, acc: ACC[i % 10] };
}
function shade(hex, f) {
  const n = parseInt(hex.slice(1), 16);
  const c = [n >> 16, (n >> 8) & 255, n & 255].map((v) => Math.max(0, Math.min(255, Math.round(v * f))));
  return "#" + c.map((v) => v.toString(16).padStart(2, "0")).join("");
}
const spriteCache = new Map();
function spriteGrid(L, asleep) {
  const key = JSON.stringify(L) + asleep;
  if (spriteCache.has(key)) return spriteCache.get(key);
  const g = BODY.map((r) => r.split(""));
  const set = (x, y, c) => { if (g[y] && x >= 0 && x < 10) g[y][x] = c; };
  if (L.style === 1) for (let y = 3; y <= 9; y++) { set(0, y, "h"); set(9, y, "h"); }
  if (L.style === 2) { set(4, 0, "h"); set(5, 0, "h"); }
  if (L.style === 3) { set(2, 0, "h"); set(4, 0, "h"); set(6, 0, "h"); set(1, 2, "h"); set(8, 2, "h"); }
  if (L.acc === 1) ".geggggeg.".split("").forEach((c, x) => c !== "." && set(x, 5, c));
  if (L.acc === 2) { for (let x = 2; x <= 7; x++) set(x, 1, "k"); for (let y = 4; y <= 6; y++) { set(0, y, "k"); set(9, y, "k"); } }
  if (asleep) g[5] = g[5].map((c) => (c === "e" ? "z" : c));
  const col = { h: L.hair, s: L.skin, e: "#1a1420", m: shade(L.skin, 0.78), t: L.shirt, g: "#14121f", k: "#2b2b3a", z: shade(L.skin, 0.62) };
  const px = [];
  g.forEach((r, y) => r.forEach((c, x) => { if (c !== ".") px.push([x, y, col[c]]); }));
  spriteCache.set(key, px);
  return px;
}

// ---------- Verbes lisibles (jamais d'outil, de chemin ni de commande brute) ----------
const RAW = /[\\\/|;&$<>`{}=]|^\s*(cd|git|python3?|node|npm|npx|pip|cat|ls|sed|awk|grep|rg|echo|tail|head|curl|powershell|pwsh|bash|sh|mkdir|rm|cp|mv|taskkill|schtasks|wc|find|export|ml|gh|winget)\b|\.(py|js|json|jsonl|md|ps1|txt|html|css|sh)\b|\s-{1,2}\w/i;
const base = (p) => String(p).split(/[\\\/]/).filter(Boolean).pop() || "";
function short(s, n) {
  s = String(s || "").replace(/\s+/g, " ").trim();
  if (s.length <= n) return s;
  const c = s.lastIndexOf(" ", n);
  return s.slice(0, c > 12 ? c : n) + "…";
}
function human(tool, sum) {
  tool = tool || ""; sum = String(sum || "");
  if (/^(Read|Grep|Glob|LS)$/.test(tool)) return "Lit des fichiers";
  if (/^(Write|Edit|MultiEdit|NotebookEdit)$/.test(tool)) { const f = base(sum); return /^[\w .\-]+\.\w{1,6}$/.test(f) ? "Écrit " + f : "Écrit un fichier"; }
  if (/^(Bash|PowerShell)$/.test(tool)) return sum && !RAW.test(sum) ? short(sum, 60) : "Lance une commande";
  if (tool === "WebSearch") return "Cherche sur le web" + (sum && !RAW.test(sum) ? " : " + short(sum, 40) : "");
  if (tool === "WebFetch") return "Lit une page web";
  if (/^(Agent|Task)$/.test(tool)) return "Délègue une mission";
  if (/^mcp__/.test(tool)) return /browser|chrome/i.test(tool) ? "Utilise le navigateur" : "Utilise un outil externe";
  if (tool === "Skill") return "Utilise une compétence";
  if (tool === "ToolSearch") return "Cherche un outil";
  if (tool === "SendMessage") return "Envoie un message";
  if (/^(TodoWrite|Task\w+)$/.test(tool)) return "Met à jour sa liste";
  if (/^Artifact/.test(tool)) return "Publie une page";
  return tool ? "Travaille" : "";
}
const EV_VERB = { SessionStart: "Démarre", SubagentStart: "Démarre sa mission", SubagentStop: "Termine sa mission", Stop: "Termine", SessionEnd: "Session close" };
const humanEv = (e) => (e.tool ? human(e.tool, e.summary) : EV_VERB[e.event] || "") + (e.event === "PostToolUseFailure" ? " (échec)" : "");
const roleShort = (r) => String(r || "").split(/\s*[:(—–]\s*/)[0];

// ---------- Bureaux : grille régulière, salles = groupes étiquetés ----------
const CW = 40, CH = 40;
const ROOM_PAL = {
  direction: { wall: "#2c2447", trim: "#3d3360", f1: "#5a3d2b", f2: "#523726", name: "Direction" },
  recherche: { wall: "#1f3042", trim: "#2c4560", f1: "#2f4a3b", f2: "#2a4335", name: "Recherche" },
  atelier: { wall: "#29293e", trim: "#3a3a58", f1: "#3b4057", f2: "#353a50", name: "Atelier" },
  qualite: { wall: "#33243f", trim: "#4a3560", f1: "#4a3456", f2: "#43304e", name: "Qualité" },
  renforts: { wall: "#2b2a2a", trim: "#403d3a", f1: "#45403a", f2: "#3e3a34", name: "Renforts" },
};
const EXTRA_PAL = [["#253a3a", "#355454", "#3a5048", "#354a42"], ["#3a2a2a", "#553c3c", "#563f35", "#4f3930"], ["#2a2f3f", "#3c4560", "#40465a", "#3a4054"]];
function roomPal(id) {
  if (ROOM_PAL[id]) return ROOM_PAL[id];
  let h = 0; for (const c of id) h = (h * 31 + c.charCodeAt(0)) >>> 0;
  const p = EXTRA_PAL[h % EXTRA_PAL.length];
  return { wall: p[0], trim: p[1], f1: p[2], f2: p[3], name: id.charAt(0).toUpperCase() + id.slice(1) };
}

let rooms = [], scale = 3, layoutKey = "", frame = 0;

function deskAgents() {
  const team = (S && S.team && S.team.agents) || [];
  const list = team.map((a, i) => ({ ...a, look: look(i), room: a.room || "bureau" })).filter((a) => a.status !== "fired");
  const known = new Set(team.map((a) => a.id));
  Object.keys(live).filter((k) => !known.has(k) && !team.some((a) => a.name === k) && status(live[k]) === "working")
    .sort().forEach((k, j) => list.push({ id: k, name: k, role: "Renfort (sous-agent hors équipe)", room: "renforts", visitor: true, look: look(team.length + 3 + j) }));
  return list;
}
const liveOf = (a) => live[a.id] || live[a.name] || null;
const lookOf = (id) => { const i = ((S && S.team && S.team.agents) || []).findIndex((a) => a.id === id); return look(i < 0 ? 0 : i); };

function layout() {
  const box = $("office");
  const agents = deskAgents();
  scale = box.clientWidth >= 900 ? 4 : 3;
  const byRoom = new Map();
  agents.forEach((a) => { if (!byRoom.has(a.room)) byRoom.set(a.room, []); byRoom.get(a.room).push(a); });
  const key = scale + "|" + [...byRoom].map(([r, l]) => r + ":" + l.map((a) => a.id + (a.status || "") + (a.current_task || "") + (a.role || "")).join(",")).join(";") + "|" + !!(S && S.errors && S.errors.team);
  if (key === layoutKey) return;
  layoutKey = key;
  box.innerHTML = "";
  rooms = [];
  if (S && S.errors && S.errors.team && agents.length) box.insertAdjacentHTML("beforeend", `<p class="err" style="width:100%;text-align:center">team.json illisible : ${esc(S.errors.team)} (seuls les agents actifs sont montrés)</p>`);
  if (!agents.length) {
    box.innerHTML = `<p class="office-empty">${S && S.errors && S.errors.team ? "team.json illisible : " + esc(S.errors.team) : "Aucun agent dans team.json."}</p>`;
    return;
  }
  for (const [id, list] of byRoom) {
    const pal = roomPal(id);
    const sec = document.createElement("section");
    sec.className = "room";
    sec.style.setProperty("--n", list.length);
    sec.innerHTML = `<h3 class="room-label">${esc(pal.name)}</h3><div class="desks"></div>`;
    const grid = sec.querySelector(".desks");
    const desks = list.map((a, k) => {
      const b = document.createElement("button");
      b.className = "desk";
      b.style.setProperty("--ac", a.look.shirt);
      b.innerHTML = `<span class="scene" style="background:${pal.f1}"><canvas width="${CW}" height="${CH}" style="width:${CW * scale}px;height:${CH * scale}px" aria-hidden="true"></canvas></span>` +
        `<b class="nm">${esc(a.name)}</b><span class="role">${esc(roleShort(a.role))}</span>` +
        (a.current_task ? `<span class="task">Tâche : ${esc(a.current_task)}</span>` : "") +
        `<span class="st"></span><span class="bubble"></span>`;
      b.addEventListener("click", () => openAgent(a.id));
      grid.appendChild(b);
      const ctx = b.querySelector("canvas").getContext("2d");
      ctx.imageSmoothingEnabled = false;
      return { a, el: b, ctx, pal, first: k === 0 };
    });
    box.appendChild(sec);
    rooms.push({ id, desks });
  }
}

function rect(ctx, x, y, w, h, c) { ctx.fillStyle = c; ctx.fillRect(x, y, w, h); }

function drawScene(d) {
  const { ctx, pal } = d;
  for (let y = 14; y < CH; y += 6) for (let x = 0; x < CW; x += 6) rect(ctx, x, y, 6, 6, ((x + y) / 6) % 2 ? pal.f1 : pal.f2);
  rect(ctx, 0, 0, CW, 14, pal.wall);
  rect(ctx, 0, 13, CW, 1, pal.trim);
  rect(ctx, 0, 14, CW, 1, "rgba(0,0,0,.35)");
  if (d.first) {   // fenêtre de nuit, une par salle
    rect(ctx, 2, 1, 16, 11, pal.trim);
    rect(ctx, 3, 2, 14, 9, "#141c40");
    rect(ctx, 10, 2, 1, 9, pal.trim);
    [[2, 3], [10, 5], [5, 8], [12, 8], [3, 6]].forEach(([sx, sy], i) => {
      if (REDUCED || (frame >> 3) % 5 !== i) rect(ctx, 3 + sx, sy, 1, 1, "#e9e6ff");
    });
  }
  drawDesk(ctx, { a: d.a, x: 0, y: 0 });
}

function drawDesk(ctx, d) {
  const { a, x, y } = d;
  const l = liveOf(a);
  const working = status(l) === "working" && a.status !== "paused";
  const tc = toolColor(l && l.tool);
  const f = REDUCED ? 0 : frame;
  if (working) {
    ctx.globalAlpha = 0.14; rect(ctx, x + 1, y + 11, 20, 18, tc);
    ctx.globalAlpha = 0.14; rect(ctx, x + 3, y + 13, 16, 14, tc);
    ctx.globalAlpha = 1;
  }
  rect(ctx, x + 19, y + 16, 12, 10, "#2e2a45"); rect(ctx, x + 19, y + 16, 12, 1, "#423c63");
  const sx = x + 20, sy = y + 13 + (working ? 0 : 1);
  for (const [px, py, c] of spriteGrid(a.look, !working)) rect(ctx, sx + px, sy + py, 1, 1, c);
  rect(ctx, x + 2, y + 26, 36, 2, "#8a6a4a");
  rect(ctx, x + 2, y + 28, 36, 1, "#4a3526");
  rect(ctx, x + 2, y + 29, 36, 5, "#5e4532");
  rect(ctx, x + 3, y + 34, 2, 4, "#3d2c20"); rect(ctx, x + 35, y + 34, 2, 4, "#3d2c20");
  rect(ctx, sx, y + 26, 10, 1, "#c9c6d8");
  const up = working && !REDUCED && f % 2 === 0;
  rect(ctx, sx + 1, y + (working ? (up ? 24 : 25) : 25), 2, 1, a.look.skin);
  rect(ctx, sx + 7, y + (working ? (up ? 25 : 24) : 25), 2, 1, a.look.skin);
  rect(ctx, x + 33, y + 23, 3, 3, "#e9e4f5"); rect(ctx, x + 36, y + 24, 1, 1, "#e9e4f5");
  rect(ctx, x + 4, y + 15, 13, 9, "#1b1a26");
  rect(ctx, x + 9, y + 24, 3, 2, "#1b1a26"); rect(ctx, x + 7, y + 25, 7, 1, "#2a2838");
  if (working) {
    rect(ctx, x + 5, y + 16, 11, 7, shade(tc, 0.35));
    for (let i = 0; i < 3; i++) {
      const w = 3 + ((i * 5 + (f >> 1) * 3 + a.id.length) % 7);
      rect(ctx, x + 6 + (i === 1 ? 1 : 0), y + 17 + i * 2, Math.min(w, 9), 1, tc);
    }
  } else {
    rect(ctx, x + 5, y + 16, 11, 7, "#0d0c18");
    rect(ctx, x + 15, y + 23, 1, 1, a.status === "paused" ? "#ef5f6b" : "#f2b838");
    if (a.status !== "paused") {
      const ph = REDUCED ? 0 : (f >> 2) % 3;
      ctx.globalAlpha = 0.85;
      zee(ctx, x + 29, y + 7 - ph, 5, "#c4bcef");
      zee(ctx, x + 35, y + 2 - ph, 4, "#8e86bd");
      ctx.globalAlpha = 1;
    }
  }
}
function zee(ctx, x, y, n, c) {
  rect(ctx, x, y, n, 1, c); rect(ctx, x, y + n - 1, n, 1, c);
  for (let i = 1; i < n - 1; i++) rect(ctx, x + n - 1 - i, y + i, 1, 1, c);
}

function draw() { for (const r of rooms) for (const d of r.desks) drawScene(d); }

let timer = null;
function loop() {
  clearTimeout(timer);
  if (document.hidden) return;
  frame++;
  draw();
  const anyWorking = rooms.some((r) => r.desks.some((d) => status(liveOf(d.a)) === "working"));
  timer = setTimeout(loop, REDUCED ? 1000 : anyWorking ? 125 : 500);   // ≤ 8 i/s
}

// ---------- Textes des bureaux + bandeau (1×/s) ----------
const teamChip = (a) => {
  if (a.status === "fired") return ["licencié", "bad"];
  if (a.status === "paused") return ["en pause", "warn"];
  return status(liveOf(a)) === "working" ? ["au travail", "good"] : ["au repos", ""];
};
function updateDesks() {
  for (const r of rooms) for (const d of r.desks) {
    const l = liveOf(d.a), st = status(l), a = d.a;
    const working = st === "working" && a.status !== "paused";
    const bub = d.el.querySelector(".bubble"), sm = d.el.querySelector(".st");
    const bubble = working ? humanEv({ tool: l.tool, summary: l.summary, event: l.last_event }) || "Au travail" : "";
    let line;
    if (a.status === "paused") line = "En pause";
    else if (working) line = "Au travail";
    else line = "Au repos" + (a.visitor ? "" : " · " + nextLabel(a));
    if (bub.textContent !== bubble) bub.textContent = bubble;
    bub.style.setProperty("--tool", toolColor(l && l.tool));
    if (sm.textContent !== line) sm.textContent = line;
    d.el.classList.toggle("working", working);
    d.el.classList.toggle("paused", a.status === "paused");
    d.el.setAttribute("aria-label", `${a.name}, ${roleShort(a.role)} : ${line}${bubble ? ", " + bubble : ""}`);
  }
  document.querySelectorAll("[data-chip]").forEach((el) => {
    const a = ((S && S.team && S.team.agents) || []).find((x) => x.id === el.dataset.chip);
    if (!a) return;
    const [t, c] = teamChip(a);
    if (el.textContent !== t) { el.textContent = t; el.className = "chip " + c; }
  });
  const all = deskAgents();
  const w = all.filter((a) => status(liveOf(a)) === "working" && a.status !== "paused");
  $("work-val").textContent = w.length;
  $("work-of").textContent = ` / ${all.length} au bureau`;
  $("work-sub").textContent = w.length ? w.map((a) => a.name).join(", ") : "tout le monde dort";
  $("t-work").classList.toggle("has", w.length > 0);
  const on = es && es.readyState === 1 && Date.now() - lastMsg < 40000;
  $("live").classList.toggle("on", !!on);
  $("live-txt").textContent = on ? "en direct · maj " + ago(S && S.server_now) : "reconnexion…";
  const off = $("offline");
  off.hidden = !!on || !S;
  if (!off.hidden) off.textContent = "Hors ligne : ces données ne sont plus à jour (dernière mise à jour " + ago(S.server_now) + "). Reconnexion en cours.";
}

// ---------- Cartes ----------
const age = (f) => { const t = typeof f === "number" ? f : S && S.mtimes && S.mtimes[f]; return t ? `<span class="age" title="fraîcheur du fichier ${esc(f)}">maj ${ago(t)}</span>` : `<span class="age">pas encore de données</span>`; };
const errBox = (sec) => (S.errors && S.errors[sec] ? `<p class="err">Fichier illisible : ${esc(S.errors[sec])}</p>` : "");
const EXP_ST = { ready: ["prêt", "info"], running: ["en cours", "good"], blocked: ["bloqué", "warn"], scaled: ["étendu", "gold"], adjusted: ["ajusté", "info"], killed: ["tué", "bad"] };
const LEAD_ST = { testing: ["en test", "good"], scored: ["notée", ""], parked: ["en pause", ""], killed: ["abandonnée", "bad"], scaled: ["étendue", "gold"], new: ["nouvelle", "info"] };
const RUN_ST = { ok: "good", done: "good", success: "good", completed: "good", lock_test_done: "good", quota: "warn", timeout: "warn", skipped_locked: "", failed: "bad", error: "bad", failure: "bad", auth: "bad", wrapper_error: "bad" };
const RUN_LBL = { skipped_locked: "verrou pris", quota: "quota", timeout: "délai dépassé", failed: "échec", error: "erreur", ok: "ok", done: "fini", success: "ok", lock_test_done: "test verrou", auth: "connexion Claude", wrapper_error: "erreur lanceur" };
const CONF = { low: "faible", med: "moyenne", medium: "moyenne", high: "haute" };
const plain = (s) => String(s || "").replace(/[*_`#>|]+/g, "").replace(/\[([^\]]+)\]\([^)]*\)/g, "$1").replace(/\s+/g, " ").trim();
const chip = (lbl, cls) => `<span class="chip ${cls || ""}">${esc(lbl)}</span>`;
const daysLeft = (d) => { const t = Date.parse(d + "T23:59:59"); return isNaN(t) ? null : Math.ceil((t / 1000 - now()) / 86400); };
const row = (attrs, main, sub, right) => `<li><button class="row" ${attrs}><span class="main"><span class="t">${main}</span>${sub ? `<span class="s">${sub}</span>` : ""}</span>${right ? `<span class="r">${right}</span>` : ""}</button></li>`;

function card(id, title, n, src, body) {
  return `<article class="card" id="card-${id}"><h3>${esc(title)}${n != null ? ` <span class="n">${esc(n)}</span>` : ""}${src ? age(src) : ""}</h3>${body}</article>`;
}

function renderCards() {
  const out = [];
  const ap = S.approvals || [], tk = (S.tasks && S.tasks.open) || [];
  out.push(card("valider", "À valider", ap.length, "approvals.json", errBox("approvals") + (ap.length ? `<ul>${ap.map((a, i) =>
    row(`data-k="ap" data-i="${i}"`, esc(a.question), esc(a.reason || ""), `${chip(a.recommendation === "yes" ? "je dis oui" : "je dis non", "big " + (a.recommendation === "yes" ? "good" : "bad"))}<br>${eur(a.cost_eur)}`)).join("")}</ul>`
    : `<p class="empty">Aucune décision n'attend ta réponse.</p>`)));
  out.push(card("taches", "Tes tâches", tk.length ? `${tk.length} · ${hours(S.tasks.est_hours)}` : 0, "tasks.json", errBox("tasks") + (tk.length ? `<ul>${tk.map((t, i) =>
    row(`data-k="task" data-i="${i}"`, esc(t.title), esc(t.purpose || ""), `${esc(t.est_minutes ?? "?")} min`)).join("")}</ul>`
    : `<p class="empty">Aucune tâche ouverte.</p>`)));

  const ex = S.experiments || [];
  const exT = Math.max(0, ...Object.entries(S.mtimes || {}).filter(([f]) => f.startsWith("experiments/")).map(([, t]) => t || 0)) || "experiments/";
  out.push(card("tests", "Tests", ex.filter((e) => ["running", "blocked", "ready"].includes(e.status)).length + " actifs", exT, errBox("experiments") + (ex.length ? `<ul>${ex.map((e, i) => {
    const st = EXP_ST[e.status] || [e.status || "?", ""], dl = daysLeft(e.kill_date);
    const live = !["killed", "scaled"].includes(e.status);
    const when = e.kill_date ? (live && dl != null ? (dl < 0 ? `<span class="late">échu depuis ${-dl} j</span>` : `J-${dl}`) : "") + `<br>${fmtDate(e.kill_date)}` : "";
    return row(`data-k="exp" data-i="${i}"`, esc(e.title || e.id), chip(st[0], st[1]) + (e.error ? ` <span class="late">${esc(e.error)}</span>` : (e.blocked_on && e.blocked_on.length ? " " + esc(e.blocked_on[0]) : "")), when);
  }).join("")}</ul>` : `<p class="empty">Aucun test lancé.</p>`)));

  const rv = S.revenue;
  out.push(card("revenu", "Revenu net", null, "revenue.json", errBox("revenue") + (rv ? `<p class="ctx">Détail des encaissements · ${eur(rv.total_net)} net depuis le début</p>
    ${rv.entries.length ? `<ul>${rv.entries.slice().reverse().map((e) => `<li class="row static"><span class="main"><span class="t">${esc(e.source)}</span><span class="s">${fmtDate(e.date)}</span></span><span class="r">${eur(e.net_eur)}</span></li>`).join("")}</ul>` : `<p class="empty">Aucun revenu enregistré ce mois-ci.</p>`}` : "")));

  const xp = S.expenses;
  out.push(card("budget", "Budget", null, "expenses.json", errBox("expenses") + (xp ? `<p class="ctx">Détail des dépenses du mois</p>
    ${xp.entries.length ? `<ul>${xp.entries.map((e) => `<li class="row static"><span class="main"><span class="t">${esc(e.item)}</span><span class="s">${fmtDate(e.date)}${e.recurring ? " · mensuel" : ""}</span></span><span class="r">${eur(e.amount_eur)}</span></li>`).join("")}</ul>` : `<p class="empty">Aucune dépense ce mois-ci.</p>`}` : "")));

  const ld = S.leads;
  out.push(card("pistes", "Meilleures pistes", ld ? ld.count : null, "pipeline.json", errBox("leads") + (ld && ld.top.length ? `<p class="ctx">${Object.entries(ld.counts).map(([k, v]) => `${v} ${esc((LEAD_ST[k] || [k])[0])}`).join(" · ")}</p><ul>${ld.top.map((l, i) =>
    row(`data-k="lead" data-i="${i}"`, esc(l.name), `${chip((LEAD_ST[l.status] || [l.status])[0], (LEAD_ST[l.status] || [])[1])} confiance ${esc(CONF[l.confidence] || l.confidence || "?")}<span class="score"><i style="width:${(l.total / 45) * 100}%"></i></span>`, `<b style="color:var(--text)">${esc(l.total)}</b>/45<br>~${esc(l.est_monthly_eur ?? "?")} €/m`)).join("")}</ul>` : `<p class="empty">Aucune piste.</p>`)));

  const jr = S.journal || [];
  out.push(card("decisions", "Décisions récentes", null, "journal.md", errBox("journal") + (S.state_md ? `<ul>${row(`data-k="doc" data-p="state.md" data-t="Situation (state.md)"`, "Situation actuelle", "state.md", "")}</ul>` : "") + (jr.length ? `<ul>${jr.map((j, i) =>
    row(`data-k="dec" data-i="${i}"`, esc(j.title), esc(short(plain(j.body), 110)), "")).join("")}</ul>` : `<p class="empty">Journal vide pour l'instant.</p>`)));

  const team = (S.team && S.team.agents) || [];
    out.push(card("equipe", "Équipe", team.filter((a) => a.status !== "fired").length, "team.json", errBox("team") + (team.length ? `<ul>${team.map((a) =>
    row(`data-k="agent" data-id="${esc(a.id)}"`, `<span class="swatch" style="background:${lookOf(a.id).shirt}"></span>${esc(a.name)} <span class="chip">${esc(a.model || "?")}</span>`, esc(a.status === "fired" ? `licencié le ${fmtDate(a.fired)} : ${a.reason || ""}` : `${roomPal(a.room || "").name} · ${roleShort(a.role)}`), `<span data-chip="${esc(a.id)}" class="chip ${teamChip(a)[1]}">${teamChip(a)[0]}</span>`)).join("")}</ul>` : `<p class="empty">Aucun agent.</p>`)));

  const rn = S.runs || [];
  out.push(card("runs", "Runs récents", null, "runs.jsonl", errBox("runs") + (rn.length ? `<ul>${rn.map((r, i) =>
    row(`data-k="run" data-i="${i}"`, esc(r.goal || "run"), esc(ago(tsOf(r.ts))) + (r.minutes != null ? ` · ${esc(r.minutes)} min` : ""), chip(RUN_LBL[r.status] || r.status || "?", RUN_ST[r.status] ?? "warn"))).join("")}</ul>` : `<p class="empty">Aucun run planifié pour l'instant.</p>`)));

  const ss = S.sessions || [];
  out.push(card("sessions", "Sessions", ss.length || null, ss.length ? ss[0].mtime : "sessions/", errBox("sessions") + (ss.length ? `<ul>${ss.map((s) =>
    row(`data-k="doc" data-p="${esc(s.file)}" data-t="${esc(s.name)}"`, esc(s.title || s.name), esc(s.name), esc(ago(s.mtime)))).join("")}</ul>` : `<p class="empty">Pas encore de résumé de session.</p>`)));

  const html = out.join("");
  if ($("cards").dataset.h !== html) { $("cards").innerHTML = html; $("cards").dataset.h = html; }
}

function renderStrip() {
  const rv = S.revenue, xp = S.expenses, ap = S.approvals || [], tk = S.tasks || { open: [], est_hours: 0 };
  $("rev-val").textContent = rv ? eur(rv.month_net).replace(" €", "") : "?";
  $("rev-bar").style.width = rv ? Math.min(100, rv.month_net / 10) + "%" : "0";
  $("rev-sub").textContent = rv ? `${Math.round(rv.month_net / 10)} % · maj ${ago(S.mtimes["revenue.json"])}` : "revenue.json illisible";
  $("bud-val").textContent = xp ? eur(xp.month).replace(" €", "") : "?";
  $("bud-of").textContent = ` / ${xp ? xp.budget : 60} €`;
  $("bud-bar").style.width = xp ? Math.min(100, (xp.month / (xp.budget || 60)) * 100) + "%" : "0";
  $("bud-bar").classList.toggle("over", !!xp && xp.month > xp.budget);
  $("bud-sub").textContent = xp ? `reste ${eur(xp.budget - xp.month)} · maj ${ago(S.mtimes["expenses.json"])}` : "expenses.json illisible";
  const tgt = ((S.state_md || "").match(/Date cible[^:]*:\s*\**\s*(\d{2}\/\d{2}\/\d{4})/) || [])[1];
  $("headline").textContent = (rv && rv.month_net > 0 ? `${eur(rv.month_net)} net ce mois-ci` : "Rien ne rapporte encore") + " · " + (ap.length ? `${ap.length} décision${ap.length > 1 ? "s t'attendent" : " t'attend"}` : "aucune décision en attente") + (tgt ? ` · 1 000 €/mois visés le ${tgt}` : "");
  const n = ap.length + tk.open.length;
  $("you-val").textContent = n;
  $("you-unit").textContent = n ? ` · ${hours(tk.est_hours)}` : "";
  $("you-sub").textContent = n ? `${ap.length} à valider · ${tk.open.length} tâche${tk.open.length > 1 ? "s" : ""}` : "rien ne t'attend";
  $("t-you").classList.toggle("has", n > 0);
  $("t-you").href = ap.length ? "#card-valider" : "#card-taches";
}

// ---------- Tiroir (détail à la demande) ----------
const dlg = $("drawer");
function openDrawer(title, html) {
  $("dr-title").textContent = title;
  $("dr-body").innerHTML = html;
  if (!dlg.open) { dlg.showModal(); history.pushState({ drawer: 1 }, ""); }
  $("dr-body").scrollTop = 0;
}
function closeDrawer() { if (dlg.open) { dlg.close(); } }
$("dr-close").onclick = () => history.state && history.state.drawer ? history.back() : closeDrawer();
dlg.addEventListener("click", (e) => { if (e.target === dlg) $("dr-close").onclick(); });
dlg.addEventListener("cancel", (e) => { e.preventDefault(); $("dr-close").onclick(); });
addEventListener("popstate", closeDrawer);

const dl = (pairs) => `<dl>${pairs.filter(([, v]) => v != null && v !== "" && !(Array.isArray(v) && !v.length)).map(([k, v]) => `<dt>${esc(k)}</dt><dd>${Array.isArray(v) ? v.map(esc).join("<br>") : esc(v)}</dd>`).join("")}</dl>`;
function md(text) {
  const inl = (s) => esc(s).replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>").replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\[([^\]]+)\]\((https?:\/\/[^)\s]+)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>');
  let out = "", list = false, table = [];
  const flush = () => { if (list) { out += "</ul>"; list = false; } if (table.length) { out += `<pre>${esc(table.join("\n"))}</pre>`; table = []; } };
  for (const line of String(text).split(/\r?\n/)) {
    if (/^\s*\|/.test(line)) { if (list) { out += "</ul>"; list = false; } table.push(line); continue; }
    if (table.length) { out += `<pre>${esc(table.join("\n"))}</pre>`; table = []; }
    const h = line.match(/^(#{1,3})\s+(.*)/), li = line.match(/^\s*(?:[-*]|\d+\.)\s+(.*)/);
    if (h) { flush(); out += `<h${h[1].length + 2}>${inl(h[2])}</h${h[1].length + 2}>`; }
    else if (li) { if (!list) { out += "<ul>"; list = true; } out += `<li>${inl(li[1])}</li>`; }
    else if (!line.trim()) flush();
    else { if (list) { out += "</ul>"; list = false; } out += `<p>${inl(line)}</p>`; }
  }
  flush();
  return out;
}
async function openDoc(path, title) {
  openDrawer(title, `<p class="empty">Chargement…</p>`);
  try {
    const r = await fetch("api/doc?path=" + encodeURIComponent(path));
    if (!r.ok) throw new Error(r.status === 403 ? "accès refusé" : "erreur " + r.status);
    const t = await r.text();
    let html;
    if (path.endsWith(".json")) { try { html = `<pre>${esc(JSON.stringify(JSON.parse(t), null, 2))}</pre>`; } catch { html = `<p class="err">JSON illisible</p><pre>${esc(t)}</pre>`; } }
    else html = md(t);
    if ($("dr-title").textContent === title) $("dr-body").innerHTML = html;
  } catch (e) { $("dr-body").innerHTML = `<p class="err">Impossible de lire ${esc(path)} : ${esc(e.message)}</p>`; }
}
const rawBtn = (p, t) => `<button class="rawbtn" data-k="doc" data-p="${esc(p)}" data-t="${esc(t)}">Fichier complet</button>`;

function openAgent(id) {
  const team = (S && S.team && S.team.agents) || [];
  const inTeam = team.find((x) => x.id === id);
  const a = inTeam || { id, name: id, role: "Renfort (sous-agent hors équipe)", visitor: true };
  const l = liveOf(a), st = status(l);
  const evs = (l && l.recent) || [];
  const done = evs.filter((e) => /^PostToolUse/.test(e.event) && e.tool);
  const flying = evs[0] && evs[0].event === "PreToolUse" ? evs[0] : null;
  const acts = (flying ? [flying] : []).concat(done).slice(0, 3);
  const errs = done.filter((e) => e.event === "PostToolUseFailure").length;
  const [tl, tc] = inTeam ? teamChip(a) : [st === "working" ? "au travail" : "au repos", st === "working" ? "good" : ""];
  openDrawer(a.name, `<p>${chip(tl, tc)} ${l ? "dernier signe " + esc(ago(tsOf(l.last_active))) : "aucune activité enregistrée"}${errs ? " " + chip(errs + (errs > 1 ? " échecs récents" : " échec récent"), "bad") : ""}</p>` +
    `<h4>3 dernières actions</h4>` + (acts.length ? acts.map((e) => `<div class="ev"><span class="when">${esc(e === flying ? "en cours" : ago(tsOf(e.ts)))}</span><span class="what"><span class="swatch" style="background:${toolColor(e.tool)}"></span>${esc(humanEv(e))}</span></div>`).join("") : `<p class="empty">Aucune action récente enregistrée.</p>`) +
    dl([["Tâche en cours", a.current_task], ["Dernier résultat", a.last_result], ["Dernier run", a.last_run && fmtDate(a.last_run) + " " + fmtTime(a.last_run)], ["Prochain passage", inTeam ? nextLabel(a).replace(/^prochain /, "") : null]]) +
    `<details class="cfg"><summary>Configuration</summary>` +
    dl([["Rôle", a.role], ["Salle", a.room && roomPal(a.room).name], ["Mesure", a.metric], ["Modèle", a.model], ["Planning", a.schedule], ["Entrées", a.inputs], ["Sorties", a.outputs], ["Note critique", a.avg_critic_score], ["Statut", a.status], ["Embauché", a.hired && fmtDate(a.hired)], ["Licencié", a.fired && `${fmtDate(a.fired)} : ${a.reason || ""}`], ["Fichier", a.file]]) + `</details>`);
}

document.addEventListener("click", (e) => {
  const b = e.target.closest("[data-k]");
  if (!b || !S) return;
  const i = +b.dataset.i, k = b.dataset.k;
  if (k === "doc") return openDoc(b.dataset.p, b.dataset.t);
  if (k === "agent") return openAgent(b.dataset.id);
  if (k === "exp") {
    const x = S.experiments[i], st = EXP_ST[x.status] || [x.status, ""], d = daysLeft(x.kill_date);
    return openDrawer(x.title || x.id, `<p>${chip(st[0], st[1])} ${x.kill_date ? `date de décision ${esc(fmtDate(x.kill_date))}${d != null ? ` (${d < 0 ? "échue depuis " + -d + " j" : "J-" + d})` : ""}` : ""}</p>` +
      dl([["Hypothèse", x.hypothesis], ["Mesure", x.metric], ["Seuil", x.threshold], ["Coût", x.cost_eur != null ? eur(x.cost_eur) : null], ["Heures prévues", x.hours_budget], ["Début", x.start && fmtDate(x.start)], ["Bloqué par", x.blocked_on], ["Agent", x.owner_agent], ["Piste", x.lead_id], ["Décision", x.decision], ["Décidé le", x.decided_at && fmtDate(x.decided_at)]]) +
      `<h4>Résultats</h4>` + ((x.results || []).length ? `<ul>${x.results.map((r) => `<li><b>${esc(fmtDate(r.date))}</b>${r.value != null ? " · " + esc(typeof r.value === "object" ? JSON.stringify(r.value) : r.value) : ""} : ${esc(r.note)}</li>`).join("")}</ul>` : `<p class="empty">Pas encore de résultat.</p>`) + rawBtn(x._file, x.title || x.id));
  }
  if (k === "lead") {
    const l = S.leads.top[i], sc = l.scores || {};
    const SC = { time_to_first_euro: "Délai 1er euro (×2)", evidence: "Preuves (×2)", monthly_revenue: "Revenu mensuel", startup_cost: "Coût de départ", baptiste_hours: "Heures Baptiste", automation: "Automatisation", risk: "Risque" };
    return openDrawer(l.name, `<p>${chip((LEAD_ST[l.status] || [l.status])[0], (LEAD_ST[l.status] || [])[1])} <b>${esc(l.total)}</b>/45 · confiance ${esc(CONF[l.confidence] || l.confidence)} · ${l.evidenced ? "prouvée" : "non prouvée"}</p>` +
      dl([["Description", l.description], ["Atout", l.edge], ["Catégorie", l.category], ["Revenu estimé", l.est_monthly_eur != null ? l.est_monthly_eur + " €/mois" : null], ["Coût de départ", l.startup_cost_eur != null ? eur(l.startup_cost_eur) : null], ["1er euro", l.first_euro_days != null ? `~${l.first_euro_days} j` : null], ["Premier test", l.first_test], ["Légal", l.legal_notes]]) +
      `<h4>Notes</h4>` + Object.entries(SC).map(([k2, lbl]) => `<div class="ev"><span class="what" style="flex:1">${esc(lbl)}<span class="score"><i style="width:${(sc[k2] || 0) * 20}%"></i></span></span><span class="when" style="text-align:right">${esc(sc[k2] ?? "?")}/5</span></div>`).join("") +
      `<h4>Sources</h4>` + ((l.sources || []).length ? `<ul>${l.sources.map((s) => `<li>${/^https?:\/\//.test(s.url) ? `<a href="${esc(s.url)}" target="_blank" rel="noopener noreferrer">${esc(s.kind)}</a>` : esc(s.kind)}${s.financial_interest ? " (intéressée)" : " (neutre)"} : ${esc(s.finding)}</li>`).join("")}</ul>` : `<p class="empty">Aucune source.</p>`));
  }
  if (k === "ap") {
    const a = S.approvals[i];
    return openDrawer("À valider", `<p><b>${esc(a.question)}</b></p>` + dl([["Ma recommandation", a.recommendation === "yes" ? "oui" : "non"], ["Pourquoi", a.reason], ["Coût", eur(a.cost_eur)], ["Demandé", fmtDate(a.created) + " " + fmtTime(a.created)], ["Réf.", a.id]]) + `<p class="ctx">Réponds sur Telegram.</p>`);
  }
  if (k === "task") {
    const t = S.tasks.open[i];
    return openDrawer(t.title, dl([["Pourquoi", t.purpose], ["Temps estimé", t.est_minutes != null ? t.est_minutes + " min" : null], ["À renvoyer", t.deliverable], ["Débloque", t.blocks], ["Créée", fmtDate(t.created)], ["Réf.", t.id]]) +
      `<h4>Étapes</h4>` + ((t.steps || []).length ? `<ol>${t.steps.map((s) => `<li>${esc(s)}</li>`).join("")}</ol>` : `<p class="empty">Pas d'étapes.</p>`));
  }
  if (k === "dec") { const j = S.journal[i]; return openDrawer(j.title, md(j.body) + rawBtn("journal.md", "Journal")); }
  if (k === "run") {
    const r = S.runs[i];
    return openDrawer(`Run ${r.goal || ""}`, `<p>${chip(RUN_LBL[r.status] || r.status || "?", RUN_ST[r.status] ?? "warn")} ${esc(fmtDate(r.ts))} ${esc(fmtTime(r.ts))}</p>` + dl(Object.entries(r).map(([kk, v]) => [kk, typeof v === "object" ? JSON.stringify(v) : String(v)])));
  }
});

// ---------- Données ----------
function seedLive() {
  const team = (S.team && S.team.agents) || [];
  for (const a of team) if (a.live) live[a.id] = a.live;
  for (const v of (S.team && S.team.visitors) || []) live[v.id] = v.live;
}
async function refresh() {
  try {
    const r = await fetch("api/state", { cache: "no-store" });
    if (!r.ok) throw new Error(r.status);
    S = await r.json();
    skew = S.server_now - Date.now() / 1000;
    seedLive();
    renderStrip(); renderCards(); layout(); updateDesks();
  } catch (e) {
    $("live-txt").textContent = "serveur injoignable";
    $("live").classList.remove("on");
  }
}
function applyEvent(e) {
  if (!e || !e.agent) return;
  const team = (S && S.team && S.team.agents) || [];
  const a = team.find((x) => x.id === e.agent || x.name === e.agent);
  const key = a ? a.id : e.agent;
  const l = live[key] || (live[key] = { recent: [] });
  l.last_event = e.event; l.last_active = e.ts; l.status = null;
  if (e.tool) { l.tool = e.tool; l.summary = e.summary || ""; }
  l.recent = [e, ...(l.recent || [])].slice(0, 14);
  layout(); updateDesks();
  if (!timer || REDUCED) loop();
}
function connect() {
  if (es) es.close();
  es = new EventSource("api/events");
  es.onopen = () => { lastMsg = Date.now(); refresh(); };
  es.onmessage = (m) => { lastMsg = Date.now(); try { applyEvent(JSON.parse(m.data)); } catch { /* ligne invalide ignorée */ } };
  es.addEventListener("ping", (m) => { lastMsg = Date.now(); const t = +m.data; if (t) skew = t - Date.now() / 1000; });
  es.onerror = () => updateDesks();
}

// chien de garde : connexion muette 40 s (veille, réseau coupé) = on rouvre
setInterval(() => { if (!document.hidden && Date.now() - lastMsg > 40000) connect(); }, 10000);
setInterval(() => { if (!document.hidden && S) { updateDesks(); renderStrip(); } }, 1000);
setInterval(() => { if (!document.hidden) refresh(); }, 30000);
document.addEventListener("visibilitychange", () => {
  if (document.hidden) return clearTimeout(timer);
  refresh();
  if (Date.now() - lastMsg > 20000) connect();
  loop();
});
addEventListener("online", () => { connect(); refresh(); });
let rz; addEventListener("resize", () => { clearTimeout(rz); rz = setTimeout(() => { layout(); updateDesks(); draw(); }, 150); });

refresh().then(loop);
connect();
