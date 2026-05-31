CREATE TABLE IF NOT EXISTS memory_assets (
    asset_id TEXT PRIMARY KEY,
    asset_type TEXT NOT NULL,
    domain TEXT NOT NULL,
    owner_role TEXT,
    freshness_score REAL,
    accessibility_score REAL,
    context_score REAL,
    authority_link_score REAL
);
