"""
Stock-flow model for interdependence stress.
"""

from __future__ import annotations


def simulate(periods: int = 18) -> list[dict[str, float]]:
    dependency_stress = 30.0
    resilience_buffer = 50.0
    rows = []

    for period in range(1, periods + 1):
        stress_inflow = 4.0 + 0.03 * dependency_stress
        stress_outflow = 0.10 * resilience_buffer
        dependency_stress = max(0.0, dependency_stress + stress_inflow - stress_outflow)

        buffer_recovery = 2.5
        buffer_depletion = 0.05 * dependency_stress
        resilience_buffer = max(0.0, resilience_buffer + buffer_recovery - buffer_depletion)

        rows.append({
            "period": period,
            "dependency_stress": round(dependency_stress, 2),
            "resilience_buffer": round(resilience_buffer, 2),
        })

    return rows


def main() -> None:
    print("period,dependency_stress,resilience_buffer")
    for row in simulate():
        print(f"{row['period']},{row['dependency_stress']},{row['resilience_buffer']}")


if __name__ == "__main__":
    main()
