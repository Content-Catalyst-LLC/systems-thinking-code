assumptions <- read.csv("data/raw/synthetic_assumptions.csv")
assumptions$priority_numeric <- ifelse(assumptions$revision_priority == "high", 1, ifelse(assumptions$revision_priority == "medium", 0.65, 0.35))
assumptions$test_urgency <- assumptions$confidence * assumptions$priority_numeric
write.csv(assumptions[order(-assumptions$test_urgency), ], "outputs/tables/r_assumption_sensitivity.csv", row.names = FALSE)
cat("Wrote outputs/tables/r_assumption_sensitivity.csv\n")
