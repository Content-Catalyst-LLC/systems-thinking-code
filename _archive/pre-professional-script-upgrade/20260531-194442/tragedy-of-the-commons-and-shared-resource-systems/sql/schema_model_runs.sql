CREATE TABLE IF NOT EXISTS model_runs (
  run_id TEXT PRIMARY KEY,
  resource_id TEXT NOT NULL,
  scenario TEXT NOT NULL,
  years INTEGER,
  final_stock REAL,
  min_stock REAL,
  total_benefit REAL,
  total_depletion_cost REAL,
  commons_status TEXT,
  FOREIGN KEY (resource_id) REFERENCES shared_resources(resource_id)
);
