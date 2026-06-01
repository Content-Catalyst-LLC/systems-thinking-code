# Policy repair scenario comparison summary.
root <- normalizePath(file.path(getwd()), mustWork = FALSE)
input <- file.path(root, "outputs", "tables", "policy_repair_scenario_comparison.csv")
out <- file.path(root, "outputs", "tables", "policy_repair_final_values.csv")
if (file.exists(input)) {
  df <- read.csv(input)
  final <- df[df$month == max(df$month), ]
  write.csv(final, out, row.names = FALSE)
  message("Wrote ", out)
} else {
  message("Run python/policy_repair_scenario_comparison.py first.")
}
