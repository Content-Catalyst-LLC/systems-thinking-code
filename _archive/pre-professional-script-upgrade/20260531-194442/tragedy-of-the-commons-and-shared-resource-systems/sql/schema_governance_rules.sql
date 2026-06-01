CREATE TABLE IF NOT EXISTS governance_rules (
  rule_id TEXT PRIMARY KEY,
  resource_id TEXT NOT NULL,
  scenario TEXT NOT NULL,
  quota_multiplier REAL,
  monitoring_strength REAL,
  sanction_strength REAL,
  restoration_investment REAL,
  participation_score REAL,
  FOREIGN KEY (resource_id) REFERENCES shared_resources(resource_id)
);
