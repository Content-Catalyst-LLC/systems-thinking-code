CREATE TABLE IF NOT EXISTS administrative_burden (
    case_id TEXT PRIMARY KEY,
    program TEXT,
    group_name TEXT,
    learning_cost REAL,
    compliance_cost REAL,
    psychological_cost REAL,
    digital_burden REAL,
    appeal_burden REAL,
    support_available REAL
);
