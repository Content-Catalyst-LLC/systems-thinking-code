CREATE TABLE IF NOT EXISTS institutional_memory_assets (
  memory_id TEXT PRIMARY KEY,
  memory_asset TEXT NOT NULL,
  baseline_quality REAL CHECK (baseline_quality BETWEEN 0 AND 100),
  target_quality REAL CHECK (target_quality BETWEEN 0 AND 100),
  loss_risk TEXT,
  notes TEXT
);
