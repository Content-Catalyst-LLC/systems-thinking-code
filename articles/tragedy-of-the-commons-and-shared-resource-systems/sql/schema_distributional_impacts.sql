CREATE TABLE IF NOT EXISTS distributional_impacts (
  impact_id TEXT PRIMARY KEY,
  resource_id TEXT NOT NULL,
  user_group TEXT NOT NULL,
  benefit_share REAL,
  depletion_burden_share REAL,
  voice_in_governance REAL,
  vulnerability_score REAL,
  FOREIGN KEY (resource_id) REFERENCES shared_resources(resource_id)
);
