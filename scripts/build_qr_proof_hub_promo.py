#!/usr/bin/env python3
"""Build a scannable, closed-gate QR proof-hub promo card for Afterparty Forge 2045."""
from __future__ import annotations

import json
from pathlib import Path

import cv2
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / 'assets/launch/qr-proof-hub'
SITE_ASSET_DIR = ROOT / 'site/assets/img/launch'
PAYLOAD_PATH = ASSET_DIR / 'afterparty-forge-proof-hub-payload.txt'
CLEAN_QR_PATH = ASSET_DIR / 'afterparty-forge-proof-hub-clean-qr.png'
CARD_PATH = ASSET_DIR / 'afterparty-forge-proof-hub-card.png'
SITE_CARD_PATH = SITE_ASSET_DIR / 'afterparty-forge-proof-hub-card.png'
MANIFEST_PATH = ROOT / 'site/data/qr-proof-hub-promo.json'

PAYLOAD = """AFTERPARTY FORGE 2045 PROOF HUB
LOCAL: site/index.html
DOC: docs/launch/RELAUNCH_PACKAGE_DRAFT.md
VERIFY: PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_site.py
CLOSED UNTIL HUMAN YES: no posting/outreach/payments/upload/GPU/training/cron.
""".strip()

RISKY_FLAGS = {
    'public_posting': False,
    'outreach': False,
    'paid_promotion': False,
    'payment_links': False,
    'claim_revenue': False,
    'claim_affiliation': False,
    'youtube_upload': False,
    'publishes_stream': False,
    'records_audio': False,
    'uploads_private_media': False,
    'starts_gpu': False,
    'starts_paid_api': False,
    'downloads_models': False,
    'starts_training': False,
    'submits_hackathon': False,
    'mutates_cron': False,
}


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',
        '/usr/share/fonts/truetype/liberation2/LiberationMono-Bold.ttf' if bold else '/usr/share/fonts/truetype/liberation2/LiberationMono-Regular.ttf',
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def decode_qr(path: Path) -> str:
    img = cv2.imread(str(path))
    if img is None:
        raise RuntimeError(f'OpenCV could not read {path}')
    data, _pts, _ = cv2.QRCodeDetector().detectAndDecode(img)
    return data


def make_qr() -> Image.Image:
    qr = qrcode.QRCode(error_correction=ERROR_CORRECT_H, box_size=13, border=4)
    qr.add_data(PAYLOAD)
    qr.make(fit=True)
    return qr.make_image(fill_color='black', back_color='white').convert('RGB')


def centered(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, fnt, fill) -> None:
    x, y = xy
    box = draw.textbbox((0, 0), text, font=fnt)
    draw.text((x - (box[2] - box[0]) // 2, y), text, font=fnt, fill=fill)


def build_card(qr_img: Image.Image) -> Image.Image:
    w, h = 1600, 2150
    img = Image.new('RGB', (w, h), (8, 0, 17))
    d = ImageDraw.Draw(img)

    # Neon grid / flyer texture, outside QR quiet zone.
    for x in range(-200, w + 200, 80):
        color = (16, 38, 55) if x % 160 else (28, 72, 90)
        d.line([(x, 0), (x - 520, h)], fill=color, width=1)
    for y in range(120, h, 95):
        d.line([(0, y), (w, y)], fill=(28, 10, 44), width=1)
    for i in range(22):
        x = 80 + (i * 167) % (w - 160)
        y = 220 + (i * 251) % (h - 440)
        d.text((x, y), '◇', font=font(28, True), fill=(0, 245, 255))
        d.text((x + 31, y + 19), '2045', font=font(18), fill=(255, 43, 214))

    d.rounded_rectangle([48, 48, w - 48, h - 48], radius=42, outline=(0, 245, 255), width=5)
    d.rounded_rectangle([72, 72, w - 72, h - 72], radius=30, outline=(255, 43, 214), width=3)
    centered(d, (w // 2, 115), 'AFTERPARTY FORGE 2045', font(66, True), (0, 245, 255))
    centered(d, (w // 2, 202), 'QR PROOF HUB · MANUAL REVIEW ONLY', font(34, True), (250, 255, 0))
    centered(d, (w // 2, 255), 'Scan to see repo-local proof paths + verifier command', font(26), (230, 220, 255))

    qr_w, qr_h = qr_img.size
    mount_x, mount_y = (w - qr_w) // 2, 345
    mount = [mount_x - 42, mount_y - 42, mount_x + qr_w + 42, mount_y + qr_h + 42]
    d.rounded_rectangle(mount, radius=32, fill=(248, 244, 226), outline=(250, 255, 0), width=8)
    img.paste(qr_img, (mount_x, mount_y))

    d.rounded_rectangle([115, 1580, w - 115, 1865], radius=28, fill=(14, 2, 29), outline=(0, 245, 255), width=3)
    lines = [
        'LOCAL PROOF PATHS: site/index.html · docs/launch · docs/proof',
        'VERIFY: PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_site.py',
        'CLOSED GATES: no posting · no outreach · no payments · no upload',
        'NO GPU · NO TRAINING · NO REVENUE CLAIM · NO CRON MUTATION',
    ]
    yy = 1618
    for idx, line in enumerate(lines):
        d.text((145, yy), line, font=font(24, idx == 0), fill=(255, 255, 255) if idx < 2 else (255, 179, 71))
        yy += 58

    centered(d, (w // 2, 1940), 'HUMAN YES REQUIRED BEFORE ANY PUBLIC OR COMMERCIAL ACTION', font(25, True), (255, 43, 214))
    return img


def main() -> None:
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    SITE_ASSET_DIR.mkdir(parents=True, exist_ok=True)
    PAYLOAD_PATH.write_text(PAYLOAD + '\n', encoding='utf-8')
    qr_img = make_qr()
    qr_img.save(CLEAN_QR_PATH)
    card = build_card(qr_img)
    card.save(CARD_PATH)
    card.save(SITE_CARD_PATH)

    clean_decode = decode_qr(CLEAN_QR_PATH)
    card_decode = decode_qr(CARD_PATH)
    if clean_decode != PAYLOAD:
        raise SystemExit('clean QR decode did not match payload')
    if card_decode != PAYLOAD:
        raise SystemExit('card QR decode did not match payload')

    manifest = {
        'status': 'qr_proof_hub_promo_manual_scan_only_closed_until_human_yes',
        'created_by': 'scripts/build_qr_proof_hub_promo.py',
        'manual_distribution_required': True,
        'auto_post_enabled': False,
        'requires_human_approval': True,
        'human_approval_question': 'Do you approve using this exact QR proof-hub promo card in the named manual channel, with no posting/upload/payment/outreach beyond that approved channel?',
        'qr_payload_path': str(PAYLOAD_PATH.relative_to(ROOT)),
        'clean_qr_path': str(CLEAN_QR_PATH.relative_to(ROOT)),
        'archive_card_path': str(CARD_PATH.relative_to(ROOT)),
        'site_card_path': str(SITE_CARD_PATH.relative_to(ROOT)),
        'opencv_decode': {'clean_qr_matches_payload': True, 'card_matches_payload': True},
        'proof_paths': [
            str(PAYLOAD_PATH.relative_to(ROOT)),
            str(CLEAN_QR_PATH.relative_to(ROOT)),
            str(CARD_PATH.relative_to(ROOT)),
            str(SITE_CARD_PATH.relative_to(ROOT)),
            'docs/launch/QR_PROOF_HUB_PROMO_ASSET.md',
            'docs/launch/RELAUNCH_PACKAGE_DRAFT.md',
            'docs/proof/AFTERPARTY_PROOF_LEDGER.json',
            'site/index.html',
        ],
        'blocked_without_approval': [
            'posting the card publicly',
            'scheduling or starting an X/Twitter Space',
            'starting a livestream or screen recording',
            'uploading the card or any private media to YouTube/social platforms',
            'adding a checkout, payment link, invoice, or marketplace listing',
            'claiming revenue, customers, affiliation, sponsorship, or live external results',
            'sending DMs, email outreach, forms, or paid promotion',
            'starting GPU, training, model-download, paid API, or cron-mutation work',
        ],
        'risky_flags': RISKY_FLAGS,
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')
    print('QR PROOF HUB OK clean_decode=true card_decode=true')


if __name__ == '__main__':
    main()
