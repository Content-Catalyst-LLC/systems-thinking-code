# Base-R early warning diagnostics for resilience outputs.

root <- getwd()
if (basename(root) == "r") {
  root <- normalizePath(file.path(root, ".."), mustWork = FALSE)
}
table_dir <- file.path(root, "outputs", "tables")
dir.create(table_dir, recursive = TRUE, showWarnings = FALSE)

path <- file.path(table_dir, "resilience_threshold_regime_results.csv")
if (!file.exists(path)) {
  stop("Missing resilience results. Run python/run_all_resilience_workflows.py first.")
}

df <- read.csv(path, stringsAsFactors = FALSE)
scenarios <- unique(df$scenario)

roll_var <- function(x, n = 6) {
  out <- rep(NA_real_, length(x))
  for (i in seq_along(x)) {
    if (i >= n) out[i] <- var(x[(i - n + 1):i])
  }
  out
}

rows <- list()
for (s in scenarios) {
  x <- df[df$scenario == s, ]
  margin_var <- roll_var(x$threshold_margin, 6)
  warning <- x$threshold_margin <= 15 | x$recovery_time_index >= 0.80 | (!is.na(margin_var) & margin_var > median(margin_var, na.rm = TRUE))
  rows[[s]] <- data.frame(
    scenario = s,
    warning_years = sum(warning, na.rm = TRUE),
    peak_recovery_time = max(x$recovery_time_index),
    lowest_margin = min(x$threshold_margin),
    first_shifted_year = ifelse(any(x$regime == "shifted regime"), min(x$year[x$regime == "shifted regime"]), NA),
    stringsAsFactors = FALSE
  )
}

warning_summary <- do.call(rbind, rows)
warning_summary$warning_level <- ifelse(warning_summary$warning_years >= 10, "high", ifelse(warning_summary$warning_years >= 4, "moderate", "low"))
write.csv(warning_summary, file.path(table_dir, "r_early_warning_summary.csv"), row.names = FALSE)
print(warning_summary)
