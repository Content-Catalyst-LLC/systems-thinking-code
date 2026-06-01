CREATE TABLE IF NOT EXISTS feedback_signals (
  signal_id TEXT PRIMARY KEY,
  signal_name TEXT NOT NULL,
  signal_quality REAL CHECK (signal_quality BETWEEN 0 AND 1),
  delay_periods INTEGER,
  noise_level REAL CHECK (noise_level BETWEEN 0 AND 1),
  affected_decision TEXT
);
