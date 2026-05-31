"""
Resilience diagnostics for repeated events and structural risk.
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

    event_frequency_change = float(last["event_frequency"]) - float(first["event_frequency"])
    trust_change = float(last["public_trust"]) - float(first["public_trust"])
    capacity_change = float(last["institutional_capacity"]) - float(first["institutional_capacity"])
    risk_change = float(last["structural_risk"]) - float(first["structural_risk"])
    resilience_change = float(last["resilience_buffer"]) - float(first["resilience_buffer"])

    if risk_change > 15 and resilience_change < -10:
        status = "structural_fragility_rising"
    elif capacity_change > 0 and trust_change >= 0:
        status = "adaptive_capacity_improving"
    else:
        status = "mixed_pattern_requires_review"

    return {
        "event_frequency_change": event_frequency_change,
        "trust_change": trust_change,
        "capacity_change": capacity_change,
        "risk_change": risk_change,
        "resilience_change": resilience_change,
        "diagnostic_status": status,
    }


def main() -> None:
    for key, value in diagnose(load_rows()).items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
