---
name: afterparty-manual-invoice-planning-checklist
version: 0.1.0
description: "Prepare a local-only manual invoice planning checklist after an awake-approved route; never create or send payment artifacts unattended."
metadata:
  afterparty_forge:
    entity: Afterparty Forge 2045
    status: draft_only_not_sent
    closed_until_human_yes: true
---

# Afterparty Manual Invoice Planning Checklist

## Trigger

Use only after an awake operator has selected `wake_operator_next_action_router.route_id == approve_manual_invoice_planning` and supplied an approved buyer/receipt, scope or quote sheet, selected draft tier, manual invoice workflow path, and approval expiration.

## Steps

1. Read `docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json`.
2. Confirm `wake_operator_manual_invoice_planning_checklist.status == draft_only_not_sent`.
3. Confirm the approved buyer explicitly asked to buy after seeing proof.
4. Attach only existing repo-local proof paths from:
   - `docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json`
   - `docs/proof/AFTERPARTY_PROOF_LEDGER.json`
   - `tools/entity-tool-suite.json`
   - `docs/tools/AFTERPARTY_FORGE_TOOL_SUITE.md`
5. Draft local planning fields only: receipt id, route id, buyer/org, scope quote sheet, tier, invoice workflow path, proof paths, exclusions, and expiration.
6. Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py` and `git diff --check` before any awake operator uses the checklist.

## Closed Gates

Unattended runs must not create checkout links, payment links, invoices, follow-up sends, public posts, HF uploads, private media movement, GPU/training jobs, model downloads, cron mutations, revenue claims, or affiliation claims.

## Pitfalls

- A planning checklist is not an invoice.
- A selected tier is not verified revenue.
- Do not copy tokens, `.env` contents, credential-store values, buyer private data, or payment details into the repo.
- Do not imply OpenAI/event/sponsor affiliation.

## Example Run

```text
Input: approved route approve_manual_invoice_planning, selected tier 155, scope quote sheet id local/demo-001.
Output: local-only checklist fields and proof path list for awake review.
External action: none.
Verification: scripts/verify_entity_pipeline.py + git diff --check pass.
```
