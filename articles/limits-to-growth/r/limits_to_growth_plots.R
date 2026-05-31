# Limits-to-growth plot workflow using base R.
base_dir <- normalizePath(file.path(dirname(commandArgs(trailingOnly = FALSE)[1]), ".."), mustWork = FALSE)
# When run interactively, set base_dir manually if needed.
base_dir <- normalizePath(file.path(getwd()), mustWork = FALSE)
input <- file.path(base_dir, "data", "synthetic_growth_variables.csv")
if (!file.exists(input)) input <- file.path(dirname(getwd()), "data", "synthetic_growth_variables.csv")
rows <- read.csv(input)
out_dir <- file.path(dirname(input), "..", "outputs", "figures")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
png(file.path(out_dir, "limits_to_growth_scale.png"), width = 900, height = 600)
plot(rows$year, rows$system_scale, type = "l", lwd = 2, xlab = "Year", ylab = "System scale", main = "Limits to Growth: System Scale")
dev.off()
