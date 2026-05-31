# Overshoot behavior plots using base R.
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile %||% "r/overshoot_behavior_plots.R"), ".."), mustWork = FALSE)
indicators <- read.csv(file.path(root, "data", "processed", "indicators.csv"))
out_dir <- file.path(root, "outputs", "figures")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
png(file.path(out_dir, "overshoot_pressure_by_domain.png"), width = 900, height = 600)
plot(indicators$month, indicators$pressure, type = "n", xlab = "Month", ylab = "Pressure", main = "Overshoot Pressure by Domain")
for (domain in unique(indicators$domain)) {
  d <- indicators[indicators$domain == domain, ]
  lines(d$month, d$pressure, lwd = 2)
}
legend("topleft", legend = unique(indicators$domain), lty = 1, lwd = 2, bty = "n")
dev.off()
