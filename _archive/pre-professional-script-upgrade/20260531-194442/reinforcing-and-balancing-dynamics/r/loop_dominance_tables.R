# Loop dominance table using synthetic scenario data.

article_dir <- dirname(dirname(normalizePath(sys.frame(1)$ofile)))
scenarios <- read.csv(file.path(article_dir, "data", "synthetic_scenarios.csv"))
print(scenarios)
