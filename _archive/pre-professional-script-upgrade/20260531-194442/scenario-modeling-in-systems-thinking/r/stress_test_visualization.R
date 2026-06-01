data_dir <- file.path("..", "data")
out_dir <- file.path("..", "outputs", "figures")
dir.create(out_dir, recursive = TRUE, showWarnings = FALSE)

stress <- read.csv(file.path(data_dir, "synthetic_stress_tests.csv"))

png(file.path(out_dir, "stress_test_severity.png"), width = 900, height = 600)
barplot(stress$severity, names.arg = stress$stress_id, las = 2,
        main = "Synthetic Stress Test Severity", ylab = "Severity")
dev.off()

cat("Wrote stress test visualization\n")
