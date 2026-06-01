"""Rank network nodes by criticality and export a compact diagnostic table."""

from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"


def main() -> None:
    source = TABLES / "network_node_criticality.csv"
    if not source.exists():
        raise FileNotFoundError(f"Missing {source}. Run network_dependency_cascade_model.py first.")

    with source.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    ranked = sorted(rows, key=lambda r: float(r["criticality_index"]), reverse=True)
    output = []
    for rank, row in enumerate(ranked, start=1):
        output.append({
            "rank": rank,
            "node_id": row["node_id"],
            "category": row["category"],
            "criticality_index": row["criticality_index"],
            "degree_score": row["degree_score"],
            "dependency_exposure_score": row["dependency_exposure_score"],
            "bridge_approximation_score": row["bridge_approximation_score"],
            "priority": "critical review" if rank <= 5 else "monitor",
        })

    path = TABLES / "network_node_criticality_ranked.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
