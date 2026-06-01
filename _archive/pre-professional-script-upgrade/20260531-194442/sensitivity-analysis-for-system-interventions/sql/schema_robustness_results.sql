CREATE TABLE IF NOT EXISTS robustness_results (
    result_id INTEGER PRIMARY KEY,
    policy_name TEXT NOT NULL,
    minimum_score REAL NOT NULL,
    median_score REAL,
    maximum_burden REAL,
    robustness_rank INTEGER
);
