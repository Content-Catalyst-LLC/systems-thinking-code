CREATE TABLE IF NOT EXISTS documentation_quality (
    asset_id TEXT PRIMARY KEY,
    completeness REAL,
    searchability REAL,
    ownership_defined INTEGER,
    last_review_months INTEGER,
    decision_rationale INTEGER,
    context_preserved INTEGER,
    update_status TEXT
);
