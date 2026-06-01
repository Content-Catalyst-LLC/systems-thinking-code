# Policy timing plot placeholder
policy <- read.csv("../data/synthetic_policy_timing.csv")
policy$effect_visible_period <- policy$start_period + policy$implementation_delay
print(policy[, c("policy_id", "policy_name", "effect_visible_period", "evaluation_period")])
