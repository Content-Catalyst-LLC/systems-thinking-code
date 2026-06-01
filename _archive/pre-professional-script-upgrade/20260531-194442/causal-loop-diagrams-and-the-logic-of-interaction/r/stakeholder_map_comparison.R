# Compare stakeholder causal assumptions.
base_dir <- normalizePath(file.path(getwd()), mustWork = FALSE)
if (!dir.exists(file.path(base_dir, "data"))) base_dir <- normalizePath(file.path(getwd(), ".."), mustWork = FALSE)

maps <- read.csv(file.path(base_dir, "data", "synthetic_stakeholder_maps.csv"), stringsAsFactors = FALSE)
print(table(maps$stakeholder_group))
print(table(maps$polarity, maps$confidence))
