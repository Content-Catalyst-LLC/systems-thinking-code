CREATE TABLE IF NOT EXISTS indicators (
    period INTEGER PRIMARY KEY,
    actual_risk REAL,
    perceived_risk REAL,
    response_delay REAL,
    maintenance_backlog REAL,
    public_trust REAL,
    system_capacity REAL
);
