# Private Demo Buyer-Safe Script — Afterparty Forge 2045

`status: private_demo_buyer_script_draft_only_closed_until_human_yes`

This is a copy/paste-ready private-demo script for an awake operator. It is **not** outreach, not a public post, not a payment request, and not a claim that revenue/customers/affiliation already exist.

## Exact human approval question

Do you approve running this exact private Afterparty Forge 2045 buyer demo manually with one named recipient, with no recording, no public posting, no outreach automation, no payment link, no invoice, no upload, no GPU/training, and no claim of OpenAI affiliation or verified revenue?

If the answer is not an explicit yes for a named recipient and time, keep the action closed.

## 60-second proof-pack walkthrough

1. **Open the proof hub** — show `site/index.html` or `docs/index.html` and say: “This page is the local proof surface; nothing here posts, invoices, uploads, or streams automatically.”
2. **Show the closed-gate lanes** — click the Entity Tool Suite and First-Dollar Revenue Path links; point out that money actions remain closed until human approval.
3. **Show the launch-safe assets** — open the X thread drafts, captions pack, and launch screen checklist cards; say they are manual-review artifacts only.
4. **Run the verifier** — in terminal run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_site.py`; expected highlight: `VERIFY OK site relaunch surfaces closed-gate links/json/entity`.
5. **State the offer boundary** — “If this is useful, the next step is a scoped private demo or quote worksheet after you approve scope; I am not sending invoices or checkout links in this unattended pipeline.”

## 90-second demo beats

- **0:00–0:15 — Frame the problem.** “Afterparty Forge 2045 turns a failed or messy launch into a controlled proof room: assets, scripts, verifier checks, and closed gates.”
- **0:15–0:35 — Show visible proof.** Open the logo contact sheet, manual X drafts, captions/transcript pack, and launch screen checklist cards.
- **0:35–0:55 — Show safety discipline.** Open `site/data/launch-screen-checklist.json` or this script manifest and show risky flags are false.
- **0:55–1:15 — Show verification.** Run the verifier command and read the success marker only if it passes.
- **1:15–1:30 — Ask one bounded question.** “Which one lane should we polish next for your real launch: screen-share proof, private buyer script, captions pack, or offer copy?”

## Do-not-say lines

- Do not say “we made revenue” unless a real payment is verified by the awake operator.
- Do not say “we are affiliated with OpenAI,” “official launch partner,” or “inside access.”
- Do not promise public posting, X Space scheduling, YouTube upload, outreach, invoice creation, payment links, GPU work, model training, or private-media upload during the demo.
- Do not imply the buyer’s private data will be uploaded, recorded, trained on, or shared.
- Do not quote a final price as binding; use the scope/quote worksheet after human approval.

## Objection responses

- **“Is this live?”** — “The repo proof and verifier are real; public launch actions remain closed until a human approves exact copy/media/recipient.”
- **“Can you post this for us?”** — “Not from the unattended lane. I can prepare draft copy and a checklist; an awake operator must approve and perform posting.”
- **“Can you take payment now?”** — “No checkout or invoice is created here. If you want to buy, the operator can prepare a manual invoice plan after explicit approval.”
- **“Can you train a custom model?”** — “This pack can prepare local datasets and safety checks, but upload/training/GPU starts remain closed until a separate human yes.”
- **“Can you use our private footage?”** — “Only after a human confirms rights, storage location, redaction, and upload/recording gates.”

## Terminal proof commands

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_site.py
git diff --check
git status --short --branch
python3 -m json.tool site/data/private-demo-buyer-script.json >/tmp/private-demo-buyer-script.json
```

Expected highlights:

- `VERIFY OK site relaunch surfaces closed-gate links/json/entity`
- `git diff --check` prints no whitespace errors
- JSON parses without error
- Any remaining uncommitted files should be the current intentional increment only

## Proof paths

- `site/index.html`
- `docs/index.html`
- `docs/revenue/PRIVATE_DEMO_BUYER_SAFE_SCRIPT.md`
- `site/data/private-demo-buyer-script.json`
- `docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json`
- `docs/tools/AFTERPARTY_FORGE_TOOL_SUITE.md`
- `tools/entity-tool-suite.json`
- `docs/social/X_THREAD_DRAFTS.md`
- `docs/youtube/CAPTIONS_TRANSCRIPTS_PACK.md`
- `docs/launch/SCREEN_CHECKLIST.md`
- `scripts/verify_site.py`

## Failure recovery

- If `verify_site.py` fails, stop the demo and show the failing file/needle without editing live in front of the buyer.
- If a link is missing, keep public/commercial actions closed and fix the repo locally before resuming.
- If the buyer asks for payment, invoice, posting, upload, or recording, capture it as a follow-up decision for an awake operator; do not perform it inside the unattended pipeline.
- If the buyer asks for private data/media, pause until rights, storage, redaction, and upload/recording gates are explicitly approved.

## Post-demo cleanup

- Close any local preview browser tabs that show private paths.
- Do not retain buyer notes in public docs; use a private approved CRM or local note only after consent.
- Run `git status --short --branch` and verify no accidental generated artifacts or secrets were created.
- Keep all external actions closed unless the operator separately approves one exact next action.

## Blocked without approval

- Sending or scheduling this script to any recipient.
- Creating outreach, DMs, emails, public posts, X Spaces, livestreams, or YouTube uploads.
- Recording audio/video or uploading private media.
- Creating payment links, invoices, checkout sessions, or claiming revenue.
- Claiming OpenAI affiliation, customer results, attendance, sponsorship, or verified launch outcomes.
- Starting GPU jobs, paid APIs, model downloads, training, or dataset uploads.
- Mutating cron jobs or unattended launch automation.
