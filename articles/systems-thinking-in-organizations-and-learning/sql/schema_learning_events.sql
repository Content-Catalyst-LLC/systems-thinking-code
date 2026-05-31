CREATE TABLE IF NOT EXISTS learning_events (
  period INTEGER NOT NULL,
  team_id TEXT NOT NULL,
  learning_events INTEGER NOT NULL,
  documented_lessons INTEGER NOT NULL,
  lessons_embedded INTEGER NOT NULL,
  retrospective_quality REAL NOT NULL,
  PRIMARY KEY (period, team_id)
);
