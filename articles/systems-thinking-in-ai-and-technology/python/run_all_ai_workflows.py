"""Run all dependency-light Python workflows for AI and technology systems."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "ai_technology_systems_model.py",
    "validation_checks.py",
    "feedback_loop_scenarios.py",
    "fairness_drift_diagnostics.py",
    "automation_burden_model.py",
    "governance_readiness_index.py",
    "technology_dependency_mapping.py",
]


def main() -> None:
    for script in SCRIPTS:
        print(f"\n=== Running {script} ===")
        subprocess.run([sys.executable, str(ROOT / "python" / script)], cwd=str(ROOT), check=True)
    print("\nAll dependency-light Python AI and technology workflows completed.")

if __name__ == "__main__":
    main()
