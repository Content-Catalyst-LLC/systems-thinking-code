# Trend summary table for synthetic indicators
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
df <- read.csv(file.path(root, "data", "synthetic_time_series_indicators.csv"))
out_dir <- file.path(root, "outputs")
dir.create(out_dir, showWarnings = FALSE, recursive = TRUE)

metrics <- setdiff(names(df), "year")
summary <- data.frame(
  indicator = metrics,
  first_value = sapply(metrics, function(m) df[[m]][1]),
  last_value = sapply(metrics, function(m) df[[m]][nrow(df)])
)
summary$change <- summary$last_value - summary$first_value
write.csv(summary, file.path(out_dir, "r_trend_summary.csv"), row.names = FALSE)
print(summary)
