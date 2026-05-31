CREATE TABLE IF NOT EXISTS outputs (
  scenario TEXT NOT NULL,
  period INTEGER NOT NULL,
  high_advantage_mean REAL NOT NULL,
  low_advantage_mean REAL NOT NULL,
  advantage_gap REAL NOT NULL,
  capacity_gap REAL NOT NULL,
  visibility_gap REAL NOT NULL
);
