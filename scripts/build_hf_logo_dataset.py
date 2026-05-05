#!/usr/bin/env python3
from pathlib import Path
import shutil, json
SRC=Path(__file__).resolve().parents[1]/'datasets/logo-seed'
OUT=Path('/opt/data/workspace/hf-dataset-exports/jimsky-afterparty-logo-seed')
if OUT.exists(): shutil.rmtree(OUT)
(OUT/'images').mkdir(parents=True)
(OUT/'captions').mkdir()
for p in (SRC/'images').glob('*.png'): shutil.copy2(p, OUT/'images'/p.name)
for p in (SRC/'captions').glob('*.txt'): shutil.copy2(p, OUT/'captions'/p.name)
for name in ['metadata.jsonl','metadata.full.jsonl','dataset_manifest.json','README.md']:
    shutil.copy2(SRC/name, OUT/name)
print('HF_EXPORT_READY', OUT)
