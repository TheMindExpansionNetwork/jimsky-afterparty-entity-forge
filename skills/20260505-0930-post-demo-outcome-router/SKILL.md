---
name: post-demo-outcome-router
description: Draft-only receipt and next-action router for Afterparty Forge private demos; keeps follow-up, payment, upload, GPU/training, and public claims closed until awake approval.
version: 0.1.0
metadata:
  hermes:
    tags: [afterparty-forge, revenue-prep, private-demo, safety]
---

# Post-Demo Outcome Router

## Trigger

Use after an awake operator has already approved and delivered a private Afterparty Forge demo and needs a local, non-sending outcome receipt.

## Steps

1. Record only non-secret receipt fields: demo date, approved recipient/channel, proof paths shown, questions asked, requested next step, selected outcome, and approval expiration.
2. Choose exactly one outcome label from `post_demo_outcome_capture.allowed_outcome_labels`.
3. Route to the matching safe next step in `docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json`.
4. If the route mentions invoice, upload, follow-up, public copy, or training/GPU, stop until a fresh awake approval exists for exact scope/channel/environment.
5. Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py` and `git diff --check` before relying on the receipt/router.

## Safety Gates

- No unattended follow-up messages, DMs, emails, forms, checkout/payment links, revenue claims, affiliation claims, private uploads, public dataset release, GPU/training, model downloads, token printing, or cron mutation.
- Manual invoice remains an awake-operator workflow only after buyer identity, price tier, and scope are verified.
- Hugging Face checks remain local-only until a separate approved private upload uses secure environment tokens without printing them.

## Pitfalls

- Do not treat buyer interest as verified revenue.
- Do not convert `interested_manual_invoice_after_yes` into a checkout URL during unattended mode.
- Do not add raw private demo notes, secrets, or buyer personal data to git.

## Example

Outcome: `needs_more_proof_before_followup` -> add repo-local proof/verifier coverage, then ask the awake operator to approve any follow-up copy later.
