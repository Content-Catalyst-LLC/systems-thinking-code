"""Summarize bridge-like nodes and dependency exposure for governance review."""

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

    bridge_threshold = mean(float(row["bridge_approximation_score"]) for row in rows)
    exposure_threshold = mean(float(row["dependency_exposure_score"]) for row in rows)

    output = []
    for row in rows:
        bridge_score = float(row["bridge_approximation_score"])
        exposure_score = float(row["dependency_exposure_score"])
        output.append({
            "node_id": row["node_id"],
            "category": row["category"],
            "bridge_approximation_score": round(bridge_score, 4),
            "dependency_exposure_score": round(exposure_score, 4),
            "bridge_flag": bridge_score >= bridge_threshold,
            "exposure_flag": exposure_score >= exposure_threshold,
            "diagnostic": (
                "bridge and exposure priority" if bridge_score >= bridge_threshold and exposure_score >= exposure_threshold else
                "bridge priority" if bridge_score >= bridge_threshold else
                "dependency exposure priority" if exposure_score >= exposure_threshold else
                "routine monitoring"
            ),
        })

    path = TABLES / "bridge_node_dependency_diagnostics.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
