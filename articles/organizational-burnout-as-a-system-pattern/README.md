# Organizational Burnout as a System Pattern

This article scaffold supports the Systems Thinking article **“Organizational Burnout as a System Pattern.”** It provides synthetic data, reproducible examples, and multi-language starting points for studying burnout as a dynamic system pattern rather than only an individual stress condition.

## Purpose

The repository is designed for systems-thinking education, organizational learning analysis, public-interest management research, and reproducible modeling demonstrations. It uses synthetic data only and focuses on workload-capacity dynamics, hidden labor, recovery deficits, urgency, rework, turnover, institutional memory, and redesign scenarios.

## Structure

- `python/` — workload-capacity modeling, recovery deficits, hidden labor, urgency-rework loops, turnover feedback, institutional memory, and redesign scenarios.
- `r/` — base R summaries and visual-ready tables for organizational burnout patterns.
- `julia/` — nonlinear burnout, capacity, recovery, and memory feedback examples.
- `sql/` — schemas for roles, workload, hidden labor, recovery indicators, burnout risk, turnover, memory assets, redesign scenarios, model runs, and outputs.
- `rust/`, `go`, `cpp`, `fortran`, `c` — lightweight systems-language scaffolds for diagnostics and simulation.
- `docs/` — modeling principles, article notes, burnout-system framework, workload-capacity notes, hidden-labor notes, diagnostic questions, ethics, assumptions, and responsible use.
- `data/` — synthetic datasets.
- `outputs/` — generated tables and figures.
- `notebooks/` — notebook placeholders.

## Article thesis

Organizational burnout emerges when work systems repeatedly draw down human capacity faster than they restore it. The system may continue to function through overtime, hidden labor, emotional absorption, rework, and sacrifice, but those adaptations can hide structural depletion until turnover, errors, distrust, and institutional memory loss accelerate.

## Suggested workflows

```bash
python3 python/burnout_system_baseline.py
python3 python/workload_capacity_model.py
python3 python/recovery_deficit_simulation.py
python3 python/hidden_labor_analysis.py
python3 python/burnout_redesign_scenarios.py
```

The scripts write lightweight outputs to `outputs/tables/` using only standard-library Python.
