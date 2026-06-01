# Feedback Loop Polarity and Causal Signs

This article scaffold supports the Systems Thinking article **Feedback Loop Polarity and Causal Signs**.

The repository demonstrates how to represent causal-loop variables, signed causal edges, reinforcing and balancing loop polarity, delays, sign uncertainty, and scenario sensitivity using synthetic data and reproducible examples.

## Purpose

The scaffold is designed for learning, documentation, and reproducible systems-analysis examples. It is not a production forecasting system or a substitute for domain expertise, stakeholder interpretation, or ethical review.

## Directory structure

- `python/` — signed causal graphs, loop polarity calculation, validation, and scenario sensitivity.
- `r/` — signed-edge tables, polarity summaries, and visualization workflows.
- `julia/` — signed-network dynamics and loop-polarity examples.
- `sql/` — schemas for variables, signed edges, feedback loops, polarity, scenarios, and model runs.
- `rust/` — command-line polarity diagnostics scaffold.
- `go/` — signed pathway utility scaffold.
- `cpp/` — efficient signed-graph and loop-polarity examples.
- `fortran/` — recurrence examples for signed feedback.
- `c/` — low-level signed-loop scanning scaffold.
- `docs/` — article notes, modeling principles, causal-sign style guide, and responsible-use notes.
- `data/` — synthetic datasets.
- `outputs/` — generated outputs placeholder.
- `notebooks/` — notebook placeholders.

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/feedback-loop-polarity-and-causal-signs/python/run_advanced_pandas_workflow.py
```
