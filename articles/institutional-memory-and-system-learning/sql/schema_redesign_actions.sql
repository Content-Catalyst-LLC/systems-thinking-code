CREATE TABLE IF NOT EXISTS redesign_actions (
    action_id TEXT PRIMARY KEY,
    period INTEGER,
    domain TEXT,
    action_type TEXT,
    memory_source TEXT,
    authority_connected INTEGER,
    embedded_in_routine INTEGER,
    expected_memory_gain REAL
);
