CREATE TABLE IF NOT EXISTS public_value_metrics (
    metric_id TEXT PRIMARY KEY,
    domain TEXT,
    equity REAL,
    access REAL,
    service_quality REAL,
    trust REAL,
    resilience REAL,
    sustainability REAL,
    dignity REAL
);
