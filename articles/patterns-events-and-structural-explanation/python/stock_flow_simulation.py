"""
Stock-flow simulation for structural explanation.

Maintenance backlog is treated as a stock that accumulates when incoming work
exceeds completed work.
"""

from __future__ import annotations


def simulate_backlog(initial_backlog: float = 120.0, periods: int = 18) -> list[dict[str, float]]:
    backlog = initial_backlog
    rows: list[dict[str, float]] = []

    for period in range(1, periods + 1):
        incoming_work = 11.0 + (period * 0.25)
        completed_work = max(5.0, 10.5 - backlog / 100.0)
        backlog = backlog + incoming_work - completed_work

        rows.append(
            {
                "period": period,
                "incoming_work": round(incoming_work, 2),
                "completed_work": round(completed_work, 2),
                "backlog": round(backlog, 2),
            }
        )

    return rows


def main() -> None:
    print("period,incoming_work,completed_work,backlog")
    for row in simulate_backlog():
        print(f"{row['period']},{row['incoming_work']},{row['completed_work']},{row['backlog']}")


if __name__ == "__main__":
    main()
