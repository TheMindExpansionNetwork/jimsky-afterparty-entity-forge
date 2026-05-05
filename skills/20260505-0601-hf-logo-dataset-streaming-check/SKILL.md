---
name: 20260505-0601-hf-logo-dataset-streaming-check
description: "Safely verify the Afterparty Forge logo-seed Hugging Face imagefolder dataset without uploading, training, GPU, or public release."
version: 0.1.0
metadata:
  hermes:
    tags: [afterparty-forge, huggingface, dataset, imagefolder, streaming-check, closed-gate]
---

# HF Logo Dataset Streaming Check

## Trigger

Use this skill when an awake operator or future closed-gate builder needs to prove the `datasets/logo-seed/` export is ready for a private Hugging Face `imagefolder` dataset, or to verify an already-approved private upload streams correctly.

## Safety Gates

- Do **not** upload anything unless the operator has explicitly approved the exact repo ID and private/public setting.
- Default repo privacy remains `private`.
- Do **not** print `HF_TOKEN`, `HUGGINGFACE_HUB_TOKEN`, `.env`, credential-store values, cookies, or OAuth files.
- Do **not** start training, GPU jobs, model downloads, public posting, outreach, payments, or cron mutation.
- Treat this as a verification-only lane unless the current prompt explicitly authorizes upload.

## Local Verification Steps

1. From the repo root, run the project verifier:

   ```bash
   PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py
   ```

2. Confirm the logo manifest and loader rows parse:

   ```bash
   python3 - <<'PY'
   import json
   from pathlib import Path
   root = Path('datasets/logo-seed')
   manifest = json.loads((root / 'dataset_manifest.json').read_text())
   rows = [json.loads(line) for line in (root / 'metadata.jsonl').read_text().splitlines() if line.strip()]
   assert manifest['count'] == len(rows) == 10
   for row in rows:
       assert (root / row['file_name']).exists(), row['file_name']
       assert row.get('text') and 'Afterparty Forge 2045' in row['text']
   print('local_logo_seed_rows_ok', len(rows))
   PY
   ```

3. If the optional `datasets` package is available, run a local streaming smoke check without network or upload:

   ```bash
   python3 - <<'PY'
   from datasets import load_dataset
   ds = load_dataset('imagefolder', data_dir='datasets/logo-seed', split='train', streaming=True)
   first = next(iter(ds))
   assert first.get('image') is not None
   assert first.get('text') and 'Afterparty Forge 2045' in first['text']
   print('local_imagefolder_streaming_ok', sorted(first.keys()))
   PY
   ```

   If `datasets` is not installed, record `optional_datasets_package_missing` rather than installing new packages during an unattended run.

## Approved Private Upload Verification

Only after a human has approved the upload and repo ID:

1. Authenticate from the environment without printing secrets:

   ```bash
   python3 - <<'PY'
   import os
   from huggingface_hub import HfApi
   token = os.environ.get('HF_TOKEN') or os.environ.get('HUGGINGFACE_HUB_TOKEN')
   if not token:
       raise SystemExit('missing_hf_token')
   who = HfApi(token=token).whoami(token=token)
   print('hf_auth_ok', who.get('name') or 'authenticated')
   PY
   ```

2. Upload with `scripts/upload_hf_dataset.py` only if that script still defaults to private and the target repo matches the approved repo.
3. Verify the remote dataset info includes `private=True`, a README, `dataset_manifest.json`, `metadata.jsonl`, and all 10 image paths.
4. Run a remote streaming check with the explicit token and record only non-secret status, file counts, commit SHA, and private flag.

## Pitfalls

- Hugging Face may auto-detect mixed JSONL schemas incorrectly; keep this logo-seed export simple: `metadata.jsonl` rows should expose `file_name` plus `text` for imagefolder loading, while `metadata.full.jsonl` remains provenance-only.
- Contact-sheet labels are review aids; the individual training images and captions are the dataset source of truth.
- Do not convert a successful private dataset verification into a training run. Training is a separate awake-human approval gate.

## Verification Before Commit

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py
git diff --check
```

Then secret-scan the changed and untracked text files before committing.

## Example Run

```text
local_logo_seed_rows_ok 10
local_imagefolder_streaming_ok ['image', 'text']
VERIFY OK afterparty entity pipeline images=10
```
