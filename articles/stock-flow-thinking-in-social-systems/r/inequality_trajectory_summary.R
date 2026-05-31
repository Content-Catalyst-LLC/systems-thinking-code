# Inequality trajectory summary using synthetic model output.
root <- normalizePath(file.path(getwd()), mustWork = FALSE)
input <- file.path(root, "outputs", "tables", "inequality_accumulation_trajectories.csv")
out <- file.path(root, "outputs", "tables", "inequality_trajectory_summary.csv")
if (file.exists(input)) {
  df <- read.csv(input)
  summary <- aggregate(wealth_stock ~ group, data = df[df$month == max(df$month), ], FUN = mean)
  write.csv(summary, out, row.names = FALSE)
  message("Wrote ", out)
} else {
  message("Run python/inequality_accumulation_model.py first.")
}
