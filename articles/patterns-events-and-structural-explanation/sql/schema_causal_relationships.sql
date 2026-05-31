CREATE TABLE IF NOT EXISTS causal_relationships (
    relationship_id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_variable TEXT NOT NULL,
    target_variable TEXT NOT NULL,
    polarity TEXT NOT NULL CHECK (polarity IN ('positive', 'negative')),
    delay TEXT NOT NULL,
    relationship_note TEXT
);
