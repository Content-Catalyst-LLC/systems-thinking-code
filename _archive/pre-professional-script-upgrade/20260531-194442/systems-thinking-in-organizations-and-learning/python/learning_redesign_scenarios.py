from __future__ import annotations

from common import read_csv, write_csv, clamp


def main() -> None:
    scenarios = read_csv("synthetic_redesign_scenarios.csv")
    rows = []
    baseline_learning = 0.34
    baseline_burden = 0.68
    for scenario in scenarios:
        capacity = float(scenario["capacity_investment"])
        feedback = float(scenario["feedback_quality_gain"])
        workload = float(scenario["workload_reduction"])
        memory = float(scenario["memory_embedding_gain"])
        burden_reduction = float(scenario["expected_burden_reduction"])
        learning_gain = clamp(baseline_learning + (feedback * 0.35) + (capacity * 0.20) + (memory * 0.25) + (workload * 0.15))
        burden_after = clamp(baseline_burden - burden_reduction)
        rows.append({
            "scenario_id": scenario["scenario_id"],
            "scenario_name": scenario["scenario_name"],
            "learning_effectiveness": round(learning_gain, 3),
            "burden_after": round(burden_after, 3),
            "scenario_assessment": "strong" if learning_gain > 0.55 and burden_after < 0.50 else "partial" if learning_gain > 0.45 else "weak",
        })
    out = write_csv("learning_redesign_scenarios.csv", rows, ["scenario_id", "scenario_name", "learning_effectiveness", "burden_after", "scenario_assessment"])
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
