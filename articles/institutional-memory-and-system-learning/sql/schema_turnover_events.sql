CREATE TABLE IF NOT EXISTS turnover_events (
    period INTEGER,
    team TEXT,
    turnover_count INTEGER,
    critical_role_departures INTEGER,
    handoff_quality REAL,
    onboarding_burden REAL,
    relationship_loss_score REAL
);
