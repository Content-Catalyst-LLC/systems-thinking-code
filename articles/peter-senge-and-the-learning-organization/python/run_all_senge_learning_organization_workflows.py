#!/usr/bin/env python3
"""
Run all dependency-light Python workflows for the Peter Senge learning organization article.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
PYTHON_DIR = ARTICLE_ROOT / "python"

SCRIPTS = [
    "senge_learning_organization_model.py",
    "five_disciplines_diagnostics.py",
    "defensive_routines_model.py",
    "institutional_memory_model.py",
    "team_learning_scorecard.py",
    "learning_capacity_sensitivity.py",
    "validation_checks.py",
]


def main() -> None:
    for script in SCRIPTS:
        script_path = PYTHON_DIR / script
        if not script_path.exists():
            print(f"Skipping missing optional workflow: {script}")
            continue
        print(f"\n=== Running {script} ===")
        subprocess.run([sys.executable, str(script_path)], cwd=str(ARTICLE_ROOT), check=True)

    expected = ARTICLE_ROOT / "outputs" / "tables" / "senge_learning_organization_timeseries.csv"
    if not expected.exists():
        raise FileNotFoundError(f"Expected core output was not created: {expected}")

    print("\nAll dependency-light Python Senge learning organization workflows completed.")


if __name__ == "__main__":
    main()
