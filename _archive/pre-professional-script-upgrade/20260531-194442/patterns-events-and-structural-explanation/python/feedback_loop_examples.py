"""
Feedback loop examples showing recurring system behavior.
"""

from __future__ import annotations


def simulate_trust_delay_loop(periods: int = 12) -> list[dict[str, float]]:
    trust = 62.0
    delay = 14.0
    demand_pressure = 70.0
    rows: list[dict[str, float]] = []

    for period in range(1, periods + 1):
        delay += (demand_pressure / 100.0) - (trust / 150.0)
        trust -= delay / 30.0
        demand_pressure += max(0.0, (65.0 - trust) / 25.0)

        rows.append(
            {
                "period": period,
                "trust": round(trust, 2),
                "delay": round(delay, 2),
                "demand_pressure": round(demand_pressure, 2),
            }
        )

    return rows


def main() -> None:
    print("period,trust,delay,demand_pressure")
    for row in simulate_trust_delay_loop():
        print(f"{row['period']},{row['trust']},{row['delay']},{row['demand_pressure']}")


if __name__ == "__main__":
    main()
