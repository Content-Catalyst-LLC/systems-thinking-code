# Constrained growth visualization using base R.
base_dir <- getwd()
input <- file.path(base_dir, "outputs", "tables", "constrained_growth_comparison.csv")
if (!file.exists(input)) input <- file.path(base_dir, "data", "synthetic_growth_variables.csv")
rows <- read.csv(input)
out_dir <- file.path(base_dir, "outputs", "figures")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
png(file.path(out_dir, "constrained_growth_visualization.png"), width = 900, height = 600)
if ("constrained_growth" %in% names(rows)) {
  plot(rows$year, rows$constrained_growth, type = "l", lwd = 2, xlab = "Year", ylab = "Growth", main = "Constrained Growth")
} else {
  plot(rows$year, rows$system_scale, type = "l", lwd = 2, xlab = "Year", ylab = "System scale", main = "Observed Synthetic Growth")
}
dev.off()
