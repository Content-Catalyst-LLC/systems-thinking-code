# Distributional outcome summary placeholder.

groups <- data.frame(
  group = c("high_buffer_households", "low_buffer_households", "disabled_applicants", "frontline_workers"),
  delay_sensitivity = c(0.15, 0.75, 0.65, 0.40),
  burden_sensitivity = c(0.20, 0.85, 0.95, 0.70)
)

groups$risk_flag <- ifelse(groups$delay_sensitivity + groups$burden_sensitivity > 1.2, "high", "monitor")

dir.create(file.path("outputs", "tables"), recursive = TRUE, showWarnings = FALSE)
write.csv(groups, file.path("outputs", "tables", "distributional_outcome_summary.csv"), row.names = FALSE)
