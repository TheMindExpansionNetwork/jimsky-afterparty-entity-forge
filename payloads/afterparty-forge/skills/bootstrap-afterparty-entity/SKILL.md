---
name: bootstrap-afterparty-entity
description: Bootstrap or customize an Afterparty Forge digital entity payload safely.
version: 0.1.0
---

# Bootstrap Afterparty Entity

Use when creating a clone of Afterparty Forge 2045.

1. Read `manifest.json`, `.env.example`, and `docs/SAFETY_BOUNDARIES.md`.
2. Ask only non-secret creator questions: name, role, vibe, allowed demos, visual palette.
3. Generate local identity docs and dataset captions.
4. Run `scripts/verify_entity_pipeline.py`.
5. Keep public posting, training, GPU, spend, wallets, and private uploads closed until human approval.
