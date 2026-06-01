#!/usr/bin/env python3
"""
Run all dependency-light Python workflows for the Jay Forrester and system dynamics article.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
PYTHON_DIR = ARTICLE_ROOT / "python"

SCRIPTS = [
    "forrester_system_dynamics_model.py",
    "stock_flow_delay_scenarios.py",
    "policy_resistance_diagnostics.py",
    "feedback_loop_leverage_model.py",
    "institutional_learning_index.py",
    "sensitivity_delay_analysis.py",
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

    expected = ARTICLE_ROOT / "outputs" / "tables" / "forrester_system_dynamics_timeseries.csv"
    if not expected.exists():
        raise FileNotFoundError(f"Expected core output was not created: {expected}")

    print("\nAll dependency-light Python Forrester system dynamics workflows completed.")


if __name__ == "__main__":
    main()
