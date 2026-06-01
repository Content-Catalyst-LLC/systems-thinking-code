CREATE TABLE IF NOT EXISTS feedback_loops (
    loop_id TEXT PRIMARY KEY,
    loop_name TEXT NOT NULL,
    loop_type TEXT NOT NULL CHECK (loop_type IN ('reinforcing', 'balancing')),
    description TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
