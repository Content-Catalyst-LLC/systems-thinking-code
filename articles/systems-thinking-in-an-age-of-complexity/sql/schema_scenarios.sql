CREATE TABLE IF NOT EXISTS scenarios (
  scenario_id TEXT PRIMARY KEY,
  scenario_name TEXT NOT NULL,
  complexity_pressure REAL,
  resilience_capacity REAL,
  accountability_score REAL,
  harm_exposure REAL,
  transformation_capacity REAL
);
