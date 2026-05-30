# Basic systems visualization using base R.

get_script_dir <- function() {
  args <- commandArgs(trailingOnly = FALSE)
  file_arg <- grep("^--file=", args, value = TRUE)
  if (length(file_arg) > 0) return(dirname(normalizePath(sub("^--file=", "", file_arg))))
  getwd()
}

article_dir <- dirname(get_script_dir())
indicators <- read.csv(file.path(article_dir, "data", "synthetic_indicators.csv"))
output_dir <- file.path(article_dir, "outputs")
if (!dir.exists(output_dir)) dir.create(output_dir, recursive = TRUE)

png(file.path(output_dir, "trust_capacity_resilience.png"), width = 900, height = 600)
plot(indicators$period, indicators$public_trust, type = "l", lwd = 2, ylim = c(0, 100), xlab = "Period", ylab = "Index", main = "System Indicators Over Time")
lines(indicators$period, indicators$institutional_capacity, lwd = 2, lty = 2)
lines(indicators$period, indicators$resilience_buffer, lwd = 2, lty = 3)
legend("topright", legend = c("Public trust", "Institutional capacity", "Resilience buffer"), lwd = 2, lty = c(1, 2, 3))
dev.off()
