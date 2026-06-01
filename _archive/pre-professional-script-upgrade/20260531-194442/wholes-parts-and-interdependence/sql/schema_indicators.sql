CREATE TABLE IF NOT EXISTS indicators (
    period INTEGER PRIMARY KEY,
    system_capacity REAL NOT NULL,
    dependency_stress REAL NOT NULL,
    resilience_buffer REAL NOT NULL,
    coordination_quality REAL NOT NULL,
    local_performance REAL NOT NULL,
    whole_system_outcome REAL NOT NULL
);
