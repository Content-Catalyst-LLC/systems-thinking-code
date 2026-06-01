# Counterfactual comparison using synthetic assumptions

script_path <- tryCatch(normalizePath(sys.frame(1)$ofile), error = function(e) file.path(getwd(), "r", "counterfactual_comparison.R"))
article_dir <- dirname(dirname(script_path))
cf <- read.csv(file.path(article_dir, "data", "synthetic_counterfactuals.csv"))

run_cf <- function(row, periods = 12) {
  trust <- 64
  capacity <- 58
  demand <- 70
  backlog <- 100 - as.numeric(row$backlog_reduction)

  for (period in seq_len(periods)) {
    demand_now <- demand * as.numeric(row$demand_multiplier)
    capacity <- capacity + 1.8 * as.numeric(row$resource_multiplier) - backlog / 200
    delay <- max(1, (demand_now / max(capacity, 1)) * 10 * as.numeric(row$delay_multiplier))
    backlog <- backlog + demand_now * 0.15 - capacity * 0.10
    trust <- trust + capacity / 140 - delay / 18
  }

  data.frame(
    counterfactual_id = row$counterfactual_id,
    name = row$name,
    final_trust = round(trust, 2),
    final_capacity = round(capacity, 2),
    final_backlog = round(backlog, 2)
  )
}

results <- do.call(rbind, lapply(seq_len(nrow(cf)), function(i) run_cf(cf[i, ])))
print(results)
