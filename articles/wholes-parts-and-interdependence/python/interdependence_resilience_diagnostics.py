"""
Interdependence resilience diagnostics.
"""

from __future__ import annotations

import csv
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "synthetic_indicators.csv"


def load_rows() -> list[dict[str, str]]:
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def diagnose(rows: list[dict[str, str]]) -> dict[str, float | str]:
    latest = rows[-1]
    system_capacity = float(latest["system_capacity"])
    dependency_stress = float(latest["dependency_stress"])
    resilience_buffer = float(latest["resilience_buffer"])
    coordination_quality = float(latest["coordination_quality"])

    resilience_score = (system_capacity + resilience_buffer + coordination_quality - dependency_stress) / 3

    if resilience_score >= 35:
        status = "moderate_resilience"
    elif resilience_score >= 25:
        status = "fragility_warning"
    else:
        status = "high_fragility"

    return {
        "resilience_score": round(resilience_score, 2),
        "status": status,
    }


def main() -> None:
    result = diagnose(load_rows())
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
