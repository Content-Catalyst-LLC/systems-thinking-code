# Resource depletion summary table.
base_dir <- getwd()
input <- file.path(base_dir, "data", "synthetic_resource_stocks.csv")
rows <- read.csv(input)
summary_table <- data.frame(
  starting_resource = rows$resource_stock[1],
  ending_resource = rows$resource_stock[nrow(rows)],
  minimum_resource = min(rows$resource_stock),
  maximum_extraction = max(rows$extraction)
)
out_dir <- file.path(base_dir, "outputs", "tables")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
write.csv(summary_table, file.path(out_dir, "resource_depletion_summary.csv"), row.names = FALSE)
