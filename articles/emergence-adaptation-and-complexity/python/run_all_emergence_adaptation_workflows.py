#!/usr/bin/env python3
"""Run dependency-light emergence/adaptation/complexity workflows from the article root.

This runner intentionally sets cwd to the article directory before launching scripts,
so relative output paths such as outputs/tables resolve inside the article folder.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
PYTHON_DIR = ARTICLE_ROOT / "python"
TABLES_DIR = ARTICLE_ROOT / "outputs" / "tables"

SCRIPTS = [
    "emergence_adaptation_complexity_model.py",
    "validation_checks.py",
    "adaptive_agent_scenarios.py",
    "shock_response_model.py",
]

REQUIRED_OUTPUTS = [
    TABLES_DIR / "emergence_adaptation_complexity_timeseries.csv",
    TABLES_DIR / "emergence_adaptation_complexity_summary.csv",
]


def run_script(script_name: str) -> None:
    script_path = PYTHON_DIR / script_name
    if not script_path.exists():
        print(f"Skipping missing optional script: {script_name}")
        return

    print(f"\n=== Running {script_name} ===")
    subprocess.run([sys.executable, str(script_path)], cwd=str(ARTICLE_ROOT), check=True)


def main() -> None:
    TABLES_DIR.mkdir(parents=True, exist_ok=True)

    for script_name in SCRIPTS:
        run_script(script_name)

    missing = [str(path) for path in REQUIRED_OUTPUTS if not path.exists()]
    if missing:
        raise SystemExit("Missing required output(s) after Python workflows:\n" + "\n".join(missing))

    print("\nAll dependency-light Python complexity workflows completed from the article root.")


if __name__ == "__main__":
    main()
