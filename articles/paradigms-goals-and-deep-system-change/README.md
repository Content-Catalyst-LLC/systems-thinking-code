# Paradigms, Goals, and Deep System Change

This companion repository supports the Systems Thinking article **Paradigms, Goals, and Deep System Change**.

The scaffold demonstrates how changing system goals, objective functions, boundary assumptions, metrics, rule sets, and paradigm assumptions can change behavior over time. The examples use synthetic data and are intended for learning, transparent modeling, policy discussion, and responsible systems analysis.

## Repository structure

- `python/` — goal-structure simulations, objective-function comparison, boundary expansion, metric sensitivity, rule-set comparison, and distributional analysis
- `r/` — visual summaries, scenario tables, objective comparisons, boundary summaries, and distributional outputs
- `julia/` — nonlinear goal dynamics, paradigm-shift simulation, and objective-function scanning
- `sql/` — schemas for system goals, paradigm assumptions, objective functions, metrics, boundary costs, scenario outputs, and model runs
- `rust/` — command-line goal diagnostics scaffold
- `go/` — paradigm scenario runner scaffold
- `cpp/` — efficient objective scanning and goal-feedback examples
- `fortran/` — recurrence model for goal dynamics
- `c/` — low-level goal-feedback simulation utility
- `docs/` — modeling principles, assumptions, responsible-use notes, and article notes
- `data/` — synthetic datasets
- `outputs/` — generated figures and tables
- `notebooks/` — placeholder notebooks for future walkthroughs

## Responsible-use note

These examples are for synthetic-data education, article support, systems modeling, and institutional learning. They are not decision engines for employment, benefits, discipline, surveillance, policing, eligibility, credit, insurance, healthcare access, or other high-stakes determinations. Any real-world use would require participatory design, domain expertise, data governance, rights protections, uncertainty analysis, and accountability mechanisms.

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/paradigms-goals-and-deep-system-change/python/run_advanced_pandas_workflow.py
```
