# Limits to Growth

This article scaffold supports the Systems Thinking article **“Limits to Growth.”**

The examples model how reinforcing growth loops encounter constraints such as capacity, ecological stocks, trust, infrastructure condition, governance maturity, and legitimacy. The repository uses synthetic data only and is intended for educational, research, and reproducible modeling workflows.

## Structure

- `python/` — constrained growth, resource depletion, capacity investment, delayed constraint feedback, overshoot diagnostics, and distributional constraint examples.
- `r/` — visualizations and summary tables for limits-to-growth behavior.
- `julia/` — nonlinear growth, dynamic capacity constraints, and overshoot/recovery models.
- `sql/` — schemas for growth variables, constraints, resource stocks, capacity investments, scenarios, runs, and outputs.
- `rust/`, `go/`, `cpp/`, `fortran/`, `c/` — lightweight systems-modeling scaffolds.
- `docs/` — modeling principles, diagnostic questions, responsible-use notes, and article notes.
- `data/` — synthetic datasets.
- `outputs/` — generated outputs and placeholders.
- `notebooks/` — notebook placeholders.

## Responsible use

These examples are not forecasting tools. They are transparent systems-thinking demonstrations for exploring how growth loops, constraints, delays, depletion, and capacity investments interact. Use them to support critical inquiry, scenario comparison, and ethical systems analysis—not to justify predetermined policy decisions.

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/limits-to-growth/python/run_advanced_pandas_workflow.py
```
