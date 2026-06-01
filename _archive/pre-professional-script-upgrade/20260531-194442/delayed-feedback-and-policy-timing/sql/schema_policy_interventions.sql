CREATE TABLE IF NOT EXISTS policy_interventions (
  policy_id TEXT PRIMARY KEY,
  policy_name TEXT NOT NULL,
  domain TEXT NOT NULL,
  adoption_month INTEGER NOT NULL,
  implementation_start_month INTEGER NOT NULL,
  expected_effect_lag_months INTEGER NOT NULL,
  target_stock TEXT NOT NULL,
  policy_intensity REAL NOT NULL
);
