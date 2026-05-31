# Nested systems summary

article_dir <- normalizePath(file.path(getwd(), "articles", "systems-thinking-and-levels-of-analysis"), mustWork = FALSE)
if (!dir.exists(article_dir)) article_dir <- normalizePath(file.path(getwd(), ".."), mustWork = FALSE)

entities <- read.csv(file.path(article_dir, "data", "synthetic_system_entities.csv"))
levels <- read.csv(file.path(article_dir, "data", "synthetic_system_levels.csv"))
merged <- merge(entities, levels, by = "level_id")
print(merged[, c("entity_name", "level_name", "parent_entity_id", "baseline_capacity", "risk_exposure")])
