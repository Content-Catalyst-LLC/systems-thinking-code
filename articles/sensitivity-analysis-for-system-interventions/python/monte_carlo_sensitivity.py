#!/usr/bin/env python3
"""Monte Carlo sensitivity example using synthetic uncertainty ranges."""
from pathlib import Path
import csv
import random
import statistics

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)
random.seed(42)

def score(delay: float, demand: float, repair: float, harm: float, trust: float, buffer: float) -> float:
    value = 0.55 - 0.025 * delay - 1.5 * demand + 1.7 * repair - 1.8 * harm + 0.22 * trust + 0.75 * buffer
    return max(0.0, min(1.0, value))

def main() -> None:
    runs = []
    for run_id in range(1, 1001):
        delay = random.uniform(1, 18)
        demand = random.uniform(0.00, 0.12)
        repair = random.uniform(0.02, 0.20)
        harm = random.uniform(0.01, 0.15)
        trust = random.uniform(0.10, 1.20)
        buffer = random.uniform(0.00, 0.40)
        runs.append({
            "run_id": run_id,
            "implementation_delay": round(delay, 3),
            "demand_growth": round(demand, 4),
            "repair_rate": round(repair, 4),
            "harm_rate": round(harm, 4),
            "trust_elasticity": round(trust, 4),
            "capacity_buffer": round(buffer, 4),
            "resilience_score": round(score(delay, demand, repair, harm, trust, buffer), 4),
        })
    with (OUT / "monte_carlo_sensitivity_runs.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(runs[0].keys()))
        writer.writeheader()
        writer.writerows(runs)
    values = [r["resilience_score"] for r in runs]
    print(f"Wrote {OUT / 'monte_carlo_sensitivity_runs.csv'}")
    print(f"Mean resilience: {statistics.mean(values):.3f}; min: {min(values):.3f}; max: {max(values):.3f}")

if __name__ == "__main__":
    main()
