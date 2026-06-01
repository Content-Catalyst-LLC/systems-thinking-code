CREATE TABLE IF NOT EXISTS system_states (
  state_id TEXT PRIMARY KEY,
  scenario_name TEXT NOT NULL,
  period INTEGER NOT NULL,
  system_state REAL NOT NULL,
  reference_goal REAL,
  observed_state REAL,
  notes TEXT
);
