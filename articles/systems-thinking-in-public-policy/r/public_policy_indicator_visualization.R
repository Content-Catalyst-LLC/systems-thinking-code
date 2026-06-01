# R Workflow: Public Policy Indicators, Distributional Diagnostics, and Feedback Visualization
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
results_path <- file.path(root, "outputs", "tables", "public_policy_scenario_results.csv")
outputs <- file.path(root, "outputs", "tables")
dir.create(outputs, recursive = TRUE, showWarnings = FALSE)
if (file.exists(results_path)) {
  policy_results <- read.csv(results_path)
  final_rows <- do.call(rbind, lapply(split(policy_results, policy_results$scenario), function(x) x[which.max(x$year), ]))
  policy_summary <- final_rows[, c("scenario", "policy_outcome", "public_trust", "implementation_capacity", "administrative_burden", "feedback_closure", "distribution_gap")]
  names(policy_summary) <- c("scenario", "final_outcome", "final_trust", "final_capacity", "average_burden", "feedback_closure", "distribution_gap")
  write.csv(policy_summary, file.path(outputs, "r_public_policy_indicator_summary.csv"), row.names = FALSE)
  print(policy_summary)
}
