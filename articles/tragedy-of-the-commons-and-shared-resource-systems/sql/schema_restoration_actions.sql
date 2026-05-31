CREATE TABLE IF NOT EXISTS restoration_actions (
  action_id TEXT PRIMARY KEY,
  resource_id TEXT NOT NULL,
  action_name TEXT NOT NULL,
  annual_cost REAL,
  expected_recovery_rate REAL,
  distributional_priority TEXT,
  implementation_delay INTEGER,
  FOREIGN KEY (resource_id) REFERENCES shared_resources(resource_id)
);
