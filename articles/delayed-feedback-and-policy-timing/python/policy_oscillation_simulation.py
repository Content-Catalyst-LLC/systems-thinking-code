"""Simulate a delayed balancing response that can oscillate."""
from __future__ import annotations

from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs" / "tables"


def simulate(months: int = 48, goal: float = 1.0, delay: int = 5, correction: float = 0.45) -> list[tuple[int, float]]:
    values = [0.35] * (delay + 1)
    results = []
    for t in range(months):
        delayed_value = values[-delay]
        next_value = values[-1] + correction * (goal - delayed_value)
        next_value = max(0.0, min(1.8, next_value))
        values.append(next_value)
        results.append((t, next_value))
    return results


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "policy_oscillation_simulation.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["month", "system_state"])
        writer.writerows(simulate())


if __name__ == "__main__":
    main()
