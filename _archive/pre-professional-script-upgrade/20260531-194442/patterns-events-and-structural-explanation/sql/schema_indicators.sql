CREATE TABLE IF NOT EXISTS indicators (
    period INTEGER PRIMARY KEY,
    event_frequency REAL NOT NULL,
    public_trust REAL NOT NULL,
    institutional_capacity REAL NOT NULL,
    response_delay REAL NOT NULL,
    maintenance_backlog REAL NOT NULL,
    workload_pressure REAL NOT NULL,
    resilience_buffer REAL NOT NULL,
    structural_risk REAL NOT NULL
);
