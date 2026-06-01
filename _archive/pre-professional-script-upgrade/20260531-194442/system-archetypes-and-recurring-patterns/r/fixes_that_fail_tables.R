# Summarize fixes-that-fail output.
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
data_path <- file.path(root, "outputs", "tables", "fixes_that_fail_model.csv")
out_dir <- file.path(root, "outputs", "tables")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

df <- read.csv(data_path)
summary <- data.frame(
  initial_problem = df$problem_level[1],
  final_problem = df$problem_level[nrow(df)],
  max_problem = max(df$problem_level),
  max_quick_fix = max(df$quick_fix)
)
write.csv(summary, file.path(out_dir, "fixes_that_fail_summary.csv"), row.names = FALSE)
cat("Wrote fixes-that-fail summary\n")
