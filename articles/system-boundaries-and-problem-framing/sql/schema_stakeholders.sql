CREATE TABLE IF NOT EXISTS stakeholders (
    stakeholder_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    affected TEXT,
    included TEXT,
    decision_authority TEXT,
    knowledge_type TEXT,
    burden_score REAL
);
