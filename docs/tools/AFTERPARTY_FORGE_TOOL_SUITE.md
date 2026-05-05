# Afterparty Forge 2045 Tool Suite

Status: `entity_tools_seeded`, `closed_until_human_yes_for_money_actions`

The entity now has a concrete tool suite: each tool has a purpose, output artifact, verifier posture, and safety gate.

This increment adds `contract_version: 2026-05-05.prep_only.v1` in `tools/entity-tool-suite.json`. Each tool now carries an explicit input contract, output contract, verifier expectation, and awake-operator handoff. The contract is prep-only: it can draft offers, proof ledgers, demo scripts, local lead schemas, and static-site manifest polish, but it cannot execute payment, outreach, spend, training/GPU, private upload, or public-posting actions while unattended.

## Tools

### 1. Offer Builder
- Purpose: turn proof artifacts into a buyer-facing offer.
- Inputs: website URL, videos, logo dataset, entity docs, proof ledger.
- Outputs: offer title, deliverables, buyer fit, price ladder draft.
- Closed gate: no payment links or outreach without awake approval.

### 2. Launch Packager
- Purpose: assemble a release bundle from repos, Pages, videos, logo assets, and docs.
- Outputs: launch checklist, media list, public-safe copy, blockers.
- Closed gate: no public posting outside configured Pages without approval.

### 3. Proof Ledger
- Purpose: map claims to exact proof paths and verifier commands.
- Outputs: claim/proof/status rows and red/yellow/green truth labels.
- Artifact: `docs/proof/AFTERPARTY_PROOF_LEDGER.json` now records green/yellow claims, exact proof paths, allowed copy, forbidden copy, and the verifier command for each claim.
- Closed gate: no green labels for unverifiable claims; no HF upload, revenue, outreach, payment, GPU/training, or affiliation claims without separate awake verification.

### 4. Demo Router
- Purpose: choose a safe next demo path.
- Outputs: private demo route, public page route, paid-offer route, dataset-release route.
- Closed gate: no DMs, emails, submissions, or payments while user sleeps.

### 5. Revenue Scout
- Purpose: prepare money-making moves that can be executed after human approval.
- Outputs: buyer types, listing copy, service ladder, local lead schema.
- Closed gate: draft-only; no spam, no forms, no claimed revenue.

### 6. Unicode Interface Director
- Purpose: turn the entity proof into neon UI language and video/card assets.
- Outputs: Unicode HUD scripts, visual cards, narrated videos, interface copy.
- Closed gate: no fake status screenshots.

### 7. Dataset Release Auditor
- Purpose: prepare local image/text dataset verification and a private-default Hugging Face streaming check handoff.
- Outputs: local parse/open-image checklist, HF repo privacy/streaming check plan, release blockers.
- Closed gate: no unattended HF upload, private media movement, GPU/training, model downloads, token printing, or remote-verified claims.

### 8. Buyer Proof FAQ Builder
- Purpose: answer proof questions with exact repo-local evidence before any buyer-facing use.
- Outputs: safe FAQ answer drafts, proof path lists, forbidden-claim reminders, approval fields.
- Closed gate: no sending, posting, checkout/payment, outreach, revenue/affiliation claims, HF upload claims, GPU/training, or model-download claims without awake approval.

## First awake command

Review the public explainer page, then pick one route:

1. Private demo.
2. First-dollar offer.
3. Public open-source call.
4. HF dataset public release.
5. Keep building autonomously.

## Prep-only first-dollar offer draft

The current first-dollar path is a **local offer draft**, not a live storefront. The draft now names the buyer audience, deliverables, exclusions, a local lead schema, a 7-minute private demo script, objection-safe responses, and a wake-operator checkout decision matrix in `docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json`.

The checkout matrix is prep-only: it helps an awake operator choose `private_demo_only`, `manual_invoice_after_yes`, or `keep_building_proof` after reviewing proof. Closed gates remain unchanged: no payment links, outreach, spend, revenue claims, public posting, GPU/training, wallets, private upload, or affiliation claims without an awake human yes.

## Local lead scoring rubric

`docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json` now includes a `local_lead_scoring_rubric` for **human-supplied leads only**. It scores explicit interest, proof availability, offer fit, low-risk scope, and awake-operator capacity to decide whether a lead is a private-demo candidate, needs more proof, or should not be contacted unattended. The rubric is draft-only and explicitly forbids scraping, outreach/forms, checkout/payment links, revenue/affiliation claims, private uploads, and GPU/training jobs until a human approves the exact next action.

## Hugging Face dataset streaming check plan

`docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json` now includes `hf_dataset_streaming_check_plan` for the logo-seed image/text lane. It is a **local verification and awake-operator handoff only**: parse 10 metadata rows, open 10 local PNGs, confirm captions, then run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py`. Optional remote streaming checks are documented for a later human-approved private Hugging Face upload using `HF_TOKEN`/`HUGGINGFACE_HUB_TOKEN` from the secure environment, but unattended upload, public release, private media movement, GPU/training, model downloads, token printing, and remote-verified claims remain closed.

## Wake-operator private demo packet

`docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json` now includes `wake_operator_private_demo_packet`. It compresses the proof ledger, tool contracts, first-dollar draft, and existing static site into a three-minute private walkthrough script for an awake operator. The packet is **draft-only and not sent**: recipient, channel, message path, offer tier, and expiration must be approved before use. It explicitly keeps sending, checkout/payment links, cold outreach/forms, revenue or affiliation claims, private upload/dataset publishing, GPU/training/model downloads, and cron mutation closed until a separate human yes.

## Buyer proof FAQ

`docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json` now includes `buyer_proof_faq`, paired with the `buyer-proof-faq-builder` tool contract. The FAQ answers only with repo-local proof paths and safe caveats: no revenue earned, no live checkout, no cold outreach sent, no affiliation claim, no HF remote-streaming claim before an awake upload check, and no GPU/training/model-download claim. It is **draft-only and not sent** until an awake operator approves the recipient/page, channel, question subset, message path, and expiration.
