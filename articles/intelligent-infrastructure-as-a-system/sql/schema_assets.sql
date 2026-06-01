CREATE TABLE IF NOT EXISTS infrastructure_assets (
  asset_id TEXT PRIMARY KEY,
  category TEXT NOT NULL,
  condition_score REAL NOT NULL CHECK (condition_score BETWEEN 0 AND 100),
  age_years REAL NOT NULL,
  service_criticality REAL NOT NULL CHECK (service_criticality BETWEEN 0 AND 100),
  redundancy_score REAL NOT NULL CHECK (redundancy_score BETWEEN 0 AND 100),
  equity_priority REAL NOT NULL CHECK (equity_priority BETWEEN 0 AND 100),
  climate_exposure REAL NOT NULL CHECK (climate_exposure BETWEEN 0 AND 100),
  cyber_dependency REAL NOT NULL CHECK (cyber_dependency BETWEEN 0 AND 100)
);
