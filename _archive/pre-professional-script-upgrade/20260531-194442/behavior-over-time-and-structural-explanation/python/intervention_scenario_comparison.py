#!/usr/bin/env python3
"""Compare simple baseline and intervention scenarios for service delay."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)


def run_scenario(name: str, prevention: float, years: int = 10):
    backlog = 40.0
    delay = 20.0
    rows = []
    for year in range(1, years + 1):
        backlog = max(0.0, backlog + 10.0 - prevention)
        delay = max(0.0, 0.45 * backlog)
        rows.append({"scenario": name, "year": year, "backlog": backlog, "service_delay": delay})
    return rows


def main() -> None:
    rows = []
    rows.extend(run_scenario("baseline", prevention=4.0))
    rows.extend(run_scenario("prevention_investment", prevention=11.0))
    df = pd.DataFrame(rows)
    df.to_csv(OUT / "intervention_scenario_comparison.csv", index=False)
    plt.figure()
    for scenario, group in df.groupby("scenario"):
        plt.plot(group["year"], group["service_delay"], marker="o", label=scenario)
    plt.title("Service Delay by Scenario")
    plt.xlabel("Year")
    plt.ylabel("Service Delay")
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUT / "intervention_scenario_comparison.png", dpi=160)
    plt.close()
    print(df.groupby("scenario").tail(1))


if __name__ == "__main__":
    main()
