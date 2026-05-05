---
name: 20260505-1102-manual-invoice-doc-verifier-catchup
description: Verify the manual-invoice planning checklist is discoverable in the tool-suite docs while all invoice/payment actions remain closed.
version: 0.1.0
metadata:
  tags: [afterparty-forge, verifier-catchup, revenue-safety, manual-invoice, closed-gates]
---

# Manual Invoice Planning Doc + Verifier Catch-up

## Trigger

Use after `wake_operator_manual_invoice_planning_checklist` and the `manual-invoice-planning-checklist-builder` contract exist in the revenue JSON/tool manifest, but the human-facing tool-suite Markdown needs an indexed tool entry and verifier coverage.

## Safe Steps

1. Read `docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json`, `tools/entity-tool-suite.json`, and `docs/tools/AFTERPARTY_FORGE_TOOL_SUITE.md`.
2. Confirm the next-action router includes `approve_manual_invoice_planning` and the manual-invoice checklist is `draft_only_not_sent`.
3. Add or maintain a `### 14. Manual Invoice Planning Checklist Builder` section in the tool-suite Markdown.
4. Patch `scripts/verify_entity_pipeline.py` to assert the Markdown section includes:
   - `approve_manual_invoice_planning`
   - `no invoice creation/sending`
   - the existing closed-gate sentence that external money actions stay closed.
5. Run verification from the repo root:
   - `PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py`
   - `git diff --check`
   - changed-file secret scan over modified/untracked text files.

## Safety Gates

- Do not create invoices, checkout links, payment links, or payment processor artifacts.
- Do not send or schedule follow-up messages.
- Do not claim revenue, affiliation, sponsorship, or buyer commitment.
- Do not upload to Hugging Face, move private media, start GPU/training jobs, download models, expose tokens, or mutate cron jobs.

## Pitfalls

- A manual-invoice checklist is not an invoice and must never be described as payment-ready.
- Markdown discoverability can lag behind JSON/tool contracts; verifier coverage should keep the tool list in sync.
- Keep this as a documentation/verifier catch-up increment, not a new external money workflow.

## Example Run

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py
git diff --check
```

Expected result: the verifier passes and confirms the manual-invoice planning checklist remains draft-only with all invoice/payment/follow-up/upload/GPU/training gates closed until awake human approval.
