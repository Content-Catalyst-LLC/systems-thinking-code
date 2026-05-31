# Externality scenario plots with base R

article_dir <- dirname(dirname(normalizePath(sys.frame(1)$ofile)))
data_path <- file.path(article_dir, "data", "synthetic_externalities.csv")
output_dir <- file.path(article_dir, "outputs", "figures")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

externalities <- read.csv(data_path)
externalities$true_cost <- with(externalities, internal_cost + external_cost - external_benefit)

png(file.path(output_dir, "externality_true_costs.png"), width = 900, height = 600)
barplot(
  externalities$true_cost,
  names.arg = externalities$cost_category,
  las = 2,
  main = "Synthetic True Costs Including Externalities",
  ylab = "True cost"
)
dev.off()

print(externalities)
