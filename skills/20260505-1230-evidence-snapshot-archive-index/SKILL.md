---
name: 20260505-1230-evidence-snapshot-archive-index
description: Prep-only local evidence snapshot archive index builder for Afterparty Forge 2045.
version: 0.1.0
---

# Evidence Snapshot Archive Index Builder

## Trigger
Use when an awake operator has an approved evidence snapshot and local operator notes, and needs a repo-local index entry before deciding whether any private note, buyer proof packet, dataset handoff, or public copy is allowed.

## Safety gates
- Draft-only and local/private by default.
- Do not send or schedule archive entries.
- Do not create checkout/payment links, invoices, follow-ups, public posts, HF uploads, GPU/training jobs, model downloads, wallets, or cron mutations.
- Do not claim revenue, sponsorship, OpenAI/event affiliation, HF upload/streaming, or training unless separately verified while awake.

## Steps
1. Confirm `wake_operator_evidence_snapshot_checklist.status == draft_only_not_sent`.
2. Confirm notes are based on `docs/revenue/EVIDENCE_SNAPSHOT_OPERATOR_NOTES_TEMPLATE.md`.
3. Record only local archive fields: snapshot id, route id, notes path, proof paths checked, verifier command/result, git or Pages reference, closed gates, and expiration.
4. Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py`.
5. Run `git diff --check` and changed-file secret scan before any commit or handoff.

## Pitfalls
- An archive entry is not buyer copy and is not an invoice attachment.
- Do not use the archive to imply a payment, upload, public release, or revenue event happened.
- Keep HF token checks in a secure environment only; never print tokens.

## Example
An operator may add a local archive row after a private demo receipt, but every external use still requires a fresh awake approval and verifier pass.
