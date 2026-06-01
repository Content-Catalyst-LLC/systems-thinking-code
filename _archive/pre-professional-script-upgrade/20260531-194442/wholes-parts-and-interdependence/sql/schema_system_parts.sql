CREATE TABLE IF NOT EXISTS system_parts (
    part_id TEXT PRIMARY KEY,
    part_name TEXT NOT NULL,
    level TEXT NOT NULL,
    part_type TEXT NOT NULL,
    criticality TEXT NOT NULL,
    baseline_capacity REAL NOT NULL
);
