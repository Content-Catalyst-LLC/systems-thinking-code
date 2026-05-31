CREATE TABLE IF NOT EXISTS causal_relationships (
    relationship_id INTEGER PRIMARY KEY,
    source_variable_id TEXT NOT NULL,
    target_variable_id TEXT NOT NULL,
    polarity TEXT CHECK (polarity IN ('positive', 'negative', 'mixed')),
    delay_category TEXT,
    causal_role TEXT,
    relationship_note TEXT
);
