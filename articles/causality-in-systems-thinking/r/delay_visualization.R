# Delay behavior visualization

script_path <- tryCatch(normalizePath(sys.frame(1)$ofile), error = function(e) file.path(getwd(), "r", "delay_visualization.R"))
article_dir <- dirname(dirname(script_path))
output_dir <- file.path(article_dir, "outputs")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

period <- 1:24
backlog <- numeric(length(period))
capacity <- numeric(length(period))
backlog[1] <- 100
capacity[1] <- 58

for (i in 2:length(period)) {
  backlog[i] <- backlog[i - 1] + 18 - capacity[i - 1] * 0.22
  capacity[i] <- capacity[i - 1] - max(0, backlog[i] - 120) * 0.01
}

png(file.path(output_dir, "delay_accumulation_plot.png"), width = 900, height = 600)
plot(period, backlog, type = "l", lwd = 2, xlab = "Period", ylab = "Backlog", main = "Accumulation Before Visible Failure")
abline(h = 150, lty = 2)
dev.off()

print(data.frame(period = period, backlog = round(backlog, 2), capacity = round(capacity, 2)))
