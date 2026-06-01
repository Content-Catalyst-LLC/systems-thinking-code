CREATE TABLE IF NOT EXISTS system_indicators (
    indicator_id INTEGER PRIMARY KEY AUTOINCREMENT,
    scenario_id TEXT,
    period INTEGER NOT NULL,
    variable_id TEXT NOT NULL,
    observed_value REAL NOT NULL,
    FOREIGN KEY (scenario_id) REFERENCES scenarios(scenario_id),
    FOREIGN KEY (variable_id) REFERENCES system_variables(variable_id)
);
