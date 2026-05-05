---
name: public-copy-qa-checklist
description: Prep-only QA checklist for Afterparty Forge public-copy drafts before any awake-approved posting or publication.
version: 0.1.0
metadata:
  hermes:
    tags: [afterparty-forge, public-copy, qa, revenue-safety, closed-gate]
---

# Public Copy QA Checklist

## Trigger

Use when Afterparty Forge 2045 has a `wake_operator_public_copy_draft` and an awake operator needs a final local review before deciding whether to post or publish copy.

## Safety gates

- Do not post, schedule, boost, send outreach, create payment/checkout links, create/send invoices, upload to Hugging Face, print tokens, start GPU/training/model-download jobs, mutate cron, or claim revenue/affiliation.
- Treat the checklist as local/private QA only until a separate awake approval names the exact copy path, page/channel context, post/publish scope, verifier result, and expiration.
- Green claims must have repo-local proof paths and current verifier output; HF/revenue/affiliation/external-delivery claims stay yellow or are removed unless independently verified.

## Steps

1. Open `docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json` and find `wake_operator_public_copy_draft` plus `wake_operator_public_copy_qa_checklist`.
2. Confirm every referenced proof path exists: proof ledger, revenue JSON, tool-suite manifest, tool-suite docs, site mirror, docs mirror, and verifier script.
3. Review the draft copy for forbidden claims: earned revenue, live checkout/payment/invoices, affiliation, verified HF upload/streaming, unattended GPU/training/model downloads, outreach, or public posting.
4. Ensure the draft repeats that payment, outreach, uploads, GPU/training, model downloads, and revenue/affiliation claims remain closed until separate human approval.
5. Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py` and `git diff --check` before any awake operator uses the QA result.

## Pitfalls

- Do not treat this QA checklist as approval to publish; it is only a preparation artifact.
- Do not add checkout URLs, invoice instructions, DM/email calls to action, token-bearing commands, or post scheduling instructions.
- Do not turn yellow claims into green claims unless the verifier and proof ledger can substantiate them.

## Example run

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py
git diff --check
```

Expected result: verifier passes, no whitespace errors, and the public-copy QA lane remains draft-only with all external gates closed.
