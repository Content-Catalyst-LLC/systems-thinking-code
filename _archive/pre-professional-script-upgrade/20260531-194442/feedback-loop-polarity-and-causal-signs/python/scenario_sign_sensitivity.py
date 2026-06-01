#!/usr/bin/env python3
"""Document scenario assumptions for causal-sign sensitivity review."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCENARIOS = ROOT / "data" / "synthetic_scenarios.csv"


def main() -> None:
    with SCENARIOS.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            print(f"{row['scenario_id']}: {row['scenario_name']}")
            print(f"  {row['description']}")
            print(f"  Changed assumption: {row['changed_assumption']}")


if __name__ == "__main__":
    main()
