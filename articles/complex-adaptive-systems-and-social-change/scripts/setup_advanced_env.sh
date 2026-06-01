#!/usr/bin/env bash
set -Eeuo pipefail

ARTICLE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ARTICLE_DIR"

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-advanced.txt

echo "Advanced environment ready."
echo "Run: source .venv/bin/activate"
