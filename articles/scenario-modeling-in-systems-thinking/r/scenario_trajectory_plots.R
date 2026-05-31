data_dir <- file.path("..", "data")
out_dir <- file.path("..", "outputs", "figures")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

outputs <- read.csv(file.path(data_dir, "synthetic_model_outputs.csv"))

png(file.path(out_dir, "scenario_trust_trajectories.png"), width = 900, height = 600)
plot(NULL, xlim = range(outputs$year), ylim = range(outputs$trust_stock),
     xlab = "Year", ylab = "Trust stock", main = "Synthetic Scenario Trust Trajectories")
for (scenario in unique(outputs$scenario_id)) {
  rows <- outputs[outputs$scenario_id == scenario, ]
  lines(rows$year, rows$trust_stock, type = "b")
}
legend("topright", legend = unique(outputs$scenario_id), lty = 1, pch = 1, cex = 0.8)
dev.off()

cat("Wrote scenario trajectory plot\n")
