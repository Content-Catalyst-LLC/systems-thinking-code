#!/usr/bin/env python3
"""Create distributional burden outputs for article demonstration."""

from __future__ import annotations

from pathlib import Path
import csv

ARTICLE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ARTICLE_DIR / "outputs" / "tables" / "distributional_burden_outputs.csv"


def main() -> None:
    groups = {
        "applicants": [40, 45, 51, 58, 63, 60, 55],
        "caseworkers": [35, 39, 43, 49, 54, 52, 48],
        "community_orgs": [32, 36, 41, 47, 53, 50, 45],
    }

    rows = []
    for group, values in groups.items():
        rows.append(
            {
                "group": group,
                "initial_burden": values[0],
                "peak_burden": max(values),
                "final_burden": values[-1],
                "peak_minus_initial": max(values) - values[0],
            }
        )

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
