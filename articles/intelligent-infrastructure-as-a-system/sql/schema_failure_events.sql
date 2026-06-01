CREATE TABLE IF NOT EXISTS failure_events (
  failure_id TEXT PRIMARY KEY,
  asset_id TEXT NOT NULL REFERENCES infrastructure_assets(asset_id),
  failure_type TEXT NOT NULL,
  failure_year INTEGER NOT NULL,
  service_loss_index REAL CHECK (service_loss_index BETWEEN 0 AND 100),
  affected_population INTEGER,
  recovery_hours REAL,
  notes TEXT
);
