CREATE TABLE IF NOT EXISTS capacity_stocks (
    period INTEGER PRIMARY KEY,
    workforce_capacity REAL,
    infrastructure_condition REAL,
    public_trust REAL,
    repair_capacity REAL,
    administrative_burden REAL
);
