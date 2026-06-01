CREATE TABLE IF NOT EXISTS outputs (
  output_id INTEGER PRIMARY KEY,
  run_id TEXT NOT NULL,
  output_name TEXT NOT NULL,
  output_path TEXT NOT NULL
);
