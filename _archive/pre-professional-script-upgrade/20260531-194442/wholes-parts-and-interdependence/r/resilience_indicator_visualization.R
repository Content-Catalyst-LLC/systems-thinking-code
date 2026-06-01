# Resilience indicator visualization using base R

script_args <- commandArgs(trailingOnly = FALSE)
file_arg <- script_args[grep("--file=", script_args)]
script_path <- if (length(file_arg) > 0) sub("--file=", "", file_arg[1]) else "r/resilience_indicator_visualization.R"
article_dir <- dirname(dirname(normalizePath(script_path)))

indicators <- read.csv(file.path(article_dir, "data", "synthetic_indicators.csv"))
output_dir <- file.path(article_dir, "outputs", "figures")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

png(file.path(output_dir, "resilience_indicator_plot.png"), width = 900, height = 600)
plot(indicators$period, indicators$resilience_buffer, type = "l", xlab = "Period", ylab = "Resilience buffer", main = "Resilience Buffer Over Time")
dev.off()

print("Wrote outputs/figures/resilience_indicator_plot.png")
