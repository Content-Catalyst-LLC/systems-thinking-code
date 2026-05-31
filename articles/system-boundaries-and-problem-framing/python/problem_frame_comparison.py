"""
Problem-frame comparison.

Shows how different frames imply different intervention logics.
"""

from __future__ import annotations

import csv
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "synthetic_problem_frames.csv"


def main() -> None:
    with DATA_PATH.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    print("frame_id,frame_name,primary_question,likely_intervention,main_risk")
    for row in rows:
        print(
            f"{row['frame_id']},{row['frame_name']},"
            f"{row['primary_question']},{row['likely_intervention']},{row['main_risk']}"
        )


if __name__ == "__main__":
    main()
