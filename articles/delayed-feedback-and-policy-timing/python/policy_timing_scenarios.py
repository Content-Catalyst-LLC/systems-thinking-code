"""Compare policy-timing scenarios using synthetic outcome trajectories."""
from __future__ import annotations

from pathlib import Path
import csv
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
OUT = ROOT / "outputs" / "tables"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    final_rows = {}
    with (DATA / "outcomes.csv").open(newline="") as f:
        for row in csv.DictReader(f):
            final_rows[row["scenario_id"]] = row

    with (OUT / "final_scenario_comparison.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["scenario_id", "month", "outcome_score", "accumulated_harm", "public_trust", "cost_index"])
        for scenario_id, row in sorted(final_rows.items()):
            writer.writerow([scenario_id, row["month"], row["outcome_score"], row["accumulated_harm"], row["public_trust"], row["cost_index"]])


if __name__ == "__main__":
    main()
