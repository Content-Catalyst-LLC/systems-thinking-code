# Scenario comparison for "What Is Systems Thinking?"

get_script_dir <- function() {
  args <- commandArgs(trailingOnly = FALSE)
  file_arg <- grep("^--file=", args, value = TRUE)
  if (length(file_arg) > 0) {
    return(dirname(normalizePath(sub("^--file=", "", file_arg))))
  }
  return(getwd())
}

script_dir <- get_script_dir()
article_dir <- dirname(script_dir)
scenario_path <- file.path(article_dir, "data", "synthetic_scenarios.csv")
scenarios <- read.csv(scenario_path)

run_scenario <- function(row, periods = 12) {
  trust <- 62
  capacity <- 55
  demand <- 70
  delay <- 14
  resilience <- 40

  for (period in seq_len(periods)) {
    current_demand <- demand * row$demand_multiplier
    if (row$shock_period > 0 && period >= row$shock_period) {
      current_demand <- current_demand + row$shock_size
    }
    capacity <- capacity + (row$resource_multiplier * 2.0) - (current_demand / 100.0)
    delay <- max(1.0, delay * row$delay_multiplier + (current_demand - capacity) / 80.0)
    trust <- trust + (capacity / 100.0) - (delay / 20.0)
    resilience <- resilience + (capacity / 120.0) - (current_demand / 150.0)
  }

  data.frame(
    scenario_id = row$scenario_id,
    scenario_name = row$scenario_name,
    final_trust = round(trust, 2),
    final_capacity = round(capacity, 2),
    final_delay = round(delay, 2),
    final_resilience = round(resilience, 2)
  )
}

results <- do.call(rbind, lapply(seq_len(nrow(scenarios)), function(i) run_scenario(scenarios[i, ])))
print(results)
