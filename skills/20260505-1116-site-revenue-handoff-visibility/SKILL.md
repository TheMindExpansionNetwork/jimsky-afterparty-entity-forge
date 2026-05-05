---
name: afterparty-site-revenue-handoff-visibility
description: Surface prep-only revenue handoff lanes on the static site without enabling sending, invoices, payments, uploads, GPU/training, or public claims.
version: 0.1.0
metadata:
  hermes:
    tags: [afterparty-forge, static-site, revenue-safety, closed-gates, verifier]
---

# Afterparty Site Revenue Handoff Visibility

## Trigger

Use when the repo already contains prep-only revenue handoff structures in `docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json` and `tools/entity-tool-suite.json`, but the static site does not yet show them to the awake operator.

## Steps

1. Confirm the handoff lanes already exist and remain draft-only:
   - `private_followup_draft_template.status == draft_only_not_sent`
   - `wake_operator_manual_invoice_planning_checklist.status == draft_only_not_sent`
   - all tool contracts keep `money_actions_enabled=false`, `external_delivery_enabled=false`, and `training_or_gpu_enabled=false`.
2. Add a display-only static-site section linking to the revenue JSON, tool-suite doc, and tool-suite manifest.
3. Mirror the section into `docs/index.html` when the repo uses `docs/` as the GitHub Pages source mirror.
4. Patch `scripts/verify_entity_pipeline.py` to assert the section and its closed-gate language exist in both `site/index.html` and `docs/index.html`.
5. Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py
git diff --check
```

6. Run a changed-file secret scan before committing.

## Safety Gates

- Do not create forms, checkout URLs, payment links, invoice files, follow-up senders, uploaders, GPU/training launchers, model downloads, or cron controls.
- The site copy must say the lanes are draft-only/not-sent/local planning only.
- External money and delivery actions stay closed until separate awake human approval.

## Pitfalls

- Static visibility is not authorization: do not phrase a card as if a follow-up or invoice workflow is ready to execute.
- Keep `site/index.html` and `docs/index.html` synchronized; the verifier should catch drift.
- Link only to existing repo-local proof paths.

## Example Run

A safe increment adds a `revenue-handoff-lanes` site section for private follow-up drafts and manual invoice planning, verifies both pages contain `no sending, invoice creation, checkout/payment links`, and commits the display-only polish.
