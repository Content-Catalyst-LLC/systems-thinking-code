CREATE TABLE IF NOT EXISTS model_runs (
  run_id TEXT PRIMARY KEY,
  scenario TEXT,
  linear_weight REAL,
  feedback_weight REAL,
  boundary_weight REAL,
  power_weight REAL,
  expected_learning_quality REAL
);
