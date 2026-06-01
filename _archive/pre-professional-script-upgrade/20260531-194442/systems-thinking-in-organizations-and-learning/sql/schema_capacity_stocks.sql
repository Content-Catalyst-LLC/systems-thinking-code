CREATE TABLE IF NOT EXISTS capacity_stocks (
  period INTEGER NOT NULL,
  team_id TEXT NOT NULL,
  capacity REAL NOT NULL,
  recovery REAL NOT NULL,
  depletion REAL NOT NULL,
  PRIMARY KEY (period, team_id)
);
