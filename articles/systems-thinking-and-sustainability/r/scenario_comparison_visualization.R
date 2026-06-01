root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
input <- file.path(root, "outputs", "tables", "sustainability_stock_flow_results.csv")
outputs <- file.path(root, "outputs", "tables")
dir.create(outputs, recursive = TRUE, showWarnings = FALSE)
if (file.exists(input)) {
  results <- read.csv(input)
  summary <- aggregate(stock ~ scenario, results, function(x) tail(x, 1))
  names(summary)[2] <- "final_stock"
  write.csv(summary, file.path(outputs, "scenario_comparison_summary.csv"), row.names = FALSE)
}
