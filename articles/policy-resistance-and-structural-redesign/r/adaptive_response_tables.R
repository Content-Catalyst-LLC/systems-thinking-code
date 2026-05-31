# Adaptive response summary table.
path <- file.path("data", "raw", "synthetic_actor_responses.csv")
if (file.exists(path)) {
  responses <- read.csv(path)
  responses$response_risk_index <- round(0.5 * responses$response_strength + 0.25, 3)
  print(responses)
}
