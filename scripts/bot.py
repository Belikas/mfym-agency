"""Bot Telegram de l'agence : service permanent (long polling), indépendant des sessions Claude.
- n'accepte que TELEGRAM_CHAT_ID (au premier /start, si vide, enregistre ce chat) ;
- envoie les approbations et tâches non encore envoyées (memory/approvals.json, tasks.json) ;
- boutons Oui/Non -> approvals.json + déclenche un run ; bouton Fait -> tasks.json ;
- textes, fichiers, photos -> memory/inbox.jsonl (fichiers dans memory/inbox_files/) ;
- /secret CLE valeur -> écrit dans .env et efface le message."""
import json, subprocess, time, traceback, urllib.request
from datetime import datetime
from pathlib import Path
import tg

ROOT, M = tg.ROOT, tg.M
FILES = M / "inbox_files"
TRIGGER = ROOT / "run" / "trigger.flag"
LOCK = ROOT / "run" / "agency.lock"
OFFSET = ROOT / "run" / "bot_offset.txt"
HEARTBEAT = ROOT / "run" / "bot_alive.txt"
RUN_PS1 = ROOT / "scripts" / "run.ps1"


def now():
    return datetime.now().astimezone().isoformat(timespec="seconds")


def save(name, data):
    data["updated"] = now()
    tmp = M / f"{name}.tmp"
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    tmp.replace(M / name)


def inbox(entry):
    entry = {"ts": now(), **entry}
    with (M / "inbox.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def push_outbox():
    """Envoie ce que les runs ont préparé (telegram_message_id vide)."""
    ap = tg.load("approvals.json")
    changed = False
    for a in ap["approvals"]:
        if a["status"] == "pending" and not a.get("telegram_message_id"):
            reco = "Oui" if a["recommendation"] == "yes" else "Non"
            text = f"APPROBATION {a['id']}\n{a['question']}\nCoût : {a['cost_eur']:.0f} €\nMa reco : {reco} — {a['reason']}"
            mid = tg.send(text, "approval", [[{"text": "Oui", "callback_data": f"ap:{a['id']}:yes"},
                                              {"text": "Non", "callback_data": f"ap:{a['id']}:no"}]])
            if mid:
                a["telegram_message_id"], changed = mid, True
    if changed:
        save("approvals.json", ap)
    tk = tg.load("tasks.json")
    changed = False
    for t in tk["tasks"]:
        if t["status"] == "open" and not t.get("telegram_message_id"):
            steps = "\n".join(f"{i}. {s}" for i, s in enumerate(t["steps"], 1))
            text = (f"TÂCHE {t['id']} (~{t['est_minutes']} min)\n{t['title']}\nPourquoi : {t['purpose']}\n{steps}\n"
                    f"À renvoyer : {t['deliverable']}\n(réponds à ce message pour envoyer)")
            mid = tg.send(text, "task", [[{"text": "Fait", "callback_data": f"tk:{t['id']}:done"}]])
            if mid:
                t["telegram_message_id"], changed = mid, True
    if changed:
        save("tasks.json", tk)


def trigger_run():
    TRIGGER.touch()


def maybe_launch():
    """Lance le run 'reponses' si demandé et si aucun run ne tient le verrou."""
    if TRIGGER.exists() and not LOCK.exists():
        TRIGGER.unlink()
        subprocess.Popen(["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(RUN_PS1),
                          "-Goal", "reponses", "-MaxTurns", "40", "-TimeoutMin", "30"],
                         cwd=ROOT, creationflags=subprocess.CREATE_NO_WINDOW)


def find_by_msg(items, mid):
    return next((x for x in items if x.get("telegram_message_id") == mid), None)


def on_callback(cq):
    kind, item_id, val = cq["data"].split(":", 2)
    tg.api("answerCallbackQuery", callback_query_id=cq["id"], text="Noté")
    if kind == "ap":
        ap = tg.load("approvals.json")
        a = next((x for x in ap["approvals"] if x["id"] == item_id), None)
        if a and a["status"] == "pending":
            a["status"], a["answered_at"] = val, now()
            save("approvals.json", ap)
            inbox({"type": "callback", "approval_id": item_id, "text": val, "message_id": cq["message"]["message_id"]})
            tg.api("editMessageReplyMarkup", chat_id=cq["message"]["chat"]["id"], message_id=cq["message"]["message_id"],
                   reply_markup={"inline_keyboard": [[{"text": f"Réponse : {'Oui' if val == 'yes' else 'Non'}", "callback_data": "noop:x:x"}]]})
            trigger_run()
    elif kind == "tk":
        tk = tg.load("tasks.json")
        t = next((x for x in tk["tasks"] if x["id"] == item_id), None)
        if t and t["status"] == "open":
            t["status"], t["done_at"] = "done", now()
            save("tasks.json", tk)
            inbox({"type": "callback", "task_id": item_id, "text": "done", "message_id": cq["message"]["message_id"]})
            tg.api("editMessageReplyMarkup", chat_id=cq["message"]["chat"]["id"], message_id=cq["message"]["message_id"],
                   reply_markup={"inline_keyboard": [[{"text": "Fait", "callback_data": "noop:x:x"}]]})
            trigger_run()


def download(file_id, name):
    FILES.mkdir(exist_ok=True)
    info = tg.api("getFile", file_id=file_id)
    token = tg.env()["TELEGRAM_BOT_TOKEN"]
    dest = FILES / f"{datetime.now():%Y%m%d-%H%M%S}-{Path(name).name}"
    with urllib.request.urlopen(f"https://api.telegram.org/file/bot{token}/{info['file_path']}", timeout=60) as r:
        dest.write_bytes(r.read())
    return str(dest.relative_to(ROOT))


def on_message(msg):
    chat_id = str(msg["chat"]["id"])
    text = msg.get("text") or msg.get("caption") or ""
    if text.startswith("/secret "):
        parts = text.split(maxsplit=2)
        tg.api("deleteMessage", chat_id=chat_id, message_id=msg["message_id"])
        if len(parts) == 3 and parts[1].isupper() and parts[1] not in ("ANTHROPIC_API_KEY", "TELEGRAM_CHAT_ID"):
            tg.set_env(parts[1], parts[2])
            tg.send(f"{parts[1]} enregistré dans .env, message effacé.", "alert")
            inbox({"type": "command", "text": f"/secret {parts[1]} (valeur masquée)", "message_id": msg["message_id"]})
        else:
            tg.send("Format : /secret NOM_EN_MAJUSCULES valeur", "alert")
        return
    if text == "/status":
        tg.send(tg.digest(), "alert")
        return
    entry = {"type": "text", "text": text, "message_id": msg["message_id"], "processed": False}
    reply = msg.get("reply_to_message")
    if reply:
        mid = reply["message_id"]
        t = find_by_msg(tg.load("tasks.json")["tasks"], mid)
        a = find_by_msg(tg.load("approvals.json")["approvals"], mid)
        if t:
            entry["task_id"] = t["id"]
        if a:
            entry["approval_id"] = a["id"]
    if msg.get("document"):
        entry.update(type="file", file_path=download(msg["document"]["file_id"], msg["document"].get("file_name", "fichier")))
    elif msg.get("photo"):
        entry.update(type="photo", file_path=download(msg["photo"][-1]["file_id"], "photo.jpg"))
    inbox(entry)
    tg.api("setMessageReaction", chat_id=chat_id, message_id=msg["message_id"], reaction=[{"type": "emoji", "emoji": "👍"}])
    if entry.get("task_id") or entry["type"] != "text":
        trigger_run()


def main():
    offset = int(OFFSET.read_text()) if OFFSET.exists() else 0
    last_push = 0
    while True:
        HEARTBEAT.write_text(now())
        e = tg.env()
        if not e.get("TELEGRAM_BOT_TOKEN"):
            time.sleep(60)
            continue
        try:
            if time.time() - last_push > 30:
                push_outbox()
                maybe_launch()
                last_push = time.time()
            for u in tg.api("getUpdates", offset=offset, timeout=25, allowed_updates=["message", "callback_query"]):
                offset = u["update_id"] + 1
                OFFSET.write_text(str(offset))
                src = u.get("message") or u.get("callback_query", {}).get("message") or {}
                chat_id = str(src.get("chat", {}).get("id", ""))
                if not e.get("TELEGRAM_CHAT_ID") and u.get("message", {}).get("text", "").startswith("/start"):
                    tg.set_env("TELEGRAM_CHAT_ID", chat_id)
                    tg.log_local("bot", f"chat ID enregistré : {chat_id}")
                    tg.send("Bot de l'agence connecté. Tu recevras ici approbations, tâches, alertes et le digest du soir.", "alert")
                    continue
                if chat_id != tg.env().get("TELEGRAM_CHAT_ID"):
                    tg.log_local("bot", f"message ignoré d'un chat inconnu {chat_id}")
                    continue
                if "callback_query" in u:
                    if not u["callback_query"]["data"].startswith("noop"):
                        on_callback(u["callback_query"])
                else:
                    on_message(u["message"])
        except Exception:
            tg.log_local("bot-error", traceback.format_exc(limit=3))
            time.sleep(15)


if __name__ == "__main__":
    main()
