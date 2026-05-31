CREATE TABLE IF NOT EXISTS balancing_loops (
    loop_id TEXT PRIMARY KEY,
    loop_name TEXT NOT NULL,
    current_variable TEXT NOT NULL,
    target_variable TEXT NOT NULL,
    correction_variable TEXT NOT NULL,
    description TEXT
);
