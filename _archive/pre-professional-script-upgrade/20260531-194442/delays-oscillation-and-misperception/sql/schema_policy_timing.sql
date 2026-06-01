CREATE TABLE IF NOT EXISTS policy_timing (
    policy_id TEXT PRIMARY KEY,
    policy_name TEXT NOT NULL,
    start_period INTEGER,
    implementation_delay INTEGER,
    evaluation_period INTEGER,
    expected_effect_direction TEXT
);
