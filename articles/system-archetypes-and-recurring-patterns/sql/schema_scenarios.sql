CREATE TABLE IF NOT EXISTS scenarios (
    scenario_id TEXT PRIMARY KEY,
    scenario_name TEXT NOT NULL,
    archetype_id TEXT NOT NULL,
    intervention_focus TEXT,
    assumption_note TEXT,
    FOREIGN KEY (archetype_id) REFERENCES archetypes(archetype_id)
);
