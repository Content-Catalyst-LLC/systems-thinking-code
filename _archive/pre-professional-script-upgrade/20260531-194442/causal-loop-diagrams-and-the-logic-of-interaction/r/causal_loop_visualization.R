# Lightweight visualization placeholder using base R only.
base_dir <- normalizePath(file.path(getwd()), mustWork = FALSE)
if (!dir.exists(file.path(base_dir, "data"))) base_dir <- normalizePath(file.path(getwd(), ".."), mustWork = FALSE)

bot <- read.csv(file.path(base_dir, "data", "synthetic_behavior_over_time.csv"), stringsAsFactors = FALSE)
outputs_dir <- file.path(base_dir, "outputs")
dir.create(outputs_dir, showWarnings = FALSE, recursive = TRUE)

png(file.path(outputs_dir, "behavior_over_time_public_trust.png"), width = 900, height = 600)
plot(bot$time_step, bot$public_trust, type = "l", xlab = "Time step", ylab = "Public trust", main = "Behavior Over Time: Public Trust")
dev.off()

cat("Wrote outputs/behavior_over_time_public_trust.png\n")
