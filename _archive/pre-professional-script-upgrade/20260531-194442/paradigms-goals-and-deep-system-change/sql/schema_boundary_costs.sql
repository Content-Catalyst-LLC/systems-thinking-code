CREATE TABLE IF NOT EXISTS boundary_costs (
  cost_id TEXT PRIMARY KEY,
  scenario_id TEXT NOT NULL,
  cost_name TEXT NOT NULL,
  internal_cost REAL NOT NULL,
  externalized_cost REAL NOT NULL,
  affected_group TEXT,
  time_horizon_years INTEGER
);
