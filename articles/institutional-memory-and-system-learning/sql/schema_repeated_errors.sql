CREATE TABLE IF NOT EXISTS repeated_errors (
    error_id TEXT PRIMARY KEY,
    period INTEGER,
    domain TEXT,
    error_type TEXT,
    prior_lesson_available INTEGER,
    lesson_consulted INTEGER,
    repeat_count INTEGER,
    preventability_score REAL
);
