# Compare relief-only and repair-oriented scenarios.
args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
script_path <- if (length(file_arg)) sub("^--file=", "", file_arg[[1]]) else "r/relief_repair_comparison.R"
root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = FALSE)
outputs <- read.csv(file.path(root, "data", "synthetic_outputs.csv"))
print(outputs[order(outputs$final_symptom_level), ])
