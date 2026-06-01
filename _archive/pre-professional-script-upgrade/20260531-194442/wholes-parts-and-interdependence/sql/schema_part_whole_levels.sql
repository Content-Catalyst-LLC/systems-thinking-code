CREATE TABLE IF NOT EXISTS part_whole_levels (
    level_id TEXT PRIMARY KEY,
    level_name TEXT NOT NULL,
    parent_level TEXT,
    description TEXT
);
