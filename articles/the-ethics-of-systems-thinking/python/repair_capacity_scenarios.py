#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "repair_capacity_scenarios.csv"


def main() -> None:
    path = RAW / "synthetic_repair_actions.csv"
    if not path.exists():
        print("Skipping repair capacity scenarios; missing synthetic_repair_actions.csv")
        return

    rows = list(csv.DictReader(path.open("r", encoding="utf-8")))
    output = []

    for row in rows:
        repair_depth = float(row["repair_depth"])
        voice = float(row["affected_voice_required"])
        structure = float(row["structural_change_required"])
        repair_quality = (repair_depth * 0.40 + voice * 0.25 + structure * 0.35) * 100.0
        output.append({
            "repair_id": row["repair_id"],
            "repair_type": row["repair_type"],
            "repair_quality_score": round(repair_quality, 3),
            "affected_voice_required": round(voice, 3),
            "structural_change_required": round(structure, 3),
            "diagnostic": "transformative repair" if repair_quality >= 75 else "partial repair",
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
