# Basic stock-flow plot from synthetic observations.
root <- normalizePath(file.path(getwd(), ".."), mustWork = FALSE)
if (!dir.exists(file.path(root, "outputs"))) dir.create(file.path(root, "outputs"), recursive = TRUE)
observations <- read.csv(file.path(root, "data", "synthetic_stock_flow_observations.csv"))
png(file.path(root, "outputs", "stock_flow_observations.png"), width = 900, height = 600)
plot(observations$period, observations$trust, type = "l", xlab = "Period", ylab = "Index", main = "Synthetic Trust Stock Over Time")
dev.off()
