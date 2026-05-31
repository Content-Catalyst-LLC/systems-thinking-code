# Causal pattern summary for "Causality in Systems Thinking"

script_path <- tryCatch(normalizePath(sys.frame(1)$ofile), error = function(e) file.path(getwd(), "r", "causal_pattern_summary.R"))
article_dir <- dirname(dirname(script_path))
edges <- read.csv(file.path(article_dir, "data", "synthetic_causal_edges.csv"))

cat("Causal role summary\n")
print(as.data.frame(table(edges$causal_role)))

cat("\nDelay summary\n")
print(as.data.frame(table(edges$delay)))
