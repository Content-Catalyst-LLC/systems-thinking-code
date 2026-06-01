CREATE TABLE IF NOT EXISTS model_runs (
  run_id TEXT PRIMARY KEY,
  scenario_id TEXT,
  run_timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
  model_name TEXT NOT NULL,
  notes TEXT
);
