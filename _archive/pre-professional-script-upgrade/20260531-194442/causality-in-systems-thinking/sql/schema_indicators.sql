CREATE TABLE IF NOT EXISTS indicators (
    period INTEGER PRIMARY KEY,
    public_trust REAL,
    institutional_capacity REAL,
    service_demand REAL,
    response_delay REAL,
    maintenance_backlog REAL,
    adaptive_capacity REAL
);
