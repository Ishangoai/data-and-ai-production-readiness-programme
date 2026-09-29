"""Resolve an explicitly selected folder; no credentials or cloud calls."""
import json
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
cfg = json.loads((root / 'course.json').read_text())
name = sys.argv[1]
if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9-]{0,38}', name):
    raise SystemExit('Invalid GitHub username')
folder = 'example' if name in cfg['instructors'] or name == 'example' else name
if not (root / 'src/students' / folder / 'api/main.py').is_file():
    raise SystemExit(f'No API found in src/students/{folder}; create the student folder first.')
service = cfg['service_prefix'] + '-' + folder.lower()
if len(service) > 49:
    raise SystemExit('Service name too long: shorten service_prefix in course.json.')
print(f'folder={folder}')
print(f'service={service}')
print(f'target={"ROOT" if folder == "example" else "STUDENT"}')
for key in ['project_id', 'region', 'registry', 'deployment_service_account',
            'runtime_service_account', 'workload_identity_provider']:
    print(f'{key}={cfg[key]}')
