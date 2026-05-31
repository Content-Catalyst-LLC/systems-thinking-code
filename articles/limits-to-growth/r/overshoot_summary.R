# Overshoot summary.
base_dir <- getwd()
input <- file.path(base_dir, "data", "synthetic_outputs.csv")
rows <- read.csv(input)
rows$overshoot_flag <- as.logical(rows$overshoot_flag)
summary <- aggregate(remaining_resource ~ overshoot_flag, data = rows, FUN = mean)
out_dir <- file.path(base_dir, "outputs", "tables")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)
write.csv(summary, file.path(out_dir, "overshoot_summary.csv"), row.names = FALSE)
