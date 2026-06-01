# Wholes, Parts, and Interdependence

Companion materials for the article **“Wholes, Parts, and Interdependence.”**

This folder translates core systems-thinking concepts into reproducible examples:

- whole-system behavior
- part-whole relationships
- interdependence and dependency pathways
- local optimization and system-wide effects
- failure propagation
- nested systems and levels of analysis
- resilience and fragility diagnostics
- synthetic indicators and scenario workflows

## Folder Structure

```text
python/    dependency matrices, part-whole networks, local optimization, failure propagation, resilience diagnostics
r/         dependency visualization, part-whole summaries, scenario comparison, resilience indicator plots
julia/     dynamic interdependence and nonlinear part-whole feedback examples
sql/       schemas for system parts, dependency relationships, levels, scenarios, indicators, and model runs
rust/      command-line interdependence diagnostics scaffold
go/        dependency pathway utility scaffold
cpp/       efficient dependency network and failure propagation examples
fortran/   recurrence and interdependence examples
c/         low-level dependency simulation utilities
docs/      modeling principles and article notes
data/      synthetic datasets
outputs/   generated outputs
notebooks/ notebook placeholders
```

## Purpose

The goal is to make part-whole systems thinking concrete. The examples are intentionally synthetic so readers can study interdependence, dependency, nested levels, local optimization, cascading risk, and resilience without relying on sensitive or proprietary data.

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/wholes-parts-and-interdependence/python/run_advanced_pandas_workflow.py
```
