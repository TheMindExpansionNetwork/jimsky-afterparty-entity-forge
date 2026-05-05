---
name: evidence-snapshot-reuse-decision-matrix
description: Draft-only local matrix for deciding how an evidence snapshot archive entry may be reused without external action.
version: 0.1.0
---

# Evidence Snapshot Reuse Decision Matrix

## Trigger

Use when an awake operator has a local evidence snapshot archive entry and needs to decide whether it can become a private note, buyer proof packet draft, dataset handoff draft, or public-copy draft.

## Steps

1. Confirm `wake_operator_evidence_snapshot_archive_index.status == draft_only_local_index_not_sent`.
2. Pick exactly one `wake_operator_evidence_snapshot_reuse_decision_matrix.reuse_route_options[].route_id`.
3. Recheck every proof path named by the archive entry against the current repo state.
4. Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py` and `git diff --check`.
5. Keep the output local/private unless an awake operator separately approves recipient, channel, copy path, and expiration.

## Safety gates

No sending, scheduling, checkout/payment links, invoice creation/sending, HF upload, token printing, public posting, outreach automation, revenue/affiliation claims, GPU/training/model downloads, spend, wallet actions, or cron mutation.

## Verification

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py
git diff --check
```

## Example

Route an approved archive entry to `reuse_as_private_operator_note`; record verifier output and keep the note local/private until a separate human yes.
