"""Create compact scenario-level cascade metrics from the main cascade timeseries."""

from __future__ import annotations
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"


def main() -> None:
    source = TABLES / "network_cascade_timeseries.csv"
    if not source.exists():
        raise FileNotFoundError(f"Missing {source}. Run network_dependency_cascade_model.py first.")

    with source.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    output = []
    for scenario in sorted(set(row["scenario"] for row in rows)):
        subset = [row for row in rows if row["scenario"] == scenario]
        final = subset[-1]
        output.append({
            "scenario": scenario,
            "initial_failures": final["initial_failures"],
            "cascade_depth": int(final["step"]),
            "final_failed_count": int(final["failed_count"]),
            "final_service_loss_index": float(final["service_loss_index"]),
            "requires_executive_review": int(final["failed_count"]) >= 4,
        })

    path = TABLES / "cascade_scenario_review.csv"
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
