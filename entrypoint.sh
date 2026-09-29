#!/usr/bin/env bash
set -euo pipefail
cd /app
student="${GITHUB_USER:-example}"
if [[ "${DEPLOYMENT_TARGET:-ROOT}" != "STUDENT" ]]; then student=example; fi
if [[ ! "$student" =~ ^[A-Za-z0-9][A-Za-z0-9-]*$ ]] || [[ ! -f "src/students/$student/api/main.py" ]]; then
  echo "No API folder for selected student: $student" >&2
  exit 1
fi
export PYTHONPATH="/app/src/students/$student${PYTHONPATH:+:$PYTHONPATH}"
exec /app/.venv/bin/python -m uvicorn api.main:app --host 0.0.0.0 --port "${PORT:-8080}"
