CREATE TABLE IF NOT EXISTS delayed_consequences (
    period INTEGER NOT NULL,
    fix_id TEXT NOT NULL,
    delayed_consequence TEXT NOT NULL,
    consequence_level REAL NOT NULL,
    affected_stock TEXT NOT NULL,
    distributional_note TEXT,
    PRIMARY KEY (period, fix_id, delayed_consequence)
);
