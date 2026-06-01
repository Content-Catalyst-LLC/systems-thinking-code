"""Run all dependency-light Python workflows for this article."""

from __future__ import annotations
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = [
    "network_dependency_cascade_model.py",
    "node_criticality_diagnostics.py",
    "bridge_node_analysis.py",
    "cascade_scenario_model.py",
    "infrastructure_interdependence_model.py",
    "dependency_matrix_export.py",
    "export_network_outputs.py",
    "validation_checks.py",
]


def main() -> None:
    for script in SCRIPTS:
        print(f"\n=== Running {script} ===")
        subprocess.run([sys.executable, str(ROOT / "python" / script)], cwd=str(ROOT), check=True)
    print("\nAll dependency-light Python network workflows completed.")


if __name__ == "__main__":
    main()
