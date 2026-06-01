# Climate Systems and Feedback Dynamics

This article folder contains professional, runnable systems-analysis workflows for the article **Climate Systems and Feedback Dynamics**.

The default workflows are dependency-light and are designed to run on a standard macOS/Homebrew Python installation without requiring pandas. Advanced pandas/matplotlib workflows are included as optional enhancements for richer tables, figures, and Excel exports.

## Default workflow

```bash
cd ~/Downloads/systems-thinking-code/articles/climate-systems-and-feedback-dynamics
python3 python/run_all_climate_workflows.py
```

If R is installed:

```bash
Rscript r/run_all_climate_workflows.R
```

## Optional advanced workflow

From the repository root:

```bash
cd ~/Downloads/systems-thinking-code
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r articles/climate-systems-and-feedback-dynamics/requirements-advanced.txt
python articles/climate-systems-and-feedback-dynamics/python/run_advanced_pandas_climate_workflow.py
```

## Outputs

Default workflow outputs are written to:

- `outputs/tables/climate_feedback_scenario_timeseries.csv`
- `outputs/tables/climate_feedback_scenario_summary.csv`
- `outputs/tables/climate_vulnerability_risk_diagnostics.csv`
- `outputs/tables/policy_delay_emissions_diagnostics.csv`
- `outputs/reports/climate_workflow_validation_report.md`

Base R outputs figures to `outputs/figures/` when `Rscript` is available.

## Professional use notes

These workflows are synthetic and designed for scenario reasoning, workflow demonstration, education, documentation, and reproducible methods. They are not official climate projections and should not be used for engineering, regulatory, financial, insurance, legal, public-safety, or site-specific climate-risk decisions without validated data, peer-reviewed models, uncertainty analysis, and domain review.
