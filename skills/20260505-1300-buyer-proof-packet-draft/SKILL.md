---
name: buyer-proof-packet-draft
description: Prep-only buyer proof packet draft lane for Afterparty Forge evidence snapshot reuse decisions.
version: 0.1.0
metadata:
  hermes:
    tags: [afterparty-forge, revenue-prep, proof-packet, closed-gates]
---

# Buyer Proof Packet Draft

## Trigger

Use when an awake operator has a local evidence snapshot archive entry and chooses the `prepare_buyer_proof_packet_draft` route from the evidence snapshot reuse decision matrix.

## Steps

1. Confirm the archive entry and snapshot IDs are awake-approved and local/private.
2. Recheck every proof path in `docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json` under `wake_operator_buyer_proof_packet_draft.required_proof_paths`.
3. Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py`.
4. Draft only local packet fields: safe proof summaries, green/yellow labels, forbidden copy, verifier result, and expiration.
5. Require a separate awake approval before any packet is sent, posted, attached to an invoice, or used as buyer/public copy.

## Safety Gates

Keep these closed until separate human approval: sending/scheduling, checkout/payment links, invoice creation/sending, manual invoice workflow execution, outreach automation, HF upload/public dataset release, token printing, GPU/training/model downloads, public posting, revenue claims, affiliation claims, and cron mutation.

## Pitfalls

- Do not promote yellow HF/revenue/affiliation claims to green without independent verification.
- Do not treat a local proof packet draft as external buyer copy.
- Do not include tokens, private media, payment URLs, or live invoice instructions.

## Verification

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py
git diff --check
```

## Example Run

An operator selects `prepare_buyer_proof_packet_draft`; the builder fills local packet fields, cites `docs/proof/AFTERPARTY_PROOF_LEDGER.json`, records the verifier command, and leaves all external delivery and money gates closed.
