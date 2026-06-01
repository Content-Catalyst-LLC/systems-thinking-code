"""Analyze implementation milestones for delayed policy effects."""
from __future__ import annotations

from pathlib import Path
import csv
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
OUT = ROOT / "outputs" / "tables"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    progress = defaultdict(list)
    with (DATA / "implementation_milestones.csv").open(newline="") as f:
        for row in csv.DictReader(f):
            progress[row["policy_id"]].append(float(row["completion_ratio"]))

    with (OUT / "implementation_progress_summary.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["policy_id", "average_completion_ratio"])
        for policy_id, values in sorted(progress.items()):
            writer.writerow([policy_id, round(sum(values) / len(values), 3)])


if __name__ == "__main__":
    main()
