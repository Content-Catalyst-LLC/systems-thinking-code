CREATE TABLE IF NOT EXISTS model_runs (
  run_id TEXT PRIMARY KEY,
  scenario TEXT NOT NULL,
  model TEXT NOT NULL,
  notes TEXT
);
