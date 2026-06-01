article_root <- if (basename(getwd()) == "r") normalizePath("..") else normalizePath(".")
out_dir <- file.path(article_root, "outputs", "tables")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
robust <- read.csv(file.path(article_root, "data", "synthetic_robustness_results.csv"))
robust <- robust[order(robust$robustness_rank), ]
write.csv(robust, file.path(out_dir, "r_robustness_summary.csv"), row.names = FALSE)
