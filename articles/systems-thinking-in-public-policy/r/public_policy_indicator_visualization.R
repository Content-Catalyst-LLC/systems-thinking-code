source(file.path(dirname(sys.frame(1)$ofile), "_workflow_utils.R"))
root <- article_root(); ensure_dirs(root)
results_path <- file.path(root, "outputs", "tables", "public_policy_scenario_results.csv")
if (!file.exists(results_path)) stop("Run python/run_all_public_policy_workflows.py before this R script.")
policy_results <- read.csv(results_path)
final_rows <- latest_by_scenario(policy_results)
policy_summary <- final_rows[, c("scenario", "policy_outcome", "public_trust", "implementation_capacity", "administrative_burden", "feedback_closure", "distribution_gap")]
names(policy_summary) <- c("scenario", "final_outcome", "final_trust", "final_capacity", "average_burden", "feedback_closure", "distribution_gap")
policy_summary$diagnostic <- ifelse(policy_summary$final_outcome >= 80 & policy_summary$final_trust >= 70 & policy_summary$distribution_gap <= 20,
                                    "strong public-value trajectory",
                                    ifelse(policy_summary$final_outcome >= 65 & policy_summary$final_trust >= 55,
                                           "improving but monitor burden and equity",
                                           ifelse(policy_summary$final_outcome >= 50 & policy_summary$final_trust < 55,
                                                  "technical improvement with legitimacy risk",
                                                  "weak or fragile trajectory")))
write.csv(policy_summary, file.path(root, "outputs", "tables", "r_policy_scenario_diagnostics.csv"), row.names = FALSE)
print(policy_summary)
