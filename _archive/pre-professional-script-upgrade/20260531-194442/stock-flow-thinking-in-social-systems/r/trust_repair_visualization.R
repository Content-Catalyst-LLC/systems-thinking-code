# Trust repair visualization from synthetic scenario outputs.
root <- normalizePath(file.path(getwd()), mustWork = FALSE)
outdir <- file.path(root, "outputs", "figures")
dir.create(outdir, recursive = TRUE, showWarnings = FALSE)
files <- list.files(file.path(root, "outputs", "tables"), pattern = "^trust_.*[.]csv$", full.names = TRUE)
if (length(files) == 0) {
  message("Run python/trust_legitimacy_repair.py first.")
} else {
  png(file.path(outdir, "trust_repair_scenarios.png"), width = 900, height = 600)
  first <- TRUE
  for (file in files) {
    df <- read.csv(file)
    if (first) {
      plot(df$month, df$public_trust, type = "l", lwd = 2, ylim = c(0, 100), xlab = "Month", ylab = "Public trust", main = "Synthetic Trust Repair Scenarios")
      first <- FALSE
    } else {
      lines(df$month, df$public_trust, lwd = 2, lty = 2)
    }
  }
  legend("bottomright", legend = basename(files), lty = seq_along(files), lwd = 2, bty = "n")
  dev.off()
}
