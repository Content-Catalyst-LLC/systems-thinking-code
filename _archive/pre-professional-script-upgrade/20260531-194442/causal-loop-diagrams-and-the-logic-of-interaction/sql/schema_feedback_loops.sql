CREATE TABLE IF NOT EXISTS feedback_loops (
    loop_id TEXT PRIMARY KEY,
    loop_name TEXT NOT NULL,
    edge_sequence TEXT NOT NULL,
    expected_polarity TEXT,
    interpretation TEXT
);
