"""Policy delay simulation for backlog and capacity planning."""
from __future__ import annotations
from _policy_utils import OUT_TABLES, ensure_outputs, write_csv_dict


def simulate_delay(delay_years: int, years: int = 15) -> list[dict]:
    backlog = 100.0
    capacity = 45.0
    rows = []
    for year in range(years + 1):
        if year >= delay_years:
            capacity += 2.0
        incoming_demand = 8.0
        processed = capacity * 0.15
        backlog = max(0.0, backlog + incoming_demand - processed)
        rows.append({
            "delay_years": delay_years,
            "year": year,
            "capacity": round(capacity, 2),
            "incoming_demand": incoming_demand,
            "processed": round(processed, 2),
            "backlog": round(backlog, 2),
        })
    return rows


def main() -> None:
    ensure_outputs()
    rows = []
    for delay in [0, 2, 5, 8]:
        rows.extend(simulate_delay(delay))
    write_csv_dict(OUT_TABLES / "policy_delay_simulation.csv", rows)
    print(f"Wrote {OUT_TABLES / 'policy_delay_simulation.csv'}")

if __name__ == "__main__":
    main()
