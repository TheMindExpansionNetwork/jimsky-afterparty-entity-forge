# Hugging Face Dataset Usage Notes — Afterparty Forge 2045

**Status:** private-first usage guide. This document does not authorize uploads, training, GPU jobs, public posting, or live provider execution.

## Dataset lane

The logo seed dataset is designed as a small Hugging Face `imagefolder` export:

- Local source: `datasets/logo-seed/`
- Manifest: `datasets/logo-seed/dataset_manifest.json`
- Loader metadata: `datasets/logo-seed/metadata.jsonl`
- Provenance metadata: `datasets/logo-seed/metadata.full.jsonl`
- Approved default repo ID: `TheMindExpansionNetwork/jimsky-afterparty-logo-seed`
- Privacy default: `private`

## Local verification before any upload

Run these commands from the repo root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py
python3 -m json.tool datasets/logo-seed/dataset_manifest.json >/dev/null
git diff --check
```

Expected verifier signal:

```text
VERIFY OK afterparty entity pipeline images=10
```

## Optional private Hub streaming check

Only run this after an awake operator has supplied Hugging Face auth through the secure environment and approved a private upload or verification refresh. Do not paste tokens into chat, docs, commits, or shell history.

```bash
python3 - <<'PY'
import os
from datasets import load_dataset

repo_id = "TheMindExpansionNetwork/jimsky-afterparty-logo-seed"
token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_HUB_TOKEN")
if not token:
    raise SystemExit("HF token missing from secure environment; skipping Hub streaming check")

ds = load_dataset(repo_id, split="train", streaming=True, token=token)
row = next(iter(ds))
print("remote_streaming_ok", sorted(row.keys()))
print("first_text", row.get("text", "")[:120])
PY
```

The expected row keys should include at least `image` and `text`. If Hub auto-discovery fails, keep the repo private and add explicit dataset card configs before using the data for any training lane.

## Trainer handoff notes

- Treat this as a seed/reference asset pack, not a completed model dataset.
- Use `metadata.jsonl` for loader-friendly image/caption rows.
- Use `metadata.full.jsonl` for provenance, hashes, dimensions, and review audit trails.
- Do not train overnight from this repo without explicit awake-human approval.
- Do not upload private media, model weights, provider logs, `.env`, OAuth files, or cache directories.

## Closed gates still closed

- `ALLOW_TRAINING=0`
- `ALLOW_GPU=0`
- `ALLOW_MODEL_DOWNLOADS=0`
- `ALLOW_PUBLIC_POSTING=0`
- `ALLOW_PRIVATE_UPLOAD=0` unless the awake operator explicitly approves the exact private HF dataset operation.
- `ALLOW_CRON_MUTATION=0`
