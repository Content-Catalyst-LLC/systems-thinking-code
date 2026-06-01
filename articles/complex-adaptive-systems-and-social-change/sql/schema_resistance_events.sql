CREATE TABLE IF NOT EXISTS resistance_events (
  event_id TEXT PRIMARY KEY,
  period INTEGER NOT NULL,
  resistance_type TEXT NOT NULL,
  intensity REAL CHECK (intensity BETWEEN 0 AND 1),
  target TEXT,
  notes TEXT
);
