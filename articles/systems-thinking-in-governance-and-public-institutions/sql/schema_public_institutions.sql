CREATE TABLE IF NOT EXISTS public_institutions (
    institution_id TEXT PRIMARY KEY,
    institution_type TEXT NOT NULL,
    domain TEXT NOT NULL,
    service_population INTEGER,
    capacity_score REAL,
    trust_score REAL,
    coordination_score REAL,
    memory_score REAL
);
