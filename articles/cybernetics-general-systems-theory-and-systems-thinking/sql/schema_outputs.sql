CREATE TABLE IF NOT EXISTS model_outputs (
  output_id TEXT PRIMARY KEY,
  run_id TEXT NOT NULL REFERENCES model_runs(run_id),
  period INTEGER NOT NULL,
  indicator_name TEXT NOT NULL,
  indicator_value REAL NOT NULL,
  notes TEXT
);
