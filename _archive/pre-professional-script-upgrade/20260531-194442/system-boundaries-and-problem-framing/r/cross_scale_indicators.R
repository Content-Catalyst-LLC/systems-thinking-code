# Cross-scale indicator summary

article_dir <- dirname(dirname(normalizePath(sys.frame(1)$ofile)))
data_path <- file.path(article_dir, "data", "synthetic_indicators.csv")
output_dir <- file.path(article_dir, "outputs", "tables")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

indicators <- read.csv(data_path)

summary_table <- data.frame(
  boundary_id = indicators$boundary_id,
  trust_score = indicators$trust_score,
  resilience_score = indicators$resilience_score,
  stakeholder_inclusion_ratio = indicators$stakeholder_inclusion_ratio
)

write.csv(summary_table, file.path(output_dir, "cross_scale_indicator_summary.csv"), row.names = FALSE)
print(summary_table)
