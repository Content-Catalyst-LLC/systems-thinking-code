CREATE TABLE IF NOT EXISTS outputs (
    metric TEXT PRIMARY KEY,
    baseline REAL,
    redesign REAL,
    change REAL
);
