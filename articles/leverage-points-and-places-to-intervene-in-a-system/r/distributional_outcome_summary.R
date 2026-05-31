root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
data_dir <- file.path(root, "data")
out_dir <- file.path(root, "outputs", "tables")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

df <- read.csv(file.path(data_dir, "synthetic_distributional_outcomes.csv"))
df$burden_reduction <- df$baseline_burden - df$post_intervention_burden
df$access_gain <- df$post_intervention_access - df$baseline_access
write.csv(df, file.path(out_dir, "r_distributional_outcomes.csv"), row.names = FALSE)
print(df[, c("group_name", "burden_reduction", "access_gain")])
