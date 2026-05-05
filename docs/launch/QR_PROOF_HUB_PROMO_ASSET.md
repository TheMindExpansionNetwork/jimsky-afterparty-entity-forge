# QR Proof-Hub Promo Asset

**Status:** `qr_proof_hub_promo_manual_scan_only_closed_until_human_yes`

This is a review-only Afterparty Forge 2045 launch-art card with a programmatically generated QR code. The QR payload points to repo-local proof paths and the aggregate verifier command; it is not a public link, checkout, outreach mechanism, upload, or livestream trigger.

## Generated files

- Payload text: `assets/launch/qr-proof-hub/afterparty-forge-proof-hub-payload.txt`
- Clean QR backup: `assets/launch/qr-proof-hub/afterparty-forge-proof-hub-clean-qr.png`
- Archive card: `assets/launch/qr-proof-hub/afterparty-forge-proof-hub-card.png`
- Site card copy: `site/assets/img/launch/afterparty-forge-proof-hub-card.png`
- Manifest: `site/data/qr-proof-hub-promo.json`
- Builder: `scripts/build_qr_proof_hub_promo.py`

## Operator use

1. From the repo root, rebuild and verify the asset locally:

   ```bash
   PYTHONDONTWRITEBYTECODE=1 python3 scripts/build_qr_proof_hub_promo.py
   PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_site.py
   git diff --check
   ```

2. Open `site/index.html` and inspect the `qr-proof-hub-promo` card.
3. Scan the card with a phone or QR scanner. Expected payload highlights:
   - `AFTERPARTY FORGE 2045 PROOF HUB`
   - `LOCAL: site/index.html`
   - `DOC: docs/launch/RELAUNCH_PACKAGE_DRAFT.md`
   - `VERIFY: PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_site.py`
   - `CLOSED UNTIL HUMAN YES`

## Human approval question

Do you approve using this exact QR proof-hub promo card in the named manual channel, with no posting/upload/payment/outreach beyond that approved channel?

If the channel, expiration, or audience is blank, keep the card private/local only.

## Blocked without approval

- Posting the card publicly or scheduling social posts.
- Starting an X/Twitter Space, livestream, screen recording, or YouTube upload.
- Adding checkout links, payment links, invoice actions, marketplace listings, or paid promotion.
- Sending DMs, email outreach, forms, or lead-gen campaigns.
- Claiming revenue, customers, OpenAI affiliation, sponsorship, live public launch, or verified remote results.
- Starting GPU, training, model downloads, paid APIs, uploads of private media, or cron mutation.

## Safety flags

```text
public_posting=false
outreach=false
paid_promotion=false
payment_links=false
claim_revenue=false
claim_affiliation=false
youtube_upload=false
publishes_stream=false
records_audio=false
uploads_private_media=false
starts_gpu=false
starts_paid_api=false
downloads_models=false
starts_training=false
submits_hackathon=false
mutates_cron=false
requires_human_approval=true
```

## Verification notes

The builder uses Python `qrcode` with high error correction and OpenCV `QRCodeDetector` to assert exact payload equality for both the clean QR and the final promo card. The aggregate verifier also parses `site/data/qr-proof-hub-promo.json`, checks every proof path exists, confirms decode booleans are true, requires the static-site card, and rejects any risky flag that is not explicitly `false`.
