root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
loops <- read.csv(file.path(root, "data", "synthetic_feedback_loops.csv"))
print(table(loops$loop_type))
print(loops[, c("loop_name", "loop_type", "description")])
