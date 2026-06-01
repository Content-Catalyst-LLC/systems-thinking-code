-- Systems Thinking SQL schema
-- Educational schema for system variables, causal relationships, loops, scenarios, and model runs.

CREATE TABLE IF NOT EXISTS systems (
    system_id INTEGER PRIMARY KEY,
    system_name TEXT NOT NULL,
    description TEXT NOT NULL,
    boundary_note TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS system_variables (
    variable_id INTEGER PRIMARY KEY,
    system_id INTEGER NOT NULL,
    variable_name TEXT NOT NULL,
    variable_type TEXT NOT NULL,
    unit TEXT,
    description TEXT NOT NULL,
    FOREIGN KEY (system_id) REFERENCES systems(system_id)
);

CREATE TABLE IF NOT EXISTS causal_relationships (
    relationship_id INTEGER PRIMARY KEY,
    system_id INTEGER NOT NULL,
    source_variable_id INTEGER NOT NULL,
    target_variable_id INTEGER NOT NULL,
    polarity TEXT NOT NULL,
    delay_type TEXT NOT NULL,
    evidence_note TEXT,
    FOREIGN KEY (system_id) REFERENCES systems(system_id),
    FOREIGN KEY (source_variable_id) REFERENCES system_variables(variable_id),
    FOREIGN KEY (target_variable_id) REFERENCES system_variables(variable_id)
);

CREATE TABLE IF NOT EXISTS feedback_loops (
    loop_id INTEGER PRIMARY KEY,
    system_id INTEGER NOT NULL,
    loop_name TEXT NOT NULL,
    loop_type TEXT NOT NULL,
    description TEXT NOT NULL,
    FOREIGN KEY (system_id) REFERENCES systems(system_id)
);

CREATE TABLE IF NOT EXISTS scenarios (
    scenario_id INTEGER PRIMARY KEY,
    system_id INTEGER NOT NULL,
    scenario_name TEXT NOT NULL,
    assumptions TEXT NOT NULL,
    FOREIGN KEY (system_id) REFERENCES systems(system_id)
);

CREATE TABLE IF NOT EXISTS model_runs (
    model_run_id INTEGER PRIMARY KEY,
    scenario_id INTEGER NOT NULL,
    run_timestamp TEXT NOT NULL,
    model_name TEXT NOT NULL,
    output_path TEXT NOT NULL,
    interpretation_note TEXT,
    FOREIGN KEY (scenario_id) REFERENCES scenarios(scenario_id)
);

INSERT INTO systems
(system_id, system_name, description, boundary_note)
VALUES
(1, 'Capacity and Resilience System', 'Synthetic example of capacity, disruption, learning, and resilience.', 'Boundary includes capacity, trust, disruption pressure, learning, and recovery.');

INSERT INTO system_variables
(variable_id, system_id, variable_name, variable_type, unit, description)
VALUES
(1, 1, 'Capacity', 'stock', 'index', 'Available system capacity.'),
(2, 1, 'Learning', 'flow', 'index/time', 'Learning that improves adaptive capacity.'),
(3, 1, 'Disruption Pressure', 'external_pressure', 'index', 'Stress imposed on the system.'),
(4, 1, 'Resilience', 'stock', 'index', 'Ability to absorb disruption and recover.'),
(5, 1, 'Public Trust', 'stock', 'index', 'Confidence in system competence and legitimacy.');
