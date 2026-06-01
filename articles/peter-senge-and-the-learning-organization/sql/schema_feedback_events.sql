CREATE TABLE IF NOT EXISTS feedback_events (
  event_id TEXT PRIMARY KEY,
  period INTEGER NOT NULL,
  event_type TEXT NOT NULL,
  feedback_quality REAL CHECK (feedback_quality BETWEEN 0 AND 1),
  psychological_safety REAL CHECK (psychological_safety BETWEEN 0 AND 1),
  decision_revision REAL CHECK (decision_revision BETWEEN 0 AND 1),
  notes TEXT
);
