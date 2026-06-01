# Visualize eroding goals output.
root <- normalizePath(file.path(dirname(sys.frame(1)$ofile), ".."), mustWork = FALSE)
data_path <- file.path(root, "outputs", "tables", "eroding_goals_simulation.csv")
out_dir <- file.path(root, "outputs", "figures")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

df <- read.csv(data_path)
png(file.path(out_dir, "eroding_goals.png"), width = 900, height = 650)
plot(df$time, df$goal, type = "l", lwd = 2, xlab = "Time", ylab = "Index", main = "Eroding Goals")
lines(df$time, df$actual_performance, lwd = 2, lty = 2)
legend("topright", legend = c("Goal", "Actual performance"), lwd = 2, lty = c(1, 2), bty = "n")
dev.off()
cat("Wrote eroding-goals plot\n")
