root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
input <- file.path(root, "outputs", "tables", "sensitivity_results.csv")
outputs <- file.path(root, "outputs", "tables")
dir.create(outputs, recursive = TRUE, showWarnings = FALSE)
if (file.exists(input)) {
  sensitivity <- read.csv(input)
  sensitivity$rank <- seq_len(nrow(sensitivity))
  write.csv(sensitivity, file.path(outputs, "sensitivity_ranked_table.csv"), row.names = FALSE)
}
