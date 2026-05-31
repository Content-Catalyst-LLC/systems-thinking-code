# Correction scenario comparison.
root <- normalizePath(file.path(getwd()), mustWork = FALSE)
if (!file.exists(file.path(root, "data", "processed", "outcomes.csv"))) root <- normalizePath(file.path(getwd(), ".."), mustWork = FALSE)
outcomes <- read.csv(file.path(root, "data", "processed", "outcomes.csv"))
out_dir <- file.path(root, "outputs", "tables")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
summary <- aggregate(cbind(system_performance, stock_level, correction_cost, distributional_burden) ~ scenario_id, data = outcomes[outcomes$month == max(outcomes$month), ], FUN = mean)
write.csv(summary, file.path(out_dir, "correction_comparison_final.csv"), row.names = FALSE)
