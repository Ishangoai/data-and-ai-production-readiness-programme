"""Copy the reference lessons without overwriting an existing student folder."""
import re
import shutil
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
if len(sys.argv) != 2 or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9-]{0,38}', sys.argv[1]):
    raise SystemExit('Usage: python scripts/new_student.py YOUR-GITHUB-USERNAME')
name = sys.argv[1]
target = root / 'src' / 'students' / name
if target.exists():
    raise SystemExit(f'{target} already exists; nothing overwritten.')
shutil.copytree(root / 'src/students/example', target,
                ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.pytest_cache'))
print(f'Created src/students/{name}. Keep this spelling and capitalization for deployment.')
