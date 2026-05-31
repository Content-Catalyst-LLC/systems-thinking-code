CREATE TABLE IF NOT EXISTS events (
    event_id TEXT PRIMARY KEY,
    period INTEGER NOT NULL,
    location TEXT NOT NULL,
    system_area TEXT NOT NULL,
    event_type TEXT NOT NULL,
    severity INTEGER NOT NULL CHECK (severity BETWEEN 1 AND 5),
    affected_group TEXT NOT NULL,
    condition_note TEXT
);
