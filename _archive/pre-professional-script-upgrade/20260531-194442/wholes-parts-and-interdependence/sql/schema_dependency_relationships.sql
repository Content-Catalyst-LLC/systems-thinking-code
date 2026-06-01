CREATE TABLE IF NOT EXISTS dependency_relationships (
    relationship_id INTEGER PRIMARY KEY AUTOINCREMENT,
    source_part TEXT NOT NULL,
    target_part TEXT NOT NULL,
    dependency_type TEXT NOT NULL,
    weight REAL NOT NULL,
    delay TEXT NOT NULL,
    relationship_note TEXT,
    FOREIGN KEY (source_part) REFERENCES system_parts(part_name),
    FOREIGN KEY (target_part) REFERENCES system_parts(part_name)
);
