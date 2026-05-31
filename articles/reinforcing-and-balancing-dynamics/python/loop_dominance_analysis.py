"""Compare reinforcing and balancing pressures over time."""

from __future__ import annotations


def simulate(initial: float = 10.0, reinforcing_rate: float = 0.15, balancing_strength: float = 0.04, capacity: float = 100.0, periods: int = 25) -> list[tuple[int, float, str]]:
    value = initial
    rows: list[tuple[int, float, str]] = []
    for period in range(1, periods + 1):
        reinforcing = reinforcing_rate * value
        balancing = balancing_strength * value * (value / capacity)
        dominant = "reinforcing" if reinforcing > balancing else "balancing"
        value = value + reinforcing - balancing
        rows.append((period, round(value, 4), dominant))
    return rows


def main() -> None:
    print("period,value,dominant_pressure")
    for period, value, dominant in simulate():
        print(f"{period},{value},{dominant}")


if __name__ == "__main__":
    main()
