#!/usr/bin/env python3
"""
Run all dependency-light Python workflows for the Complex Adaptive Systems and Social Change article.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
PYTHON_DIR = ARTICLE_ROOT / "python"

SCRIPTS = [
    "complex_adaptive_social_change_model.py",
    "social_diffusion_threshold_scenarios.py",
    "coalition_learning_diagnostics.py",
    "backlash_resistance_model.py",
    "governance_learning_index.py",
    "transformation_momentum_score.py",
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

    expected = ARTICLE_ROOT / "outputs" / "tables" / "complex_adaptive_social_change_timeseries.csv"
    if not expected.exists():
        raise FileNotFoundError(f"Expected core output was not created: {expected}")

    print("\nAll dependency-light Python complex adaptive social change workflows completed.")


if __name__ == "__main__":
    main()
