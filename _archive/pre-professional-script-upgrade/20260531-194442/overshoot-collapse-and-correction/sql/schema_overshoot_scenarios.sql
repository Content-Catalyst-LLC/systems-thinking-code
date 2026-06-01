CREATE TABLE IF NOT EXISTS overshoot_scenarios (
  scenario_id TEXT PRIMARY KEY,
  scenario_name TEXT NOT NULL,
  domain TEXT NOT NULL,
  growth_rate REAL NOT NULL,
  feedback_delay INTEGER NOT NULL,
  correction_strength REAL NOT NULL,
  buffer_restoration REAL NOT NULL
);
