CREATE TABLE IF NOT EXISTS system_boundaries (
    boundary_id TEXT PRIMARY KEY,
    boundary_name TEXT NOT NULL,
    spatial_scope TEXT,
    time_horizon TEXT,
    level_of_analysis TEXT,
    description TEXT
);
