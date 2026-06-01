from __future__ import annotations

from collections import defaultdict

from _common import f, read_csv, write_csv

signals = defaultdict(list)
for row in read_csv("synthetic_feedback_signals.csv"):
    usable = f(row["raw_feedback"]) * f(row["signal_quality"]) * f(row["timeliness"]) * f(row["authority_connection"])
    signals[row["unit_id"]].append(usable)

learning = defaultdict(list)
for row in read_csv("synthetic_learning_events.csv"):
    if f(row["feedback_items"]) == 0:
        conversion = 0.0
    else:
        conversion = f(row["structural_changes"]) / f(row["feedback_items"])
    learning[row["unit_id"]].append(conversion)

memory = {row["unit_id"]: (1 - f(row["knowledge_decay_risk"])) for row in read_csv("synthetic_memory_assets.csv")}

rows = []
for unit_id in sorted(signals):
    feedback_quality = sum(signals[unit_id]) / len(signals[unit_id])
    learning_conversion = sum(learning[unit_id]) / len(learning[unit_id])
    memory_retention = memory.get(unit_id, 0.0)
    effectiveness = feedback_quality * (1 + learning_conversion) * memory_retention
    rows.append({
        "unit_id": unit_id,
        "feedback_quality": round(feedback_quality, 4),
        "learning_conversion": round(learning_conversion, 4),
        "memory_retention": round(memory_retention, 4),
        "learning_effectiveness_index": round(effectiveness, 4),
    })

path = write_csv("learning_effectiveness_index.csv", rows)
print(f"Wrote {path}")
