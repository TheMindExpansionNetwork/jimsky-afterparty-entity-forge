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

## First awake command

Review the public explainer page, then pick one route:

1. Private demo.
2. First-dollar offer.
3. Public open-source call.
4. HF dataset public release.
5. Keep building autonomously.

## Prep-only first-dollar offer draft

The current first-dollar path is a **local offer draft**, not a live storefront. The draft now names the buyer audience, deliverables, exclusions, a local lead schema, a 7-minute private demo script, and objection-safe responses in `docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json`.

Closed gates remain unchanged: no payment links, outreach, spend, revenue claims, public posting, GPU/training, wallets, or affiliation claims without an awake human yes.
