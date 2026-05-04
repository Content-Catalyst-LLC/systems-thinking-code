"""
Feedback loop simulation for systems thinking.

This script compares reinforcing and balancing feedback over time.
"""

from __future__ import annotations

import pandas as pd


def simulate_reinforcing(initial: float = 10.0, rate: float = 0.08, steps: int = 60) -> pd.DataFrame:
    """Simulate reinforcing feedback."""
    values = [initial]

    for _ in range(1, steps):
        values.append(values[-1] + rate * values[-1])

    return pd.DataFrame({"time": range(steps), "value": values, "loop_type": "reinforcing"})


def simulate_balancing(initial: float = 10.0, target: float = 100.0, correction: float = 0.12, steps: int = 60) -> pd.DataFrame:
    """Simulate balancing feedback toward a target."""
    values = [initial]

    for _ in range(1, steps):
        gap = target - values[-1]
        values.append(values[-1] + correction * gap)

    return pd.DataFrame({"time": range(steps), "value": values, "loop_type": "balancing"})


def main() -> None:
    reinforcing = simulate_reinforcing()
    balancing = simulate_balancing()

    results = pd.concat([reinforcing, balancing], ignore_index=True)

    print(results.head())
    print(results.tail())

    results.to_csv("../outputs/feedback_loop_simulation.csv", index=False)


if __name__ == "__main__":
    main()
