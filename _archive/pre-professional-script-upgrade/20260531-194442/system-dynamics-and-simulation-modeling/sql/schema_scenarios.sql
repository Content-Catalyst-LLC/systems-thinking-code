CREATE TABLE IF NOT EXISTS scenarios (
    scenario_id TEXT PRIMARY KEY,
    scenario_name TEXT NOT NULL,
    policy_strength REAL,
    implementation_delay REAL,
    feedback_delay REAL,
    demand_growth_rate REAL,
    capacity_investment_rate REAL,
    notes TEXT
);
