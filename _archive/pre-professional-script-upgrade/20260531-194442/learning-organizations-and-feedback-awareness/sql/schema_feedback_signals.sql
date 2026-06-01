CREATE TABLE IF NOT EXISTS feedback_signals (
  period INTEGER,
  unit_id TEXT,
  unit_name TEXT,
  raw_feedback REAL,
  signal_quality REAL,
  timeliness REAL,
  authority_connection REAL,
  feedback_burden REAL
);
