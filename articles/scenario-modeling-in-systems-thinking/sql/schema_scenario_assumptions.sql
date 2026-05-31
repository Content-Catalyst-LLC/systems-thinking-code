CREATE TABLE IF NOT EXISTS scenario_assumptions (
    scenario_id TEXT NOT NULL,
    assumption_name TEXT NOT NULL,
    assumption_value REAL,
    assumption_units TEXT,
    rationale TEXT,
    PRIMARY KEY (scenario_id, assumption_name)
);
