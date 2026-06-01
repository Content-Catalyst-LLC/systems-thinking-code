# Compare final outcomes from synthetic scenario summary.
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
data_path <- file.path(root, "outputs", "tables", "scenario_comparison_summary.csv")
out_dir <- file.path(root, "outputs", "tables")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

df <- read.csv(data_path)
df$problem_change <- df$final_problem - df$initial_problem
df$capacity_change <- df$final_capacity - df$initial_capacity
df$trust_change <- df$final_trust - df$initial_trust
write.csv(df, file.path(out_dir, "recurring_pattern_comparison.csv"), row.names = FALSE)
cat("Wrote recurring-pattern comparison\n")
