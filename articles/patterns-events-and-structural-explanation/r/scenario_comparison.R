# Scenario comparison using simplified structural risk logic.

article_dir <- dirname(dirname(normalizePath(sys.frame(1)$ofile)))
scenarios <- read.csv(file.path(article_dir, "data", "synthetic_scenarios.csv"))

run_scenario <- function(row, periods = 12) {
  trust <- 62
  capacity <- 55
  backlog <- 120
  structural_risk <- 52

  for (period in seq_len(periods)) {
    shock <- ifelse(row$shock_period > 0 && period >= row$shock_period, row$shock_size, 0)
    capacity <- capacity + (2 * row$capacity_multiplier) - (backlog / 150)
    backlog <- backlog + (5 * row$backlog_multiplier) + shock / 10 - (capacity / 20)
    structural_risk <- structural_risk + (backlog / 200) - (capacity / 120)
    trust <- trust + row$trust_repair_rate - (structural_risk / 120)
  }

  data.frame(
    scenario_id = row$scenario_id,
    scenario_name = row$scenario_name,
    final_trust = round(trust, 2),
    final_capacity = round(capacity, 2),
    final_backlog = round(backlog, 2),
    final_structural_risk = round(structural_risk, 2)
  )
}

results <- do.call(rbind, lapply(seq_len(nrow(scenarios)), function(i) run_scenario(scenarios[i, ])))
print(results)
