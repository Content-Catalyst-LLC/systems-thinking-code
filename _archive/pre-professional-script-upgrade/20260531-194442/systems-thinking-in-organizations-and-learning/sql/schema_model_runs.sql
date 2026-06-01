CREATE TABLE IF NOT EXISTS model_runs (
  run_id TEXT PRIMARY KEY,
  model_name TEXT NOT NULL,
  run_timestamp TEXT NOT NULL,
  notes TEXT
);
