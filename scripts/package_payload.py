#!/usr/bin/env python3
from pathlib import Path
import zipfile
root=Path(__file__).resolve().parents[1]
dist=root/'dist'; dist.mkdir(exist_ok=True)
out=dist/'afterparty-forge-payload.zip'
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
    for p in (root/'payloads/afterparty-forge').rglob('*'):
        if p.is_file(): z.write(p, p.relative_to(root))
    for p in (root/'datasets/logo-seed').rglob('*'):
        if p.is_file(): z.write(p, p.relative_to(root))
print('PACKAGE_OK', out)
