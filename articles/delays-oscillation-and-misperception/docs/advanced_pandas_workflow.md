# Optional Advanced pandas Workflow

This folder includes a dependency-light professional workflow and an optional advanced pandas layer.

The advanced pandas layer is for richer professional analysis: scenario tables, Excel workbooks, grouped diagnostics, threshold-margin summaries, and matplotlib figures when available.

## Default rule

The standard workflow should always run without pandas or external Python packages. The advanced workflow is optional and should never be required for the normal smoke test.

## Setup

From the repository root:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/delays-oscillation-and-misperception/python/run_advanced_pandas_workflow.py
```

Or run every article's advanced workflow:

```bash
cd ~/Downloads/systems-thinking-code
. .venv/bin/activate
python scripts/run_all_advanced_pandas_workflows.py
```

## Outputs

The workflow writes:

```text
outputs/tables/advanced_pandas_scenario_timeseries.csv
outputs/tables/advanced_pandas_scenario_summary.csv
outputs/tables/advanced_pandas_workbook.xlsx
outputs/figures/advanced_pandas_threshold_margin.png
outputs/figures/advanced_pandas_system_capacity.png
```

## Professional-use note

The data are synthetic and intended for methods demonstration, planning, model design, and reproducible workflow development. They are not empirical findings and should not be used for real-world decisions without validated data, stakeholder review, uncertainty analysis, and domain-specific interpretation.
