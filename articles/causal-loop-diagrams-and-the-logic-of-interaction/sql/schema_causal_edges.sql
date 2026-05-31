CREATE TABLE IF NOT EXISTS causal_edges (
    edge_id TEXT PRIMARY KEY,
    source_variable TEXT NOT NULL,
    target_variable TEXT NOT NULL,
    polarity TEXT CHECK (polarity IN ('positive', 'negative')),
    delay_steps INTEGER DEFAULT 0,
    mechanism TEXT,
    evidence_note TEXT
);
