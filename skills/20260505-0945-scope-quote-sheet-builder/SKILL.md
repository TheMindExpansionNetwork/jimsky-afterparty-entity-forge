---
name: 20260505-0945-scope-quote-sheet-builder
description: Draft a closed-gate scope/quote worksheet after an approved Afterparty Forge private demo.
version: 0.1.0
metadata:
  hermes:
    tags: [afterparty-forge, revenue-prep, scope, quote, closed-gate]
---

# Scope Quote Sheet Builder

## Trigger
Use after an awake-approved private demo or local post-demo outcome indicates interest, but before any quote, invoice, checkout link, follow-up, upload, GPU/training, or public claim is approved.

## Steps
1. Read `docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json` and confirm `wake_operator_scope_quote_sheet.status == draft_only_not_sent`.
2. Choose a draft tier from the existing `price_ladder`; do not create payment links or collect money.
3. Map each deliverable to existing proof paths such as the proof ledger, payload manifest, tool-suite manifest, relaunch draft, static site, or verifier.
4. Fill explicit exclusions: no checkout/payment URL, no unattended outreach/follow-up, no revenue/affiliation claim, no HF upload/private media movement, no GPU/training/model downloads, no cron mutation.
5. Require awake approval fields for buyer/receipt, scope summary, tier, manual invoice workflow path, follow-up message path, and expiration before use.

## Safety Gates
- `payment_links=false`, `outreach=false`, `claim_revenue=false`, and all upload/GPU/training/model-download gates remain closed.
- The worksheet is local draft copy only; it is not a sent quote and not a live offer.
- Do not print tokens, credential files, or private buyer data.

## Verification
Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py
git diff --check
```

## Example Run
After a private demo receipt is approved, draft the `$155` tier as a payload manifest + verifier handoff, attach `payloads/afterparty-forge/manifest.json`, `tools/entity-tool-suite.json`, and `scripts/verify_entity_pipeline.py` as proof paths, and stop until the awake operator approves the exact quote and message path.
