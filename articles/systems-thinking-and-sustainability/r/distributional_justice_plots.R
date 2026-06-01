root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
impacts <- read.csv(file.path(root, "data", "synthetic_distributional_impacts.csv"))
outputs <- file.path(root, "outputs", "tables")
dir.create(outputs, recursive = TRUE, showWarnings = FALSE)
impacts$net_justice <- impacts$benefits - impacts$harms - impacts$transition_costs
write.csv(impacts[order(impacts$net_justice), ], file.path(outputs, "distributional_justice_ranked.csv"), row.names = FALSE)
