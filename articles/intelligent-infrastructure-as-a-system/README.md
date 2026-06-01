# Intelligent Infrastructure as a System

Professional companion repository scaffold for the article **“Intelligent Infrastructure as a System.”**

This folder supports reproducible systems analysis of intelligent infrastructure, including physical asset condition, sensor coverage, predictive maintenance, cyber-physical dependency, climate exposure, equity priority, governance readiness, workforce capacity, public accountability, and resilience.

## Purpose

The scaffold is designed for synthetic-data methods demonstration, infrastructure systems analysis, public-interest technology review, resilience planning, and reproducible workflow development. It is intentionally structured so the default workflows can run without fragile package dependencies, while advanced workflows can use optional Python packages when a virtual environment is installed.

## Folder structure

- `python/` — dependency-light Python workflows and optional advanced pandas/matplotlib workflow
- `r/` — base R diagnostics and visualization scripts
- `julia/` — nonlinear asset deterioration and resilience threshold examples
- `sql/` — relational schemas for intelligent infrastructure systems data
- `c/`, `cpp/`, `fortran/`, `go/`, `rust/` — compact systems-language examples for validation, simulation, and fast scanning
- `data/raw/` — synthetic source data
- `data/processed/` — cleaned or exported derived datasets
- `outputs/tables/` — generated CSV tables and diagnostics
- `outputs/figures/` — generated plots
- `docs/` — methods, assumptions, ethics, validation, and workflow notes
- `notebooks/` — placeholder notebooks for future walkthroughs
- `scripts/` — setup and convenience scripts

## Default workflow

```bash
cd ~/Downloads/systems-thinking-code/articles/intelligent-infrastructure-as-a-system
python3 python/run_all_intelligent_infrastructure_workflows.py
Rscript r/run_all_intelligent_infrastructure_workflows.R
```

## Optional advanced workflow

```bash
cd ~/Downloads/systems-thinking-code/articles/intelligent-infrastructure-as-a-system
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-advanced.txt
python python/advanced_pandas_infrastructure_dashboard.py
```

## Responsible use

The synthetic examples are for learning, planning, diagnostics, and reproducibility. They should not be used as operational infrastructure risk tools without local data validation, engineering review, cybersecurity review, community engagement, legal review, and public accountability.
