# Aggregation and distribution examples

article_dir <- normalizePath(file.path(getwd(), "articles", "systems-thinking-and-levels-of-analysis"), mustWork = FALSE)
if (!dir.exists(article_dir)) article_dir <- normalizePath(file.path(getwd(), ".."), mustWork = FALSE)

entities <- read.csv(file.path(article_dir, "data", "synthetic_system_entities.csv"))

print(paste("Average capacity:", round(mean(entities$baseline_capacity), 2)))
print(paste("Average risk exposure:", round(mean(entities$risk_exposure), 2)))
print(entities[order(-entities$risk_exposure), c("entity_name", "level_id", "risk_exposure")])
