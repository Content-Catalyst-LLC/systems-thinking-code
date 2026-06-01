#!/usr/bin/env python3
"""Stock-flow accumulation example for maintenance backlog."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)


def simulate(years=12, initial_stock=20.0, deterioration=14.0, preventive_work=6.0):
    rows = []
    stock = initial_stock
    for year in range(1, years + 1):
        inflow = deterioration
        outflow = preventive_work
        stock = max(0.0, stock + inflow - outflow)
        rows.append({"year": year, "inflow_deterioration": inflow, "outflow_prevention": outflow, "maintenance_backlog": stock})
    return pd.DataFrame(rows)


def main() -> None:
    df = simulate()
    df.to_csv(OUT / "stock_flow_backlog_simulation.csv", index=False)
    plt.figure()
    plt.plot(df["year"], df["maintenance_backlog"], marker="o")
    plt.title("Maintenance Backlog Accumulation")
    plt.xlabel("Year")
    plt.ylabel("Backlog")
    plt.tight_layout()
    plt.savefig(OUT / "stock_flow_backlog_simulation.png", dpi=160)
    plt.close()
    print(df)


if __name__ == "__main__":
    main()
