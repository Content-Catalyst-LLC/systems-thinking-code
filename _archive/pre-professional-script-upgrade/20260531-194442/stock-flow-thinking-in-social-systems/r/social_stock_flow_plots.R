# Social stock-flow plot workflow using synthetic data.
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile %||% getwd()), ".."), mustWork = FALSE)
input <- file.path(root, "outputs", "tables", "social_stock_flow_baseline.csv")
outdir <- file.path(root, "outputs", "figures")
dir.create(outdir, recursive = TRUE, showWarnings = FALSE)

if (!file.exists(input)) {
  message("Run python/social_stock_flow_model.py first to create baseline table.")
} else {
  df <- read.csv(input)
  png(file.path(outdir, "social_stock_flow_baseline.png"), width = 900, height = 600)
  plot(df$month, df$public_trust, type = "l", lwd = 2, ylim = range(df[, -1]), xlab = "Month", ylab = "Index / stock value", main = "Synthetic Social Stock Trajectories")
  lines(df$month, df$household_security, lwd = 2, lty = 2)
  lines(df$month, df$institutional_capacity, lwd = 2, lty = 3)
  lines(df$month, df$capability, lwd = 2, lty = 4)
  legend("topleft", legend = c("Public trust", "Household security", "Institutional capacity", "Capability"), lty = 1:4, lwd = 2, bty = "n")
  dev.off()
}
