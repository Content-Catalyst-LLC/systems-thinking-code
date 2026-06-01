CREATE TABLE IF NOT EXISTS model_runs (
  run_id TEXT PRIMARY KEY,
  run_timestamp TEXT NOT NULL,
  model_name TEXT NOT NULL,
  parameters_json TEXT
);
