# Multilevel summary tables for Systems Thinking and Levels of Analysis

article_dir <- normalizePath(file.path(getwd(), "articles", "systems-thinking-and-levels-of-analysis"), mustWork = FALSE)
if (!dir.exists(article_dir)) article_dir <- normalizePath(file.path(getwd(), ".."), mustWork = FALSE)

indicators <- read.csv(file.path(article_dir, "data", "synthetic_indicators.csv"))

summary_table <- data.frame(
  indicator = names(indicators)[-1],
  start = as.numeric(indicators[1, -1]),
  end = as.numeric(indicators[nrow(indicators), -1])
)
summary_table$change <- summary_table$end - summary_table$start

print(summary_table)
