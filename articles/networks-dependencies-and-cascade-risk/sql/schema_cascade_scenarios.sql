CREATE TABLE IF NOT EXISTS cascade_scenarios (
  scenario_id TEXT PRIMARY KEY,
  scenario_name TEXT NOT NULL,
  initial_failure_nodes TEXT NOT NULL,
  notes TEXT
);
