CREATE TABLE IF NOT EXISTS interventions (
  intervention_id TEXT PRIMARY KEY,
  intervention_name TEXT NOT NULL,
  leverage_id TEXT,
  cost_index REAL,
  implementation_delay_months REAL,
  expected_strength REAL
);
