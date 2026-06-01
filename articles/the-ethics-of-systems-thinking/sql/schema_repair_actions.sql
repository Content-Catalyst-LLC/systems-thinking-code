CREATE TABLE IF NOT EXISTS repair_actions (
  repair_id TEXT PRIMARY KEY,
  repair_type TEXT NOT NULL,
  repair_depth REAL CHECK (repair_depth BETWEEN 0 AND 1),
  affected_voice_required REAL CHECK (affected_voice_required BETWEEN 0 AND 1),
  structural_change_required REAL CHECK (structural_change_required BETWEEN 0 AND 1),
  notes TEXT
);
