# Systems Thinking and Levels of Analysis

Companion materials for the article **Systems Thinking and Levels of Analysis**.

This folder supports level-aware systems analysis across micro, meso, macro, and cross-scale dynamics.

## Repository Structure

```text
python/    micro-meso-macro modeling, nested systems, cross-scale dependencies, aggregation examples, intervention comparisons, and resilience diagnostics
r/         multilevel summaries, distribution plots, cross-scale indicators, intervention comparisons, and nested-system summaries
julia/     dynamic cross-scale examples and nonlinear level-feedback examples
sql/       schemas for levels, entities, cross-scale relationships, scenarios, indicators, and model runs
rust/      command-line levels diagnostics scaffold
go/        cross-scale pathway utility scaffold
cpp/       efficient nested-network and cross-scale feedback examples
fortran/   recurrence and level-dynamics examples
c/         low-level cross-scale simulation utilities
docs/      modeling principles, article notes, assumptions, limitations, and responsible-use notes
data/      synthetic datasets
outputs/   generated output placeholders
notebooks/ notebook placeholders
```

## Purpose

The repository shows how systems thinking can represent problems across levels of analysis: individual, interactional, organizational, institutional, network, socio-ecological, and cross-scale. It is designed for synthetic-data research, methods demonstration, institutional learning, and reproducible workflows.

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/systems-thinking-and-levels-of-analysis/python/run_advanced_pandas_workflow.py
```
