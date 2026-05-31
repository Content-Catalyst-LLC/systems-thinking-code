# Summarize shifting-the-burden output.
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
data_path <- file.path(root, "outputs", "tables", "shifting_the_burden_model.csv")
out_dir <- file.path(root, "outputs", "tables")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

df <- read.csv(data_path)
summary <- data.frame(
  initial_capacity = df$fundamental_capacity[1],
  final_capacity = df$fundamental_capacity[nrow(df)],
  initial_symptom = df$symptom[1],
  final_symptom = df$symptom[nrow(df)]
)
write.csv(summary, file.path(out_dir, "shifting_burden_summary.csv"), row.names = FALSE)
cat("Wrote shifting-the-burden summary\n")
