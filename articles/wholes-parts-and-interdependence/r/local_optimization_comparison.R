# Local optimization comparison

script_args <- commandArgs(trailingOnly = FALSE)
file_arg <- script_args[grep("--file=", script_args)]
script_path <- if (length(file_arg) > 0) sub("--file=", "", file_arg[1]) else "r/local_optimization_comparison.R"
article_dir <- dirname(dirname(normalizePath(script_path)))

indicators <- read.csv(file.path(article_dir, "data", "synthetic_indicators.csv"))

local_change <- tail(indicators$local_performance, 1) - indicators$local_performance[1]
whole_change <- tail(indicators$whole_system_outcome, 1) - indicators$whole_system_outcome[1]

result <- data.frame(
  metric = c("local_performance_change", "whole_system_outcome_change"),
  value = c(local_change, whole_change)
)

print(result)

output_dir <- file.path(article_dir, "outputs", "tables")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)
write.csv(result, file.path(output_dir, "local_optimization_comparison.csv"), row.names = FALSE)
