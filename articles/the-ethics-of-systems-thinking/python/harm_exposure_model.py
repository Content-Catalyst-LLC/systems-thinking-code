#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "harm_exposure_diagnostics.csv"


def main() -> None:
    path = RAW / "synthetic_harm_exposure.csv"
    if not path.exists():
        print("Skipping harm exposure diagnostics; missing synthetic_harm_exposure.csv")
        return

    rows = list(csv.DictReader(path.open("r", encoding="utf-8")))
    output = []

    for row in rows:
        exposure = float(row["exposure_score"])
        protection = float(row["protection_score"])
        burden = float(row["cumulative_burden"])
        harm_gap = exposure - protection
        priority = "urgent harm-reduction priority" if harm_gap >= 40 or burden >= 70 else "monitor and redesign"
        output.append({
            "group_id": row["group_id"],
            "group_name": row["group_name"],
            "exposure_score": round(exposure, 3),
            "protection_score": round(protection, 3),
            "harm_exposure_gap": round(harm_gap, 3),
            "cumulative_burden": round(burden, 3),
            "diagnostic": priority,
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
