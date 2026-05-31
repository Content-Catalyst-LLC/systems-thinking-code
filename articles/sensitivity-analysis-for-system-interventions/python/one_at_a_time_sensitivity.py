#!/usr/bin/env python3
"""One-at-a-time sensitivity analysis for a synthetic system intervention."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

BASE = {
    "implementation_delay": 6.0,
    "demand_growth": 0.04,
    "repair_rate": 0.08,
    "harm_rate": 0.05,
    "trust_elasticity": 0.60,
    "capacity_buffer": 0.15,
}

def system_score(params: dict[str, float]) -> float:
    value = (
        0.55
        - 0.025 * params["implementation_delay"]
        - 2.0 * params["demand_growth"]
        - 1.7 * params["harm_rate"]
        + 1.8 * params["repair_rate"]
        + 0.25 * params["trust_elasticity"]
        + 0.80 * params["capacity_buffer"]
    )
    return max(0.0, min(1.0, value))

def main() -> None:
    rows: list[dict[str, object]] = []
    baseline = system_score(BASE)
    with (DATA / "synthetic_parameter_ranges.csv").open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            param = row["parameter"]
            for label in ["low", "medium", "high"]:
                params = dict(BASE)
                params[param] = float(row[label])
                score = system_score(params)
                rows.append({
                    "parameter": param,
                    "case": label,
                    "value": params[param],
                    "resilience_score": round(score, 4),
                    "difference_from_baseline": round(score - baseline, 4),
                })

    with (OUT / "one_at_a_time_sensitivity.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {OUT / 'one_at_a_time_sensitivity.csv'}")

if __name__ == "__main__":
    main()
