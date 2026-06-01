CREATE TABLE IF NOT EXISTS complexity_indicators (
  indicator_id TEXT PRIMARY KEY,
  scenario_name TEXT NOT NULL,
  interdependence REAL CHECK (interdependence BETWEEN 0 AND 1),
  feedback_intensity REAL CHECK (feedback_intensity BETWEEN 0 AND 1),
  delay_pressure REAL CHECK (delay_pressure BETWEEN 0 AND 1),
  adaptation_rate REAL CHECK (adaptation_rate BETWEEN 0 AND 1),
  uncertainty REAL CHECK (uncertainty BETWEEN 0 AND 1)
);
