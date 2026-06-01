# What Is Systems Thinking?

Companion materials for the article **“What Is Systems Thinking?”**

This folder translates core systems-thinking concepts into reproducible examples:

- feedback loops
- stock-flow dynamics
- causal relationships
- delay behavior
- scenario comparison
- network structure
- resilience diagnostics
- synthetic indicators
- model-run documentation

## Folder Structure

```text
python/    feedback, stock-flow, network, scenario, and resilience examples
r/         scenario comparison, delay behavior, causal summaries, and visualization
julia/     dynamic systems and nonlinear feedback examples
sql/       system variables, causal relationships, scenarios, indicators, and model-run schemas
rust/      command-line systems diagnostics scaffold
go/        causal-network and pathway utility scaffold
cpp/       efficient network and feedback examples
fortran/   recurrence and dynamic-system examples
c/         low-level stock-flow simulation utilities
docs/      modeling principles and article notes
data/      synthetic datasets
outputs/   generated outputs
notebooks/ notebook placeholders
```

## Purpose

The goal is to make systems thinking concrete. The code and data are intentionally synthetic so that readers can study structure, causality, feedback, accumulation, delay, and resilience without relying on sensitive or proprietary data.

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/what-is-systems-thinking/python/run_advanced_pandas_workflow.py
```
