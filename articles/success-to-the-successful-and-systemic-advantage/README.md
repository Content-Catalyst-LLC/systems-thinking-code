# Success to the Successful and Systemic Advantage

Companion code and documentation for the Systems Thinking article **“Success to the Successful and Systemic Advantage.”**

This scaffold demonstrates how cumulative advantage can be modeled through reinforcing feedback loops, resource allocation rules, initial conditions, network visibility, preferential attachment, path dependence, and distributional outcomes. The examples use synthetic data and reproducible workflows to explore:

- success-to-the-successful feedback loops;
- cumulative advantage and systemic disadvantage;
- resource allocation based on prior success, need, and improvement potential;
- preferential attachment and visibility loops;
- path dependence and lock-in;
- distributional analysis of advantage gaps;
- responsible-use notes for modeling inequality, opportunity, and institutional resource flows.

All datasets are synthetic and intended for learning, systems modeling, public-interest analysis, and reproducible methods demonstrations. They are not intended for individual ranking, employment selection, punitive scoring, credit decisions, student tracking, surveillance, or automated eligibility decisions.

## Main repository folders

- `data/` contains synthetic actors, initial conditions, resource allocations, advantage metrics, network edges, intervention scenarios, model runs, and outputs.
- `python/` contains runnable cumulative-advantage, allocation, network, and distributional models.
- `r/` contains base-R summaries and visualization-ready tables.
- `julia/` contains nonlinear and network-oriented examples.
- `sql/` contains database schemas for systemic advantage analysis.
- `docs/` contains framework notes, diagnostic questions, assumptions, and responsible-use guidance.
- `outputs/` is used for generated figures and tables.

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/success-to-the-successful-and-systemic-advantage/python/run_advanced_pandas_workflow.py
```
