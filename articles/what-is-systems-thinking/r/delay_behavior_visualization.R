# Delay behavior visualization using base R.

period <- 1:30
no_delay <- 100 * (1 - exp(-0.20 * period))
with_delay <- ifelse(period < 8, 0, 100 * (1 - exp(-0.16 * (period - 7))))

output_dir <- file.path(dirname(dirname(normalizePath(commandArgs(trailingOnly = FALSE)[grep("^--file=", commandArgs(trailingOnly = FALSE))] |> sub("^--file=", "", x = _)))), "outputs")
if (!dir.exists(output_dir)) dir.create(output_dir, recursive = TRUE)

png(file.path(output_dir, "delay_behavior_visualization.png"), width = 900, height = 600)
plot(period, no_delay, type = "l", lwd = 2, ylim = c(0, 105), xlab = "Period", ylab = "Response", main = "Delay Behavior in a Simple System")
lines(period, with_delay, lwd = 2, lty = 2)
legend("bottomright", legend = c("No delay", "Delayed response"), lwd = 2, lty = c(1, 2))
dev.off()
