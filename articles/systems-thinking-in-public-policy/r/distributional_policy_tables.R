root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
impacts <- read.csv(file.path(root, "data", "synthetic_distributional_impacts.csv"))
outputs <- file.path(root, "outputs", "tables")
dir.create(outputs, recursive = TRUE, showWarnings = FALSE)
impacts$net_policy_impact <- impacts$benefits - impacts$burdens - impacts$risks
impacts$access_risk_flag <- ifelse(impacts$access_score < 45, "high access risk", "monitor")
impacts <- impacts[order(impacts$net_policy_impact), ]
write.csv(impacts, file.path(outputs, "distributional_policy_tables.csv"), row.names = FALSE)
print(impacts)
