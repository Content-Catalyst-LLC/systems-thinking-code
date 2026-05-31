# Behavior-over-time plot using base R.

article_dir <- normalizePath(file.path(dirname(sys.frame(1)$ofile %||% getwd()), ".."), mustWork = FALSE)
input_path <- file.path(article_dir, "data", "synthetic_model_outputs.csv")
output_dir <- file.path(article_dir, "outputs", "figures")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

if (file.exists(input_path)) {
  df <- read.csv(input_path)
  png(file.path(output_dir, "behavior_over_time_backlog.png"), width = 900, height = 600)
  plot(df$time_month, df$backlog, type = "n", xlab = "Month", ylab = "Backlog", main = "Synthetic Backlog Trajectories")
  for (run in unique(df$run_id)) {
    part <- df[df$run_id == run, ]
    lines(part$time_month, part$backlog)
  }
  dev.off()
  cat("Wrote behavior-over-time figure\n")
}

`%||%` <- function(a, b) if (!is.null(a)) a else b
