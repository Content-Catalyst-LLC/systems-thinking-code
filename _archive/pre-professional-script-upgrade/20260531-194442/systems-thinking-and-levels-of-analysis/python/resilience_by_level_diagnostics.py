"""Diagnose resilience signals across multiple levels of a synthetic system."""

from __future__ import annotations

import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "synthetic_indicators.csv"


def load_rows() -> list[dict[str, float]]:
    with DATA.open(newline="", encoding="utf-8") as handle:
        return [{key: float(value) for key, value in row.items()} for row in csv.DictReader(handle)]


def main() -> None:
    rows = load_rows()
    first, last = rows[0], rows[-1]
    changes = {
        "individual_burden_change": last["individual_burden"] - first["individual_burden"],
        "organizational_capacity_change": last["organizational_capacity"] - first["organizational_capacity"],
        "institutional_trust_change": last["institutional_trust"] - first["institutional_trust"],
        "network_redundancy_change": last["network_redundancy"] - first["network_redundancy"],
        "system_resilience_change": last["system_resilience"] - first["system_resilience"],
    }
    for key, value in changes.items():
        print(f"{key},{value:.2f}")


if __name__ == "__main__":
    main()
