"""Administrative burden diagnostics using synthetic indicator weights."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "synthetic_burden_indicators.csv"
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

WEIGHTS = {
    "forms_required": 1.4,
    "documentation_requests": 1.6,
    "average_wait_days": 0.25,
    "portal_failures_per_100_users": 0.7,
    "appeal_steps": 1.8,
    "caseworker_access": -0.12,
    "language_access": -0.10,
    "discouraged_applicants": 0.18,
}


def main() -> None:
    score = 0.0
    components = []
    with DATA.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["indicator_name"]
            value = float(row["baseline_value"])
            weight = WEIGHTS.get(name, 0.0)
            contribution = value * weight
            score += contribution
            components.append({"indicator": name, "value": value, "weight": weight, "contribution": round(contribution, 2)})

    path = OUT / "administrative_burden_diagnostics.csv"
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["indicator", "value", "weight", "contribution"])
        writer.writeheader()
        writer.writerows(components)
        writer.writerow({"indicator": "total_burden_score", "value": "", "weight": "", "contribution": round(score, 2)})
    print(f"Wrote {path}")


if __name__ == "__main__":
    main()
