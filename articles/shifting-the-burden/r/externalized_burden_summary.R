# Externalized burden summary by group.
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = TRUE)
df <- read.csv(file.path(root, "data", "synthetic_externalized_burdens.csv"))
summary_df <- aggregate(burden_score ~ group, data = df, FUN = mean)
names(summary_df)[2] <- "average_burden_score"
write.csv(summary_df, file.path(root, "outputs", "tables", "externalized_burden_summary_r.csv"), row.names = FALSE)
print(summary_df)
