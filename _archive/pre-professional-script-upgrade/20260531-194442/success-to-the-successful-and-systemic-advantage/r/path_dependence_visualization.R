# Create a visualization-ready table from path-dependence outputs.
root <- getwd()
file <- file.path(root, "outputs", "tables", "path_dependence_outputs.csv")
if (file.exists(file)) {
  d <- read.csv(file)
  final <- subset(d, period == max(period))
  write.csv(final, file.path(root, "outputs", "tables", "r_path_dependence_final_period.csv"), row.names = FALSE)
} else {
  message("Run python/path_dependence_model.py first.")
}
