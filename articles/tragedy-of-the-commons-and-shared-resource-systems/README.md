# Tragedy of the Commons and Shared Resource Systems

Companion code and documentation for the Systems Thinking article **“Tragedy of the Commons and Shared Resource Systems.”**

This scaffold demonstrates how shared resource systems can be modeled through commons stocks, user behavior, regeneration, governance rules, monitoring indicators, restoration pathways, and distributional impacts. The examples use synthetic data and reproducible workflows to explore:

- shared resource stock-flow dynamics;
- open-access depletion and governance scenarios;
- free riding, cooperation, monitoring, and sanctions;
- quota and restoration policy comparisons;
- distributional burden analysis across user groups;
- practical responsible-use documentation for commons analysis.

All datasets are synthetic and are intended for learning, public-interest analysis, systems modeling, and reproducible methods demonstrations. They are not intended for enforcement targeting, surveillance, punitive scoring, or individual-level decision-making.

## Main repository folders

- `data/` contains synthetic shared resource, user, governance, monitoring, restoration, distributional impact, and model-output datasets.
- `python/` contains runnable stock-flow and scenario models.
- `r/` contains base-R summaries and visualization-ready tables.
- `julia/` contains nonlinear and agent-style modeling examples.
- `sql/` contains database schemas for commons system modeling.
- `docs/` contains framework notes, diagnostic questions, assumptions, and responsible-use guidance.
- `outputs/` is used for generated figures and tables.

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/tragedy-of-the-commons-and-shared-resource-systems/python/run_advanced_pandas_workflow.py
```
