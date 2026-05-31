#!/usr/bin/env python3
"""Parameter sweep for implementation delay and repair rate."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

def outcome(delay: float, repair: float, harm: float = 0.05, demand: float = 0.04) -> float:
    return max(0.0, min(1.0, 0.60 - 0.030 * delay + 1.9 * repair - 1.5 * harm - 1.2 * demand))

def main() -> None:
    rows = []
    repair_values = [x / 100 for x in range(2, 22, 2)]
    for delay in range(1, 19):
        for repair in repair_values:
            rows.append({"implementation_delay": delay, "repair_rate": repair, "resilience_score": round(outcome(delay, repair), 4)})
    with (OUT / "delay_repair_parameter_sweep.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {OUT / 'delay_repair_parameter_sweep.csv'}")

if __name__ == "__main__":
    main()
