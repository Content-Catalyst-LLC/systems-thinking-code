CREATE TABLE IF NOT EXISTS model_runs (
  run_id TEXT PRIMARY KEY,
  scenario_id TEXT NOT NULL,
  model_name TEXT NOT NULL,
  run_timestamp TEXT NOT NULL,
  notes TEXT
);
