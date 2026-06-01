# Delay behavior visualization.

article_dir <- dirname(dirname(normalizePath(sys.frame(1)$ofile)))
output_dir <- file.path(article_dir, "outputs")
dir.create(output_dir, showWarnings = FALSE, recursive = TRUE)

indicators <- read.csv(file.path(article_dir, "data", "synthetic_indicators.csv"))

png(file.path(output_dir, "response_delay_over_time.png"), width = 900, height = 600)
plot(
  indicators$period,
  indicators$response_delay,
  type = "l",
  lwd = 3,
  xlab = "Period",
  ylab = "Response Delay",
  main = "Response Delay Over Time"
)
dev.off()

print("Saved outputs/response_delay_over_time.png")
