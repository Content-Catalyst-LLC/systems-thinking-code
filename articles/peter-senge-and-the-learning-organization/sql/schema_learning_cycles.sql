CREATE TABLE IF NOT EXISTS learning_cycles (
  cycle_id TEXT PRIMARY KEY,
  period INTEGER NOT NULL,
  feedback_use_index REAL CHECK (feedback_use_index BETWEEN 0 AND 100),
  inquiry_strength REAL CHECK (inquiry_strength BETWEEN 0 AND 100),
  decision_revision_quality REAL CHECK (decision_revision_quality BETWEEN 0 AND 100),
  notes TEXT
);
