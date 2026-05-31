# Problem frame summary

article_dir <- dirname(dirname(normalizePath(sys.frame(1)$ofile)))
frames_path <- file.path(article_dir, "data", "synthetic_problem_frames.csv")
output_dir <- file.path(article_dir, "outputs", "tables")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

frames <- read.csv(frames_path)
write.csv(frames, file.path(output_dir, "problem_frame_summary.csv"), row.names = FALSE)

print(frames)
