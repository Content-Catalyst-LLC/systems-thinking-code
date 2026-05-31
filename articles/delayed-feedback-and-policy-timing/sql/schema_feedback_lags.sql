CREATE TABLE IF NOT EXISTS feedback_lags (
  lag_id TEXT PRIMARY KEY,
  policy_id TEXT NOT NULL,
  effect_lag_months INTEGER NOT NULL,
  information_lag_months INTEGER NOT NULL,
  decision_lag_months INTEGER NOT NULL,
  implementation_lag_months INTEGER NOT NULL,
  recovery_lag_months INTEGER NOT NULL,
  FOREIGN KEY (policy_id) REFERENCES policy_interventions(policy_id)
);
