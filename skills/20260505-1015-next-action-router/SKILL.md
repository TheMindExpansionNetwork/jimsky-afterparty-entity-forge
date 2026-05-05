---
name: 20260505-1015-next-action-router
description: Draft-only wake-operator next action router for Afterparty Forge 2045 buyer-safe handoffs.
version: 0.1.0
---

# Wake Operator Next Action Router

## Trigger

Use after an approved private demo receipt, post-demo outcome, scope/quote worksheet, or dataset release question exists and the operator needs exactly one next step.

## Steps

1. Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py`.
2. Read `docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json` and locate `wake_operator_next_action_router`.
3. Choose exactly one `route_id`: `keep_building_repo_proof`, `approve_private_followup_draft`, `approve_manual_invoice_planning`, or `approve_private_hf_dataset_check`.
4. Fill the approval fields outside unattended mode before any external action.
5. If approval is absent or expired, do only repo-local proof, docs, manifests, or verifier work.

## Safety Gates

- No follow-up sending, checkout/payment links, manual invoice execution, revenue claims, affiliation claims, HF upload, token printing, GPU/training/model downloads, public posting, or cron mutation while unattended.
- HF checks stay local-only until an awake operator approves a private repo id and secure token environment.
- Manual invoice planning is not invoice creation and does not prove revenue.

## Verification

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py
git diff --check
```

## Example

If the receipt says the buyer needs more proof, choose `keep_building_repo_proof`, add a missing proof path or verifier assertion, and keep every external gate closed.
