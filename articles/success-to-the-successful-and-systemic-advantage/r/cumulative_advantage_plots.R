# Base-R summary for cumulative advantage outputs.
# Fallback for direct Rscript execution
root <- normalizePath(file.path(getwd()), mustWork = FALSE)
out_file <- file.path(root, "outputs", "tables", "cumulative_advantage_outputs.csv")
if (!file.exists(out_file)) {
  message("Run python/cumulative_advantage_simulation.py first, or use this script as a template.")
} else {
  d <- read.csv(out_file)
  summary_table <- aggregate(advantage_index ~ period + actor_group, data = d, FUN = mean)
  write.csv(summary_table, file.path(root, "outputs", "tables", "r_cumulative_advantage_summary.csv"), row.names = FALSE)
}
