"""Behavior-over-time summary for synthetic indicators."""

from __future__ import annotations

import csv
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "synthetic_indicators.csv"


def load_rows() -> list[dict[str, str]]:
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def summarize_change(rows: list[dict[str, str]], variable: str) -> dict[str, float | str]:
    first = float(rows[0][variable])
    last = float(rows[-1][variable])
    change = last - first
    direction = "increasing" if change > 0 else "decreasing" if change < 0 else "flat"
    return {"variable": variable, "first": first, "last": last, "change": round(change, 2), "direction": direction}


def main() -> None:
    rows = load_rows()
    variables = ["public_trust", "service_demand", "workload", "response_delay", "maintenance_backlog", "system_capacity"]
    print("variable,first,last,change,direction")
    for variable in variables:
        result = summarize_change(rows, variable)
        print(f"{result['variable']},{result['first']},{result['last']},{result['change']},{result['direction']}")


if __name__ == "__main__":
    main()
