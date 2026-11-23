# Claude Code pack for logistics — waitlist / preorder

*(The Stock Report assistant is already finished and free on signup, see below. The rest of the pack is in presale, decision on December 20, 2026.)*

## Claude Code for logistics: a stock report readable in a few minutes, not a manual re-typing job

You run a warehouse, a transport flow, or inventory, and a good chunk of your week goes into repetitive tasks: reading an Excel/CSV export to pull out a summary, writing the same carrier follow-up email for the tenth time, copying a delivery delay into a customer email, cross-checking two files to track down a missing SKU.

I'm building a pack of assistants ("skills") for **Claude Code**, Anthropic's command-line AI tool, built specifically for these logistics tasks — not for developers. The idea: you give it a file, or an instruction in French, and the assistant does the formatting and writing — you keep the decision.

I worked in logistics before I coded: this pack starts from problems I've seen from the inside, not a generic list of prompts.

## Who it's for

Warehouse managers and inventory leads who process an Excel/CSV export (WMS, inventory, stockouts) every day, and who are comfortable installing a tool by following a step-by-step guide even without knowing how to code. (Transport and reporting roles are also targeted — see "And also" below.)

## Who it's not for

- You're looking for a full WMS or ERP: this pack doesn't replace your core software, it works alongside it (exports, emails, summaries).
- You want the full pack delivered today: it doesn't exist yet, see below (only the Stock Report assistant, free on signup, is already finished).
- You've never opened Claude Code and don't want to install a command-line tool (even a simple one): this pack isn't for you yet in this first version.
- You need an English-only tool: the Stock Report assistant's output, error messages and expected column headers are currently in French (see below for a real sample).

## Why not a free pack?

There are already free, massive skill packs for Claude Code (for example mattpocock/skills or the official anthropics/skills pack, several hundred thousand installs combined between the two). They cover generic dev work very well: code review, tests, debugging, project structure. What they don't have: anything specific to logistics, no transport/inventory vocabulary (stockout, overstock, carrier dispute, service rate), no ready-to-use use case for this sector. Copying a free generic prompt won't save you the time this pack aims to save on your exports and follow-up emails — that's the real difference between paying €19 and digging through free resources. Unverified estimate, to be confirmed with the first signups: aiming to cut a stock report that today takes 20-30 minutes of manual copying down to a few minutes.

## Target use cases (concrete examples, not a fixed feature list)

The exact content isn't locked in, it will be built with the first signups — as a guide, between 4 and 6 assistants are targeted for this first version, no more, to keep it properly testable. The most universal use case, targeted first:

**Stock Report**: from an Excel/CSV export of your WMS, produce a readable summary (stockouts, overstocks, SKUs to watch) without rebuilding a pivot table by hand.

This assistant already exists for real (it's the only one in the pack at this stage): here is its actual output on a sample export of 100 SKUs that I built to test it (not a real customer's export — none has been provided yet):
> 8 réf. en rupture (REF-1064, REF-1065, REF-1067…) · 8 surstocks à écouler (REF-1092, REF-1091…) · 6 écart(s) d'inventaire à vérifier (REF-1097, REF-1095…)

(Real output, shown exactly as generated — the assistant's reports are in French today.)

The full report (stockouts, below minimum threshold, to watch, dormant overstocks, inventory discrepancies) is one page long; this line is just the summary.

**And also**, in the same vein:
- **Carrier follow-up**: a clear, factual follow-up email built from a parcel number and a delay reason.
- **Delivery delay analysis**: a structured explanation built from a planned date and an actual date, usable for a customer or your management.
- **Reporting summary**: a delivery or stock export turned into a few actionable lines for a meeting.

These examples guide the upcoming work; they are not a guaranteed item-by-item delivery list.

## How it will work, once delivered

1. You receive a ZIP file + a step-by-step installation guide.
2. You install it in Claude Code by following at most 4 steps (copying files, running one command, checking it works).
3. You open one of your real files (export, email) and test a use case.
4. You keep direct contact with me (email) to report a bug or request an adjustment: reply within 48 business hours, free updates included for 6 months after delivery.

Tested before delivery on Windows and macOS, on the version of Claude Code current at the time of delivery (not a version frozen today that would be outdated by launch), with a guide verified step by step — not a blind copy-paste. Each assistant will pass the standard SKILL.md format (checked, no hardcoded paths) before delivery. License: personal or professional use within your organization, no redistribution of the pack. Each update during the 6 included months comes with a dated changelog (what changed).

## This is a presale, not a regular purchase

Be clear with yourself before committing:

- **The pack doesn't exist yet.** This page exists to check whether enough people are interested before I spend time building it.
- **Decision deadline: December 20, 2026.** If too few people have signed up or preordered by that date, I won't build the pack, I'll tell you, and I'll fully refund any preorder, with no waiting period.
- **If the threshold is reached**, I commit to delivering the pack within 4 weeks of December 20, 2026.
- **14-day money-back guarantee** after delivery if the pack doesn't match what's described here, no questions asked.
- **No review, no sales count, and no spots-remaining counter on this page is made up.** At this stage, there isn't one: this is the first version of this offer.

## Two ways to show you're interested

- **Free waitlist**: leave your email, you immediately receive the **Stock Report** assistant described above — it's already finished, not a promise — and you're notified as soon as the decision on the rest of the pack is made (build or drop), no commitment.
- **Launch-price preorder**: €19 instead of the €29 planned regular price once the pack ships. You only pay if you choose to preorder now; full automatic refund if the project doesn't happen. The Stock Report assistant is included immediately, same as the waitlist.

[Join the waitlist] — [Preorder for €19]

## FAQ

**Does the pack already exist, can I get it right now?**
No, the full pack is in presale: it isn't delivered today. Only the Stock Report assistant is finished and is sent to you immediately on signup. If you need the full pack right away, wait for the December 20 decision, or don't preorder.

**What happens if the project is dropped?**
You're refunded in full, automatically, with no action needed on your part if you preordered. If you only joined the waitlist, you're simply informed.

**Is this pack affiliated with or endorsed by Anthropic?**
No. This pack is not an official Anthropic product. Claude Code and Claude are Anthropic tools; this pack is a set of third-party assistants built to use them, sold independently.

**Do I need to know how to code to use it?**
No, but you need to know how to install a tool by following a step-by-step guide (copying files, running a command). If the idea of opening a command line is a total blocker for you, this pack isn't for you yet.

**Will the final content be exactly what's described above?**
The use cases listed are the ones targeted first, built from real logistics problems. The exact number of assistants and their final form will be confirmed to signups before delivery, not improvised afterward.

## Summary

Claude Code assistant pack for logistics (inventory, transport, reporting), in development, delivered within 4 weeks if enough people sign up before December 20, 2026, full refund otherwise. Not affiliated with Anthropic. Two risk-free options: free waitlist or refundable €19 preorder.
