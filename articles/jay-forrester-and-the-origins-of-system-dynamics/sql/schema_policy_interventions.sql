CREATE TABLE IF NOT EXISTS policy_interventions (
  policy_id TEXT PRIMARY KEY,
  policy_name TEXT NOT NULL,
  policy_type TEXT NOT NULL,
  expected_effect TEXT,
  likely_delay TEXT,
  likely_compensating_feedback TEXT,
  notes TEXT
);
