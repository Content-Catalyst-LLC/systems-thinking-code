# Behavior Over Time and Structural Explanation

This article scaffold supports the Systems Thinking article **Behavior Over Time and Structural Explanation**.

The repository demonstrates how visible events can be placed within behavior-over-time patterns and connected to structural explanation through trend analysis, recurrence detection, stock-flow accumulation, feedback-generated behavior, and scenario comparison.

## Scope

This scaffold is designed for synthetic-data research, teaching, reproducible methods demonstration, and systems-thinking practice. It is not a forecasting service, risk-rating product, automated policy tool, or substitute for domain expertise, affected-community knowledge, governance review, or ethical judgment.

## Repository structure

- `python/` — behavior-over-time analysis, structural explanation models, recurrence detection, stock-flow accumulation, feedback-generated patterns, and intervention scenarios
- `r/` — behavior-over-time plots, trend summaries, recurrence visualization, structural pattern comparison, and scenario comparison
- `julia/` — dynamic and nonlinear behavior examples
- `sql/` — schemas for events, time-series indicators, structural variables, causal relationships, scenarios, and model runs
- `rust/` — command-line diagnostics scaffold for behavior patterns
- `go/` — temporal pathway utility scaffold
- `cpp/` — efficient time-series and structural dynamics examples
- `fortran/` — recurrence behavior model example
- `c/` — low-level temporal simulation utility
- `docs/` — modeling principles, article notes, assumptions, responsible-use notes
- `data/` — synthetic datasets
- `outputs/` — generated output placeholder
- `notebooks/` — notebook placeholders

## Suggested use

Run the Python and R examples first to generate behavior-over-time plots and summary tables. Then review the SQL schemas and systems notes to understand how events, indicators, structures, scenarios, and interventions can be represented in a reproducible research workflow.

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/behavior-over-time-and-structural-explanation/python/run_advanced_pandas_workflow.py
```
