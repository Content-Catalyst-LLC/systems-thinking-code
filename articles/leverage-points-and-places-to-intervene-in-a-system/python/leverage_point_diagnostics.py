"""Leverage-point diagnostics using synthetic systems-thinking data."""
from __future__ import annotations

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)


def main() -> None:
    leverage = pd.read_csv(DATA / "synthetic_leverage_points.csv")
    interventions = pd.read_csv(DATA / "synthetic_interventions.csv")
    merged = interventions.merge(leverage, on="leverage_id", how="left")
    merged["leverage_score"] = (
        merged["expected_strength"] * 10
        - merged["cost_index"] * 0.5
        - merged["implementation_delay_months"] * 0.05
    )
    ranked = merged.sort_values("leverage_score", ascending=False)
    ranked.to_csv(OUT / "leverage_point_ranking.csv", index=False)
    print(ranked[["intervention_name", "leverage_name", "expected_depth", "leverage_score"]])


if __name__ == "__main__":
    main()
