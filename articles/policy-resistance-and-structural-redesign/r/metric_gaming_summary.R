# Metric gaming summary.
path <- file.path("data", "raw", "synthetic_metrics_targets.csv")
if (file.exists(path)) {
  metrics <- read.csv(path)
  print(table(metrics$gaming_risk))
  print(metrics)
}
