CREATE TABLE IF NOT EXISTS externalities (
    externality_id TEXT PRIMARY KEY,
    boundary_id TEXT,
    cost_category TEXT,
    internal_cost REAL,
    external_cost REAL,
    external_benefit REAL,
    notes TEXT,
    FOREIGN KEY (boundary_id) REFERENCES system_boundaries(boundary_id)
);
