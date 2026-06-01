CREATE TABLE IF NOT EXISTS stress_tests (
    stress_id TEXT PRIMARY KEY,
    description TEXT NOT NULL,
    severity REAL NOT NULL,
    affected_stock TEXT,
    monitoring_signal TEXT
);
