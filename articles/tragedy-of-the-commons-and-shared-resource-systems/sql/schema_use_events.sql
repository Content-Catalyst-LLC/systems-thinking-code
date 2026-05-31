CREATE TABLE IF NOT EXISTS use_events (
  event_id TEXT PRIMARY KEY,
  resource_id TEXT NOT NULL,
  user_id TEXT NOT NULL,
  event_year INTEGER NOT NULL,
  use_amount REAL NOT NULL,
  reported BOOLEAN DEFAULT TRUE,
  FOREIGN KEY (resource_id) REFERENCES shared_resources(resource_id),
  FOREIGN KEY (user_id) REFERENCES resource_users(user_id)
);
