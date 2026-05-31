#!/usr/bin/env python3
"""Simple structural explanation scoring for synthetic system variables."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)


def main() -> None:
    edges = pd.read_csv(DATA / "synthetic_causal_edges.csv")
    variables = pd.read_csv(DATA / "synthetic_structural_variables.csv")
    incoming = edges.groupby("target").size().rename("incoming_links")
    outgoing = edges.groupby("source").size().rename("outgoing_links")
    summary = variables.set_index("name").join(incoming).join(outgoing).fillna(0)
    summary["structural_attention_score"] = summary["incoming_links"] + summary["outgoing_links"]
    summary.sort_values("structural_attention_score", ascending=False).to_csv(OUT / "structural_explanation_scores.csv")
    print(summary.sort_values("structural_attention_score", ascending=False))


if __name__ == "__main__":
    main()
