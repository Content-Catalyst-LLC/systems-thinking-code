CREATE TABLE IF NOT EXISTS open_system_exchanges (
  exchange_id TEXT PRIMARY KEY,
  system_domain TEXT NOT NULL,
  input_flow TEXT,
  output_flow TEXT,
  externality_risk TEXT,
  boundary_question TEXT
);
