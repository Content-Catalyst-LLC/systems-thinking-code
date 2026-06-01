CREATE TABLE IF NOT EXISTS quick_fixes (
    fix_id TEXT PRIMARY KEY,
    fix_name TEXT NOT NULL,
    target_symptom TEXT NOT NULL,
    immediate_effect REAL NOT NULL,
    side_effect_delay INTEGER NOT NULL,
    side_effect_strength REAL NOT NULL,
    notes TEXT
);
