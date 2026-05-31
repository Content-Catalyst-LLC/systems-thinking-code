CREATE TABLE IF NOT EXISTS model_runs (
    run_id TEXT NOT NULL,
    scenario_id TEXT NOT NULL,
    time_step INTEGER NOT NULL,
    problem_level REAL,
    capacity REAL,
    trust REAL,
    resource_stock REAL,
    goal_level REAL,
    PRIMARY KEY (run_id, time_step),
    FOREIGN KEY (scenario_id) REFERENCES scenarios(scenario_id)
);
