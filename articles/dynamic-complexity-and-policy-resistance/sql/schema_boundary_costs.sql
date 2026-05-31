CREATE TABLE IF NOT EXISTS boundary_costs (
  cost_id TEXT PRIMARY KEY,
  source_policy TEXT NOT NULL,
  cost_shifted_to TEXT NOT NULL,
  cost_type TEXT NOT NULL,
  delay_months INTEGER NOT NULL,
  relative_magnitude REAL NOT NULL
);
