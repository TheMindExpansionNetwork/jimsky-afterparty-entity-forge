#!/usr/bin/env python3
"""Aggregate site/relaunch verifier for Afterparty Forge 2045.

This is the cron-safe entrypoint expected by autonomous website improvers. It
keeps launch surfaces closed-by-default while checking static HTML, local JSON,
repo-local links, and the deeper entity pipeline verifier.
"""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
RISKY_TRUE_STRINGS = [
    'starts_gpu: true',
    'starts_paid_api: true',
    'publishes_stream: true',
    'records_audio: true',
    'uploads_private_media: true',
    'downloads_models: true',
    'starts_training: true',
    'submits_hackathon: true',
    'mutates_cron: true',
    'payment_links: true',
    'outreach: true',
    'claim_revenue: true',
]
REQUIRED_HTML_NEEDLES = [
    'AFTERPARTY FORGE 2045',
    'entity-tool-suite',
    'Money actions remain closed until human approval',
]
REQUIRED_RELAUNCH_NEEDLES = [
    'Human-Gated Relaunch Package Draft',
    'not approved for public posting',
    'PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py',
    'git diff --check',
    'If any field is blank, keep the action closed.',
    'public posting, outreach, spend, training, GPU work, or model downloads without explicit approval',
]
REQUIRED_X_THREAD_DOC_NEEDLES = [
    'draft-only, manual-post only',
    'auto_post_enabled: false',
    'public_posting: false',
    'Do you approve posting exactly one of these draft threads',
    'No tweet may imply OpenAI affiliation, revenue earned, live customers, public launch, or remote upload',
    'Blocked without approval',
]
X_THREAD_RISKY_FLAGS = [
    'auto_post_enabled',
    'public_posting',
    'outreach',
    'paid_promotion',
    'claim_revenue',
    'claim_affiliation',
    'starts_gpu',
    'starts_paid_api',
    'publishes_stream',
    'records_audio',
    'uploads_private_media',
    'downloads_models',
    'starts_training',
    'submits_hackathon',
    'mutates_cron',
]
YOUTUBE_CAPTION_RISKY_FLAGS = [
    'youtube_upload',
    'caption_upload',
    'public_posting',
    'paid_promotion',
    'outreach',
    'claim_revenue',
    'claim_affiliation',
    'starts_gpu',
    'starts_paid_api',
    'publishes_stream',
    'records_audio',
    'uploads_private_media',
    'downloads_models',
    'starts_training',
    'submits_hackathon',
    'mutates_cron',
]
REQUIRED_YOUTUBE_CAPTION_DOC_NEEDLES = [
    'caption_transcript_pack_ready_manual_upload_only',
    'Do you approve using these exact captions/transcript',
    'Manual upload only',
    'no upload action is enabled',
    'Blocked without approval',
    'PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_site.py',
]
LAUNCH_SCREEN_RISKY_FLAGS = [
    'public_posting',
    'x_space_creation',
    'livestream_creation',
    'youtube_upload',
    'caption_upload',
    'payment_links',
    'outreach',
    'paid_promotion',
    'spend',
    'claim_revenue',
    'claim_affiliation',
    'records_audio',
    'uploads_private_media',
    'starts_gpu',
    'starts_paid_api',
    'downloads_models',
    'starts_training',
    'submits_hackathon',
    'mutates_cron',
]
REQUIRED_LAUNCH_SCREEN_DOC_NEEDLES = [
    'launch_screen_checklist_manual_run_only_closed_until_human_yes',
    'Do you approve running this exact Afterparty Forge 2045 screen checklist manually',
    'PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_site.py',
    'VERIFY OK site relaunch surfaces closed-gate links/json/entity',
    'no recording, no public posting, no outreach, no livestream, no payment link',
    'Blocked without approval',
]
PRIVATE_DEMO_BUYER_RISKY_FLAGS = [
    'outreach',
    'public_posting',
    'x_space_creation',
    'livestream_creation',
    'youtube_upload',
    'caption_upload',
    'payment_links',
    'invoice_creation',
    'manual_invoice_execution',
    'auto_payment_enabled',
    'claim_revenue',
    'claim_affiliation',
    'records_audio',
    'uploads_private_media',
    'starts_gpu',
    'starts_paid_api',
    'downloads_models',
    'starts_training',
    'submits_hackathon',
    'mutates_cron',
]
QR_PROOF_HUB_RISKY_FLAGS = [
    'public_posting',
    'outreach',
    'paid_promotion',
    'payment_links',
    'claim_revenue',
    'claim_affiliation',
    'youtube_upload',
    'publishes_stream',
    'records_audio',
    'uploads_private_media',
    'starts_gpu',
    'starts_paid_api',
    'downloads_models',
    'starts_training',
    'submits_hackathon',
    'mutates_cron',
]
REQUIRED_QR_PROOF_HUB_DOC_NEEDLES = [
    'qr_proof_hub_promo_manual_scan_only_closed_until_human_yes',
    'Do you approve using this exact QR proof-hub promo card',
    'PYTHONDONTWRITEBYTECODE=1 python3 scripts/build_qr_proof_hub_promo.py',
    'PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_site.py',
    'CLOSED UNTIL HUMAN YES',
    'Blocked without approval',
]
REQUIRED_PRIVATE_DEMO_BUYER_DOC_NEEDLES = [
    'private_demo_buyer_script_draft_only_closed_until_human_yes',
    'Do you approve running this exact private Afterparty Forge 2045 buyer demo manually',
    'PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_site.py',
    'VERIFY OK site relaunch surfaces closed-gate links/json/entity',
    'Do not say “we made revenue” unless a real payment is verified',
    'Blocked without approval',
]


class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refs: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if key in {'href', 'src'} and value:
                self.refs.append((key, value))


def fail(message: str) -> None:
    raise SystemExit(message)


def repo_path_for_ref(html_path: Path, ref: str) -> Path | None:
    if ref.startswith(('http://', 'https://', 'mailto:', '#')):
        return None
    if ref.startswith('/'):
        return ROOT / ref.lstrip('/')
    return (html_path.parent / ref).resolve()


def verify_html(path: Path) -> None:
    text = path.read_text(encoding='utf-8')
    for needle in REQUIRED_HTML_NEEDLES:
        if needle not in text:
            fail(f'{path}: missing required visible string: {needle}')
    parser = LinkCollector()
    parser.feed(text)
    for attr, ref in parser.refs:
        target = repo_path_for_ref(path, ref)
        if target is None:
            continue
        try:
            target.relative_to(ROOT)
        except ValueError:
            fail(f'{path}: {attr} escapes repo root: {ref}')
        if not target.exists():
            fail(f'{path}: missing local {attr} target: {ref}')


def verify_json_files() -> None:
    for path in sorted((ROOT / 'site').glob('data/*.json')) + sorted((ROOT / 'docs').rglob('*.json')) + sorted((ROOT / 'tools').glob('*.json')):
        json.loads(path.read_text(encoding='utf-8'))
        text = path.read_text(encoding='utf-8').lower()
        for risky in RISKY_TRUE_STRINGS:
            if risky in text:
                fail(f'{path}: risky flag appears open: {risky}')


def verify_relaunch_doc() -> None:
    path = ROOT / 'docs/launch/RELAUNCH_PACKAGE_DRAFT.md'
    if not path.exists():
        fail(f'missing {path.relative_to(ROOT)}')
    text = path.read_text(encoding='utf-8')
    for needle in REQUIRED_RELAUNCH_NEEDLES:
        if needle not in text:
            fail(f'{path.relative_to(ROOT)} missing launch-safety needle: {needle}')
    lowered = text.lower()
    for risky in RISKY_TRUE_STRINGS:
        if risky in lowered:
            fail(f'{path.relative_to(ROOT)} risky flag appears open: {risky}')


def verify_x_thread_drafts() -> None:
    doc_path = ROOT / 'docs/social/X_THREAD_DRAFTS.md'
    manifest_path = ROOT / 'site/data/x-thread-drafts.json'
    if not doc_path.exists():
        fail(f'missing {doc_path.relative_to(ROOT)}')
    if not manifest_path.exists():
        fail(f'missing {manifest_path.relative_to(ROOT)}')
    doc_text = doc_path.read_text(encoding='utf-8')
    for needle in REQUIRED_X_THREAD_DOC_NEEDLES:
        if needle not in doc_text:
            fail(f'{doc_path.relative_to(ROOT)} missing X-thread safety needle: {needle}')
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    if manifest.get('status') != 'x_thread_drafts_manual_post_only_closed_until_human_yes':
        fail('x thread manifest status is not closed-until-human-yes')
    if manifest.get('manual_post_required') is not True:
        fail('x thread manifest must require manual posting')
    if manifest.get('requires_human_approval') is not True:
        fail('x thread manifest must require human approval')
    flags = manifest.get('risky_flags') or {}
    for flag in X_THREAD_RISKY_FLAGS:
        if flag == 'auto_post_enabled':
            if manifest.get(flag) is not False:
                fail(f'x thread manifest risky flag appears open: {flag}')
        elif flags.get(flag) is not False:
            fail(f'x thread manifest risky flag appears open or missing: {flag}')
    if len(manifest.get('threads') or []) < 3:
        fail('x thread manifest must include at least three draft thread entries')
    if len(manifest.get('blocked_without_approval') or []) < 5:
        fail('x thread manifest needs a substantial blocked-without-approval list')
    for proof in manifest.get('proof_paths') or []:
        if not (ROOT / proof).exists():
            fail(f'x thread manifest proof path missing: {proof}')


def verify_youtube_caption_pack() -> None:
    doc_path = ROOT / 'docs/youtube/CAPTIONS_TRANSCRIPTS_PACK.md'
    manifest_path = ROOT / 'site/data/youtube-captions-pack.json'
    if not doc_path.exists():
        fail(f'missing {doc_path.relative_to(ROOT)}')
    if not manifest_path.exists():
        fail(f'missing {manifest_path.relative_to(ROOT)}')
    doc_text = doc_path.read_text(encoding='utf-8')
    for needle in REQUIRED_YOUTUBE_CAPTION_DOC_NEEDLES:
        if needle not in doc_text:
            fail(f'{doc_path.relative_to(ROOT)} missing captions-pack safety needle: {needle}')
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    if manifest.get('status') != 'caption_transcript_pack_ready_manual_upload_only':
        fail('youtube captions manifest status is not manual-upload-only')
    if manifest.get('manual_upload_required') is not True:
        fail('youtube captions manifest must require manual upload')
    if manifest.get('auto_upload_enabled') is not False:
        fail('youtube captions manifest auto upload must be disabled')
    if manifest.get('requires_human_approval') is not True:
        fail('youtube captions manifest must require human approval')
    if 'Do you approve' not in (manifest.get('human_approval_question') or ''):
        fail('youtube captions manifest needs an explicit human approval question')
    flags = manifest.get('risky_flags') or {}
    for flag in YOUTUBE_CAPTION_RISKY_FLAGS:
        if flags.get(flag) is not False:
            fail(f'youtube captions manifest risky flag appears open or missing: {flag}')
    if len(manifest.get('blocked_without_approval') or []) < 8:
        fail('youtube captions manifest needs a substantial blocked-without-approval list')
    caption_files = manifest.get('caption_files') or []
    if len(caption_files) < 2:
        fail('youtube captions manifest must include VTT and SRT caption files')
    for item in caption_files:
        rel = item.get('path')
        if not rel or not (ROOT / rel).exists():
            fail(f'youtube captions caption path missing: {rel}')
        if int(item.get('cue_count') or 0) < 6:
            fail(f'youtube captions cue count too low: {rel}')
    if len(manifest.get('chapters') or []) < 5:
        fail('youtube captions manifest must include chapter markers')
    if len(manifest.get('shorts_hooks') or []) < 3:
        fail('youtube captions manifest must include at least three Shorts hooks')
    for proof in manifest.get('proof_paths') or []:
        if not (ROOT / proof).exists():
            fail(f'youtube captions manifest proof path missing: {proof}')


def verify_launch_screen_checklist() -> None:
    doc_path = ROOT / 'docs/launch/SCREEN_CHECKLIST.md'
    manifest_path = ROOT / 'site/data/launch-screen-checklist.json'
    if not doc_path.exists():
        fail(f'missing {doc_path.relative_to(ROOT)}')
    if not manifest_path.exists():
        fail(f'missing {manifest_path.relative_to(ROOT)}')
    doc_text = doc_path.read_text(encoding='utf-8')
    for needle in REQUIRED_LAUNCH_SCREEN_DOC_NEEDLES:
        if needle not in doc_text:
            fail(f'{doc_path.relative_to(ROOT)} missing launch-screen safety needle: {needle}')
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    if manifest.get('status') != 'launch_screen_checklist_manual_run_only_closed_until_human_yes':
        fail('launch screen checklist status is not closed-until-human-yes')
    if manifest.get('manual_run_required') is not True:
        fail('launch screen checklist must require manual run')
    if manifest.get('auto_stream_enabled') is not False:
        fail('launch screen checklist auto stream must be disabled')
    if manifest.get('requires_human_approval') is not True:
        fail('launch screen checklist must require human approval')
    if 'Do you approve' not in (manifest.get('human_approval_question') or ''):
        fail('launch screen checklist needs an explicit human approval question')
    flags = manifest.get('risky_flags') or {}
    for flag in LAUNCH_SCREEN_RISKY_FLAGS:
        if flags.get(flag) is not False:
            fail(f'launch screen checklist risky flag appears open or missing: {flag}')
    if len(manifest.get('blocked_without_approval') or []) < 8:
        fail('launch screen checklist needs a substantial blocked-without-approval list')
    if len(manifest.get('click_path') or []) < 5:
        fail('launch screen checklist needs a substantial proof-hub click path')
    if len(manifest.get('terminal_proof_commands') or []) < 4:
        fail('launch screen checklist needs terminal proof commands')
    for proof in manifest.get('proof_paths') or []:
        if not (ROOT / proof).exists():
            fail(f'launch screen checklist proof path missing: {proof}')
    for html_rel in ['site/index.html', 'docs/index.html']:
        html_text = (ROOT / html_rel).read_text(encoding='utf-8')
        if 'launch-screen-checklist' not in html_text:
            fail(f'{html_rel} missing launch screen checklist card')


def verify_private_demo_buyer_script() -> None:
    doc_path = ROOT / 'docs/revenue/PRIVATE_DEMO_BUYER_SAFE_SCRIPT.md'
    manifest_path = ROOT / 'site/data/private-demo-buyer-script.json'
    if not doc_path.exists():
        fail(f'missing {doc_path.relative_to(ROOT)}')
    if not manifest_path.exists():
        fail(f'missing {manifest_path.relative_to(ROOT)}')
    doc_text = doc_path.read_text(encoding='utf-8')
    for needle in REQUIRED_PRIVATE_DEMO_BUYER_DOC_NEEDLES:
        if needle not in doc_text:
            fail(f'{doc_path.relative_to(ROOT)} missing private-demo buyer safety needle: {needle}')
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    if manifest.get('status') != 'private_demo_buyer_script_draft_only_closed_until_human_yes':
        fail('private demo buyer script status is not closed-until-human-yes')
    if manifest.get('manual_demo_required') is not True:
        fail('private demo buyer script must require manual demo')
    if manifest.get('auto_outreach_enabled') is not False:
        fail('private demo buyer script auto outreach must be disabled')
    if manifest.get('auto_payment_enabled') is not False:
        fail('private demo buyer script auto payment must be disabled')
    if manifest.get('requires_human_approval') is not True:
        fail('private demo buyer script must require human approval')
    if 'Do you approve' not in (manifest.get('human_approval_question') or ''):
        fail('private demo buyer script needs an explicit human approval question')
    flags = manifest.get('risky_flags') or {}
    for flag in PRIVATE_DEMO_BUYER_RISKY_FLAGS:
        if flags.get(flag) is not False:
            fail(f'private demo buyer script risky flag appears open or missing: {flag}')
    if len(manifest.get('demo_beats') or []) < 5:
        fail('private demo buyer script needs enough demo beats')
    if len(manifest.get('blocked_without_approval') or []) < 8:
        fail('private demo buyer script needs a substantial blocked-without-approval list')
    if len(manifest.get('terminal_proof_commands') or []) < 4:
        fail('private demo buyer script needs terminal proof commands')
    for proof in manifest.get('proof_paths') or []:
        if not (ROOT / proof).exists():
            fail(f'private demo buyer script proof path missing: {proof}')
    for html_rel in ['site/index.html', 'docs/index.html']:
        html_text = (ROOT / html_rel).read_text(encoding='utf-8')
        if 'private-demo-buyer-script' not in html_text:
            fail(f'{html_rel} missing private demo buyer script card')


def verify_qr_proof_hub_promo() -> None:
    doc_path = ROOT / 'docs/launch/QR_PROOF_HUB_PROMO_ASSET.md'
    manifest_path = ROOT / 'site/data/qr-proof-hub-promo.json'
    if not doc_path.exists():
        fail(f'missing {doc_path.relative_to(ROOT)}')
    if not manifest_path.exists():
        fail(f'missing {manifest_path.relative_to(ROOT)}')
    doc_text = doc_path.read_text(encoding='utf-8')
    for needle in REQUIRED_QR_PROOF_HUB_DOC_NEEDLES:
        if needle not in doc_text:
            fail(f'{doc_path.relative_to(ROOT)} missing QR proof-hub safety needle: {needle}')
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    if manifest.get('status') != 'qr_proof_hub_promo_manual_scan_only_closed_until_human_yes':
        fail('QR proof-hub manifest status is not closed-until-human-yes')
    if manifest.get('manual_distribution_required') is not True:
        fail('QR proof-hub manifest must require manual distribution')
    if manifest.get('auto_post_enabled') is not False:
        fail('QR proof-hub manifest auto posting must be disabled')
    if manifest.get('requires_human_approval') is not True:
        fail('QR proof-hub manifest must require human approval')
    if 'Do you approve' not in (manifest.get('human_approval_question') or ''):
        fail('QR proof-hub manifest needs an explicit human approval question')
    decode = manifest.get('opencv_decode') or {}
    if decode.get('clean_qr_matches_payload') is not True or decode.get('card_matches_payload') is not True:
        fail('QR proof-hub manifest must record successful OpenCV decode for clean QR and card')
    flags = manifest.get('risky_flags') or {}
    for flag in QR_PROOF_HUB_RISKY_FLAGS:
        if flags.get(flag) is not False:
            fail(f'QR proof-hub risky flag appears open or missing: {flag}')
    if len(manifest.get('blocked_without_approval') or []) < 8:
        fail('QR proof-hub manifest needs a substantial blocked-without-approval list')
    for proof in manifest.get('proof_paths') or []:
        if not (ROOT / proof).exists():
            fail(f'QR proof-hub proof path missing: {proof}')
    payload_rel = manifest.get('qr_payload_path')
    payload_text = (ROOT / payload_rel).read_text(encoding='utf-8') if payload_rel else ''
    if 'CLOSED UNTIL HUMAN YES' not in payload_text:
        fail('QR proof-hub payload must include closed-until-human-yes copy')
    for html_rel in ['site/index.html', 'docs/index.html']:
        html_text = (ROOT / html_rel).read_text(encoding='utf-8')
        if 'qr-proof-hub-promo' not in html_text:
            fail(f'{html_rel} missing QR proof-hub promo card')


def run_entity_verifier() -> None:
    result = subprocess.run(
        [sys.executable, 'scripts/verify_entity_pipeline.py'],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        sys.stdout.write(result.stdout)
        sys.stderr.write(result.stderr)
        fail(f'entity verifier failed with exit code {result.returncode}')
    if 'VERIFY OK afterparty entity pipeline images=10' not in result.stdout:
        fail('entity verifier did not print expected success marker')


def main() -> None:
    for rel in ['site/index.html', 'docs/index.html']:
        path = ROOT / rel
        if not path.exists():
            fail(f'missing {rel}')
        verify_html(path)
    verify_json_files()
    verify_relaunch_doc()
    verify_x_thread_drafts()
    verify_youtube_caption_pack()
    verify_launch_screen_checklist()
    verify_private_demo_buyer_script()
    verify_qr_proof_hub_promo()
    run_entity_verifier()
    print('VERIFY OK site relaunch surfaces closed-gate links/json/entity')


if __name__ == '__main__':
    main()
