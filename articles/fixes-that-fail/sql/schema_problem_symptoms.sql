CREATE TABLE IF NOT EXISTS problem_symptoms (
    period INTEGER NOT NULL,
    system TEXT NOT NULL,
    problem_symptom TEXT NOT NULL,
    symptom_level REAL NOT NULL,
    demand_index REAL,
    visible_pressure REAL,
    PRIMARY KEY (period, system, problem_symptom)
);
