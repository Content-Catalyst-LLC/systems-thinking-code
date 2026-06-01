-- Professional schema for resilience, thresholds, and regime shifts.
-- Intended for SQLite/PostgreSQL-style adaptation.

CREATE TABLE IF NOT EXISTS resilience_scenarios (
  scenario_id INTEGER PRIMARY KEY,
  scenario_name TEXT NOT NULL,
  intervention_year INTEGER,
  transformation_effect REAL,
  notes TEXT
);

CREATE TABLE IF NOT EXISTS resilience_timeseries (
  scenario_id INTEGER NOT NULL,
  year INTEGER NOT NULL,
  resilience REAL NOT NULL,
  pressure REAL NOT NULL,
  threshold_margin REAL NOT NULL,
  recovery_time_index REAL NOT NULL,
  regime TEXT NOT NULL,
  PRIMARY KEY (scenario_id, year)
);

CREATE TABLE IF NOT EXISTS vulnerability_groups (
  group_name TEXT PRIMARY KEY,
  exposure REAL NOT NULL,
  sensitivity REAL NOT NULL,
  adaptive_capacity REAL NOT NULL,
  voice REAL NOT NULL,
  vulnerability_index REAL NOT NULL,
  priority TEXT NOT NULL
);
