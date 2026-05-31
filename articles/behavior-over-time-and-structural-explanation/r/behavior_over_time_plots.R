# Behavior-over-time plots for synthetic indicators
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
data_path <- file.path(root, "data", "synthetic_time_series_indicators.csv")
out_dir <- file.path(root, "outputs")
dir.create(out_dir, showWarnings = FALSE, recursive = TRUE)

df <- read.csv(data_path)
metrics <- c("maintenance_backlog", "service_delay_index", "public_trust", "workload_index", "turnover_rate")

for (metric in metrics) {
  png(file.path(out_dir, paste0(metric, "_r_plot.png")), width = 900, height = 600)
  plot(df$year, df[[metric]], type = "b", xlab = "Year", ylab = metric, main = gsub("_", " ", metric))
  dev.off()
}
