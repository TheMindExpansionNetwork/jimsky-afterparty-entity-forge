#!/usr/bin/env python3
from pathlib import Path
from PIL import Image
import json, re, sys
root=Path(__file__).resolve().parents[1]
required=['README.md','automation/SAFETY_BOUNDARIES.md','docs/entity/IDENTITY.md','docs/pipeline/ENTITY_PIPELINE.md','payloads/afterparty-forge/manifest.json','datasets/logo-seed/metadata.jsonl','site/index.html','docs/index.html','docs/tools/AFTERPARTY_FORGE_TOOL_SUITE.md','docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json','docs/proof/AFTERPARTY_PROOF_LEDGER.json','tools/entity-tool-suite.json','docs/launch/RELAUNCH_PACKAGE_DRAFT.md','docs/social/X_THREAD_DRAFTS.md','site/data/x-thread-drafts.json','scripts/verify_site.py']
missing=[p for p in required if not (root/p).exists()]
if missing: raise SystemExit('missing '+str(missing))
json.loads((root/'payloads/afterparty-forge/manifest.json').read_text())
rm=json.loads((root/'docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json').read_text())
assert rm.get('approved_to_execute') is False
assert rm.get('closed_gates',{}).get('payment_links') is False
assert rm.get('closed_gates',{}).get('outreach') is False
offer=rm.get('buyer_facing_offer_draft',{})
assert offer.get('headline') and 'forkable entity launch kit' in offer['headline']
assert len(offer.get('deliverables',[])) >= 4
assert any('payment links' in item for item in offer.get('not_included_without_approval',[]))
assert not re.search(r'https?://[^\s]*(stripe|paypal|gumroad|checkout|buy)', json.dumps(offer, sort_keys=True), re.I)
qual=offer.get('buyer_qualification_checklist',{})
assert qual.get('status') == 'draft_only_not_sent'
assert len(qual.get('must_confirm_before_contact',[])) >= 4
assert len(qual.get('disqualifiers',[])) >= 3
assert any('wallet' in item.lower() for item in qual.get('disqualifiers',[]))
assert any('approved_channel' == item for item in qual.get('approval_fields',[]))
demo=offer.get('private_demo_script',{})
assert demo.get('status') == 'draft_only_not_sent'
assert demo.get('duration_minutes') == 7
assert len(demo.get('beats',[])) >= 4
for beat in demo.get('beats',[]):
    assert (root/beat.get('proof_path','')).exists(), beat
assert any('revenue' in line.lower() for line in demo.get('forbidden_lines',[]))
objections=offer.get('buyer_objection_responses',[])
assert len(objections) >= 3
assert all(o.get('objection') and o.get('safe_response') for o in objections)
assert any('payment' in o.get('safe_response','').lower() for o in objections)
assert any('training' in o.get('safe_response','').lower() for o in objections)
acceptance=offer.get('private_demo_acceptance_checklist',{})
assert acceptance.get('status') == 'draft_only_not_sent'
assert len(acceptance.get('proof_paths_required',[])) >= 4
for rel in acceptance.get('proof_paths_required',[]):
    assert not rel.startswith('/') and '..' not in Path(rel).parts
    assert (root/rel).exists(), f"acceptance proof path missing: {rel}"
assert len(acceptance.get('must_pass_before_demo',[])) >= 5
assert any('verifier command passes' in item.lower() for item in acceptance.get('must_pass_before_demo',[]))
assert 'approved_demo_channel' in acceptance.get('operator_decision_fields',[])
closed=acceptance.get('closed_gate_confirmation',{})
for key in ['payment_links','outreach_automation','public_posting','gpu_or_training','private_upload','revenue_claim','affiliation_claim']:
    assert closed.get(key) is False, key
checkout_matrix=offer.get('wake_operator_checkout_decision_matrix',{})
assert checkout_matrix.get('status') == 'draft_only_not_sent'
assert 'checkout link' in checkout_matrix.get('purpose','').lower()
options=checkout_matrix.get('decision_options',[])
assert len(options) >= 3
option_ids={o.get('option_id') for o in options}
assert {'private_demo_only','manual_invoice_after_yes','keep_building_proof'} <= option_ids
for option in options:
    assert option.get('recommended_when') and option.get('allowed_next_step')
    assert option.get('still_closed'), option
assert 'approved_payment_workflow_path' in checkout_matrix.get('approval_required_fields',[])
for forbidden in ['checkout URL creation','cold outreach','claiming revenue','starting GPU/training jobs']:
    assert forbidden in checkout_matrix.get('forbidden_until_approval',[])
assert 'verify_entity_pipeline.py' in checkout_matrix.get('verification_note','')
lead_rubric=offer.get('local_lead_scoring_rubric',{})
assert lead_rubric.get('status') == 'draft_only_not_sent'
assert lead_rubric.get('max_score') == 10
assert len(lead_rubric.get('score_bands',[])) >= 3
assert {b.get('label') for b in lead_rubric.get('score_bands',[])} >= {'private_demo_candidate','needs_more_proof','do_not_contact_unattended'}
criteria=lead_rubric.get('criteria',[])
assert len(criteria) >= 5
assert sum(c.get('points',0) for c in criteria) == 10
assert all(c.get('evidence_required') for c in criteria)
for forbidden in ['sending outreach or forms','creating checkout or payment links','starting GPU/training jobs or uploading private data']:
    assert forbidden in lead_rubric.get('forbidden_uses',[])
assert 'draft-only' in lead_rubric.get('verification_note','')
demo_packet=offer.get('wake_operator_private_demo_packet',{})
assert demo_packet.get('status') == 'draft_only_not_sent'
assert 'private demo' in demo_packet.get('packet_title','').lower()
assert 'not earned revenue' in demo_packet.get('operator_script_intro','').lower()
assets=demo_packet.get('demo_assets',[])
assert len(assets) >= 5
for asset in assets:
    rel=asset.get('path','')
    assert rel and not rel.startswith('/') and '..' not in Path(rel).parts
    assert (root/rel).exists(), f"demo packet asset missing: {rel}"
assert len(demo_packet.get('three_minute_flow',[])) >= 4
for field in ['approved_demo_recipient','approved_demo_channel','approved_message_path','approval_expires_utc']:
    assert field in demo_packet.get('approval_required_before_use',[]), field
for forbidden in ['sending the demo packet','creating checkout or payment links','cold outreach or form submission','claiming revenue or affiliation','uploading private data or publishing datasets','starting GPU/training/model-download jobs','mutating cron jobs']:
    assert forbidden in demo_packet.get('forbidden_until_approval',[]), forbidden
assert 'verify_entity_pipeline.py' in demo_packet.get('verification_note','')
buyer_faq=offer.get('buyer_proof_faq',{})
assert buyer_faq.get('status') == 'draft_only_not_sent'
assert 'buyer proof questions' in buyer_faq.get('purpose','').lower()
faq_questions=buyer_faq.get('questions',[])
assert len(faq_questions) >= 4
for item in faq_questions:
    assert item.get('question') and item.get('safe_answer')
    assert item.get('proof_paths'), item
    for rel in item.get('proof_paths',[]):
        assert not rel.startswith('/') and '..' not in Path(rel).parts
        assert (root/rel).exists(), f"buyer FAQ proof path missing: {rel}"
for forbidden in ['revenue was earned','payment or checkout is live','cold outreach has been sent','OpenAI/event/sponsor affiliation exists','Hugging Face remote streaming is verified before an awake upload check passes','GPU training/model downloads were started']:
    assert forbidden in buyer_faq.get('forbidden_claims',[]), forbidden
for field in ['approved_recipient_or_page','approved_channel','approved_question_subset','approved_message_path','approval_expires_utc']:
    assert field in buyer_faq.get('approval_required_before_use',[]), field
assert 'verify_entity_pipeline.py' in buyer_faq.get('verification_note','')
post_demo=offer.get('post_demo_outcome_capture',{})
assert post_demo.get('status') == 'draft_only_not_sent'
assert 'local receipt' in post_demo.get('purpose','').lower()
expected_outcomes={'interested_manual_invoice_after_yes','needs_more_proof_before_followup','dataset_release_question_requires_approval','no_fit_do_not_contact_unattended'}
assert expected_outcomes <= set(post_demo.get('allowed_outcome_labels',[]))
for field in ['demo_date_utc','approved_demo_recipient','approved_demo_channel','proof_paths_shown','operator_selected_outcome_label','followup_approval_expires_utc']:
    assert field in post_demo.get('local_receipt_fields',[]), field
for rel in post_demo.get('proof_paths_allowed',[]):
    assert not rel.startswith('/') and '..' not in Path(rel).parts
    assert (root/rel).exists(), f"post-demo proof path missing: {rel}"
rules=post_demo.get('router_rules',[])
assert len(rules) >= 4
assert {r.get('if_outcome') for r in rules} >= expected_outcomes
for rule in rules:
    assert rule.get('safe_next_step') and rule.get('still_closed'), rule
for forbidden in ['sending follow-up messages','creating checkout or payment links','claiming revenue before payment is verified','claiming affiliation or sponsorship','uploading private data or publishing datasets','starting GPU/training/model-download jobs','mutating cron jobs']:
    assert forbidden in post_demo.get('forbidden_until_approval',[]), forbidden
assert 'verify_entity_pipeline.py' in post_demo.get('verification_note','')
scope_quote=offer.get('wake_operator_scope_quote_sheet',{})
assert scope_quote.get('status') == 'draft_only_not_sent'
assert 'scope/quote worksheet' in scope_quote.get('purpose','').lower()
assert len(scope_quote.get('allowed_use_cases',[])) >= 4
for field in ['approved_demo_receipt_id','buyer_problem_summary','selected_offer_tier_usd','included_deliverables','proof_paths_to_show','explicit_exclusions','approval_expires_utc']:
    assert field in scope_quote.get('quote_fields',[]), field
tier_guidance=scope_quote.get('tier_guidance',[])
assert len(tier_guidance) >= 3
assert {t.get('tier_usd') for t in tier_guidance} >= {55,155,555}
for tier in tier_guidance:
    assert tier.get('scope') and tier.get('required_proof_paths'), tier
    for rel in tier.get('required_proof_paths',[]):
        assert not rel.startswith('/') and '..' not in Path(rel).parts
        assert (root/rel).exists(), f"scope quote proof path missing: {rel}"
for exclusion in ['no checkout/payment URL creation','no unattended outreach or follow-up sending','no revenue or affiliation claim until independently verified','no Hugging Face upload/public dataset release/private media movement','no GPU/training/model downloads or paid provider spend']:
    assert exclusion in scope_quote.get('explicit_exclusions_required',[]), exclusion
for field in ['approved_buyer_or_demo_receipt','approved_scope_summary','approved_price_tier_usd','approved_manual_invoice_workflow_path','approved_followup_message_path','approval_expires_utc']:
    assert field in scope_quote.get('approval_required_before_use',[]), field
for forbidden in ['sending a quote or follow-up','creating checkout or payment links','claiming revenue before payment is verified','claiming affiliation or sponsorship','uploading private data or publishing datasets','starting GPU/training/model-download jobs','mutating cron jobs']:
    assert forbidden in scope_quote.get('forbidden_until_approval',[]), forbidden
assert 'verify_entity_pipeline.py' in scope_quote.get('verification_note','')
delivery_receipt=offer.get('private_demo_delivery_receipt_kit',{})
assert delivery_receipt.get('status') == 'draft_only_not_sent'
assert delivery_receipt.get('receipt_scope') == 'local_manual_record_only_no_external_delivery'
assert 'local/manual delivery receipt' in delivery_receipt.get('purpose','').lower()
for field in ['approved_demo_receipt_id','demo_date_utc','approved_demo_recipient','approved_demo_channel','proof_paths_shown','operator_selected_outcome_label','followup_approval_expires_utc']:
    assert field in delivery_receipt.get('receipt_fields',[]), field
for rel in delivery_receipt.get('required_proof_paths',[]):
    assert not rel.startswith('/') and '..' not in Path(rel).parts
    assert (root/rel).exists(), f"delivery receipt proof path missing: {rel}"
expected_receipt_outcomes={'private_demo_complete_no_followup_yet','interested_manual_invoice_after_yes','needs_more_proof_before_followup','dataset_release_question_requires_approval','no_fit_do_not_contact_unattended'}
assert expected_receipt_outcomes <= set(delivery_receipt.get('allowed_outcome_labels',[]))
assert len(delivery_receipt.get('operator_attestations_required',[])) >= 4
assert delivery_receipt.get('next_decision_router') == 'post_demo_outcome_capture'
for field in ['approved_followup_recipient','approved_followup_channel','approved_message_path','approval_expires_utc']:
    assert field in delivery_receipt.get('approval_required_before_any_followup',[]), field
for forbidden in ['sending follow-up messages','creating checkout or payment links','starting a manual invoice workflow','claiming revenue before payment is verified','claiming affiliation or sponsorship','uploading private data or publishing datasets','starting GPU/training/model-download jobs','mutating cron jobs']:
    assert forbidden in delivery_receipt.get('forbidden_until_approval',[]), forbidden
assert 'verify_entity_pipeline.py' in delivery_receipt.get('verification_note','')
next_router=offer.get('wake_operator_next_action_router',{})
assert next_router.get('status') == 'draft_only_not_sent'
assert 'exactly one' in next_router.get('purpose','').lower()
expected_inputs={'private_demo_delivery_receipt_kit','post_demo_outcome_capture','wake_operator_scope_quote_sheet','dataset_release_readiness','hf_dataset_streaming_check_plan'}
assert expected_inputs <= set(next_router.get('input_receipts_allowed',[]))
route_options=next_router.get('route_options',[])
expected_routes={'keep_building_repo_proof','approve_private_followup_draft','approve_manual_invoice_planning','approve_private_hf_dataset_check'}
assert expected_routes <= {route.get('route_id') for route in route_options}
for route in route_options:
    assert route.get('recommended_when') and route.get('allowed_repo_only_action'), route
    assert route.get('still_closed'), route
for field in ['approved_route_id','approved_human_operator','approved_recipient_or_repo_id_if_any','approved_message_or_invoice_plan_path_if_any','approval_expires_utc']:
    assert field in next_router.get('approval_required_fields',[]), field
for forbidden in ['sending follow-up messages','creating checkout or payment links','starting a manual invoice workflow','claiming revenue before payment is verified','claiming affiliation or sponsorship','uploading private data or publishing datasets','printing HF tokens or credential-store contents','starting GPU/training/model-download jobs','mutating cron jobs']:
    assert forbidden in next_router.get('forbidden_until_approval',[]), forbidden
assert 'verify_entity_pipeline.py' in next_router.get('verification_note','')
followup_template=offer.get('private_followup_draft_template',{})
assert followup_template.get('status') == 'draft_only_not_sent'
assert 'follow-up message draft' in followup_template.get('purpose','').lower()
assert followup_template.get('allowed_trigger','').startswith('wake_operator_next_action_router.route_id == approve_private_followup_draft')
for field in ['approved_demo_receipt_id','approved_route_id','approved_recipient','approved_channel','approved_message_path','proof_paths_referenced','followup_question_or_next_step','approval_expires_utc']:
    assert field in followup_template.get('draft_fields',[]), field
assert len(followup_template.get('message_constraints',[])) >= 4
assert any('payment, invoice, upload' in item for item in followup_template.get('message_constraints',[]))
for rel in followup_template.get('required_proof_paths',[]):
    assert not rel.startswith('/') and '..' not in Path(rel).parts
    assert (root/rel).exists(), f"follow-up template proof path missing: {rel}"
for forbidden in ['sending or scheduling the follow-up','creating checkout or payment links','starting a manual invoice workflow','claiming revenue before payment is verified','claiming affiliation or sponsorship','uploading private data or publishing datasets','printing HF tokens or credential-store contents','starting GPU/training/model-download jobs','mutating cron jobs']:
    assert forbidden in followup_template.get('forbidden_until_approval',[]), forbidden
assert 'verify_entity_pipeline.py' in followup_template.get('verification_note','')
manual_invoice=offer.get('wake_operator_manual_invoice_planning_checklist',{})
assert manual_invoice.get('status') == 'draft_only_not_sent'
assert 'local/manual invoice planning checklist' in manual_invoice.get('purpose','').lower()
assert manual_invoice.get('allowed_trigger','').startswith('wake_operator_next_action_router.route_id == approve_manual_invoice_planning')
for field in ['approved_demo_receipt_id','approved_route_id','approved_buyer_or_org','approved_scope_quote_sheet_id','selected_price_tier_usd','approved_manual_invoice_workflow_path','proof_paths_to_attach','explicit_exclusions','approval_expires_utc']:
    assert field in manual_invoice.get('planning_fields',[]), field
assert len(manual_invoice.get('required_preconditions',[])) >= 4
assert any('real buyer explicitly asked to buy' in item.lower() for item in manual_invoice.get('required_preconditions',[]))
for rel in manual_invoice.get('required_proof_paths',[]):
    assert not rel.startswith('/') and '..' not in Path(rel).parts
    assert (root/rel).exists(), f"manual invoice checklist proof path missing: {rel}"
assert len(manual_invoice.get('manual_invoice_copy_constraints',[])) >= 4
assert any('do not create or send invoices unattended' in item.lower() for item in manual_invoice.get('manual_invoice_copy_constraints',[]))
for forbidden in ['creating checkout or payment links','creating or sending an invoice','starting a manual invoice workflow','sending follow-up messages','claiming revenue before payment is verified','claiming affiliation or sponsorship','uploading private data or publishing datasets','printing HF tokens or credential-store contents','starting GPU/training/model-download jobs','public posting','mutating cron jobs']:
    assert forbidden in manual_invoice.get('forbidden_until_approval',[]), forbidden
assert 'verify_entity_pipeline.py' in manual_invoice.get('verification_note','')
handoff_integrity=rm.get('wake_operator_handoff_integrity_checklist',{})
assert handoff_integrity.get('status') == 'draft_only_not_sent'
assert 'handoff' in handoff_integrity.get('purpose','').lower()
assert 'wake_operator_next_action_router.route_id' in handoff_integrity.get('allowed_trigger','')
for field in ['approved_route_id','approved_human_operator','proof_paths_checked','tool_contract_ids_checked','site_mirror_checked','verifier_command_output_path','approval_expires_utc']:
    assert field in handoff_integrity.get('checklist_fields',[]), field
for rel in handoff_integrity.get('required_proof_paths',[]):
    assert not rel.startswith('/') and '..' not in Path(rel).parts
    assert (root/rel).exists(), f"handoff integrity proof path missing: {rel}"
expected_handoff_tools={'buyer-proof-faq-builder','post-demo-outcome-router','scope-quote-sheet-builder','private-demo-delivery-receipt-kit','wake-operator-next-action-router','private-followup-draft-builder','manual-invoice-planning-checklist-builder','handoff-integrity-auditor','evidence-snapshot-builder','evidence-snapshot-notes-template-builder'}
assert expected_handoff_tools <= set(handoff_integrity.get('required_tool_contract_ids',[]))
assert 'evidence-snapshot-archive-index-builder' in handoff_integrity.get('required_tool_contract_ids',[])
assert 'evidence-snapshot-reuse-decision-matrix-builder' in handoff_integrity.get('required_tool_contract_ids',[])
assert len(handoff_integrity.get('must_confirm_before_external_use',[])) >= 5
assert any('money_actions_enabled=false' in item for item in handoff_integrity.get('must_confirm_before_external_use',[]))
for forbidden in ['sending or scheduling follow-up messages','creating checkout or payment links','creating or sending invoices','starting a manual invoice workflow','claiming revenue before payment is verified','claiming affiliation or sponsorship','Hugging Face upload or public dataset release','printing HF tokens or credential-store contents','starting GPU/training/model-download jobs','public posting','mutating cron jobs']:
    assert forbidden in handoff_integrity.get('forbidden_until_approval',[]), forbidden
assert 'verify_entity_pipeline.py' in handoff_integrity.get('verification_note','')
evidence_snapshot=rm.get('wake_operator_evidence_snapshot_checklist',{})
assert evidence_snapshot.get('status') == 'draft_only_not_sent'
assert 'evidence snapshot' in evidence_snapshot.get('purpose','').lower()
assert 'wake_operator_next_action_router.route_id' in evidence_snapshot.get('allowed_trigger','')
for field in ['snapshot_id','snapshot_created_utc','approved_route_id','proof_paths_checked','verifier_command','verifier_result','git_commit_or_pages_reference','closed_gates_confirmed','operator_notes_path','approval_expires_utc']:
    assert field in evidence_snapshot.get('snapshot_fields',[]), field
for rel in evidence_snapshot.get('required_proof_paths',[]):
    assert not rel.startswith('/') and '..' not in Path(rel).parts
    assert (root/rel).exists(), f"evidence snapshot proof path missing: {rel}"
assert len(evidence_snapshot.get('must_confirm_before_snapshot_use',[])) >= 5
assert any('verifier command passed' in item.lower() for item in evidence_snapshot.get('must_confirm_before_snapshot_use',[]))
for forbidden in ['sending or scheduling the snapshot','creating checkout or payment links','creating or sending invoices','starting a manual invoice workflow','claiming revenue before payment is verified','claiming affiliation or sponsorship','Hugging Face upload or public dataset release','printing HF tokens or credential-store contents','starting GPU/training/model-download jobs','public posting','mutating cron jobs']:
    assert forbidden in evidence_snapshot.get('forbidden_until_approval',[]), forbidden
assert evidence_snapshot.get('operator_notes_template_path') == 'docs/revenue/EVIDENCE_SNAPSHOT_OPERATOR_NOTES_TEMPLATE.md'
assert evidence_snapshot.get('operator_notes_template_status') == 'draft_only_local_notes_not_sent'
assert (root/evidence_snapshot.get('operator_notes_template_path','')).exists()
for section in ['Required Header','Proof Paths Checked','Safe Note Body','Closed Gates To Repeat','Forbidden Copy']:
    assert section in evidence_snapshot.get('operator_notes_template_required_sections',[]), section
notes_template=(root/evidence_snapshot.get('operator_notes_template_path','')).read_text()
for phrase in ['draft_only_local_notes_not_sent','No sending or scheduling the snapshot','No checkout or payment links','No Hugging Face upload','No GPU/training/model-download jobs','No cron mutation']:
    assert phrase in notes_template, phrase
assert 'using operator notes as public/buyer copy without awake approval' in evidence_snapshot.get('forbidden_until_approval',[])
assert 'verify_entity_pipeline.py' in evidence_snapshot.get('verification_note','')
archive_index=rm.get('wake_operator_evidence_snapshot_archive_index',{})
assert archive_index.get('status') == 'draft_only_local_index_not_sent'
assert 'archive index' in archive_index.get('purpose','').lower()
assert archive_index.get('allowed_trigger','').startswith('wake_operator_evidence_snapshot_checklist.status == draft_only_not_sent')
for field in ['archive_entry_id','snapshot_id','snapshot_created_utc','approved_route_id','operator_notes_path','proof_paths_checked','verifier_command','verifier_result','git_commit_or_pages_reference','closed_gates_confirmed','approval_expires_utc']:
    assert field in archive_index.get('index_fields',[]), field
for rel in archive_index.get('required_proof_paths',[]):
    assert not rel.startswith('/') and '..' not in Path(rel).parts
    assert (root/rel).exists(), f"archive index proof path missing: {rel}"
assert len(archive_index.get('must_confirm_before_archive_use',[])) >= 4
assert any('not a public gallery' in item.lower() for item in archive_index.get('must_confirm_before_archive_use',[]))
for forbidden in ['sending or scheduling archive entries','creating checkout or payment links','creating or sending invoices','starting a manual invoice workflow','claiming revenue before payment is verified','claiming affiliation or sponsorship','Hugging Face upload or public dataset release','printing HF tokens or credential-store contents','starting GPU/training/model-download jobs','public posting','mutating cron jobs','using archive entries as public/buyer copy without awake approval']:
    assert forbidden in archive_index.get('forbidden_until_approval',[]), forbidden
assert 'verify_entity_pipeline.py' in archive_index.get('verification_note','')
reuse_matrix=rm.get('wake_operator_evidence_snapshot_reuse_decision_matrix',{})
assert reuse_matrix.get('status') == 'draft_only_local_matrix_not_sent'
assert 'reuse' in reuse_matrix.get('purpose','').lower()
assert reuse_matrix.get('allowed_trigger','').startswith('wake_operator_evidence_snapshot_archive_index.status == draft_only_local_index_not_sent')
for field in ['archive_entry_id','snapshot_id','proposed_reuse_route','approved_human_operator','proof_paths_rechecked','verifier_command','verifier_result','copy_status','approval_expires_utc']:
    assert field in reuse_matrix.get('decision_fields',[]), field
reuse_routes={route.get('route_id') for route in reuse_matrix.get('reuse_route_options',[])}
assert {'reuse_as_private_operator_note','prepare_buyer_proof_packet_draft','prepare_dataset_handoff_draft','prepare_public_copy_draft_after_approval'} <= reuse_routes
for route in reuse_matrix.get('reuse_route_options',[]):
    assert route.get('allowed_repo_only_action') and route.get('still_closed'), route
for rel in reuse_matrix.get('required_proof_paths',[]):
    assert not rel.startswith('/') and '..' not in Path(rel).parts
    assert (root/rel).exists(), f"reuse decision proof path missing: {rel}"
assert len(reuse_matrix.get('must_confirm_before_reuse',[])) >= 5
assert any('exactly one' in item.lower() for item in reuse_matrix.get('must_confirm_before_reuse',[]))
for forbidden in ['sending or scheduling reused notes','creating checkout or payment links','creating or sending invoices','starting a manual invoice workflow','claiming revenue before payment is verified','claiming affiliation or sponsorship','Hugging Face upload or public dataset release','printing HF tokens or credential-store contents','starting GPU/training/model-download jobs','public posting','outreach automation','mutating cron jobs','using reuse decisions as public/buyer copy without awake approval']:
    assert forbidden in reuse_matrix.get('forbidden_until_approval',[]), forbidden
assert 'verify_entity_pipeline.py' in reuse_matrix.get('verification_note','')
lead_schema=rm.get('local_lead_schema',[])
assert any(f.get('field')=='approval_status' and f.get('default')=='draft_only' for f in lead_schema)
dataset_release=rm.get('dataset_release_readiness',{})
assert dataset_release.get('status') == 'local_metadata_ready_upload_closed_until_human_yes'
assert dataset_release.get('source_manifest') == 'datasets/logo-seed/metadata.jsonl'
assert (root/dataset_release.get('source_manifest','')).exists()
assert dataset_release.get('image_root') == 'datasets/logo-seed/images'
assert (root/dataset_release.get('image_root','')).exists()
assert dataset_release.get('contact_sheet') == 'assets/brand/logo-seed/contact_sheet.jpg'
assert (root/dataset_release.get('contact_sheet','')).exists()
assert dataset_release.get('local_row_count') == 10
assert dataset_release.get('expected_image_count') == 10
hf_release=dataset_release.get('hf_release_default',{})
assert hf_release.get('repo_type') == 'dataset'
assert hf_release.get('privacy') == 'private'
assert hf_release.get('upload_allowed_unattended') is False
assert hf_release.get('requires_human_approval') is True
training_status=dataset_release.get('training_status',{})
for key in ['training_started','gpu_jobs_started','model_downloads_started']:
    assert training_status.get(key) is False, key
assert len(dataset_release.get('sample_image_records',[])) >= 3
for rec in dataset_release.get('sample_image_records',[]):
    assert rec.get('file_name','').startswith('images/')
    assert rec.get('dimensions') == [1024, 1024]
    assert rec.get('caption_present') is True
    assert re.fullmatch(r'[0-9a-f]{16}', rec.get('sha256_16',''))
for forbidden in ['Hugging Face upload','public dataset release','GPU or training job','claiming dataset availability on HF']:
    assert forbidden in dataset_release.get('forbidden_until_approval',[])
assert any('verify_entity_pipeline.py' in item for item in dataset_release.get('pre_release_checklist',[]))
hf_plan=rm.get('hf_dataset_streaming_check_plan',{})
assert hf_plan.get('status') == 'local_check_plan_ready_upload_closed_until_human_yes'
assert hf_plan.get('source_manifest') == 'datasets/logo-seed/metadata.jsonl'
assert (root/hf_plan.get('source_manifest','')).exists()
assert hf_plan.get('image_root') == 'datasets/logo-seed/images'
assert (root/hf_plan.get('image_root','')).exists()
assert hf_plan.get('expected_rows') == 10
assert hf_plan.get('expected_images') == 10
assert len(hf_plan.get('local_checks',[])) >= 4
assert any('verify_entity_pipeline.py' in item for item in hf_plan.get('local_checks',[]))
remote_checks=hf_plan.get('optional_hf_remote_checks_after_human_upload',{})
assert set(remote_checks.get('requires_token_env',[])) == {'HF_TOKEN','HUGGINGFACE_HUB_TOKEN'}
assert remote_checks.get('default_privacy') == 'private'
assert 'repo_id_placeholder' in remote_checks
assert len(remote_checks.get('checks',[])) >= 3
for forbidden in ['Hugging Face upload','public dataset release','GPU or training job','printing HF tokens or credential-store contents','claiming remote streaming is verified before an awake upload check passes']:
    assert forbidden in hf_plan.get('forbidden_until_approval',[])
assert 'awake operator approves' in hf_plan.get('human_handoff','').lower()
pl=json.loads((root/'docs/proof/AFTERPARTY_PROOF_LEDGER.json').read_text())
assert pl.get('status') == 'prep_only_claims_mapped_closed_gates'
assert pl.get('closed_gates',{}).get('payment_links') is False
assert pl.get('closed_gates',{}).get('outreach') is False
assert pl.get('closed_gates',{}).get('claim_revenue') is False
assert pl.get('closed_gates',{}).get('hf_upload') is False
claims=pl.get('claims', [])
assert len(claims) >= 5
assert any(c.get('truth_label') == 'yellow' and ('HF' in c.get('claim','') or 'Hugging Face' in c.get('claim','')) for c in claims)
for c in claims:
    assert c.get('id') and c.get('claim') and c.get('truth_label') in {'green','yellow','red'}
    assert c.get('verifier_command') == 'PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py'
    assert 'forbidden_copy' in c and c['forbidden_copy']
    for rel in c.get('proof_paths', []):
        assert not rel.startswith('/') and '..' not in Path(rel).parts
        assert (root/rel).exists(), f"proof path missing for {c.get('id')}: {rel}"
    if c.get('truth_label') == 'green':
        assert c.get('proof_paths'), c.get('id')
xpack=json.loads((root/'site/data/x-thread-drafts.json').read_text())
assert xpack.get('status') == 'x_thread_drafts_manual_post_only_closed_until_human_yes'
assert xpack.get('manual_post_required') is True
assert xpack.get('auto_post_enabled') is False
assert xpack.get('requires_human_approval') is True
for key in ['public_posting','outreach','paid_promotion','claim_revenue','claim_affiliation','starts_gpu','starts_paid_api','publishes_stream','records_audio','uploads_private_media','downloads_models','starts_training','submits_hackathon','mutates_cron']:
    assert xpack.get('risky_flags',{}).get(key) is False, key
assert len(xpack.get('threads',[])) >= 3
for thread in xpack.get('threads',[]):
    assert thread.get('status') == 'draft_only_not_posted'
    assert thread.get('post_count') == 5
    assert (root/thread.get('claims_source','')).exists(), thread
for rel in xpack.get('proof_paths',[]):
    assert not rel.startswith('/') and '..' not in Path(rel).parts
    assert (root/rel).exists(), f"x thread proof path missing: {rel}"
xdoc=(root/'docs/social/X_THREAD_DRAFTS.md').read_text()
for phrase in ['manual-post only','auto_post_enabled: false','claim_revenue: false','mutates_cron: false','Posting, scheduling, liking, replying, DMing, quoting, or boosting']:
    assert phrase in xdoc, phrase
tm=json.loads((root/'tools/entity-tool-suite.json').read_text())
assert tm.get('contract_version') == '2026-05-05.prep_only.v1'
assert len(tm.get('tools',[])) >= 8
tool_ids={tool.get('id') for tool in tm.get('tools',[])}
assert 'dataset-release-auditor' in tool_ids
assert 'buyer-proof-faq-builder' in tool_ids
assert 'post-demo-outcome-router' in tool_ids
assert 'scope-quote-sheet-builder' in tool_ids
assert 'private-demo-delivery-receipt-kit' in tool_ids
assert 'wake-operator-next-action-router' in tool_ids
assert 'private-followup-draft-builder' in tool_ids
assert 'manual-invoice-planning-checklist-builder' in tool_ids
assert 'handoff-integrity-auditor' in tool_ids
assert 'evidence-snapshot-builder' in tool_ids
assert 'evidence-snapshot-notes-template-builder' in tool_ids
assert 'evidence-snapshot-archive-index-builder' in tool_ids
assert 'evidence-snapshot-reuse-decision-matrix-builder' in tool_ids
post_demo_tool=next(tool for tool in tm.get('tools',[]) if tool.get('id')=='post-demo-outcome-router')
assert post_demo_tool.get('requires_human_approval') is True
assert any('post_demo_outcome_capture' in item for item in post_demo_tool.get('verification',[]))
scope_quote_tool=next(tool for tool in tm.get('tools',[]) if tool.get('id')=='scope-quote-sheet-builder')
assert scope_quote_tool.get('requires_human_approval') is True
assert any('wake_operator_scope_quote_sheet' in item for item in scope_quote_tool.get('verification',[]))
assert scope_quote_tool.get('money_actions_enabled') is False
delivery_receipt_tool=next(tool for tool in tm.get('tools',[]) if tool.get('id')=='private-demo-delivery-receipt-kit')
assert delivery_receipt_tool.get('requires_human_approval') is True
assert any('private_demo_delivery_receipt_kit' in item for item in delivery_receipt_tool.get('verification',[]))
assert delivery_receipt_tool.get('external_delivery_enabled') is False
next_router_tool=next(tool for tool in tm.get('tools',[]) if tool.get('id')=='wake-operator-next-action-router')
assert next_router_tool.get('requires_human_approval') is True
assert any('wake_operator_next_action_router' in item for item in next_router_tool.get('verification',[]))
assert next_router_tool.get('money_actions_enabled') is False
assert next_router_tool.get('external_delivery_enabled') is False
assert next_router_tool.get('training_or_gpu_enabled') is False
followup_tool=next(tool for tool in tm.get('tools',[]) if tool.get('id')=='private-followup-draft-builder')
assert followup_tool.get('requires_human_approval') is True
assert any('private_followup_draft_template' in item for item in followup_tool.get('verification',[]))
assert followup_tool.get('money_actions_enabled') is False
assert followup_tool.get('external_delivery_enabled') is False
assert followup_tool.get('training_or_gpu_enabled') is False
manual_invoice_tool=next(tool for tool in tm.get('tools',[]) if tool.get('id')=='manual-invoice-planning-checklist-builder')
assert manual_invoice_tool.get('requires_human_approval') is True
assert any('wake_operator_manual_invoice_planning_checklist' in item for item in manual_invoice_tool.get('verification',[]))
assert manual_invoice_tool.get('money_actions_enabled') is False
assert manual_invoice_tool.get('external_delivery_enabled') is False
assert manual_invoice_tool.get('training_or_gpu_enabled') is False
handoff_tool=next(tool for tool in tm.get('tools',[]) if tool.get('id')=='handoff-integrity-auditor')
assert handoff_tool.get('requires_human_approval') is True
assert any('wake_operator_handoff_integrity_checklist' in item for item in handoff_tool.get('verification',[]))
assert handoff_tool.get('money_actions_enabled') is False
assert handoff_tool.get('external_delivery_enabled') is False
assert handoff_tool.get('training_or_gpu_enabled') is False
evidence_tool=next(tool for tool in tm.get('tools',[]) if tool.get('id')=='evidence-snapshot-builder')
assert evidence_tool.get('requires_human_approval') is True
assert any('wake_operator_evidence_snapshot_checklist' in item for item in evidence_tool.get('verification',[]))
assert evidence_tool.get('money_actions_enabled') is False
assert evidence_tool.get('external_delivery_enabled') is False
assert evidence_tool.get('training_or_gpu_enabled') is False
notes_tool=next(tool for tool in tm.get('tools',[]) if tool.get('id')=='evidence-snapshot-notes-template-builder')
assert notes_tool.get('requires_human_approval') is True
assert any('operator notes template path exists' in item for item in notes_tool.get('verification',[]))
assert notes_tool.get('money_actions_enabled') is False
assert notes_tool.get('external_delivery_enabled') is False
assert notes_tool.get('training_or_gpu_enabled') is False
archive_tool=next(tool for tool in tm.get('tools',[]) if tool.get('id')=='evidence-snapshot-archive-index-builder')
assert archive_tool.get('requires_human_approval') is True
assert any('wake_operator_evidence_snapshot_archive_index' in item for item in archive_tool.get('verification',[]))
assert archive_tool.get('money_actions_enabled') is False
assert archive_tool.get('external_delivery_enabled') is False
assert archive_tool.get('training_or_gpu_enabled') is False
reuse_tool=next(tool for tool in tm.get('tools',[]) if tool.get('id')=='evidence-snapshot-reuse-decision-matrix-builder')
assert reuse_tool.get('requires_human_approval') is True
assert any('wake_operator_evidence_snapshot_reuse_decision_matrix' in item for item in reuse_tool.get('verification',[]))
assert reuse_tool.get('money_actions_enabled') is False
assert reuse_tool.get('external_delivery_enabled') is False
assert reuse_tool.get('training_or_gpu_enabled') is False
tool_doc=(root/'docs/tools/AFTERPARTY_FORGE_TOOL_SUITE.md').read_text()
for phrase in ['### 14. Manual Invoice Planning Checklist Builder','approve_manual_invoice_planning','no invoice creation/sending','every external money action stays closed','### 15. Handoff Integrity Auditor','wake_operator_handoff_integrity_checklist','no follow-up sending','### 16. Evidence Snapshot Builder','wake_operator_evidence_snapshot_checklist','no sending/scheduling','### 17. Evidence Snapshot Notes Template Builder','EVIDENCE_SNAPSHOT_OPERATOR_NOTES_TEMPLATE.md','notes are not sent','### 18. Evidence Snapshot Archive Index Builder','wake_operator_evidence_snapshot_archive_index','archive entries are not sent','### 19. Evidence Snapshot Reuse Decision Matrix Builder','wake_operator_evidence_snapshot_reuse_decision_matrix','reuse decisions are not sent']:
    assert phrase in tool_doc, phrase
assert 'payment links or checkout activation' in tm.get('forbidden_unattended_actions', [])
for tool in tm.get('tools', []):
    assert tool.get('closed_until_human_yes') is True
    assert tool.get('money_actions_enabled') is False
    assert tool.get('external_delivery_enabled') is False
    assert tool.get('training_or_gpu_enabled') is False
    assert len(tool.get('input_contract', [])) >= 3
    assert len(tool.get('output_contract', [])) >= 3
    assert len(tool.get('verification', [])) >= 2
    assert 'Awake operator' in tool.get('human_handoff', '')
for rel in ['site/index.html','docs/index.html']:
    page=(root/rel).read_text()
    assert 'entity-tool-suite' in page
    assert 'Money actions remain closed until human approval' in page
    assert 'revenue-handoff-lanes' in page
    assert 'Prep-Only Revenue Handoff Lanes' in page
    assert 'Private follow-up drafts, manual invoice planning, handoff integrity checks, evidence snapshots, local evidence snapshot archive indexes, and evidence snapshot reuse decision matrices' in page
    assert 'no sending, invoice creation, checkout/payment links' in page
    assert 'HF upload, token printing, GPU/training, model downloads' in page
    for tool_name in ['Dataset Release Auditor','Buyer Proof FAQ Builder','Post-Demo Outcome Router','Scope Quote Sheet Builder','Private Demo Delivery Receipt Kit','Wake Operator Next Action Router','Private Follow-up Draft Builder','Manual Invoice Planning Checklist Builder','Handoff Integrity Auditor','Evidence Snapshot Builder','Evidence Snapshot Notes Template Builder','Evidence Snapshot Archive Index Builder','Evidence Snapshot Reuse Decision Matrix Builder']:
        assert tool_name in page, f"site/docs tool-suite mirror missing {tool_name} in {rel}"
    assert 'handoff integrity checks' in page, f"site/docs handoff integrity copy missing in {rel}"
    assert 'evidence snapshots' in page, f"site/docs evidence snapshot copy missing in {rel}"
    assert 'local evidence snapshot archive indexes' in page, f"site/docs archive index copy missing in {rel}"
    assert 'reuse decision matrices' in page, f"site/docs reuse decision matrix copy missing in {rel}"
rows=[]
for line in (root/'datasets/logo-seed/metadata.jsonl').read_text().splitlines():
    if line.strip(): rows.append(json.loads(line))
assert len(rows)==10, len(rows)
for r in rows:
    p=root/'datasets/logo-seed'/r['file_name']
    assert p.exists(), p
    im=Image.open(p); im.verify()
    assert r.get('text') and 'Afterparty Forge 2045' in r['text']
patterns=[r'ghp_[A-Za-z0-9_]{20,}',r'github_pat_[A-Za-z0-9_]{20,}',r'sk-[A-Za-z0-9_-]{20,}',r'\bhf_[A-Za-z0-9]{20,}\b',r'BEGIN (RSA |OPENSSH |EC |)PRIVATE KEY']
for p in root.rglob('*'):
    if any(part in {'.git','__pycache__'} for part in p.parts) or not p.is_file() or p.suffix.lower() in {'.png','.jpg','.jpeg','.zip'}: continue
    txt=p.read_text(errors='ignore')[:1000000]
    for pat in patterns:
        if re.search(pat, txt): raise SystemExit(f'secret-like pattern in {p}')
print('VERIFY OK afterparty entity pipeline images=10')
