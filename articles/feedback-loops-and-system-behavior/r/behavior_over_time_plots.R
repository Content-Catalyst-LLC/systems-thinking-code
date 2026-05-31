# Behavior-over-time plots for feedback-loop indicators.

article_dir <- dirname(dirname(normalizePath(sys.frame(1)$ofile)))
data_path <- file.path(article_dir, "data", "synthetic_indicators.csv")
output_path <- file.path(article_dir, "outputs", "figures", "behavior_over_time.png")

data <- read.csv(data_path)

png(output_path, width = 1000, height = 700)
plot(data$period, data$maintenance_backlog, type = "l", lwd = 2,
     xlab = "Period", ylab = "Value",
     main = "Maintenance Backlog and System Capacity")
lines(data$period, data$system_capacity, lwd = 2, lty = 2)
legend("topleft", legend = c("Maintenance backlog", "System capacity"), lty = c(1, 2), lwd = 2)
dev.off()

cat("Wrote", output_path, "\n")
