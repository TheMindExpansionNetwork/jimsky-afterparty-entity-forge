---
name: 20260505-1215-evidence-snapshot-notes-template
description: Draft-only operator notes template for Afterparty Forge evidence snapshots; keeps all delivery, payment, upload, GPU, and cron gates closed.
version: 0.1.0
metadata:
  hermes:
    tags: [afterparty-forge, evidence-snapshot, revenue-safety, closed-gates]
---

# Evidence Snapshot Notes Template Increment

## Trigger

Use when an awake operator has selected an Afterparty Forge next-action route and needs a local/private notes scaffold to summarize proof paths, verifier output, and closed gates before any external handoff.

## Safety Gates

- Do not send or schedule the notes.
- Do not create invoices, checkout links, payment links, wallets, or manual invoice workflows.
- Do not claim revenue, affiliation, HF upload, remote streaming, public release, GPU/training, model downloads, or public posting unless a separate awake-approved verification record exists.
- Do not print tokens or credential-store contents.
- Do not mutate cron jobs.

## Steps

1. Start from `docs/revenue/EVIDENCE_SNAPSHOT_OPERATOR_NOTES_TEMPLATE.md`.
2. Fill only local review fields: route id, proof paths checked, verifier command/result, git or Pages reference, closed gates confirmed, and one next human decision.
3. Cross-check proof paths against `docs/proof/AFTERPARTY_PROOF_LEDGER.json` and `docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json`.
4. Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py`.
5. Run `git diff --check` and a changed-file secret scan before committing any notes/template changes.

## Verification

The focused verifier asserts:

- the notes template exists;
- `wake_operator_evidence_snapshot_checklist` references it;
- the `evidence-snapshot-notes-template-builder` contract exists;
- all money/delivery/upload/GPU/training/public-post/cron gates remain closed.

## Example Run

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py
git diff --check
```

Result: local/private evidence snapshot notes can be drafted for awake review only; no external action is enabled.
