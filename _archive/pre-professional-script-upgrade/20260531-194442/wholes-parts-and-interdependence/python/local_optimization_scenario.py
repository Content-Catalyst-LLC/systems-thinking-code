"""
Local optimization scenario.

Demonstrates how local performance can rise while whole-system outcomes fall.
"""

from __future__ import annotations

import csv
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "synthetic_indicators.csv"


def load_rows() -> list[dict[str, str]]:
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def analyze(rows: list[dict[str, str]]) -> dict[str, float | str]:
    first = rows[0]
    last = rows[-1]
    local_change = float(last["local_performance"]) - float(first["local_performance"])
    whole_change = float(last["whole_system_outcome"]) - float(first["whole_system_outcome"])

    if local_change > 0 and whole_change < 0:
        diagnosis = "local_optimization_system_decline"
    elif local_change > 0 and whole_change > 0:
        diagnosis = "aligned_improvement"
    else:
        diagnosis = "mixed_or_declining"

    return {
        "local_performance_change": round(local_change, 2),
        "whole_system_outcome_change": round(whole_change, 2),
        "diagnosis": diagnosis,
    }


def main() -> None:
    result = analyze(load_rows())
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
