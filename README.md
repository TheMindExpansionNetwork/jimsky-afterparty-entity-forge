# Jimsky Afterparty Entity Forge

**Status:** private-first, forkable, synthetic-data-ready entity pipeline seeded after the first launch miss.

This repo turns the launch lesson into a repeatable system: build a better digital entity, package its payload, create logo-ready synthetic dataset assets, verify the pack, then upload/share only after human gates are open.

## What improved tonight

- Created a new full digital-entity payload: `payloads/afterparty-forge/`
- Added an entity identity, operating manual, safety boundaries, creator pipeline, and dataset pipeline docs.
- Generated **10 usable logo images** locally with exact readable text and matching captions.
- Added a Hugging Face `imagefolder`-compatible dataset export path and uploader.
- Added deterministic verification: JSON/JSONL parse, image open checks, caption checks, secret scan, and required docs.
- Added an overnight swarm plan so builders/reviewers can keep improving this without public posting/spend/training while Jimsky sleeps.

## Entity

**Name:** Afterparty Forge 2045

**Role:** a rave-safe digital launch engineer that turns failed launch energy into better demos, assets, docs, datasets, and payloads.

**Vibe:** PLUR command center, neon warehouse, honest metrics, no fake wins.

## Quickstart

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_site.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py
python3 scripts/build_hf_logo_dataset.py
python3 scripts/package_payload.py
```

## Safety

Closed until an awake human explicitly approves: public posting, outreach, spending, training, GPU jobs, model downloads, private media uploads, wallet/payment actions, and cron mutation.

Generated: 2026-05-05T05:24:58Z
