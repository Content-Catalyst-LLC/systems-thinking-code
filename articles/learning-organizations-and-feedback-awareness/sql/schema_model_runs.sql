CREATE TABLE IF NOT EXISTS model_runs (
  run_id TEXT PRIMARY KEY,
  scenario TEXT,
  feedback_closure REAL,
  blame_reduction REAL,
  memory_investment REAL,
  authority_connection REAL,
  expected_learning_gain REAL
);
