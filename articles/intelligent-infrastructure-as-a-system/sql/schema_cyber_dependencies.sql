CREATE TABLE IF NOT EXISTS cyber_dependencies (
  dependency_id TEXT PRIMARY KEY,
  asset_id TEXT NOT NULL REFERENCES infrastructure_assets(asset_id),
  dependency_type TEXT NOT NULL,
  vendor_or_system TEXT,
  dependency_score REAL CHECK (dependency_score BETWEEN 0 AND 100),
  fallback_available BOOLEAN DEFAULT FALSE,
  notes TEXT
);
