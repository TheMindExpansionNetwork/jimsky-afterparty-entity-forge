# Afterparty Forge 2045 — Human-Gated Relaunch Package Draft

**Status:** draft-only, private-first, and not approved for public posting.
**Use when:** an awake operator wants a copy-paste relaunch plan after verifying the repo, payload, site, and optional private Hugging Face dataset.

## 0. Closed Gates Before Anything Public

Do **not** run any public launch action until an awake human explicitly confirms each gate below in writing:

- Public posting / social announcements: **closed**
- Direct outreach / DMs / email campaigns: **closed**
- Spend, subscriptions, domains, paid ads, or paid APIs: **closed**
- Training, GPU jobs, model downloads, or workflow execution: **closed**
- Private media upload beyond already-approved HF dataset verification/update: **closed**
- Wallets, payments, token actions, or marketplace listings: **closed**
- Cron creation, deletion, or mutation: **closed**

## 1. Local Proof Checklist

Run these from the repo root and paste the outputs into the operator notes before relaunch:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py
git diff --check
git status --short --untracked-files=all
```

Expected proof points:

- `VERIFY OK afterparty entity pipeline images=10`
- no whitespace errors from `git diff --check`
- clean working tree after any committed relaunch edits
- 10 logo seed images and matching captions remain present
- payload manifest still lists all closed gates

## 2. Private Demo Script

Copy/paste for a private, human-reviewed demo room only:

```text
Afterparty Forge 2045 is the rebound kit from the launch miss: a forkable digital-entity payload, logo seed dataset, static proof site, and verification pipeline.

What you can review now:
1. The entity identity and operating manual.
2. The local logo seed gallery with 10 generated marks and captions.
3. The payload pack that explains how a creator can clone their own agent without exposing secrets.
4. The verifier that checks required files, JSON/JSONL, image openings, captions, and secret-like patterns.

What is intentionally not live yet:
- no public post
- no outreach
- no spend
- no training
- no GPU/model downloads
- no live workflow execution
- no private media upload unless separately approved
```

## 3. Human Approval Prompt

Before any external relaunch, ask the operator to fill this out locally:

```text
I approve the following specific action and no broader action:
[ ] Publish static site link
[ ] Upload/update private HF dataset only
[ ] Convert private demo script into a public post
[ ] Send direct outreach to named people only
[ ] Start a training/GPU/model-download task

Approved scope:
Expiration time:
Budget limit:
Accounts/providers allowed:
Rollback/stop condition:
```

If any field is blank, keep the action closed.

## 4. Optional Hugging Face Dataset Verification Notes

If the private dataset already exists or is explicitly approved for update, verify without printing tokens:

```bash
python3 - <<'PY'
from huggingface_hub import HfApi
import os
repo_id = 'TheMindExpansionNetwork/jimsky-afterparty-logo-seed'
token = os.environ.get('HF_TOKEN') or os.environ.get('HUGGINGFACE_HUB_TOKEN')
if not token:
    raise SystemExit('HF token unavailable in environment; skip remote verification')
api = HfApi(token=token)
info = api.dataset_info(repo_id, token=token, files_metadata=True)
files = [s.rfilename for s in info.siblings or []]
print({'repo_id': repo_id, 'private': getattr(info, 'private', None), 'file_count': len(files), 'has_readme': 'README.md' in files})
PY
```

Remote upload or update remains human-approved only.

## 5. Relaunch Copy Blocks

### Short private status update

```text
Built a cleaner Afterparty Forge 2045 proof pack: a verified digital-entity payload, 10 logo seed images, a static gallery, and a private-first HF dataset path. It is still closed-gate: no public posting, outreach, spend, training, GPU work, or model downloads without explicit approval.
```

### Longer public-ready draft, not approved yet

```text
Afterparty Forge 2045 turns a failed launch signal into a repeatable digital-entity forge: payload docs, safety boundaries, logo seed data, and deterministic verification. The first version is intentionally private-first: review the proof, then decide which gates to open.
```

## 6. Next Safe Increment After This Draft

Add a focused verifier for this relaunch package that checks the closed-gate language, proof commands, and approval prompt remain present before any future packaging or launch-review run.
