# Professional Systems Workflow Upgrade

This folder has been upgraded with runnable, professional-facing systems analysis workflows.

## Python workflow

`python/run_professional_systems_workflow.py`

The Python workflow generates synthetic but realistic systems data, runs scenario comparisons, exports validation checks, and writes professional diagnostics for:

- baseline/current structure
- pressure-only intervention
- capacity-building intervention
- structural redesign

Outputs are written to `outputs/tables/` and `outputs/figures/`.

## R workflow

`r/run_professional_systems_workflow.R`

The R workflow reads the Python outputs, produces additional diagnostics, and creates base-R figures without requiring tidyverse or ggplot2.

## Professional use

These scripts are designed as adaptable professional scaffolds. Replace the synthetic assumptions with observed data, stakeholder evidence, administrative records, environmental indicators, survey data, implementation metrics, or domain-specific parameters before using them for real decisions.

## Article folder

`paradigms-goals-and-deep-system-change`
