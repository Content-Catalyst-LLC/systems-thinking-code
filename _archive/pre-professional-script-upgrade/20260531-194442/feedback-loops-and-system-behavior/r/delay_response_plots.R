# Simulate and plot delayed balancing response.

periods <- 40
goal <- 100
value <- 40
delay <- 5
correction <- 0.35
history <- rep(value, delay + 1)
rows <- data.frame(period = integer(), value = numeric())

for (period in seq_len(periods)) {
  observed <- history[1]
  value <- value + correction * (goal - observed)
  history <- c(history[-1], value)
  rows <- rbind(rows, data.frame(period = period, value = value))
}

article_dir <- dirname(dirname(normalizePath(sys.frame(1)$ofile)))
output_path <- file.path(article_dir, "outputs", "figures", "delayed_response.png")

png(output_path, width = 1000, height = 700)
plot(rows$period, rows$value, type = "l", lwd = 2,
     xlab = "Period", ylab = "Value",
     main = "Delayed Balancing Response")
abline(h = goal, lty = 2)
dev.off()

cat("Wrote", output_path, "\n")
