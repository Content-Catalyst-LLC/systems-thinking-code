`%||%` <- function(a, b) if (!is.null(a)) a else b
# Quota scenario governance table. Synthetic data only.
script_dir <- dirname(normalizePath(sys.frame(1)$ofile %||% getwd(), mustWork = FALSE))
base_dir <- normalizePath(file.path(script_dir, ".."), mustWork = FALSE)
rules <- read.csv(file.path(base_dir, "data", "synthetic_governance_rules.csv"))
rules$governance_quality <- rowMeans(rules[, c("monitoring_strength", "sanction_strength", "participation_score")])
ordered <- rules[order(-rules$governance_quality), ]
dir.create(file.path(base_dir, "outputs", "tables"), recursive = TRUE, showWarnings = FALSE)
write.csv(ordered, file.path(base_dir, "outputs", "tables", "r_quota_scenario_table.csv"), row.names = FALSE)
