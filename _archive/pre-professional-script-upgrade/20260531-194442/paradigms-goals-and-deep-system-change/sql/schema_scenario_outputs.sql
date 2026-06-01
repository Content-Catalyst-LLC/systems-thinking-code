CREATE TABLE IF NOT EXISTS scenario_outputs (
  scenario_id TEXT NOT NULL,
  scenario_name TEXT NOT NULL,
  year INTEGER NOT NULL,
  throughput REAL,
  access REAL,
  dignity REAL,
  resilience REAL,
  burden REAL,
  harm REAL,
  total_score REAL,
  PRIMARY KEY (scenario_id, year)
);
