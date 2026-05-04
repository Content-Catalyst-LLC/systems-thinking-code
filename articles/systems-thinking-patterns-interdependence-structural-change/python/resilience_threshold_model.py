"""
Resilience and threshold simulation for systems thinking.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def simulate_resilience(
    steps: int = 100,
    initial_resilience: float = 0.70,
    learning_rate: float = 0.025,
    pressure: float = 0.018,
    shock_start: int = 40,
    shock_end: int = 62,
    shock_pressure: float = 0.045
) -> pd.DataFrame:
    resilience = np.zeros(steps)
    resilience[0] = initial_resilience

    for t in range(1, steps):
        shock = shock_pressure if shock_start <= t <= shock_end else 0.0

        resilience[t] = resilience[t - 1] + learning_rate * (1 - resilience[t - 1]) - pressure - shock
        resilience[t] = min(1.0, max(0.0, resilience[t]))

    return pd.DataFrame({
        "time": np.arange(steps),
        "resilience": resilience,
        "below_threshold": resilience < 0.35
    })


def main() -> None:
    results = simulate_resilience()
    print(results.head())
    print(results.tail())
    print("Any threshold breach:", results["below_threshold"].any())

    results.to_csv("../outputs/resilience_threshold_model.csv", index=False)


if __name__ == "__main__":
    main()
