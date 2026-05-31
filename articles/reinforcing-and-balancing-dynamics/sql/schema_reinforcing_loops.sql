CREATE TABLE IF NOT EXISTS reinforcing_loops (
    loop_id TEXT PRIMARY KEY,
    loop_name TEXT NOT NULL,
    variable_a TEXT NOT NULL,
    variable_b TEXT NOT NULL,
    relationship TEXT NOT NULL,
    description TEXT
);
