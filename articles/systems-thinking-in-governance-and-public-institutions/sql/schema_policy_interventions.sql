CREATE TABLE IF NOT EXISTS policy_interventions (
    policy_id TEXT PRIMARY KEY,
    period INTEGER,
    domain TEXT,
    intervention_type TEXT,
    target_outcome TEXT,
    expected_effect REAL,
    burden_risk REAL,
    feedback_plan INTEGER,
    learning_review INTEGER
);
