# Python Workflow: Carbon Stocks, Temperature Response, and Feedback Scenario Modeling

The default Python workflow is professional and dependency-light. It uses only the standard library so smoke tests do not fail on missing pandas.

Scripts:

- `climate_feedback_dynamics_model.py` — core synthetic climate feedback scenario model
- `climate_vulnerability_risk_index.py` — vulnerability/adaptation diagnostics
- `policy_delay_emissions_model.py` — cumulative emissions and policy-delay diagnostics
- `run_all_climate_workflows.py` — default runner

The workflow exports tables and a validation report suitable for professional documentation, teaching, and reproducible methods demonstration.
