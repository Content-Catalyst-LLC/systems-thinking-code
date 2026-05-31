"""
Externality accounting example.

True cost = internal cost + external cost - external benefit
"""

from __future__ import annotations

import csv
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "synthetic_externalities.csv"


def main() -> None:
    print("externality_id,boundary_id,cost_category,true_cost")
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            true_cost = (
                float(row["internal_cost"])
                + float(row["external_cost"])
                - float(row["external_benefit"])
            )
            print(f"{row['externality_id']},{row['boundary_id']},{row['cost_category']},{round(true_cost, 2)}")


if __name__ == "__main__":
    main()
