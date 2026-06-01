CREATE TABLE IF NOT EXISTS scenarios (
    scenario_id TEXT PRIMARY KEY,
    scenario_name TEXT NOT NULL,
    boundary_id TEXT,
    frame_id TEXT,
    internal_cost_weight REAL,
    external_cost_weight REAL,
    stakeholder_weight REAL,
    time_horizon_years INTEGER,
    FOREIGN KEY (boundary_id) REFERENCES system_boundaries(boundary_id),
    FOREIGN KEY (frame_id) REFERENCES problem_frames(frame_id)
);
