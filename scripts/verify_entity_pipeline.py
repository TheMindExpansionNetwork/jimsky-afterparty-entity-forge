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
lead_schema=rm.get('local_lead_schema',[])
assert any(f.get('field')=='approval_status' and f.get('default')=='draft_only' for f in lead_schema)
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
assert len(tm.get('tools',[])) >= 6
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
rows=[]
for line in (root/'datasets/logo-seed/metadata.jsonl').read_text().splitlines():
    if line.strip(): rows.append(json.loads(line))
assert len(rows)==10, len(rows)
for r in rows:
    p=root/'datasets/logo-seed'/r['file_name']
    assert p.exists(), p
    im=Image.open(p); im.verify()
    assert r.get('text') and 'Afterparty Forge 2045' in r['text']
patterns=[r'ghp_[A-Za-z0-9_]{20,}',r'github_pat_[A-Za-z0-9_]{20,}',r'sk-[A-Za-z0-9_-]{20,}',r'hf_[A-Za-z0-9_]{20,}',r'BEGIN (RSA |OPENSSH |EC |)PRIVATE KEY']
for p in root.rglob('*'):
    if any(part in {'.git','__pycache__'} for part in p.parts) or not p.is_file() or p.suffix.lower() in {'.png','.jpg','.jpeg','.zip'}: continue
    txt=p.read_text(errors='ignore')[:1000000]
    for pat in patterns:
        if re.search(pat, txt): raise SystemExit(f'secret-like pattern in {p}')
print('VERIFY OK afterparty entity pipeline images=10')
