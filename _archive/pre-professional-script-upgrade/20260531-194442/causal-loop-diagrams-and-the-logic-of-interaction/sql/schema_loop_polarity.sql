CREATE TABLE IF NOT EXISTS loop_polarity_results (
    result_id INTEGER PRIMARY KEY AUTOINCREMENT,
    loop_id TEXT NOT NULL,
    negative_edge_count INTEGER,
    sign_product INTEGER,
    calculated_polarity TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
