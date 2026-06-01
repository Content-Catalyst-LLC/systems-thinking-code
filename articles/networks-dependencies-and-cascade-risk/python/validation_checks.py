"""Validate required network cascade outputs."""

from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"

REQUIRED = [
    "network_node_criticality.csv",
    "network_dependencies.csv",
    "network_cascade_timeseries.csv",
    "network_cascade_summary.csv",
    "network_node_criticality_ranked.csv",
    "bridge_node_dependency_diagnostics.csv",
    "cascade_scenario_review.csv",
    "infrastructure_interdependence_category_summary.csv",
    "network_dependency_matrix.csv",
    "network_risk_executive_summary.txt",
]


def count_csv_rows(path: Path) -> int:
    with path.open(newline="", encoding="utf-8") as handle:
        return max(0, sum(1 for _ in csv.DictReader(handle)))


def main() -> None:
    missing = [name for name in REQUIRED if not (TABLES / name).exists()]
    if missing:
        raise FileNotFoundError("Missing required outputs: " + ", ".join(missing))

    for name in REQUIRED:
        path = TABLES / name
        if name.endswith(".csv") and count_csv_rows(path) == 0:
            raise ValueError(f"{name} has no data rows.")

    report = TABLES / "final_validation_report.txt"
    report.write_text(
        "Validation passed.\nAll required network dependency and cascade-risk outputs are present and non-empty.\n",
        encoding="utf-8",
    )
    print("Validation passed.")


if __name__ == "__main__":
    main()
