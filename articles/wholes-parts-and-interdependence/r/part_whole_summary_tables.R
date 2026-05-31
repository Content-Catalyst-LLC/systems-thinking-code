# Part-whole summary tables

script_args <- commandArgs(trailingOnly = FALSE)
file_arg <- script_args[grep("--file=", script_args)]
script_path <- if (length(file_arg) > 0) sub("--file=", "", file_arg[1]) else "r/part_whole_summary_tables.R"
article_dir <- dirname(dirname(normalizePath(script_path)))

parts <- read.csv(file.path(article_dir, "data", "synthetic_system_parts.csv"))
summary_table <- aggregate(baseline_capacity ~ level + part_type, data = parts, FUN = mean)
summary_table$baseline_capacity <- round(summary_table$baseline_capacity, 2)
print(summary_table)

output_dir <- file.path(article_dir, "outputs", "tables")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
write.csv(summary_table, file.path(output_dir, "part_whole_summary.csv"), row.names = FALSE)
