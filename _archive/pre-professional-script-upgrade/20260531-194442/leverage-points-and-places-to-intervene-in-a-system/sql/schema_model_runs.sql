CREATE TABLE IF NOT EXISTS model_runs (
  run_id TEXT PRIMARY KEY,
  scenario TEXT NOT NULL,
  intervention_id TEXT,
  trust_change REAL,
  burden_change REAL,
  capacity_change REAL,
  resilience_change REAL,
  notes TEXT
);
