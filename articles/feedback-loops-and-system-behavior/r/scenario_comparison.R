# Scenario comparison for feedback-loop systems.

article_dir <- dirname(dirname(normalizePath(sys.frame(1)$ofile)))
scenario_path <- file.path(article_dir, "data", "synthetic_scenarios.csv")
output_path <- file.path(article_dir, "outputs", "tables", "scenario_summary.csv")

scenarios <- read.csv(scenario_path)

run_scenario <- function(row, periods = 12) {
  trust <- 62
  capacity <- 55 * row$capacity_multiplier
  demand <- 70 * row$demand_multiplier
  delay <- 14 * row$delay_factor
  backlog <- 120

  for (period in seq_len(periods)) {
    if (row$shock_period > 0 && period >= row$shock_period) {
      demand <- demand + row$shock_size / periods
    }
    capacity <- capacity + row$investment_rate * 10 - backlog / 250
    delay <- max(1, delay + (demand - capacity) / 60)
    trust <- trust + capacity / 120 - delay / 18
    backlog <- backlog + delay / 4 - row$investment_rate * 8
  }

  data.frame(
    scenario_id = row$scenario_id,
    scenario_name = row$scenario_name,
    final_trust = round(trust, 2),
    final_capacity = round(capacity, 2),
    final_delay = round(delay, 2),
    final_backlog = round(backlog, 2)
  )
}

summary <- do.call(rbind, lapply(seq_len(nrow(scenarios)), function(i) run_scenario(scenarios[i, ])))
write.csv(summary, output_path, row.names = FALSE)
print(summary)
cat("Wrote", output_path, "\n")
