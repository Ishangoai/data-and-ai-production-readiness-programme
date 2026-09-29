#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
student="${1:-example}"
if [[ ! "$student" =~ ^[A-Za-z0-9][A-Za-z0-9-]*$ ]] || [[ ! -f "src/students/$student/dagster/definitions.py" ]]; then
  echo "Usage: bash run_dagster.sh [example|GitHub-username]" >&2; exit 1
fi
uv run --locked mlflow ui --backend-store-uri sqlite:///mlflow_local_tracking.db &
MLFLOW_PID=$!
trap 'kill "$MLFLOW_PID" 2>/dev/null || true' EXIT
uv run --locked dagster dev -m "src.students.$student.dagster.definitions"
