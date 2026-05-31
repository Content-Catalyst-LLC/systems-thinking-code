CREATE TABLE IF NOT EXISTS scenarios (
  scenario_id TEXT PRIMARY KEY,
  scenario_name TEXT NOT NULL,
  description TEXT,
  changed_assumption TEXT
);
