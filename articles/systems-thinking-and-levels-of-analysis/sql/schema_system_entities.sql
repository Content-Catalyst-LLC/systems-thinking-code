CREATE TABLE IF NOT EXISTS system_entities (
    entity_id TEXT PRIMARY KEY,
    entity_name TEXT NOT NULL,
    level_id TEXT NOT NULL,
    parent_entity_id TEXT,
    baseline_capacity REAL,
    risk_exposure REAL,
    FOREIGN KEY (level_id) REFERENCES system_levels(level_id)
);
