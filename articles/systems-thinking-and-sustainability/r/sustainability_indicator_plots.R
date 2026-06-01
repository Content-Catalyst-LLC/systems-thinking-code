# R Workflow: Indicator Visualization, Sensitivity Tables, and Sustainability Diagnostics
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
indicators <- read.csv(file.path(root, "data", "synthetic_sustainability_indicators.csv"))
outputs <- file.path(root, "outputs", "tables")
dir.create(outputs, recursive = TRUE, showWarnings = FALSE)
indicators$gap_to_target <- ifelse(indicators$direction == "increase", indicators$target - indicators$current, indicators$current - indicators$target)
write.csv(indicators, file.path(outputs, "sustainability_indicator_gap_table.csv"), row.names = FALSE)
