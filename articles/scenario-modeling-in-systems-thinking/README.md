# Scenario Modeling in Systems Thinking

This article scaffold supports reproducible scenario modeling for systems thinking. It includes synthetic data, baseline and counterfactual workflows, intervention comparisons, stress tests, distributional scenario summaries, robustness checks, and modeling notes.

## Purpose

Scenario modeling helps systems thinkers compare plausible futures without treating any single future as certain. This repository focuses on:

- baseline continuation scenarios
- counterfactual and intervention pathways
- stress-test scenarios
- distributional outcomes across groups and places
- robustness assessment across uncertain futures
- sensitivity workflows for assumptions and parameters

## Repository structure

- `python/` contains scenario modeling workflows and reproducible analysis examples.
- `r/` contains visualization, comparison, and summary scripts.
- `julia/` contains dynamic and nonlinear scenario examples.
- `sql/` contains schemas for scenario definitions, assumptions, interventions, stress tests, distributional outcomes, and model runs.
- `docs/` contains modeling principles, assumptions, ethics notes, and responsible-use guidance.
- `data/` contains synthetic datasets for demonstration.
- `outputs/` is reserved for generated figures and tables.
- `notebooks/` contains notebook placeholders for future walkthroughs.

## Data notes

All datasets are synthetic and intended for methods demonstration, teaching, and reproducible analysis. They are not real administrative, demographic, health, infrastructure, ecological, financial, or community records.

## Article URL

GitHub article folder: https://github.com/Content-Catalyst-LLC/systems-thinking-code/tree/main/articles/scenario-modeling-in-systems-thinking/

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/scenario-modeling-in-systems-thinking/python/run_advanced_pandas_workflow.py
```
