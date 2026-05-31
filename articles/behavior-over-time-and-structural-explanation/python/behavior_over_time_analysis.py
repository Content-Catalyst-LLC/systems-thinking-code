#!/usr/bin/env python3
"""Behavior-over-time analysis for synthetic systems-thinking indicators."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "synthetic_time_series_indicators.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)


def main() -> None:
    df = pd.read_csv(DATA)
    metrics = ["maintenance_backlog", "service_delay_index", "public_trust", "workload_index", "turnover_rate"]
    for metric in metrics:
        plt.figure()
        plt.plot(df["year"], df[metric], marker="o")
        plt.title(metric.replace("_", " ").title())
        plt.xlabel("Year")
        plt.ylabel(metric.replace("_", " ").title())
        plt.tight_layout()
        plt.savefig(OUT / f"{metric}_behavior_over_time.png", dpi=160)
        plt.close()
    print(f"Saved behavior-over-time plots to {OUT}")


if __name__ == "__main__":
    main()
