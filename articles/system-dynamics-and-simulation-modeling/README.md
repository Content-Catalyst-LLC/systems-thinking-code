# System Dynamics and Simulation Modeling

This article scaffold supports the Systems Thinking article **System Dynamics and Simulation Modeling**.

The repository is designed for reproducible learning, scenario comparison, and systems-analysis demonstrations using synthetic data. It includes examples for stock-flow simulation, delayed feedback, scenario comparison, sensitivity analysis, and model validation across multiple languages.

## Purpose

The scaffold demonstrates how system dynamics connects structure with behavior over time. It provides reusable examples for studying:

- stocks and flows
- delayed feedback
- scenario comparison
- sensitivity analysis
- model validation checks
- policy intervention timing
- behavior-over-time outputs

## Repository Structure

- `python/` — baseline system dynamics, stock-flow simulation, delayed feedback, scenarios, sensitivity, validation
- `r/` — behavior-over-time plots, scenario summaries, validation diagnostics
- `julia/` — continuous-time dynamics, delayed feedback, nonlinear threshold simulation
- `sql/` — schemas for variables, stocks, flows, parameters, scenarios, simulation runs, and outputs
- `rust/` — command-line simulation diagnostics scaffold
- `go/` — scenario runner utility scaffold
- `cpp/` — efficient stock-flow solver and sensitivity scan examples
- `fortran/` — continuous dynamics solver example
- `c/` — low-level stock-flow engine example
- `docs/` — modeling principles, validation framework, scenario design, assumptions, responsible use
- `data/` — synthetic input datasets
- `outputs/` — generated tables and figures
- `notebooks/` — notebook placeholders

## Data Notes

All datasets are synthetic and created for methodological demonstration. They are not empirical measurements and should not be interpreted as real-world system diagnostics.

## Responsible Use

This scaffold is intended for learning, research prototyping, and transparent systems-analysis demonstrations. It should not be used as an automated decision system or as a substitute for domain expertise, stakeholder knowledge, public accountability, or ethical judgment.

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/system-dynamics-and-simulation-modeling/python/run_advanced_pandas_workflow.py
```
