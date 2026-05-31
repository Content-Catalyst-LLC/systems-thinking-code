# Boundary comparison tables for "System Boundaries and Problem Framing"

article_dir <- dirname(dirname(normalizePath(sys.frame(1)$ofile)))
data_path <- file.path(article_dir, "data", "synthetic_indicators.csv")
output_dir <- file.path(article_dir, "outputs", "tables")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

indicators <- read.csv(data_path)
indicators$net_value_full_boundary <- with(indicators, measured_value - internal_cost - external_cost)
indicators$net_value_narrow_boundary <- with(indicators, measured_value - internal_cost - 0.25 * external_cost)

write.csv(
  indicators,
  file.path(output_dir, "boundary_comparison_table.csv"),
  row.names = FALSE
)

print(indicators)
