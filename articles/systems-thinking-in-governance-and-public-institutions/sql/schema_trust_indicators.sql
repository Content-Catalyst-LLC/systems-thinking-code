CREATE TABLE IF NOT EXISTS trust_indicators (
    period INTEGER,
    domain TEXT,
    reliability REAL,
    fairness REAL,
    accountability REAL,
    harm REAL,
    burden REAL,
    opacity REAL,
    trust_score REAL
);
