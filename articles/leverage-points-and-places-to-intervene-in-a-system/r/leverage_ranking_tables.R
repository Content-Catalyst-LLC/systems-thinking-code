# Leverage ranking table from synthetic intervention data
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
data_dir <- file.path(root, "data")
out_dir <- file.path(root, "outputs", "tables")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

leverage <- read.csv(file.path(data_dir, "synthetic_leverage_points.csv"))
interventions <- read.csv(file.path(data_dir, "synthetic_interventions.csv"))
merged <- merge(interventions, leverage, by = "leverage_id")
merged$leverage_score <- merged$expected_strength * 10 - merged$cost_index * 0.5 - merged$implementation_delay_months * 0.05
merged <- merged[order(-merged$leverage_score), ]
write.csv(merged, file.path(out_dir, "r_leverage_ranking.csv"), row.names = FALSE)
print(merged[, c("intervention_name", "leverage_name", "leverage_score")])
