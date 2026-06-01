CREATE TABLE IF NOT EXISTS model_runs (
  run_id TEXT PRIMARY KEY,
  scenario_id TEXT NOT NULL,
  objective_id TEXT NOT NULL,
  paradigm_id TEXT NOT NULL,
  notes TEXT,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
