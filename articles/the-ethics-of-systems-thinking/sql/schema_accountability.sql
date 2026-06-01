CREATE TABLE IF NOT EXISTS accountability_indicators (
  indicator_id TEXT PRIMARY KEY,
  indicator_name TEXT NOT NULL,
  baseline_score REAL CHECK (baseline_score BETWEEN 0 AND 100),
  target_score REAL CHECK (target_score BETWEEN 0 AND 100),
  notes TEXT
);
