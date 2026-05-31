CREATE TABLE IF NOT EXISTS correction_actions (
  action_id TEXT PRIMARY KEY,
  scenario_id TEXT NOT NULL,
  action_name TEXT NOT NULL,
  action_month INTEGER NOT NULL,
  pressure_reduction REAL NOT NULL,
  restoration_increase REAL NOT NULL,
  feedback_improvement REAL NOT NULL,
  equity_priority TEXT NOT NULL
);
