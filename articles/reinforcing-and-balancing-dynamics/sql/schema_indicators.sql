CREATE TABLE IF NOT EXISTS indicators (
    period INTEGER PRIMARY KEY,
    public_trust REAL,
    institutional_capacity REAL,
    response_delay REAL,
    maintenance_backlog REAL,
    workload REAL,
    stress_load REAL,
    resilience_buffer REAL,
    service_quality REAL
);
