CREATE TABLE IF NOT EXISTS variety_diagnostics (
  domain TEXT PRIMARY KEY,
  disturbance_variety REAL CHECK (disturbance_variety BETWEEN 0 AND 1),
  response_variety REAL CHECK (response_variety BETWEEN 0 AND 1),
  variety_gap REAL,
  diagnostic TEXT
);
