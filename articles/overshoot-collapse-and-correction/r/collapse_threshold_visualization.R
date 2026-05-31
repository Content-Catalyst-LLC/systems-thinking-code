# Collapse threshold visualization using base R.
root <- normalizePath(file.path(getwd()), mustWork = FALSE)
if (!file.exists(file.path(root, "data", "processed", "system_stocks.csv"))) root <- normalizePath(file.path(getwd(), ".."), mustWork = FALSE)
stocks <- read.csv(file.path(root, "data", "processed", "system_stocks.csv"))
out_dir <- file.path(root, "outputs", "figures")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
png(file.path(out_dir, "stock_threshold_margin.png"), width = 900, height = 600)
barplot(stocks$initial_level - stocks$critical_threshold, names.arg = stocks$stock_name, las = 2, main = "Resilience Margin Above Critical Threshold", ylab = "Margin")
dev.off()
