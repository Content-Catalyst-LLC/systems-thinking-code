CREATE TABLE IF NOT EXISTS condition_observations (
  observation_id TEXT PRIMARY KEY,
  asset_id TEXT NOT NULL REFERENCES infrastructure_assets(asset_id),
  observed_at TEXT NOT NULL,
  condition_score REAL NOT NULL CHECK (condition_score BETWEEN 0 AND 100),
  observation_source TEXT NOT NULL,
  notes TEXT
);
