"""Adaptive actor response examples.

Shows how policy rules and incentives shape behavioral response rather than
simply producing linear compliance.
"""
from __future__ import annotations

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
RESPONSES = ROOT / "data" / "raw" / "synthetic_actor_responses.csv"
OUT = ROOT / "outputs" / "tables" / "adaptive_actor_response_scores.csv"


def response_risk(strength: float, legitimacy: float = 0.55, burden: float = 0.50) -> float:
    return max(0.0, min(1.0, 0.5 * strength + 0.3 * burden + 0.2 * (1 - legitimacy)))


def main() -> None:
    rows = []
    with RESPONSES.open(newline="") as f:
        for row in csv.DictReader(f):
            strength = float(row["response_strength"])
            row["response_risk_index"] = round(response_risk(strength), 3)
            rows.append(row)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
