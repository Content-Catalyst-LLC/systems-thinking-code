"""Classify synthetic feedback loops as leverage candidates."""
from __future__ import annotations

from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
loops = pd.read_csv(ROOT / "data" / "synthetic_feedback_loops.csv")
loops["leverage_note"] = loops["loop_type"].map(
    {
        "reinforcing": "Interrupt harmful amplification or strengthen beneficial reinforcement.",
        "balancing": "Improve goal, signal quality, delay, legitimacy, or corrective capacity.",
    }
)
print(loops[["loop_name", "loop_type", "leverage_note"]])
