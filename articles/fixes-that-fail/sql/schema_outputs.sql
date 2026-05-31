CREATE TABLE IF NOT EXISTS outputs (
    scenario TEXT PRIMARY KEY,
    final_symptom_level REAL NOT NULL,
    minimum_capacity REAL NOT NULL,
    maximum_delayed_consequence REAL NOT NULL,
    interpretation TEXT
);
