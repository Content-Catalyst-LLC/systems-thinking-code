CREATE TABLE IF NOT EXISTS resource_users (
  user_id TEXT PRIMARY KEY,
  user_group TEXT NOT NULL,
  resource_id TEXT NOT NULL,
  baseline_use REAL NOT NULL,
  private_benefit_per_unit REAL,
  private_cost_per_unit REAL,
  governance_compliance REAL,
  relative_power REAL,
  FOREIGN KEY (resource_id) REFERENCES shared_resources(resource_id)
);
