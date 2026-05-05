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


### 9. Post-Demo Outcome Router
- Purpose: capture a local, non-sending private-demo receipt and route the next safe operator decision.
- Outputs: receipt fields, outcome label, safe next-step route, closed-gate blocker list.
- Closed gate: no follow-up messages, checkout/payment links, revenue claims, HF upload, public dataset release, GPU/training, model downloads, or cron mutation without a fresh awake approval.

### 10. Scope Quote Sheet Builder
- Purpose: turn an interested post-demo outcome into a draft scope/quote worksheet for awake review.
- Outputs: buyer problem summary, selected draft tier, deliverables mapped to proof paths, explicit exclusions, approval expiration.
- Closed gate: no quote sending, checkout/payment links, manual invoice workflow, follow-up, revenue claim, HF upload, GPU/training, or cron mutation without fresh awake approval.

### 11. Private Demo Delivery Receipt Kit
- Purpose: capture a local/manual delivery receipt after an awake-approved private demo before any follow-up or invoice decision.
- Outputs: receipt fields, proof path checklist, operator attestations, and a handoff into the post-demo outcome router.
- Closed gate: no follow-up sending, checkout/payment links, manual invoice workflow, revenue/affiliation claim, HF upload, GPU/training/model download, public posting, or cron mutation without fresh awake approval.


### 12. Wake Operator Next Action Router
- Purpose: choose exactly one safe next route after a receipt, post-demo outcome, scope/quote worksheet, or dataset release question.
- Outputs: route id, approval fields, closed-gate blocker list, and repo-only follow-up checklist.
- Closed gate: no follow-up sending, checkout/payment links, manual invoice workflow, revenue/affiliation claim, HF upload/token printing, GPU/training/model downloads, public posting, or cron mutation without fresh awake approval.


### 13. Private Follow-up Draft Builder
- Purpose: prepare one private follow-up draft after an awake-approved demo receipt and next-action route.
- Outputs: draft-only message fields, proof-path list, single bounded next-step question, and closed-gate reminder block.
- Closed gate: no sending/scheduling, checkout/payment links, manual invoice workflow, revenue/affiliation claim, HF upload/token printing, GPU/training/model downloads, public posting, or cron mutation without fresh awake approval.

### 14. Manual Invoice Planning Checklist Builder
- Purpose: prepare a local/manual invoice planning checklist only after an awake-approved buyer explicitly asks to buy and the next-action router selects `approve_manual_invoice_planning`.
- Outputs: planning fields, proof paths to attach, explicit exclusions, copy constraints, and closed-gate reminder block.
- Closed gate: no invoice creation/sending, checkout/payment links, follow-up sending, revenue/affiliation claim, HF upload/token printing, GPU/training/model downloads, public posting, or cron mutation without fresh awake approval.

### 15. Handoff Integrity Auditor
- Purpose: audit a selected revenue/data handoff before an awake operator uses it outside the repo.
- Outputs: proof-path checks, tool-contract coverage, site/docs mirror confirmation, and closed-gate blockers.
- Closed gate: no follow-up sending, invoice creation/sending, checkout/payment links, HF upload/token printing, public posting, GPU/training/model downloads, revenue/affiliation claim, or cron mutation without fresh awake approval.

### 16. Evidence Snapshot Builder
- Purpose: prepare a local evidence snapshot that ties a selected revenue/data handoff to current proof paths and verifier output.
- Outputs: snapshot fields, proof path checklist, closed-gate confirmations, and approval expiration fields.
- Closed gate: no sending/scheduling, invoice creation/sending, checkout/payment links, HF upload/token printing, public posting, GPU/training/model downloads, revenue/affiliation claim, or cron mutation without separate awake approval.

### 17. Evidence Snapshot Notes Template Builder
- Purpose: give the awake operator a local notes template for turning an evidence snapshot into a private review note without inventing buyer/public copy.
- Outputs: draft-only local operator notes, proof-path checklist, closed-gate confirmation block, and one next human decision prompt.
- Artifact: `docs/revenue/EVIDENCE_SNAPSHOT_OPERATOR_NOTES_TEMPLATE.md`.
- Closed gate: notes are not sent, posted, attached to invoices, used as checkout copy, used for HF upload claims, or treated as revenue/affiliation proof without separate awake approval.

### 18. Evidence Snapshot Archive Index Builder
- Purpose: maintain a local/private index of evidence snapshots and operator notes after approved review.
- Artifact: `wake_operator_evidence_snapshot_archive_index` in `docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json`.
- Outputs: draft-only archive entry fields, proof path checklist, verifier result reference, and closed-gate confirmation block.
- Closed gate: archive entries are not sent, posted, attached to invoices, converted into checkout copy, used for HF upload claims, or treated as revenue/affiliation proof without separate awake approval.


### 19. Evidence Snapshot Reuse Decision Matrix Builder
- Purpose: decide how an approved local evidence snapshot archive entry may be reused without turning it into external copy unattended.
- Artifact: `wake_operator_evidence_snapshot_reuse_decision_matrix` in `docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json`.
- Outputs: draft-only reuse route, proof path rechecks, verifier result reference, and closed-gate confirmation block.
- Closed gate: reuse decisions are not sent, posted, attached to invoices, converted into checkout copy, used for HF upload claims, or treated as revenue/affiliation proof without separate awake approval.

### 20. Buyer Proof Packet Draft Builder
- Purpose: convert one approved evidence snapshot reuse decision into a local buyer proof packet draft for awake review.
- Artifact: `wake_operator_buyer_proof_packet_draft` in `docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json`.
- Outputs: draft-only packet fields, proof-path rechecks, safe copy blocks, forbidden copy reminders, and approval expiration fields.
- Closed gate: buyer proof packet drafts are not sent, posted, attached to invoices, converted into checkout copy, used for HF upload claims, used for revenue/affiliation proof, or used for outreach without separate awake approval.

### 21. Dataset Handoff Draft Builder
- Purpose: convert one approved evidence snapshot reuse decision into a local dataset handoff draft for awake review.
- Artifact: `wake_operator_dataset_handoff_draft` in `docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json`.
- Outputs: draft-only dataset handoff fields, local parse/open-image checklist, private-default HF approval fields, and closed-gate reminders.
- Closed gate: dataset handoff drafts do not upload to Hugging Face, publish datasets, move private media, print tokens, start GPU/training/model downloads, send handoff messages, claim remote streaming, or create buyer/public copy without separate awake approval.

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

## Post-demo outcome router

`docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json` now includes `post_demo_outcome_capture`, paired with the `post-demo-outcome-router` tool contract and a timestamped usage skill. It is a **local receipt only** for after an awake-approved private demo: it records proof paths shown and routes the operator to `interested_manual_invoice_after_yes`, `needs_more_proof_before_followup`, `dataset_release_question_requires_approval`, or `no_fit_do_not_contact_unattended`. Follow-up messages, checkout/payment links, revenue claims, affiliation claims, private upload/HF publication, GPU/training/model downloads, and cron mutation remain closed until separate human approval.
## Wake-operator scope quote sheet

`docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json` now includes `wake_operator_scope_quote_sheet`, paired with the `scope-quote-sheet-builder` tool contract and a timestamped usage skill. It is a **draft-only scope/quote worksheet** for after an approved private demo or post-demo outcome: it maps requested deliverables to existing proof paths and a draft tier, while keeping quote sending, checkout/payment links, manual invoice workflow, outreach/follow-up, revenue/affiliation claims, HF upload/public dataset release/private media movement, GPU/training/model downloads, and cron mutation closed until separate awake approval.

## Private demo delivery receipt kit

`docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json` now includes `private_demo_delivery_receipt_kit`, paired with the `private-demo-delivery-receipt-kit` tool contract and a timestamped usage skill. It is a **local/manual receipt template only** for after an awake-approved private demo: it captures what proof paths were shown, the selected outcome label, and operator attestations before routing into the post-demo outcome capture. It keeps follow-up sending, checkout/payment links, manual invoice workflow, revenue/affiliation claims, HF upload/public dataset release/private media movement, GPU/training/model downloads, and cron mutation closed until separate awake approval.

## Wake-operator next action router

`docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json` now includes `wake_operator_next_action_router`, paired with the `wake-operator-next-action-router` tool contract and a timestamped usage skill. It is a **draft-only, exactly-one-route chooser** for after an approved demo receipt, post-demo outcome, scope/quote worksheet, or dataset question. It can recommend repo-only proof building, a private follow-up draft, manual invoice planning, or a private-default HF dataset check, but it keeps follow-up sending, checkout/payment links, manual invoice execution, revenue/affiliation claims, HF upload/token printing, GPU/training/model downloads, public posting, and cron mutation closed until separate awake approval.

## Private follow-up draft template

`docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json` now includes `private_followup_draft_template`, paired with the `private-followup-draft-builder` tool contract. It is a **draft-only, not-sent** template for an already awake-approved private demo context: it records the approved receipt, route, recipient/channel, message path, proof paths, and one bounded next-step question. It keeps follow-up sending/scheduling, checkout/payment links, manual invoice workflow, revenue/affiliation claims, HF upload/token printing, GPU/training/model downloads, public posting, and cron mutation closed until separate awake approval.

## Manual invoice planning checklist

`docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json` now includes `wake_operator_manual_invoice_planning_checklist`, paired with the `manual-invoice-planning-checklist-builder` tool contract. It is a **local planning artifact only** for the `approve_manual_invoice_planning` route: it records approved receipt/scope/tier fields, proof paths to attach, explicit exclusions, and invoice-copy constraints. It does not create or send invoices, checkout links, payment links, follow-ups, public posts, uploads, GPU/training jobs, or revenue/affiliation claims; every external money action stays closed until a separate awake human approval.

## Handoff integrity auditor

`docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json` now includes `wake_operator_handoff_integrity_checklist`, paired with the `handoff-integrity-auditor` tool contract. It is a **draft-only, not-sent** integrity check for private follow-up, manual invoice planning, HF dataset checks, buyer proof FAQ, or proof-building routes. It verifies proof paths, tool contract ids, site/docs mirror language, and verifier output while keeping follow-up sending, invoice creation/sending, checkout/payment links, HF upload/token printing, public posting, GPU/training/model downloads, revenue/affiliation claims, and cron mutation closed until separate awake approval.

## Evidence snapshot checklist

`docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json` now includes `wake_operator_evidence_snapshot_checklist`, paired with the `evidence-snapshot-builder` tool contract. It is a **draft-only, local/private review artifact** for attaching current proof paths and verifier output to a selected next-action route. It keeps sending/scheduling, invoice creation/sending, checkout/payment links, HF upload/token printing, public posting, GPU/training/model downloads, revenue/affiliation claims, and cron mutation closed until separate awake approval.

## Evidence snapshot operator notes template

`docs/revenue/EVIDENCE_SNAPSHOT_OPERATOR_NOTES_TEMPLATE.md` now gives the awake operator a local notes template for evidence snapshots, paired with the `evidence-snapshot-notes-template-builder` contract. It is **draft-only and local/private**: notes are not sent, posted, used as invoice or checkout copy, used to claim HF upload/streaming, or used as revenue/affiliation proof until a separate awake approval and verification record exists.

## Evidence snapshot reuse decision matrix

`docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json` now includes `wake_operator_evidence_snapshot_reuse_decision_matrix`, paired with the `evidence-snapshot-reuse-decision-matrix-builder` contract. It is a **draft-only, local/private reuse decision matrix** for an already approved evidence snapshot archive entry. It can route a snapshot toward a private operator note, buyer proof packet draft, dataset handoff draft, or public-copy draft, but it does not send, post, invoice, upload, claim revenue, claim affiliation, start GPU/training/model downloads, or mutate cron without a separate awake approval.
