# Dependency ratio summary.
args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
script_path <- if (length(file_arg)) sub("^--file=", "", file_arg[[1]]) else "r/dependency_summary.R"
root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = FALSE)
runs <- read.csv(file.path(root, "data", "synthetic_model_runs.csv"))
summary <- aggregate(dependency_ratio ~ scenario, data = runs, FUN = max)
print(summary)
