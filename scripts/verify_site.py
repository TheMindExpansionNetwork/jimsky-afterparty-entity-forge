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
    run_entity_verifier()
    print('VERIFY OK site relaunch surfaces closed-gate links/json/entity')


if __name__ == '__main__':
    main()
