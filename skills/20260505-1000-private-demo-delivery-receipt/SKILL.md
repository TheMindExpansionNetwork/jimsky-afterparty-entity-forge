---
name: 20260505-1000-private-demo-delivery-receipt
description: "Use Afterparty Forge 2045's prep-only private demo delivery receipt kit after an awake-approved private demo."
version: 0.1.0
metadata:
  hermes:
    tags: [afterparty-forge, revenue-prep, private-demo, receipts, closed-gates]
---

# Private Demo Delivery Receipt Kit

## Trigger

Use this only after an awake operator has already approved a private demo recipient, channel, and proof scope for Afterparty Forge 2045.

## Safety gates

- This skill records a **local/manual receipt only**.
- Do not send follow-up messages, create checkout/payment links, start a manual invoice workflow, claim revenue, claim affiliation, upload/publish datasets, move private media, start GPU/training/model-download jobs, or mutate cron jobs.
- Treat every next external action as closed until a separate awake approval names the recipient, channel, copy path, price tier if any, and expiration.

## Steps

1. Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py` from the repo root before relying on the receipt template.
2. Open `docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json` and use `buyer_facing_offer_draft.private_demo_delivery_receipt_kit` as the source of truth.
3. Record the receipt fields locally: demo date, approved recipient/channel, operator handle, proof paths shown, questions answered, buyer requested next step, selected outcome label, and follow-up approval expiration.
4. Confirm every proof path shown exists in the repo and matches a green/yellow proof-ledger claim.
5. Require the operator attestations: approved delivery, repo-local proof only, no checkout/follow-up/upload/GPU/training/public claim, and verifier passed.
6. Route the result into `post_demo_outcome_capture` only as a decision aid; do not execute the follow-up.

## Verification

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py
git diff --check
```

## Example safe receipt status

```text
status: local_manual_record_only_no_external_delivery
outcome_label: private_demo_complete_no_followup_yet
next_router: post_demo_outcome_capture
closed_gates: follow-up/payment/invoice/upload/GPU/training/cron all still closed
```
