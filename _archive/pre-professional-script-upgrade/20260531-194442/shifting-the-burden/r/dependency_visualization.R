# Base R dependency visualization.
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = TRUE)
df <- read.csv(file.path(root, "data", "synthetic_dependency_indicators.csv"))
png(file.path(root, "outputs", "figures", "dependency_ratio_plot.png"), width = 900, height = 600)
plot(df$period, df$dependency_ratio, type = "b", xlab = "Period", ylab = "Dependency ratio", main = "Synthetic Dependency Ratio")
dev.off()
