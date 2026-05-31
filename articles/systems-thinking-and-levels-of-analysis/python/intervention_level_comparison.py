"""Compare intervention scenarios at different levels of analysis."""

from __future__ import annotations

import csv
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data" / "synthetic_scenarios.csv"


def score_scenario(row: dict[str, str]) -> float:
    individual = float(row["individual_support"])
    organization = float(row["organizational_capacity"])
    institution = float(row["institutional_reform"])
    network = float(row["network_redundancy"])
    ecological_stress = float(row["ecological_stress"])
    return round((individual + organization + institution + network) / ecological_stress, 3)


def main() -> None:
    with DATA.open(newline="", encoding="utf-8") as handle:
        print("scenario_id,scenario_name,cross_scale_score")
        for row in csv.DictReader(handle):
            print(f"{row['scenario_id']},{row['scenario_name']},{score_scenario(row)}")


if __name__ == "__main__":
    main()
