# Patterns, Events, and Structural Explanation

Companion materials for the article **“Patterns, Events, and Structural Explanation.”**

This folder translates the article's core systems-thinking distinction into reproducible examples:

- event records
- repeated patterns
- structural causal maps
- feedback-loop examples
- stock-flow accumulation
- scenario comparison
- resilience diagnostics
- model-run documentation

## Folder Structure

```text
python/    event-pattern analysis, structural maps, feedback, stock-flow, scenario, and resilience examples
r/         pattern visualization, event summaries, delay behavior, causal summaries, and scenario comparison
julia/     dynamic systems and nonlinear feedback examples
sql/       event, variable, causal relationship, scenario, indicator, and model-run schemas
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

The goal is to show how systems thinking moves from visible events to recurring patterns and then to the deeper structures that generate those patterns. The code and data are intentionally synthetic so readers can study recurrence, causality, feedback, accumulation, delay, and structural explanation without relying on sensitive data.

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/patterns-events-and-structural-explanation/python/run_advanced_pandas_workflow.py
```
