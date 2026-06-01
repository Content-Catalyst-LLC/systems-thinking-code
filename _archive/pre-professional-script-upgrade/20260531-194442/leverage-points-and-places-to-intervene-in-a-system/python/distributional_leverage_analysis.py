"""Distributional outcome comparison for synthetic leverage-point intervention."""
from __future__ import annotations

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATA / "synthetic_distributional_outcomes.csv")
df["burden_reduction"] = df["baseline_burden"] - df["post_intervention_burden"]
df["access_gain"] = df["post_intervention_access"] - df["baseline_access"]
df.to_csv(OUT / "distributional_leverage_summary.csv", index=False)
print(df[["group_name", "burden_reduction", "access_gain"]])
