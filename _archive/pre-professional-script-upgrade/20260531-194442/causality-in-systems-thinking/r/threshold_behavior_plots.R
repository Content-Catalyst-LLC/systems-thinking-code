# Threshold behavior plot

script_path <- tryCatch(normalizePath(sys.frame(1)$ofile), error = function(e) file.path(getwd(), "r", "threshold_behavior_plots.R"))
article_dir <- dirname(dirname(script_path))
output_dir <- file.path(article_dir, "outputs")
dir.create(output_dir, recursive = TRUE, showWarnings = FALSE)

stress <- seq(40, 100, by = 5)
threshold <- 70
response <- ifelse(stress < threshold, 0.25 * stress, 0.25 * threshold + 1.15 * (stress - threshold))

png(file.path(output_dir, "threshold_behavior_plot.png"), width = 900, height = 600)
plot(stress, response, type = "l", lwd = 2, xlab = "Stress", ylab = "System Response", main = "Nonlinear Threshold Response")
abline(v = threshold, lty = 2)
dev.off()

print(data.frame(stress = stress, response = round(response, 2)))
