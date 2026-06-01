#!/usr/bin/env python3
"""
Run all dependency-light Python workflows for The Ethics of Systems Thinking article.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
PYTHON_DIR = ARTICLE_ROOT / "python"

SCRIPTS = [
    "ethical_systems_thinking_model.py",
    "boundary_inclusion_diagnostics.py",
    "accountability_scorecard.py",
    "harm_exposure_model.py",
    "repair_capacity_scenarios.py",
    "model_risk_sensitivity.py",
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

    expected = ARTICLE_ROOT / "outputs" / "tables" / "ethical_systems_thinking_timeseries.csv"
    if not expected.exists():
        raise FileNotFoundError(f"Expected core output was not created: {expected}")

    print("\nAll dependency-light Python ethical systems workflows completed.")


if __name__ == "__main__":
    main()
