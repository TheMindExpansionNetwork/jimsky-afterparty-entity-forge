# Afterparty Forge 2045 — Captions & Transcript Pack

Status: `caption_transcript_pack_ready_manual_upload_only`

This pack is a review-only accessibility layer for a future faceless/manual-upload release video. It does **not** upload, publish, schedule, promote, record, or claim revenue. An awake operator must approve the exact final video file, title, description, captions, and destination before any public action.

## Target video

- Working title: **Afterparty Forge 2045: Human-Gated Relaunch Proof**
- Target path when rendered later: `dist/video/afterparty-forge-2045-release-720p.mp4`
- Current state: caption and transcript draft only; no upload action is enabled.
- Caption files:
  - `docs/youtube/captions/afterparty-forge-2045-release_en.vtt`
  - `docs/youtube/captions/afterparty-forge-2045-release_en.srt`
- Parseable manifest: `site/data/youtube-captions-pack.json`

## Human approval question

Do you approve using these exact captions/transcript with the final reviewed video file, and do you approve a human-only manual upload after checking the title, description, proof links, and safety copy?

If the answer is not an explicit awake **yes**, keep the video, captions, public posting, paid promotion, outreach, revenue claims, and affiliation claims closed.

## 60-second transcript draft

Afterparty Forge 2045 is a closed-gate relaunch forge for turning a failed launch into proof, assets, and a safer next move.

The repo already holds the core proof: a local entity package, logo seed dataset, tool contracts, launch draft, manual X thread drafts, and verifiers that keep money actions closed until human approval.

This is not a public launch claim. It is a private review surface: captions, transcript, chapter copy, and proof paths prepared so an awake operator can decide what, if anything, gets published.

Every risky lane stays off by default: no GPU run, no training, no paid API, no livestream, no upload of private media, no checkout link, no outreach, and no revenue claim.

The next human step is simple: run the verifier, open the proof page, review the captions against the final video, and approve or reject the upload manually.

## Chapters / description block

```text
00:00 Failed launch remix
00:08 Repo proof inventory
00:18 Manual-only release surface
00:30 Closed gates and non-claims
00:44 Operator review path
00:54 Human approval checkpoint
```

## Shorts hook drafts

1. "Failed launch? Don't fake traction. Package proof, keep gates closed, and let a human approve the next move."
2. "Afterparty Forge 2045 turns chaos into a reviewable release kit — captions included, upload disabled."
3. "The safest launch artifact is the one that proves what exists and refuses to pretend the rest happened."

## Manual upload checklist

Run these commands before any human-upload workflow:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_site.py
PYTHONDONTWRITEBYTECODE=1 python3 scripts/verify_entity_pipeline.py
git diff --check
git status --short --branch
```

Expected highlights:

- `VERIFY OK site relaunch surfaces closed-gate links/json/entity`
- `VERIFY OK afterparty entity pipeline images=10`
- no dirty tracked generated frame caches
- no secret-like token values in the changed caption/doc/manifest files

## Blocked without approval

- YouTube upload, caption upload, scheduling, or public posting
- X/Twitter posting, replies, DMs, paid boost, or Spaces/livestream start
- checkout/payment links, invoices, revenue claims, customer claims, affiliation claims
- GPU, training, model downloads, private-media upload, recording, or paid API calls
- cron mutation or any recursive autonomous scheduling

## Proof paths for reviewer

- `site/index.html`
- `docs/index.html`
- `docs/launch/RELAUNCH_PACKAGE_DRAFT.md`
- `docs/social/X_THREAD_DRAFTS.md`
- `docs/tools/AFTERPARTY_FORGE_TOOL_SUITE.md`
- `site/data/youtube-captions-pack.json`

## Safety copy for the final description

Manual upload only. No public posting, outreach, paid promotion, live stream, checkout link, revenue claim, OpenAI affiliation claim, GPU/training action, or private-media upload is approved by this repository. This video should be treated as a proof-of-work preview until an awake operator reviews and approves the exact release text and media.
