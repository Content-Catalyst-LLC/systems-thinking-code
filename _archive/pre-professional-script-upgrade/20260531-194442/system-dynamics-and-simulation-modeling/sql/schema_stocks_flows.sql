CREATE TABLE IF NOT EXISTS stocks_flows (
    relationship_id TEXT PRIMARY KEY,
    stock_variable_id TEXT NOT NULL,
    flow_variable_id TEXT NOT NULL,
    flow_direction TEXT NOT NULL CHECK (flow_direction IN ('inflow','outflow')),
    notes TEXT,
    FOREIGN KEY (stock_variable_id) REFERENCES model_variables(variable_id),
    FOREIGN KEY (flow_variable_id) REFERENCES model_variables(variable_id)
);
