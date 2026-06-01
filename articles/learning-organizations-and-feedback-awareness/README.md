# Learning Organizations and Feedback Awareness

This article scaffold supports the Systems Thinking article **“Learning Organizations and Feedback Awareness.”** It provides synthetic data, reproducible examples, and multi-language starting points for studying learning organizations, feedback awareness, psychological safety, signal distortion, institutional memory, defensive routines, and structural change.

## Purpose

The repository is designed for systems-thinking education, organizational learning analysis, public-interest management research, and reproducible modeling demonstrations. It uses synthetic data only and focuses on how organizations notice, interpret, remember, and act on feedback.

## Structure

- `python/` — feedback awareness, signal distortion, psychological safety, memory retention, defensive routines, learning effectiveness, feedback networks, and structural learning scenarios.
- `r/` — base R summaries and visual-ready tables for learning-organization patterns.
- `julia/` — nonlinear feedback and memory dynamics examples.
- `sql/` — schemas for feedback signals, channels, learning events, memory assets, psychological-safety indicators, defensive routines, structural changes, model runs, and outputs.
- `rust/`, `go/`, `cpp/`, `fortran/`, `c/` — lightweight systems-language scaffolds for diagnostics and simulation.
- `docs/` — modeling principles, article notes, feedback awareness framework, ethics notes, assumptions, and responsible-use notes.
- `data/` — synthetic datasets.
- `outputs/` — generated tables and figures.
- `notebooks/` — notebook placeholders.

## Article thesis

Learning organizations do not merely collect feedback. They build systems where feedback is safe to report, strong enough to interpret, preserved in institutional memory, connected to authority, and capable of changing structure.

## Suggested workflows

```bash
python3 python/feedback_awareness_baseline.py
python3 python/signal_distortion_model.py
python3 python/institutional_memory_retention.py
python3 python/learning_effectiveness_index.py
python3 python/structural_learning_scenarios.py
```

The scripts write lightweight outputs to `outputs/tables/` using only standard-library Python.

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/learning-organizations-and-feedback-awareness/python/run_advanced_pandas_workflow.py
```
