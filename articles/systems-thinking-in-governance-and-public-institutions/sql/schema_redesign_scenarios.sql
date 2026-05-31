CREATE TABLE IF NOT EXISTS redesign_scenarios (
    scenario_id TEXT PRIMARY KEY,
    scenario TEXT,
    burden_reduction REAL,
    trust_gain REAL,
    capacity_gain REAL,
    coordination_gain REAL,
    memory_gain REAL,
    public_value_gain REAL
);
