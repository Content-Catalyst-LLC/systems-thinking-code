CREATE TABLE IF NOT EXISTS repair_scenarios (
    scenario TEXT PRIMARY KEY,
    relief_intensity REAL NOT NULL,
    repair_investment REAL NOT NULL,
    side_effect_monitoring REAL NOT NULL,
    burden_reduction REAL NOT NULL,
    expected_pattern TEXT
);
