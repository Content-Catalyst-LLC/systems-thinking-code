# Scenario comparison summary using synthetic model outputs.

article_dir <- normalizePath(file.path(getwd()), mustWork = FALSE)
if (basename(article_dir) == "r") article_dir <- normalizePath(file.path(article_dir, ".."), mustWork = FALSE)
input_path <- file.path(article_dir, "data", "synthetic_model_outputs.csv")
output_path <- file.path(article_dir, "outputs", "tables", "scenario_summary_r.csv")
dir.create(dirname(output_path), recursive = TRUE, showWarnings = FALSE)

if (file.exists(input_path)) {
  df <- read.csv(input_path)
  final_rows <- df[ave(df$time_month, df$run_id, FUN = max) == df$time_month, ]
  write.csv(final_rows, output_path, row.names = FALSE)
  print(final_rows)
}
