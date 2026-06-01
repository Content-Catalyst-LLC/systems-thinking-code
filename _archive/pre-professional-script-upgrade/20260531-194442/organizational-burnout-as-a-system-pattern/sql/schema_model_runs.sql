CREATE TABLE IF NOT EXISTS model_runs (
  run_id TEXT PRIMARY KEY,
  scenario_id TEXT,
  time_horizon INTEGER,
  pressure_weight REAL,
  recovery_weight REAL,
  turnover_weight REAL,
  memory_weight REAL
);
