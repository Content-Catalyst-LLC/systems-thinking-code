root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
results_path <- file.path(root, "outputs", "tables", "public_policy_scenario_results.csv")
outputs <- file.path(root, "outputs", "tables")
dir.create(outputs, recursive = TRUE, showWarnings = FALSE)
if (file.exists(results_path)) {
  policy_results <- read.csv(results_path)
  scenario_list <- split(policy_results, policy_results$scenario)
  rows <- lapply(scenario_list, function(x) {
    data.frame(
      scenario = x$scenario[1],
      burden_level = mean(x$administrative_burden),
      feedback_closure = mean(x$feedback_closure),
      distribution_gap = mean(x$distribution_gap),
      final_outcome = x$policy_outcome[which.max(x$year)],
      final_trust = x$public_trust[which.max(x$year)]
    )
  })
  diagnostics <- do.call(rbind, rows)
  diagnostics <- diagnostics[order(-diagnostics$final_outcome), ]
  write.csv(diagnostics, file.path(outputs, "burden_feedback_policy_diagnostics.csv"), row.names = FALSE)
  print(diagnostics)
}
