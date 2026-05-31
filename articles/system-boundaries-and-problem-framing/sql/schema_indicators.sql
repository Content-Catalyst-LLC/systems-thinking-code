CREATE TABLE IF NOT EXISTS indicators (
    boundary_id TEXT PRIMARY KEY,
    measured_value REAL,
    internal_cost REAL,
    external_cost REAL,
    stakeholder_inclusion_ratio REAL,
    trust_score REAL,
    resilience_score REAL,
    FOREIGN KEY (boundary_id) REFERENCES system_boundaries(boundary_id)
);
