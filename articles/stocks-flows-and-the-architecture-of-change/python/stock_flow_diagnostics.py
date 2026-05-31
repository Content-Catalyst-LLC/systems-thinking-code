"""Simple stock-flow diagnostics for synthetic systems data."""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_flows() -> list[dict[str, str]]:
    with (ROOT / "data" / "synthetic_system_flows.csv").open() as handle:
        return list(csv.DictReader(handle))


def summarize_net_flows(rows: list[dict[str, str]]) -> dict[str, float]:
    summary: dict[str, float] = {}
    for row in rows:
        rate = float(row["baseline_rate"])
        sign = 1 if row["flow_type"] == "inflow" else -1
        summary[row["stock_id"]] = summary.get(row["stock_id"], 0.0) + sign * rate
    return summary


if __name__ == "__main__":
    for stock, net in summarize_net_flows(read_flows()).items():
        direction = "growing" if net > 0 else "depleting" if net < 0 else "stable"
        print(f"{stock}: net={net:.2f}, direction={direction}")
