CREATE TABLE IF NOT EXISTS coordination_edges (
    source TEXT,
    target TEXT,
    domain TEXT,
    relationship_type TEXT,
    frequency REAL,
    trust REAL,
    shared_data INTEGER,
    shared_authority INTEGER
);
