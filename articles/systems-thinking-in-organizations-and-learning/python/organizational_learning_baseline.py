from __future__ import annotations

from common import read_csv, write_csv, clamp


def main() -> None:
    feedback = {(row["team_id"], row["period"]): row for row in read_csv("synthetic_feedback_signals.csv")}
    learning = read_csv("synthetic_learning_events.csv")
    rows = []
    for event in learning:
        key = (event["team_id"], event["period"])
        signal = feedback[key]
        feedback_quality = float(signal["observed_signal"]) * (1 - float(signal["distortion"]))
        interpretive_capacity = float(event["retrospective_quality"])
        authority = float(signal["authority_to_change"])
        learning_effectiveness = clamp(feedback_quality * interpretive_capacity * authority)
        rows.append({
            "period": event["period"],
            "team_id": event["team_id"],
            "feedback_quality": round(feedback_quality, 3),
            "interpretive_capacity": round(interpretive_capacity, 3),
            "authority_to_change": round(authority, 3),
            "learning_effectiveness": round(learning_effectiveness, 3),
        })
    out = write_csv("organizational_learning_baseline.csv", rows, ["period", "team_id", "feedback_quality", "interpretive_capacity", "authority_to_change", "learning_effectiveness"])
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
