#!/usr/bin/env python3
"""
Run all dependency-light Python workflows for the Donella Meadows structural insight article.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
PYTHON_DIR = ARTICLE_ROOT / "python"

SCRIPTS = [
    "meadows_structural_insight_model.py",
    "leverage_point_diagnostics.py",
    "overshoot_delay_scenarios.py",
    "resilience_feedback_model.py",
    "paradigm_shift_sensitivity.py",
    "structural_insight_scorecard.py",
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

    expected = ARTICLE_ROOT / "outputs" / "tables" / "meadows_structural_insight_timeseries.csv"
    if not expected.exists():
        raise FileNotFoundError(f"Expected core output was not created: {expected}")

    print("\nAll dependency-light Python Meadows structural insight workflows completed.")


if __name__ == "__main__":
    main()
