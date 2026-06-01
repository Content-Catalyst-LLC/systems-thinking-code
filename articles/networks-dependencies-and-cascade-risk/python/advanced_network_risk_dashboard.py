"""
Optional advanced pandas/matplotlib workflow.

This script is intentionally optional. It fails gracefully when pandas,
matplotlib, or openpyxl are not installed.
"""

from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "tables"
FIGURES = ROOT / "outputs" / "figures"

try:
    import pandas as pd
    import matplotlib.pyplot as plt
except ModuleNotFoundError as exc:
    print("Optional advanced dependencies are missing. Run ./setup-advanced-python.sh or install requirements-advanced.txt.")
    raise SystemExit(0) from exc


def main() -> None:
    FIGURES.mkdir(parents=True, exist_ok=True)
    criticality = pd.read_csv(TABLES / "network_node_criticality.csv")
    cascade = pd.read_csv(TABLES / "network_cascade_timeseries.csv")

    top = criticality.sort_values("criticality_index", ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(11, 6))
    ax.bar(top["node_id"], top["criticality_index"])
    ax.set_title("Top Network Criticality Scores")
    ax.set_ylabel("Criticality index")
    ax.tick_params(axis="x", rotation=45)
    fig.tight_layout()
    fig.savefig(FIGURES / "advanced_network_criticality_bar.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(11, 6))
    for scenario, subset in cascade.groupby("scenario"):
        ax.plot(subset["step"], subset["failed_count"], marker="o", label=scenario)
    ax.set_title("Cascade Failure Count by Scenario")
    ax.set_xlabel("Cascade step")
    ax.set_ylabel("Failed node count")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURES / "advanced_cascade_failure_count.png", dpi=160)
    plt.close(fig)

    workbook = TABLES / "advanced_network_risk_workbook.xlsx"
    with pd.ExcelWriter(workbook) as writer:
        criticality.to_excel(writer, sheet_name="node_criticality", index=False)
        cascade.to_excel(writer, sheet_name="cascade_timeseries", index=False)

    print(f"Wrote {workbook}")


if __name__ == "__main__":
    main()
