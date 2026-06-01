CREATE TABLE IF NOT EXISTS feedback_patterns (
  pattern_id TEXT PRIMARY KEY,
  pattern_name TEXT NOT NULL,
  loop_type TEXT,
  intensity REAL CHECK (intensity BETWEEN 0 AND 1),
  delay_periods INTEGER,
  notes TEXT
);
