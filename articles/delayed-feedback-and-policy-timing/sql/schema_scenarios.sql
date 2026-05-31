CREATE TABLE IF NOT EXISTS scenarios (
  scenario_id TEXT PRIMARY KEY,
  scenario_name TEXT NOT NULL,
  intervention_timing TEXT NOT NULL,
  monitoring_frequency_months INTEGER NOT NULL,
  correction_strength REAL NOT NULL,
  description TEXT NOT NULL
);
