CREATE TABLE IF NOT EXISTS social_flows (
    flow_id TEXT PRIMARY KEY,
    stock_id TEXT NOT NULL,
    flow_name TEXT NOT NULL,
    direction TEXT CHECK(direction IN ('inflow','outflow')),
    baseline_rate REAL,
    unit TEXT,
    description TEXT,
    FOREIGN KEY(stock_id) REFERENCES social_stocks(stock_id)
);
