# Stakeholder matrix visualization with base R

article_dir <- dirname(dirname(normalizePath(sys.frame(1)$ofile)))
data_path <- file.path(article_dir, "data", "synthetic_stakeholders.csv")
output_dir <- file.path(article_dir, "outputs", "figures")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

stakeholders <- read.csv(data_path)

png(file.path(output_dir, "stakeholder_burden_scores.png"), width = 900, height = 600)
barplot(
  stakeholders$burden_score,
  names.arg = stakeholders$name,
  las = 2,
  main = "Synthetic Stakeholder Burden Scores",
  ylab = "Burden score"
)
dev.off()

print(stakeholders)
