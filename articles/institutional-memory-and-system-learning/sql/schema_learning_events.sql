CREATE TABLE IF NOT EXISTS learning_events (
    learning_id TEXT PRIMARY KEY,
    period INTEGER,
    domain TEXT,
    event_type TEXT,
    lesson_captured INTEGER,
    lesson_embedded INTEGER,
    authority_connected INTEGER,
    reuse_score REAL
);
