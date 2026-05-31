CREATE TABLE IF NOT EXISTS leverage_points (
  leverage_id TEXT PRIMARY KEY,
  leverage_name TEXT NOT NULL,
  leverage_level TEXT,
  target_variable TEXT,
  expected_depth TEXT,
  ethical_flag TEXT
);
