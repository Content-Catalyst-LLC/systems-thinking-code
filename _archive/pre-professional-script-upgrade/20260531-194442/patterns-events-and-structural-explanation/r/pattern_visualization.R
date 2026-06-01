# Pattern visualization for synthetic systems indicators.

article_dir <- dirname(dirname(normalizePath(sys.frame(1)$ofile)))
data_path <- file.path(article_dir, "data", "synthetic_indicators.csv")
output_dir <- file.path(article_dir, "outputs")
dir.create(output_dir, showWarnings = FALSE, recursive = TRUE)

indicators <- read.csv(data_path)

png(file.path(output_dir, "structural_risk_over_time.png"), width = 900, height = 600)
plot(
  indicators$period,
  indicators$structural_risk,
  type = "l",
  lwd = 3,
  xlab = "Period",
  ylab = "Structural Risk",
  main = "Structural Risk Over Time"
)
dev.off()

print("Saved outputs/structural_risk_over_time.png")
