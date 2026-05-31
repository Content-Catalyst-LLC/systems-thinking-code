CREATE TABLE IF NOT EXISTS group_trajectories (
    group_id TEXT NOT NULL,
    period INTEGER NOT NULL,
    trust REAL,
    administrative_burden REAL,
    household_security REAL,
    capability REAL,
    notes TEXT,
    PRIMARY KEY(group_id, period)
);
