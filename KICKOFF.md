# Kickoff — Make Fuck You Money

Read `CLAUDE.md` first: it holds the permanent rules. This prompt is the one-time setup that gets the agency running on its own.

## The goal of this kickoff

**Baptiste does almost nothing.** He does not read chats or long reports. He glances at a dashboard, taps Yes/No on Telegram, and does only the human-only tasks you give him, batched.

At the end of the kickoff, the agency runs by itself: scheduled runs fire automatically, agents work, their activity shows live on the dashboard (PC and phone), and Baptiste gets pinged on Telegram only when he's needed. Business milestone: first euro within 30 days.

## This kickoff spans several sessions

It won't fit in one session. Create `memory/kickoff.md` from the "Done when" checklist below, with a status and a proof for each item. Until every item is checked, each scheduled run continues the kickoff before doing business work. Business research (Phase 4) runs in parallel from the start: money comes first.

## First message, before any work

Baptiste is at the terminal right now. Send him one short message in French with the full list of things only he can do, with exact steps and time estimates. He does them while you work; don't wait.

- Create the Telegram bot with BotFather; put the token and his chat ID in `.env`.
- Generate the Claude Code auth token for headless runs (`claude setup-token`) and put it in `.env`.
- Install Tailscale on the PC (as a service) and on his phone.
- Windows settings: no sleep, Windows Update active hours, auto-login if browser automation needs a desktop session, BIOS set to power back on after a power cut.
- Check his employment contract (exclusivity, non-compete) and his micro-entreprise status.
- Create a free private GitHub repo for backups and a free healthchecks.io account.

## Phase 0 — Foundations

- Project structure, every `memory/` file from `CLAUDE.md`, JSON schemas in `memory/schemas/`.
- Git, with a daily push to the private GitHub repo. `.env`, `activity.jsonl` and logs are in `.gitignore`.
- **Guardrails for unattended runs:** use the non-interactive permission mode, plus a PreToolUse hook script (Python) that blocks writes outside the project and destructive commands. Deny rules alone are too easy to bypass. Prove it works with 3 test commands that must be blocked.

## Phase 1 — Unattended operation

Check the current official Claude Code docs first: headless mode, permission modes, hooks, scheduling. Things change fast.

- **Wrapper:** Windows Task Scheduler calls a PowerShell script that uses absolute paths (claude, Git Bash via `CLAUDE_CODE_GIT_BASH_PATH`, python), loads the auth token from `.env`, and makes sure `ANTHROPIC_API_KEY` is not set.
- **Lock** against overlapping runs. Every run is logged.
- **Cadence:** fits the Max 5x limits (rolling windows plus a weekly cap). Each run has one goal, a turn limit and a time limit (see `CLAUDE.md`).
- **Alerts:** two failures in a row, auth failure or token expiry → Telegram alert. Until the bot exists, alerts go to a log file.
- **Survives a reboot:** the scheduler, the Telegram bot, the dashboard server and Tailscale all restart on their own (Windows services via NSSM, or Task Scheduler with restart on failure). A startup check logs proof. Ask Baptiste to reboot the PC as a task, then verify.
- **Heartbeat:** ping healthchecks.io on a schedule, so Baptiste is alerted if the PC itself goes down.
- **Updates:** pin the Claude Code version. Upgrade on purpose, and test a run after each upgrade.

## Phase 2 — Telegram

The bot is a **standalone, always-on service** (Python or Node, long polling), not a Claude session. Without it, Baptiste's taps go nowhere while no session is running.

- Accepts messages only from Baptiste's chat ID.
- **Approvals:** yes/no inline buttons, each with your recommendation and the cost. Answers go to `approvals.json`. An answered approval triggers a run right away (respecting the lock) instead of waiting for the next slot.
- **Tasks:** he marks them done or replies with what you asked for (text, file, screenshot). Everything lands in `inbox.jsonl`.
- **Secrets:** a command that writes a key into `.env` and deletes his message from the chat.
- Daily digest and noise limit as in `CLAUDE.md`.

## Phase 3 — Dashboard

### What Baptiste must see, at a glance
- **The company:** rooms, each agent at its desk, who is working right now and on what, who is idle, when each one last worked and next works (from `team.json` schedules).
- **Live activity:** what each agent is doing in real time (searching what, building what, testing what).
- **Results:** revenue vs €1,000/month, budget spent vs €50–60, tests running with status and kill date, top leads and scores, recent decisions, agents hired or fired.
- **What's waiting on him:** pending approvals and tasks.
- **Detail on demand:** any agent, test, decision or session can be opened to read its full report. Nothing long is shown by default.

Key information first, understood in seconds. Reading is optional.

### How to build it
1. **Benchmark.** Study existing visualizers that show Claude Code agents as a pixel-art office: Pixel Agents (it has a standalone browser mode), Claude Office Visualizer, Pixel Agent Desk, Agents in the Office, and search for others. Look at them for real and note what works.
2. **Reuse if it's good.** If one is a solid, licensed base (several are MIT) and can run as a web app, fork or extend it rather than starting from zero. The result **must be a web app** that a phone can open.
3. **Add the missing layer.** These tools show technical activity (files read, commands run). None shows business data. Add it from `memory/`.
4. **Logging.** Python hooks (SubagentStart, SubagentStop, PreToolUse, PostToolUse; check the docs for the current list and fields) append one line per event to `activity.jsonl`. Where hooks fall short, read the session transcripts in `~/.claude/projects`, as Pixel Agents does.
5. **Phone access** through `tailscale serve` on localhost only. Never Tailscale Funnel, never a public port. Mobile layout as good as desktop.
6. **Quality loop** as `CLAUDE.md` requires: benchmark grid, 2 to 4 correction passes, critic scores ≥4/5 on every criterion.

## Phase 4 — Start the business (in parallel from the start)

- Initial wide search: at least 30 leads, 8 categories, 5 kinds of sources, all evidenced and scored in `pipeline.json`.
- Hire the first agents you need, listed in `team.json`.
- Launch the first tests (max 3, at least one at €0), or have them ready as soon as Baptiste's approvals or tasks come back.

## Done when

Each item has pass/fail proof (log line, screenshot, file) in `memory/kickoff.md`:

- [ ] The guard hook blocked all 3 test commands.
- [ ] A scheduled run fired on its own, did its work and logged, with nobody touching the PC.
- [ ] A run that finds the lock held exits cleanly.
- [ ] After a real reboot, the scheduler, bot, dashboard and Tailscale came back on their own.
- [ ] The healthchecks.io heartbeat is green.
- [ ] A Telegram approval made the full round trip: sent → tapped → recorded → triggered a run → acted on.
- [ ] The dashboard shows live agent activity and business data, on PC and on Baptiste's phone.
- [ ] The daily backup push to GitHub works.
- [ ] `pipeline.json` holds 30+ scored leads with sources.
- [ ] The first tests are launched or ready, with kill dates.
- [ ] Baptiste's open tasks are in one batched list, with estimated times.

If an item is blocked on Baptiste, it goes into his tasks and you keep going on everything else.

## When the kickoff is complete

Send one short Telegram message in French: what works now, the dashboard link, and what's waiting on him. Then switch to normal business runs.
