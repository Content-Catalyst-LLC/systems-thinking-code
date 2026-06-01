CREATE TABLE IF NOT EXISTS climate_exposure (
  exposure_id TEXT PRIMARY KEY,
  asset_id TEXT NOT NULL REFERENCES infrastructure_assets(asset_id),
  hazard_type TEXT NOT NULL,
  exposure_score REAL NOT NULL CHECK (exposure_score BETWEEN 0 AND 100),
  scenario_name TEXT,
  time_horizon TEXT
);
