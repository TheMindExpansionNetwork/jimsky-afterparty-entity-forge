# Entity Pipeline

1. **Identity seed** — name, role, oath, style, safety boundaries.
2. **Payload pack** — manifest, .env.example, config template, skills, operating manual, verifier.
3. **Visual seed** — 10 logo-capable images with exact captions and consistent palette.
4. **Dataset export** — HF imagefolder layout: `metadata.jsonl`, `images/`, `captions/`, manifest, README.
5. **Verifier** — opens all images, parses JSON/JSONL, checks captions and secret patterns.
6. **Autonomous loop** — finite builder/reviewer jobs improve one safe artifact per run.
7. **Human wake gate** — publish/train/outreach only after Jimsky approves.
