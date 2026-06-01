#!/usr/bin/env python3
"""
Run all dependency-light Python workflows for Systems Thinking in an Age of Complexity.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
PYTHON_DIR = ARTICLE_ROOT / "python"

SCRIPTS = [
    "systems_thinking_age_complexity_model.py",
    "complexity_pressure_diagnostics.py",
    "resilience_capacity_scorecard.py",
    "feedback_amplification_model.py",
    "accountability_and_boundary_diagnostics.py",
    "transformation_leverage_scenarios.py",
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

    expected = ARTICLE_ROOT / "outputs" / "tables" / "systems_thinking_age_complexity_timeseries.csv"
    if not expected.exists():
        raise FileNotFoundError(f"Expected core output was not created: {expected}")

    print("\nAll dependency-light Python age-of-complexity workflows completed.")


if __name__ == "__main__":
    main()
