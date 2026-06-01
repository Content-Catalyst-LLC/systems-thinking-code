CREATE TABLE IF NOT EXISTS policy_events (
  event_id TEXT PRIMARY KEY,
  period INTEGER NOT NULL,
  event_type TEXT NOT NULL,
  institutional_openness REAL CHECK (institutional_openness BETWEEN 0 AND 1),
  public_visibility REAL CHECK (public_visibility BETWEEN 0 AND 1),
  backlash_pressure REAL CHECK (backlash_pressure BETWEEN 0 AND 1),
  notes TEXT
);
