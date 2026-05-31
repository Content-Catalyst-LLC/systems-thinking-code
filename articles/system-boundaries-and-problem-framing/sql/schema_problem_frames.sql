CREATE TABLE IF NOT EXISTS problem_frames (
    frame_id TEXT PRIMARY KEY,
    frame_name TEXT NOT NULL,
    primary_question TEXT,
    likely_intervention TEXT,
    main_risk TEXT
);
