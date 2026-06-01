CREATE TABLE IF NOT EXISTS policy_interventions (
  intervention_id TEXT PRIMARY KEY,
  intervention_name TEXT NOT NULL,
  domain TEXT NOT NULL,
  intended_outcome TEXT NOT NULL,
  start_month INTEGER NOT NULL,
  policy_strength REAL NOT NULL,
  implementation_lag_months INTEGER NOT NULL
);
