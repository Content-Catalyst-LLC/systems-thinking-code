from __future__ import annotations

from common import read_csv, write_csv


def main() -> None:
    rows = []
    for row in read_csv("synthetic_feedback_signals.csv"):
        observed = float(row["observed_signal"])
        distortion = float(row["distortion"])
        delay = float(row["decision_delay"])
        received = observed * (1 - distortion)
        delay_penalty = min(0.35, delay * 0.04)
        actionable_signal = max(0.0, received - delay_penalty)
        rows.append({
            "period": row["period"],
            "team_id": row["team_id"],
            "observed_signal": round(observed, 3),
            "received_signal": round(received, 3),
            "actionable_signal": round(actionable_signal, 3),
            "distortion": round(distortion, 3),
            "decision_delay": row["decision_delay"],
        })
    out = write_csv("feedback_signal_distortion.csv", rows, ["period", "team_id", "observed_signal", "received_signal", "actionable_signal", "distortion", "decision_delay"])
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
