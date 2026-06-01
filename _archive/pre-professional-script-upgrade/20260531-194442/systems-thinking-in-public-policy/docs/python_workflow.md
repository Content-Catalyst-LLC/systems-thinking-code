# Python Workflow: Policy Feedback, Administrative Burden, and Scenario Modeling

Run from the article folder:

```bash
python3 python/run_all_public_policy_workflows.py
```

The Python workflow creates a professional synthetic policy-analysis pipeline:

- validates input CSV schemas;
- computes administrative burden indices;
- models public trust as a stock;
- summarizes implementation capacity;
- estimates distributional policy impact;
- simulates policy delay and backlog growth;
- runs policy scenario models;
- exports clean CSV outputs for reports and R visualizations.

Primary outputs:

- `outputs/tables/public_policy_scenario_results.csv`
- `outputs/tables/public_policy_scenario_summary.csv`
- `outputs/tables/administrative_burden_index.csv`
- `outputs/tables/public_trust_stock_flow.csv`
- `outputs/tables/implementation_capacity_summary.csv`
- `outputs/tables/distributional_policy_impact.csv`
- `outputs/tables/policy_delay_simulation.csv`
- `outputs/tables/feedback_closure_diagnostics.csv`
