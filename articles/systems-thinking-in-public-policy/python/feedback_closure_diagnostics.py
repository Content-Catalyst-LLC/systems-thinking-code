"""Feedback-loop closure diagnostics for public-policy learning."""
from __future__ import annotations
from _policy_utils import DATA, OUT_TABLES, ensure_outputs, read_csv_dict, to_float, write_csv_dict


def main() -> None:
    ensure_outputs()
    rows = read_csv_dict(DATA / "synthetic_feedback_signals.csv", ["signal_id", "source", "signal_type", "received", "acted_upon", "embedded"])
    out = []
    for row in rows:
        received = max(to_float(row, "received"), 1.0)
        acted = to_float(row, "acted_upon")
        embedded = to_float(row, "embedded")
        closure_rate = acted / received
        embedding_rate = embedded / received
        out.append({
            "signal_id": row["signal_id"],
            "source": row["source"],
            "signal_type": row["signal_type"],
            "closure_rate": round(closure_rate, 3),
            "embedding_rate": round(embedding_rate, 3),
            "learning_flag": "weak" if embedding_rate < 0.2 else "partial" if embedding_rate < 0.4 else "stronger",
        })
    write_csv_dict(OUT_TABLES / "feedback_closure_diagnostics.csv", out)
    print(f"Wrote {OUT_TABLES / 'feedback_closure_diagnostics.csv'}")

if __name__ == "__main__":
    main()
