# Simple delay-sensitivity visualization with base R
simulate <- function(delay, k, periods = 20) {
  goal <- 50
  values <- rep(80, delay + 1)
  for (i in seq_len(periods)) {
    perceived <- values[length(values) - delay]
    correction <- k * (goal - perceived)
    values <- c(values, tail(values, 1) + correction)
  }
  values[(delay + 2):length(values)]
}

root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
out_dir <- file.path(root, "outputs", "figures")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
png(file.path(out_dir, "r_delay_sensitivity.png"), width = 900, height = 600)
plot(simulate(1, 0.25), type = "l", ylim = c(0, 90), xlab = "Time", ylab = "System state", main = "Delay Sensitivity")
lines(simulate(3, 0.25), lty = 2)
lines(simulate(6, 0.25), lty = 3)
legend("topright", legend = c("delay 1", "delay 3", "delay 6"), lty = c(1, 2, 3))
dev.off()
