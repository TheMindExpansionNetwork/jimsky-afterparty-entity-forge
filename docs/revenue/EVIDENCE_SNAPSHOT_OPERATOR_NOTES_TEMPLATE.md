# Evidence Snapshot Operator Notes Template

Status: `draft_only_local_notes_not_sent`

Use this template only after an awake operator has selected a next-action route and needs a local evidence snapshot note. It is not a message, invoice, checkout page, upload request, or public post.

## Required Header

- `snapshot_id:`
- `snapshot_created_utc:`
- `approved_route_id:`
- `approved_human_operator:`
- `verifier_command:` `PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py`
- `verifier_result:`
- `git_commit_or_pages_reference:`
- `approval_expires_utc:`

## Proof Paths Checked

List only repo-local proof paths that exist at review time:

- `docs/proof/AFTERPARTY_PROOF_LEDGER.json`
- `docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json`
- `tools/entity-tool-suite.json`
- `docs/tools/AFTERPARTY_FORGE_TOOL_SUITE.md`
- `site/index.html`
- `docs/index.html`
- `scripts/verify_entity_pipeline.py`

## Safe Note Body

1. What route was approved for review?
2. Which proof paths were checked, and what truth labels were used?
3. What verifier output was observed?
4. Which closed gates were confirmed still closed?
5. What is the single next human decision?

## Closed Gates To Repeat

- No sending or scheduling the snapshot.
- No invoice creation or manual invoice workflow execution.
- No checkout or payment links.
- No follow-up/outreach automation.
- No revenue or affiliation claims until independently verified.
- No Hugging Face upload, public dataset release, or token printing.
- No GPU/training/model-download jobs.
- No public posting.
- No cron mutation.

## Forbidden Copy

Do not write that revenue was earned, affiliation exists, a payment path is live, a follow-up was sent, a dataset was uploaded, or remote HF streaming was verified unless a separate awake-approved verification record exists.
