"""Compare baseline and intervention runs for synthetic leverage-point scenarios."""
from __future__ import annotations

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs" / "tables"
OUT.mkdir(parents=True, exist_ok=True)


def main() -> None:
    runs = pd.read_csv(DATA / "synthetic_model_runs.csv")
    indicators = ["trust_change", "burden_change", "capacity_change", "resilience_change"]
    runs["composite_change"] = runs[indicators].sum(axis=1)
    runs.sort_values("composite_change", ascending=False).to_csv(
        OUT / "intervention_comparison.csv", index=False
    )
    print(runs[["scenario", "intervention_id", "composite_change", "notes"]])


if __name__ == "__main__":
    main()
