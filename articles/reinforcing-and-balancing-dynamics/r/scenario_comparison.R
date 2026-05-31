# Scenario comparison placeholder for reinforcing and balancing dynamics.

article_dir <- dirname(dirname(normalizePath(sys.frame(1)$ofile)))
indicators <- read.csv(file.path(article_dir, "data", "synthetic_indicators.csv"))
print(summary(indicators))
