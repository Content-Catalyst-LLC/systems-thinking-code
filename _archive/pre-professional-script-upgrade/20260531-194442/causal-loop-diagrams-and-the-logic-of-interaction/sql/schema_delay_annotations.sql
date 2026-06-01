CREATE TABLE IF NOT EXISTS delay_annotations (
    edge_id TEXT PRIMARY KEY,
    delay_type TEXT,
    delay_steps INTEGER,
    why_delay_matters TEXT
);
