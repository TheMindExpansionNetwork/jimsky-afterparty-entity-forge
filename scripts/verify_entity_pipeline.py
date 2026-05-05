#!/usr/bin/env python3
from pathlib import Path
from PIL import Image
import json, re, sys
root=Path(__file__).resolve().parents[1]
required=['README.md','automation/SAFETY_BOUNDARIES.md','docs/entity/IDENTITY.md','docs/pipeline/ENTITY_PIPELINE.md','payloads/afterparty-forge/manifest.json','datasets/logo-seed/metadata.jsonl','site/index.html','docs/index.html','docs/tools/AFTERPARTY_FORGE_TOOL_SUITE.md','docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json','tools/entity-tool-suite.json']
missing=[p for p in required if not (root/p).exists()]
if missing: raise SystemExit('missing '+str(missing))
json.loads((root/'payloads/afterparty-forge/manifest.json').read_text())
rm=json.loads((root/'docs/revenue/FIRST_DOLLAR_REVENUE_PATH.json').read_text())
assert rm.get('approved_to_execute') is False
assert rm.get('closed_gates',{}).get('payment_links') is False
assert rm.get('closed_gates',{}).get('outreach') is False
tm=json.loads((root/'tools/entity-tool-suite.json').read_text())
assert len(tm.get('tools',[])) >= 6
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
