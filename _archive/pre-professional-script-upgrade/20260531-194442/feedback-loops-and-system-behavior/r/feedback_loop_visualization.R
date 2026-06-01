# Feedback loop visualization for synthetic indicator data.

article_dir <- dirname(dirname(normalizePath(sys.frame(1)$ofile)))
data_path <- file.path(article_dir, "data", "synthetic_indicators.csv")
output_path <- file.path(article_dir, "outputs", "figures", "trust_delay_behavior.png")

data <- read.csv(data_path)

png(output_path, width = 1000, height = 700)
plot(data$period, data$public_trust, type = "l", lwd = 2,
     xlab = "Period", ylab = "Index / Days",
     main = "Public Trust and Response Delay Over Time")
lines(data$period, data$response_delay, lwd = 2, lty = 2)
legend("topright", legend = c("Public trust", "Response delay"), lty = c(1, 2), lwd = 2)
dev.off()

cat("Wrote", output_path, "\n")
