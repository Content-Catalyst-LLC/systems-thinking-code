"""
Stakeholder inclusion diagnostics using synthetic stakeholder data.
"""

from __future__ import annotations

import csv
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "synthetic_stakeholders.csv"


def load_rows() -> list[dict[str, str]]:
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def inclusion_ratio(rows: list[dict[str, str]]) -> float:
    affected = [row for row in rows if row["affected"] == "yes"]
    included = [row for row in affected if row["included"] in {"yes", "partial"}]
    return len(included) / len(affected) if affected else 0.0


def average_burden_excluded(rows: list[dict[str, str]]) -> float:
    excluded = [row for row in rows if row["affected"] == "yes" and row["included"] == "no"]
    if not excluded:
        return 0.0
    return sum(float(row["burden_score"]) for row in excluded) / len(excluded)


def main() -> None:
    rows = load_rows()
    print(f"stakeholder_inclusion_ratio: {round(inclusion_ratio(rows), 3)}")
    print(f"average_burden_score_for_excluded_affected_stakeholders: {round(average_burden_excluded(rows), 2)}")


if __name__ == "__main__":
    main()
