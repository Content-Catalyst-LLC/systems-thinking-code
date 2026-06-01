# Cross-scale indicator visualization using base R

article_dir <- normalizePath(file.path(getwd(), "articles", "systems-thinking-and-levels-of-analysis"), mustWork = FALSE)
if (!dir.exists(article_dir)) article_dir <- normalizePath(file.path(getwd(), ".."), mustWork = FALSE)

indicators <- read.csv(file.path(article_dir, "data", "synthetic_indicators.csv"))
outputs_dir <- file.path(article_dir, "outputs", "figures")
dir.create(outputs_dir, recursive = TRUE, showWarnings = FALSE)

png(file.path(outputs_dir, "system_resilience_over_time.png"), width = 900, height = 600)
plot(indicators$period, indicators$system_resilience, type = "l", lwd = 2,
     xlab = "Period", ylab = "System resilience", main = "System Resilience Over Time")
dev.off()
