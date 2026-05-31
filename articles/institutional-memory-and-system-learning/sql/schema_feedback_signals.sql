CREATE TABLE IF NOT EXISTS feedback_signals (
    signal_id TEXT PRIMARY KEY,
    period INTEGER,
    source_group TEXT,
    domain TEXT,
    signal_type TEXT,
    severity REAL,
    context_preserved INTEGER,
    acted_upon INTEGER,
    loop_closed INTEGER
);
