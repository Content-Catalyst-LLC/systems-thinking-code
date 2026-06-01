CREATE TABLE IF NOT EXISTS interventions (
    intervention_id TEXT PRIMARY KEY,
    scenario_id TEXT NOT NULL,
    start_year INTEGER,
    capacity_boost REAL,
    burden_reduction REAL,
    repair_flow REAL
);
