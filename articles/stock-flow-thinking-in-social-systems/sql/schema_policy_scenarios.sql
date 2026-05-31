CREATE TABLE IF NOT EXISTS policy_scenarios (
    scenario_id TEXT PRIMARY KEY,
    scenario_name TEXT NOT NULL,
    trust_repair_rate REAL,
    burden_reduction_rate REAL,
    capacity_investment_rate REAL,
    harm_reduction_rate REAL,
    notes TEXT
);
