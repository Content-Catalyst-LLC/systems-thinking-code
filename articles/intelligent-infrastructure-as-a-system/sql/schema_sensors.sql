CREATE TABLE IF NOT EXISTS infrastructure_sensors (
  sensor_id TEXT PRIMARY KEY,
  asset_id TEXT NOT NULL REFERENCES infrastructure_assets(asset_id),
  sensor_type TEXT NOT NULL,
  reliability REAL NOT NULL CHECK (reliability BETWEEN 0 AND 1),
  calibration_age_months INTEGER NOT NULL,
  false_alarm_rate REAL CHECK (false_alarm_rate BETWEEN 0 AND 1),
  missed_detection_rate REAL CHECK (missed_detection_rate BETWEEN 0 AND 1)
);
