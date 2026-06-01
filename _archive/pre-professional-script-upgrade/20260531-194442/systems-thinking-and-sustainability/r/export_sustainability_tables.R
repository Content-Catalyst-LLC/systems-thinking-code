root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
scripts <- c("sustainability_indicator_plots.R", "scenario_comparison_visualization.R", "stock_flow_summary_tables.R", "sensitivity_results_tables.R", "distributional_justice_plots.R", "resilience_diagnostics_summary.R")
for (script in scripts) {
  source(file.path(root, "r", script))
}
cat("R sustainability workflow complete.
")
