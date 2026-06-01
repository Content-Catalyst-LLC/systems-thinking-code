CREATE TABLE IF NOT EXISTS events (
  event_id TEXT PRIMARY KEY,
  event_date DATE NOT NULL,
  system_area TEXT NOT NULL,
  event_type TEXT NOT NULL,
  severity INTEGER,
  location TEXT,
  affected_group TEXT
);
