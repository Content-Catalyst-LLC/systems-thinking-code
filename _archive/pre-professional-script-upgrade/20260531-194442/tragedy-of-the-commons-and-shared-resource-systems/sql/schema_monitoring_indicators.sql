CREATE TABLE IF NOT EXISTS monitoring_indicators (
  indicator_id TEXT PRIMARY KEY,
  resource_id TEXT NOT NULL,
  indicator_name TEXT NOT NULL,
  baseline_value REAL,
  warning_threshold REAL,
  critical_threshold REAL,
  direction TEXT,
  FOREIGN KEY (resource_id) REFERENCES shared_resources(resource_id)
);
