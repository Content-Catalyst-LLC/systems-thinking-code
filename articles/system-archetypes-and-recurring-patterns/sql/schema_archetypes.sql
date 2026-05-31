CREATE TABLE IF NOT EXISTS archetypes (
    archetype_id TEXT PRIMARY KEY,
    archetype_name TEXT NOT NULL,
    core_structure TEXT NOT NULL,
    primary_risk TEXT,
    typical_leverage_point TEXT
);
