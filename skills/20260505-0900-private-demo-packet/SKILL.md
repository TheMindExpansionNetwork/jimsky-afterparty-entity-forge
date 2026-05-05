---
name: 20260505-0900-private-demo-packet
description: "Prep-only private demo packet for Afterparty Forge 2045: compress proof assets into an awake-operator walkthrough while keeping all external gates closed."
version: 0.1.0
metadata:
  hermes:
    tags: [afterparty-forge, private-demo, revenue-prep, proof-ledger, closed-gates]
---

# Afterparty Forge Private Demo Packet

## Trigger

Use when an awake operator wants to convert the Afterparty Forge 2045 proof vault into a short private walkthrough without enabling payment, outreach, upload, GPU/training, public posting, or cron mutation.

## Safety gates

- `status` must remain `draft_only_not_sent` until a human approves the exact recipient/channel/message.
- Do not send messages, submit forms, create checkout/payment links, claim revenue, claim affiliation, upload private data, publish datasets, start GPU/training/model downloads, or mutate cron jobs.
- Use only repo-local proof paths that pass `scripts/verify_entity_pipeline.py`.

## Steps

1. Open `docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json` and read `buyer_facing_offer_draft.wake_operator_private_demo_packet`.
2. Confirm each `demo_assets[].path` exists and points to repo-local proof.
3. Read the `operator_script_intro` exactly enough to preserve the no-revenue/no-affiliation/no-external-action disclaimers.
4. Follow the `three_minute_flow` as a private walkthrough: scope, proof ledger, tool contracts, then one operator decision.
5. Before any use, fill human-approved values outside unattended mode: recipient, channel, message path, optional offer tier, and approval expiration.

## Verification

Run from repo root:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py
git diff --check
```

The verifier asserts the packet is draft-only, every demo asset exists, required approval fields are present, and forbidden actions remain closed.

## Example run

An awake operator wants to review a buyer-facing demo. The operator runs the verifier, opens the private demo packet, confirms the proof ledger has current green/yellow labels, approves `private_demo_only`, and performs a manual private walkthrough. No checkout link, outreach automation, upload, GPU/training, or public posting is created by this skill.
