#!/usr/bin/env python3
"""Generate simple synthetic patterns from reinforcing and balancing feedback."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)


def main() -> None:
    rows = []
    reinforcing = 10.0
    balancing = 80.0
    goal = 30.0
    for t in range(25):
        reinforcing = reinforcing * 1.12
        balancing = balancing + 0.25 * (goal - balancing)
        rows.append({"time": t, "reinforcing_growth": reinforcing, "balancing_goal_seek": balancing})
    df = pd.DataFrame(rows)
    df.to_csv(OUT / "feedback_generated_patterns.csv", index=False)
    for col in ["reinforcing_growth", "balancing_goal_seek"]:
        plt.figure()
        plt.plot(df["time"], df[col], marker="o")
        plt.title(col.replace("_", " ").title())
        plt.xlabel("Time")
        plt.ylabel(col.replace("_", " ").title())
        plt.tight_layout()
        plt.savefig(OUT / f"{col}.png", dpi=160)
        plt.close()
    print(df.tail())


if __name__ == "__main__":
    main()
