CREATE TABLE IF NOT EXISTS memory_assets (
  role_id TEXT PRIMARY KEY,
  decision_records INTEGER,
  active_playbooks INTEGER,
  mentoring_coverage REAL,
  cross_training_score REAL,
  documentation_freshness REAL,
  memory_fragility REAL
);
