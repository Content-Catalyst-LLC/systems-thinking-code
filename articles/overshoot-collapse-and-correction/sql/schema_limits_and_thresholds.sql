CREATE TABLE IF NOT EXISTS limits_and_thresholds (
  limit_id TEXT PRIMARY KEY,
  domain TEXT NOT NULL,
  pressure_variable TEXT NOT NULL,
  capacity_variable TEXT NOT NULL,
  safe_operating_limit REAL NOT NULL,
  warning_threshold REAL NOT NULL,
  collapse_threshold REAL NOT NULL
);
