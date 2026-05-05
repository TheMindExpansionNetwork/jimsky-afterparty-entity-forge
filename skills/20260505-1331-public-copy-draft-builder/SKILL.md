---
name: public-copy-draft-builder
description: Prep-only public copy draft lane for Afterparty Forge evidence snapshot reuse decisions.
version: 0.1.0
metadata:
  hermes:
    tags: [afterparty-forge, revenue-prep, public-copy, closed-gates]
---

# Public Copy Draft Builder

## Trigger

Use when an awake operator has a local evidence snapshot archive entry and chooses the `prepare_public_copy_draft_after_approval` route from the evidence snapshot reuse decision matrix.

## Steps

1. Confirm the archive entry and snapshot IDs are awake-approved and local/private.
2. Recheck every proof path in `docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json` under `wake_operator_public_copy_draft.required_proof_paths`.
3. Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py` and `git diff --check`.
4. Draft only local copy fields: proof-backed safe copy, forbidden copy, verifier result, page/channel context, and expiration.
5. Require separate awake approval before any copy is posted, scheduled, boosted, sent, or used outside the repo.

## Safety Gates

Keep these closed until separate human approval: public posting, scheduling, paid promotion/spend, outreach/DMs, checkout/payment links, invoice creation/sending, HF upload/public dataset release, token printing, GPU/training/model downloads, revenue claims, affiliation claims, and cron mutation.

## Pitfalls

- Do not promote yellow HF/revenue/affiliation/external-delivery claims to public copy.
- Do not treat local public-copy drafts as already published or buyer-approved.
- Do not include tokens, payment URLs, live invoice instructions, or claims of verified revenue.

## Verification

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py
git diff --check
```

## Example Run

An operator selects `prepare_public_copy_draft_after_approval`; the builder fills local copy fields, cites `docs/proof/AFTERPARTY_PROOF_LEDGER.json`, records the verifier command, and leaves all external posting and money gates closed.
