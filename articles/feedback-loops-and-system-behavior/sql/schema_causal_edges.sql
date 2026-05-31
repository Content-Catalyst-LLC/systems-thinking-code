CREATE TABLE IF NOT EXISTS causal_edges (
    edge_id TEXT PRIMARY KEY,
    source_variable_id TEXT NOT NULL,
    target_variable_id TEXT NOT NULL,
    polarity TEXT NOT NULL CHECK (polarity IN ('positive', 'negative')),
    delay_category TEXT,
    relationship_note TEXT,
    FOREIGN KEY (source_variable_id) REFERENCES loop_variables(variable_id),
    FOREIGN KEY (target_variable_id) REFERENCES loop_variables(variable_id)
);
