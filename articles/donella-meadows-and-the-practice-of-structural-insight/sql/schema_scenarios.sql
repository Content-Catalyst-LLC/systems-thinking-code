CREATE TABLE IF NOT EXISTS scenarios (
  scenario_id TEXT PRIMARY KEY,
  scenario_name TEXT NOT NULL,
  information_quality REAL CHECK (information_quality BETWEEN 0 AND 1),
  rule_change_strength REAL CHECK (rule_change_strength BETWEEN 0 AND 1),
  goal_alignment REAL CHECK (goal_alignment BETWEEN 0 AND 1),
  paradigm_shift_capacity REAL CHECK (paradigm_shift_capacity BETWEEN 0 AND 1),
  equity_alignment REAL CHECK (equity_alignment BETWEEN 0 AND 1)
);
