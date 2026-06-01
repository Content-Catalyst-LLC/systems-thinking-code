# Causal network tables

script_path <- tryCatch(normalizePath(sys.frame(1)$ofile), error = function(e) file.path(getwd(), "r", "causal_network_tables.R"))
article_dir <- dirname(dirname(script_path))
edges <- read.csv(file.path(article_dir, "data", "synthetic_causal_edges.csv"))

out_degree <- aggregate(target ~ source, data = edges, FUN = length)
names(out_degree) <- c("variable", "out_degree")

in_degree <- aggregate(source ~ target, data = edges, FUN = length)
names(in_degree) <- c("variable", "in_degree")

print(merge(out_degree, in_degree, by = "variable", all = TRUE))
