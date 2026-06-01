# R Workflow: Public Policy Indicators, Distributional Diagnostics, and Feedback Visualization

Use R for policy scenario summaries, burden tables, public-trust trajectories, distributional diagnostics, implementation-capacity summaries, and publication-ready CSV outputs.

Runnable starter snippet:

```r
policy_results <- read.csv("outputs/tables/public_policy_scenario_results.csv")
policy_summary <- aggregate(
  cbind(policy_outcome, public_trust, implementation_capacity) ~ scenario,
  data = policy_results,
  FUN = function(x) tail(x, 1)
)
print(policy_summary)
```

Primary scripts:

- `public_policy_indicator_visualization.R`
- `burden_feedback_policy_diagnostics.R`
- `public_trust_trajectory_plots.R`
- `distributional_policy_tables.R`
- `implementation_capacity_summary.R`
- `export_public_policy_tables.R`
