#!/usr/bin/env python3
"""Find a synthetic delay threshold where resilience falls below a critical value."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)
CRITICAL = 0.50

def resilience(delay: float, repair: float = 0.08, harm: float = 0.05) -> float:
    return max(0.0, min(1.0, 0.68 - 0.035 * delay + 1.2 * repair - 1.4 * harm))

def main() -> None:
    rows = []
    threshold = None
    for delay in [x / 2 for x in range(2, 49)]:
        value = resilience(delay)
        rows.append({"implementation_delay": delay, "resilience_score": round(value, 4), "below_critical": value < CRITICAL})
        if threshold is None and value < CRITICAL:
            threshold = delay
    with (OUT / "delay_threshold_search.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"Delay threshold below {CRITICAL}: {threshold} months")

if __name__ == "__main__":
    main()
