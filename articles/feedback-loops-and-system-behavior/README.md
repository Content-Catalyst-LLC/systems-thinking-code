# Feedback Loops and System Behavior

Companion materials for the article **“Feedback Loops and System Behavior.”**

This folder translates core systems-thinking concepts into reproducible examples:

- reinforcing feedback loops
- balancing feedback loops
- causal polarity
- delays, overshoot, and oscillation
- behavior-over-time analysis
- policy resistance
- feedback archetypes
- causal-loop diagnostics
- synthetic indicators and scenario workflows

## Folder Structure

```text
python/    feedback-loop simulation, delay, overshoot, behavior-over-time, and diagnostics examples
r/         visualization, scenario comparison, delay plots, and feedback summary tables
julia/     nonlinear feedback dynamics and oscillation examples
sql/       schemas for feedback loops, loop variables, causal edges, scenarios, indicators, and model runs
rust/      command-line feedback diagnostics scaffold
go/        causal-loop pathway utility scaffold
cpp/       efficient feedback-network and simulation examples
fortran/   recurrence and feedback-dynamics examples
c/         low-level feedback simulation utilities
docs/      modeling principles and article notes
data/      synthetic datasets
outputs/   generated outputs
notebooks/ notebook placeholders
```

## Purpose

The goal is to make feedback-loop reasoning concrete while keeping assumptions visible. These examples are intentionally synthetic so readers can study feedback structure without relying on sensitive or proprietary data.

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/feedback-loops-and-system-behavior/python/run_advanced_pandas_workflow.py
```
