root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
d <- read.csv(file.path(root, "data", "raw", "synthetic_outputs.csv"))
d$overall_learning_score <- with(d, learning_effectiveness * 0.35 + memory_retention * 0.25 + structural_change * 0.25 + burden_reduction * 0.15)
write.csv(d[, c("scenario", "overall_learning_score")], file.path(root, "outputs", "tables", "r_learning_effectiveness_comparison.csv"), row.names = FALSE)
