"""Policy resistance model with compensating feedback."""

from __future__ import annotations


def simulate_policy_resistance(periods: int = 20) -> list[dict[str, float | int]]:
    problem_pressure = 100.0
    intended_effect = 6.0
    compensating_feedback = 0.0
    rows: list[dict[str, float | int]] = []

    for period in range(1, periods + 1):
        compensating_feedback = min(5.0, compensating_feedback + 0.25)
        observed_effect = intended_effect - compensating_feedback
        problem_pressure = max(0.0, problem_pressure - observed_effect)
        rows.append(
            {
                "period": period,
                "problem_pressure": round(problem_pressure, 2),
                "intended_effect": intended_effect,
                "compensating_feedback": round(compensating_feedback, 2),
                "observed_effect": round(observed_effect, 2),
            }
        )

    return rows


def main() -> None:
    print("period,problem_pressure,intended_effect,compensating_feedback,observed_effect")
    for row in simulate_policy_resistance():
        print(
            f"{row['period']},{row['problem_pressure']},{row['intended_effect']},"
            f"{row['compensating_feedback']},{row['observed_effect']}"
        )


if __name__ == "__main__":
    main()
