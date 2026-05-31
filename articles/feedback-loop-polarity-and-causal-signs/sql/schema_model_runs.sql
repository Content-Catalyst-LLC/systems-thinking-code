CREATE TABLE IF NOT EXISTS model_runs (
  model_run_id TEXT PRIMARY KEY,
  scenario_id TEXT,
  run_timestamp TEXT,
  notes TEXT
);
