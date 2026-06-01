#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "institutional_memory_diagnostics.csv"


def main() -> None:
    path = RAW / "synthetic_institutional_memory.csv"
    if not path.exists():
        print("Skipping institutional memory diagnostics; missing synthetic_institutional_memory.csv")
        return

    rows = list(csv.DictReader(path.open("r", encoding="utf-8")))
    output = []

    for row in rows:
        baseline = float(row["baseline_quality"])
        target = float(row["target_quality"])
        gap = target - baseline
        output.append({
            "memory_id": row["memory_id"],
            "memory_asset": row["memory_asset"],
            "baseline_quality": round(baseline, 3),
            "target_quality": round(target, 3),
            "memory_gap": round(gap, 3),
            "loss_risk": row["loss_risk"],
            "priority_class": "high priority" if gap >= 38 or row["loss_risk"] == "high" else "moderate priority",
            "notes": row["notes"],
        })

    TABLES.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
