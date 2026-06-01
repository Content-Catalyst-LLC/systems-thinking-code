boundaries <- read.csv("data/raw/synthetic_boundaries.csv")
boundaries$review_level <- ifelse(boundaries$ethical_risk_score >= 0.75, "urgent", ifelse(boundaries$ethical_risk_score >= 0.5, "review", "monitor"))
write.csv(boundaries, "outputs/tables/r_boundary_critique_summary.csv", row.names = FALSE)
cat("Wrote outputs/tables/r_boundary_critique_summary.csv\n")
