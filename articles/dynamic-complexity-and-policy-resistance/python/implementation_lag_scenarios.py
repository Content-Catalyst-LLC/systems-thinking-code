"""Implementation lag scenarios for dynamic-complexity analysis."""
from __future__ import annotations


def maturity_curve(month: int, lag: int, ramp: int = 8) -> float:
    if month <= lag:
        return 0.0
    return min(1.0, (month - lag) / ramp)


def main() -> None:
    for lag in [0, 3, 6, 12]:
        values = [round(maturity_curve(month, lag), 2) for month in range(0, 25, 4)]
        print(f"implementation_lag={lag:>2} months maturity={values}")


if __name__ == "__main__":
    main()
