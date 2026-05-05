#!/usr/bin/env python3
from pathlib import Path
import os
from huggingface_hub import HfApi, create_repo, upload_folder
repo_id='TheMindExpansionNetwork/jimsky-afterparty-logo-seed'
folder=Path('/opt/data/workspace/hf-dataset-exports/jimsky-afterparty-logo-seed')
token=os.environ.get('HF_TOKEN') or os.environ.get('HUGGINGFACE_HUB_TOKEN')
if not token: raise SystemExit('HF token missing')
api=HfApi(token=token); who=api.whoami(token=token)
create_repo(repo_id=repo_id, repo_type='dataset', private=True, exist_ok=True, token=token)
upload_folder(repo_id=repo_id, repo_type='dataset', folder_path=str(folder), path_in_repo='.', commit_message='Upload Afterparty Forge logo seed dataset', token=token)
info=api.dataset_info(repo_id, token=token, files_metadata=True)
print('HF_UPLOAD_OK', repo_id, 'private', getattr(info,'private','unknown'), 'files', len(info.siblings or []))
