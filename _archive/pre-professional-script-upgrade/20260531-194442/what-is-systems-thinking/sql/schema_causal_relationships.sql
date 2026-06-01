CREATE TABLE IF NOT EXISTS causal_relationships (
    relationship_id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_variable_id TEXT NOT NULL,
    target_variable_id TEXT NOT NULL,
    polarity TEXT CHECK (polarity IN ('positive', 'negative', 'mixed', 'unknown')),
    delay_type TEXT CHECK (delay_type IN ('none', 'short', 'medium', 'long', 'unknown')),
    relationship_note TEXT,
    FOREIGN KEY (source_variable_id) REFERENCES system_variables(variable_id),
    FOREIGN KEY (target_variable_id) REFERENCES system_variables(variable_id)
);
