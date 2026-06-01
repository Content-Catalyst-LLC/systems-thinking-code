# Relief-versus-repair comparison summary.
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = TRUE)
df <- read.csv(file.path(root, "data", "synthetic_model_runs.csv"))
df$capacity_per_dependency <- round(df$final_capacity / pmax(df$final_dependency, 0.001), 2)
write.csv(df, file.path(root, "outputs", "tables", "relief_repair_comparison.csv"), row.names = FALSE)
print(df)
