# Afterparty Forge 2045 — Launch Screen Checklist

**Status:** `launch_screen_checklist_manual_run_only_closed_until_human_yes`

This is an operator-executable screen-share run sheet for a private proof-room or recorded rehearsal. It does **not** start a livestream, create a Space, record audio/video, post to X, upload to YouTube, collect payment, or contact anyone. Manual run only.

## Exact human approval question

> Do you approve running this exact Afterparty Forge 2045 screen checklist manually on a private screen-share, with no recording, no public posting, no outreach, no livestream, no payment link, no private-media upload, and no GPU/training/model-download action?

If any part of the answer is unclear, keep the run closed.

## 0. Clean setup commands

Run from the repo root:

```bash
cd /opt/data/workspace/projects/jimsky-afterparty-entity-forge
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_site.py
git diff --check
git status --short --branch
```

Expected highlights:

- `VERIFY OK site relaunch surfaces closed-gate links/json/entity`
- no `git diff --check` output
- only intentional local changes before commit; clean tree after commit

## 1. Tab and secret hygiene

Before sharing the screen:

1. Close `.env`, credential managers, token dashboards, private DMs, billing pages, and cloud consoles.
2. Open only repo-local proof surfaces and terminal verifier output.
3. Keep browser address bars visible enough to show local/repo paths, but never show secret-bearing URLs.
4. Do not open Hugging Face/GitHub settings, X/X Developer, YouTube Studio, payment dashboards, or livestream dashboards.

## 2. 60-second proof-hub click path

Open these paths locally or in the repo viewer:

1. `site/index.html` — show the logo contact sheet and proof cards.
2. `docs/launch/RELAUNCH_PACKAGE_DRAFT.md` — show the human approval gates.
3. `docs/social/X_THREAD_DRAFTS.md` — show manual-post-only thread variants.
4. `docs/youtube/CAPTIONS_TRANSCRIPTS_PACK.md` — show captions/transcript and manual-upload-only status.
5. `docs/tools/AFTERPARTY_FORGE_TOOL_SUITE.md` — show closed tool contracts.
6. `docs/launch/SCREEN_CHECKLIST.md` — show this screen checklist and approval question.

## 3. Terminal proof commands

Paste exactly:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_site.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py
python3 - <<'PY'
import json
from pathlib import Path
for rel in [
    'site/data/launch-screen-checklist.json',
    'site/data/x-thread-drafts.json',
    'site/data/youtube-captions-pack.json',
]:
    data = json.loads(Path(rel).read_text())
    print(rel, data.get('status'), data.get('requires_human_approval'))
PY
git diff --check
```

Expected highlights:

- `VERIFY OK site relaunch surfaces closed-gate links/json/entity`
- `VERIFY OK afterparty entity pipeline images=10`
- every printed manifest line ends with `True`
- no whitespace errors

## 4. 30-second narration script

```text
Afterparty Forge 2045 is a rebound system for turning a launch miss into a verified digital-entity payload, proof site, logo seed dataset, manual social copy, and manual-upload captions pack. The proof is local and closed-gate: no public post, no livestream, no upload, no outreach, no payment link, no spend, no training, and no GPU/model download runs without an awake human saying yes to one exact action.
```

## 5. Failure recovery

- If `verify_site.py` fails, stop the demo and fix the named missing path/string/flag before claiming progress.
- If a proof path is missing, do not substitute an external dashboard; add or repair the repo-local proof first.
- If a private tab/token appears, stop screen share immediately and rotate/revoke the exposed credential outside this unattended flow.
- If a browser preview looks stale, refresh from the committed repo path and rerun the verifier.

## 6. Post-demo cleanup

```bash
git status --short --branch
```

Then close preview windows, clear terminal scrollback if any private path accidentally appeared, and keep all external actions closed until a new written approval targets exactly one action.

## Blocked without approval

- public posting or scheduled posts
- X/Twitter Spaces, livestreams, RTMP, OBS publish, or YouTube upload
- recording audio/video of private media
- direct outreach, DMs, email campaigns, forms, or lead scraping
- checkout/payment links, invoices, wallets, crypto, domains, paid ads, subscriptions, or spend
- GPU jobs, paid APIs, training, model downloads, dataset upload, or private-media upload
- cron creation, deletion, or mutation
- revenue, customer, sponsorship, OpenAI affiliation, attendance, or external-result claims

## Closed safety flags

`manual_run_required: true`
`auto_stream_enabled: false`
`requires_human_approval: true`
`public_posting: false`
`x_space_creation: false`
`livestream_creation: false`
`youtube_upload: false`
`caption_upload: false`
`payment_links: false`
`outreach: false`
`spend: false`
`claim_revenue: false`
`claim_affiliation: false`
`records_audio: false`
`uploads_private_media: false`
`starts_gpu: false`
`starts_paid_api: false`
`downloads_models: false`
`starts_training: false`
`submits_hackathon: false`
`mutates_cron: false`
