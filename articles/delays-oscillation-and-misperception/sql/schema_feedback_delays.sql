CREATE TABLE IF NOT EXISTS feedback_delays (
    relationship_id TEXT PRIMARY KEY,
    source TEXT NOT NULL,
    target TEXT NOT NULL,
    delay_periods INTEGER NOT NULL,
    polarity TEXT CHECK (polarity IN ('positive', 'negative')),
    note TEXT
);
