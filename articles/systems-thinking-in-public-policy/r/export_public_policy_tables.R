root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
scripts <- c(
  "public_policy_indicator_visualization.R",
  "burden_feedback_policy_diagnostics.R",
  "public_trust_trajectory_plots.R",
  "distributional_policy_tables.R",
  "implementation_capacity_summary.R"
)
for (script in scripts) {
  source(file.path(root, "r", script))
}
cat("R public policy workflow complete.\n")
