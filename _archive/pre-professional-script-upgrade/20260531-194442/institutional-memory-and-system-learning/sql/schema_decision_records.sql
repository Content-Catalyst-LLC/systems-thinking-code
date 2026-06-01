CREATE TABLE IF NOT EXISTS decision_records (
    decision_id TEXT PRIMARY KEY,
    period INTEGER,
    domain TEXT,
    decision_type TEXT,
    alternatives_recorded INTEGER,
    assumptions_recorded INTEGER,
    risks_recorded INTEGER,
    review_trigger_defined INTEGER,
    used_in_later_decision INTEGER
);
