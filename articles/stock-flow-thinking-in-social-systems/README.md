# Stock-Flow Thinking in Social Systems

This article scaffold supports the Systems Thinking article **Stock-Flow Thinking in Social Systems**.

The repository is designed for reproducible learning, transparent social systems modeling, and synthetic-data demonstrations. It focuses on social stocks such as trust, legitimacy, administrative burden, capability, institutional capacity, debt, wealth, and resilience, along with the flows that build or drain them.

## Purpose

This scaffold demonstrates how stock-flow thinking can clarify social accumulation and repair. It provides examples for studying:

- social stocks and social flows
- trust and legitimacy repair
- administrative burden accumulation
- inequality and compounding advantage
- capability development scenarios
- group-specific trajectories
- policy repair and burden-reduction scenarios

## Repository Structure

- `python/` — social stock-flow models, trust repair, administrative burden, inequality, capability, policy scenarios
- `r/` — stock-flow plots, trust repair visualization, burden tables, inequality trajectories, scenario comparison
- `julia/` — nonlinear social accumulation, trust feedback dynamics, repair thresholds
- `sql/` — schemas for social stocks, flows, group trajectories, policy scenarios, burden indicators, and model runs
- `rust/` — command-line social stock-flow diagnostics scaffold
- `go/` — social-flow pathway utility scaffold
- `cpp/` — efficient social-stock simulation and inequality trajectory scanning examples
- `fortran/` — recurrence-style social stock model
- `c/` — low-level social stock-flow simulation example
- `docs/` — modeling principles, measurement notes, assumptions, limitations, responsible use
- `data/` — synthetic datasets
- `outputs/` — generated figures and tables
- `notebooks/` — notebook placeholders

## Data Notes

All datasets are synthetic. They are designed to demonstrate methods and should not be interpreted as real-world measurements of communities, institutions, households, or groups.

## Responsible Use

These materials are for learning, research prototyping, institutional reflection, and reproducible methods demonstration. They should not be used for eligibility decisions, surveillance, automated classification of individuals, risk scoring, employment decisions, policing, or punitive governance.

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/stock-flow-thinking-in-social-systems/python/run_advanced_pandas_workflow.py
```
