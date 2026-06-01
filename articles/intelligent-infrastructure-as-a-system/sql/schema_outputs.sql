CREATE TABLE IF NOT EXISTS model_outputs (
  output_id TEXT PRIMARY KEY,
  run_id TEXT NOT NULL REFERENCES model_runs(run_id),
  asset_id TEXT REFERENCES infrastructure_assets(asset_id),
  indicator_name TEXT NOT NULL,
  indicator_value REAL NOT NULL,
  output_year INTEGER,
  notes TEXT
);
