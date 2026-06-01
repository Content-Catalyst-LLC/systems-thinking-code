CREATE TABLE IF NOT EXISTS feedback_loops (
    loop_id TEXT PRIMARY KEY,
    archetype_id TEXT NOT NULL,
    loop_name TEXT NOT NULL,
    loop_type TEXT CHECK(loop_type IN ('reinforcing','balancing')),
    description TEXT,
    FOREIGN KEY (archetype_id) REFERENCES archetypes(archetype_id)
);
