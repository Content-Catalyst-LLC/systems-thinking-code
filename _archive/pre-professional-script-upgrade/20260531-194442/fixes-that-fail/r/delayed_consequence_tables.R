# Summarize delayed consequences.
args <- commandArgs(trailingOnly = FALSE)
file_arg <- grep("^--file=", args, value = TRUE)
script_path <- if (length(file_arg)) sub("^--file=", "", file_arg[[1]]) else "r/delayed_consequence_tables.R"
root <- normalizePath(file.path(dirname(script_path), ".."), mustWork = FALSE)
dir.create(file.path(root, "outputs", "tables"), recursive = TRUE, showWarnings = FALSE)
conseq <- read.csv(file.path(root, "data", "synthetic_delayed_consequences.csv"))
summary <- aggregate(consequence_level ~ fix_id + affected_stock, data = conseq, FUN = max)
write.csv(summary, file.path(root, "outputs", "tables", "delayed_consequence_summary.csv"), row.names = FALSE)
print(summary)
