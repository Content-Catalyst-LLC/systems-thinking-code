CREATE TABLE IF NOT EXISTS archetype_cases (
    case_id TEXT PRIMARY KEY,
    domain TEXT NOT NULL,
    archetype_id TEXT NOT NULL,
    case_name TEXT NOT NULL,
    visible_symptom TEXT,
    structural_hypothesis TEXT,
    FOREIGN KEY (archetype_id) REFERENCES archetypes(archetype_id)
);
