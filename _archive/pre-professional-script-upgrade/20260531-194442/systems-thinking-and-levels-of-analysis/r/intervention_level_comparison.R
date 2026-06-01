# Intervention-level comparison

article_dir <- normalizePath(file.path(getwd(), "articles", "systems-thinking-and-levels-of-analysis"), mustWork = FALSE)
if (!dir.exists(article_dir)) article_dir <- normalizePath(file.path(getwd(), ".."), mustWork = FALSE)

scenarios <- read.csv(file.path(article_dir, "data", "synthetic_scenarios.csv"))
scenarios$cross_scale_score <- with(
  scenarios,
  (individual_support + organizational_capacity + institutional_reform + network_redundancy) / ecological_stress
)

print(scenarios[, c("scenario_id", "scenario_name", "cross_scale_score")])
