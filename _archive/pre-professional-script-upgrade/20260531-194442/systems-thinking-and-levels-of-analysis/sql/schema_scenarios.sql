CREATE TABLE IF NOT EXISTS scenarios (
    scenario_id TEXT PRIMARY KEY,
    scenario_name TEXT NOT NULL,
    individual_support REAL,
    organizational_capacity REAL,
    institutional_reform REAL,
    network_redundancy REAL,
    ecological_stress REAL
);
