CREATE TABLE IF NOT EXISTS maintenance_events (
  event_id TEXT PRIMARY KEY,
  asset_id TEXT NOT NULL REFERENCES infrastructure_assets(asset_id),
  event_type TEXT NOT NULL,
  event_year INTEGER NOT NULL,
  cost_estimate REAL,
  crew_hours REAL,
  service_disruption_hours REAL,
  notes TEXT
);
