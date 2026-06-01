"""
Resilience diagnostics using synthetic indicator data.
"""

from __future__ import annotations

import csv
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "synthetic_indicators.csv"


def load_rows() -> list[dict[str, str]]:
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def diagnose(rows: list[dict[str, str]]) -> dict[str, float | str]:
    first = rows[0]
    last = rows[-1]

    trust_change = float(last["public_trust"]) - float(first["public_trust"])
    capacity_change = float(last["institutional_capacity"]) - float(first["institutional_capacity"])
    backlog_change = float(last["maintenance_backlog"]) - float(first["maintenance_backlog"])
    resilience_change = float(last["resilience_buffer"]) - float(first["resilience_buffer"])

    if trust_change < -5 and backlog_change > 25 and resilience_change < -8:
        status = "fragility_rising"
    elif capacity_change > 0 and resilience_change > 0:
        status = "resilience_improving"
    else:
        status = "mixed_signal"

    return {
        "trust_change": trust_change,
        "capacity_change": capacity_change,
        "backlog_change": backlog_change,
        "resilience_change": resilience_change,
        "system_status": status,
    }


def main() -> None:
    result = diagnose(load_rows())
    for key, value in result.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
