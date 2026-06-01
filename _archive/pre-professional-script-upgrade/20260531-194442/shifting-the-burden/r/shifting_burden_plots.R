# Synthetic shifting-the-burden plot data export.
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = TRUE)
input <- file.path(root, "data", "synthetic_dependency_indicators.csv")
output <- file.path(root, "outputs", "tables", "r_dependency_summary.csv")

df <- read.csv(input)
summary_df <- data.frame(
  metric = c("initial_dependency", "final_dependency", "max_dependency"),
  value = c(df$dependency_ratio[1], tail(df$dependency_ratio, 1), max(df$dependency_ratio))
)

dir.create(dirname(output), recursive = TRUE, showWarnings = FALSE)
write.csv(summary_df, output, row.names = FALSE)
print(summary_df)
