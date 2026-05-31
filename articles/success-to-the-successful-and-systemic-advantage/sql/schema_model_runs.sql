CREATE TABLE IF NOT EXISTS model_runs (
  run_id TEXT PRIMARY KEY,
  scenario TEXT NOT NULL,
  periods INTEGER NOT NULL,
  total_resources REAL NOT NULL,
  feedback_strength REAL NOT NULL,
  network_amplification REAL NOT NULL,
  random_seed INTEGER NOT NULL
);
