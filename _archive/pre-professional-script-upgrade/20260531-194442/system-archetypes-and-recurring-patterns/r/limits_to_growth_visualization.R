# Run after python/limits_to_growth_simulation.py has generated outputs.
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
data_path <- file.path(root, "outputs", "tables", "limits_to_growth_simulation.csv")
out_dir <- file.path(root, "outputs", "figures")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

df <- read.csv(data_path)
png(file.path(out_dir, "limits_to_growth_curve.png"), width = 900, height = 650)
plot(df$time, df$system_size, type = "l", lwd = 2, xlab = "Time", ylab = "System size", main = "Limits to Growth")
abline(h = unique(df$capacity_limit)[1], lty = 2)
dev.off()
cat("Wrote limits-to-growth plot\n")
