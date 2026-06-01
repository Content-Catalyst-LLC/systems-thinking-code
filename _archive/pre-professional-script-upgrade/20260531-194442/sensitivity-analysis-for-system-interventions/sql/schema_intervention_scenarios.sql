CREATE TABLE IF NOT EXISTS intervention_scenarios (
    scenario_id INTEGER PRIMARY KEY,
    scenario_name TEXT NOT NULL,
    description TEXT,
    intervention_type TEXT,
    assumptions_json TEXT
);
