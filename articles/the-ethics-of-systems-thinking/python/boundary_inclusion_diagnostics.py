#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_ROOT = Path(__file__).resolve().parents[1]
RAW = ARTICLE_ROOT / "data" / "raw"
TABLES = ARTICLE_ROOT / "outputs" / "tables"
OUT = TABLES / "boundary_inclusion_diagnostics.csv"


def main() -> None:
    path = RAW / "synthetic_boundary_cases.csv"
    if not path.exists():
        print("Skipping boundary inclusion diagnostics; missing synthetic_boundary_cases.csv")
        return

    rows = list(csv.DictReader(path.open("r", encoding="utf-8")))
    output = []

    for row in rows:
        experienced = float(row["consequences_experienced"])
        counted = float(row["consequences_counted"])
        inclusion_score = counted / experienced if experienced else 0.0
        boundary_harm = experienced - counted
        output.append({
            "case_id": row["case_id"],
            "domain": row["domain"],
            "consequences_experienced": round(experienced, 3),
            "consequences_counted": round(counted, 3),
            "boundary_inclusion_ratio": round(inclusion_score, 3),
            "boundary_harm_gap": round(boundary_harm, 3),
            "excluded_consequence": row["excluded_consequence"],
            "boundary_question": row["boundary_question"],
            "diagnostic": "major boundary ethics gap" if inclusion_score < 0.55 else "boundary review recommended",
        })

    TABLES.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(output[0].keys()))
        writer.writeheader()
        writer.writerows(output)

    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
