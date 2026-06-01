CREATE TABLE IF NOT EXISTS indicators (
    scenario_id TEXT,
    period INTEGER,
    variable_id TEXT,
    value REAL,
    PRIMARY KEY (scenario_id, period, variable_id),
    FOREIGN KEY (scenario_id) REFERENCES scenarios(scenario_id),
    FOREIGN KEY (variable_id) REFERENCES loop_variables(variable_id)
);
