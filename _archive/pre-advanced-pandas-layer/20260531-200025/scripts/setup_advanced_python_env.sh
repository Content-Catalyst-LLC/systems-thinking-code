#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

PYTHON_BIN="${PYTHON_BIN:-}"
if [ -z "$PYTHON_BIN" ]; then
  if command -v python3 >/dev/null 2>&1; then
    PYTHON_BIN="$(command -v python3)"
  elif command -v python >/dev/null 2>&1; then
    PYTHON_BIN="$(command -v python)"
  else
    echo "Error: Python is required but was not found." >&2
    exit 1
  fi
fi

echo "Creating/updating advanced Python virtual environment at: $ROOT/.venv"
"$PYTHON_BIN" -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements-advanced.txt

python - <<'PY'
import pandas as pd
import matplotlib
print("Advanced Python environment ready")
print("pandas:", pd.__version__)
print("matplotlib:", matplotlib.__version__)
PY
