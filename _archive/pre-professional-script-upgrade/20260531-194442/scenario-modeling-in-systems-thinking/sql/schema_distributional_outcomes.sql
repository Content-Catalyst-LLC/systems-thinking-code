CREATE TABLE IF NOT EXISTS distributional_outcomes (
    scenario_id TEXT NOT NULL,
    group_name TEXT NOT NULL,
    year INTEGER NOT NULL,
    access_index REAL,
    burden_index REAL,
    risk_index REAL,
    PRIMARY KEY (scenario_id, group_name, year)
);
