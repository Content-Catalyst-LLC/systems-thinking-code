CREATE TABLE IF NOT EXISTS learning_cycles (
  cycle_id TEXT PRIMARY KEY,
  period INTEGER NOT NULL,
  feedback_quality REAL CHECK (feedback_quality BETWEEN 0 AND 1),
  participation_quality REAL CHECK (participation_quality BETWEEN 0 AND 1),
  institutional_memory REAL CHECK (institutional_memory BETWEEN 0 AND 1),
  adaptation_action TEXT
);
