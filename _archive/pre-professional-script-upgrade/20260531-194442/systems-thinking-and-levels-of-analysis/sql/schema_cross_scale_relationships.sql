CREATE TABLE IF NOT EXISTS cross_scale_relationships (
    relationship_id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_entity TEXT NOT NULL,
    target_entity TEXT NOT NULL,
    relationship_type TEXT NOT NULL,
    polarity TEXT CHECK (polarity IN ('positive', 'negative')),
    strength REAL,
    delay TEXT
);
