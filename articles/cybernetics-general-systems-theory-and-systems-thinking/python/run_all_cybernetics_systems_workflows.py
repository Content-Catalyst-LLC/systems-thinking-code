#!/usr/bin/env python3
"""
Run all dependency-light Python workflows for the cybernetics and general systems article.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
PYTHON_DIR = ARTICLE_ROOT / "python"

SCRIPTS = [
    "cybernetics_systems_model.py",
    "requisite_variety_diagnostics.py",
    "feedback_delay_model.py",
    "open_system_exchange_model.py",
    "adaptive_regulation_scorecard.py",
    "accountability_sensitivity.py",
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

    expected = ARTICLE_ROOT / "outputs" / "tables" / "cybernetics_systems_timeseries.csv"
    if not expected.exists():
        raise FileNotFoundError(f"Expected core output was not created: {expected}")

    print("\nAll dependency-light Python cybernetics and systems workflows completed.")


if __name__ == "__main__":
    main()
