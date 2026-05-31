from __future__ import annotations

from common import read_csv, write_csv, clamp


def main() -> None:
    rows = []
    for asset in read_csv("synthetic_memory_assets.csv"):
        records = float(asset["decision_records"])
        playbooks = float(asset["updated_playbooks"])
        onboarding = float(asset["onboarding_assets"])
        reused = float(asset["postmortems_reused"])
        dependency = float(asset["key_person_dependency"])
        memory_resilience = clamp((records * 0.015) + (playbooks * 0.04) + (onboarding * 0.05) + (reused * 0.06) - (dependency * 0.25))
        rows.append({
            "team_id": asset["team_id"],
            "memory_resilience": round(memory_resilience, 3),
            "learning_decay_risk": "high" if memory_resilience < 0.35 else "moderate" if memory_resilience < 0.55 else "lower",
        })
    out = write_csv("institutional_memory_decay.csv", rows, ["team_id", "memory_resilience", "learning_decay_risk"])
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
