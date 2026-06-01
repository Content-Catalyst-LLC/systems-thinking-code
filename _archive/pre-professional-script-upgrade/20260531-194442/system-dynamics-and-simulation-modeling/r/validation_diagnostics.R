# Lightweight validation diagnostics for synthetic model outputs.

article_dir <- normalizePath(file.path(getwd()), mustWork = FALSE)
if (basename(article_dir) == "r") article_dir <- normalizePath(file.path(article_dir, ".."), mustWork = FALSE)
input_path <- file.path(article_dir, "data", "synthetic_model_outputs.csv")

if (file.exists(input_path)) {
  df <- read.csv(input_path)
  stopifnot(all(df$backlog >= 0))
  stopifnot(all(df$staff_capacity >= 0))
  stopifnot(all(df$public_trust >= 0 & df$public_trust <= 100))
  cat("Validation diagnostics passed.\n")
}
