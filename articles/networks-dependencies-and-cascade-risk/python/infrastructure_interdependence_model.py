"""Summarize dependency exposure by category for infrastructure resilience review."""

from __future__ import annotations
import csv
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"


def main() -> None:
    source = TABLES / "network_node_criticality.csv"
    if not source.exists():
        raise FileNotFoundError(f"Missing {source}. Run network_dependency_cascade_model.py first.")

    with source.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    output = []
    for category in sorted(set(row["category"] for row in rows)):
        subset = [row for row in rows if row["category"] == category]
        output.append({
            "category": category,
            "node_count": len(subset),
            "average_criticality_index": round(mean(float(row["criticality_index"]) for row in subset), 4),
            "average_dependency_exposure_score": round(mean(float(row["dependency_exposure_score"]) for row in subset), 4),
            "average_recovery_capacity": round(mean(float(row["recovery_capacity"]) for row in subset), 4),
        })

    path = TABLES / "infrastructure_interdependence_category_summary.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
