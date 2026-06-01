# Jay Forrester and the Origins of System Dynamics

Professional companion repository scaffold for the article **“Jay Forrester and the Origins of System Dynamics.”**

This folder supports reproducible systems analysis inspired by Jay Forrester’s system dynamics tradition, including stocks, flows, delays, feedback loops, corrective action, policy resistance, structural leverage, institutional learning, trust, capacity, and scenario testing.

## Purpose

The scaffold is designed for synthetic-data methods demonstration, system dynamics education, public policy learning, infrastructure and organizational diagnostics, institutional capacity analysis, and reproducible workflow development. Default workflows run without external Python or R packages. Optional advanced workflows use pandas, matplotlib, and openpyxl when installed.

## Folder structure

- `python/` — dependency-light Python workflows and optional advanced pandas/matplotlib workflow
- `r/` — base R diagnostics and visualization scripts
- `julia/` — nonlinear feedback and delay model examples
- `sql/` — relational schemas for stock-flow and feedback systems data
- `c/`, `cpp/`, `fortran/`, `go/`, `rust/` — compact systems-language examples for validation, recurrence, and fast scanning
- `data/raw/` — synthetic source data
- `data/processed/` — cleaned or exported derived datasets
- `outputs/tables/` — generated CSV tables and diagnostics
- `outputs/figures/` — generated plots
- `docs/` — methods, assumptions, ethics, validation, and workflow notes
- `notebooks/` — placeholder notebooks for future walkthroughs
- `scripts/` — setup and convenience scripts

## Default workflow

```bash
cd ~/Downloads/systems-thinking-code/articles/jay-forrester-and-the-origins-of-system-dynamics
python3 python/run_all_forrester_system_dynamics_workflows.py
Rscript r/run_all_forrester_system_dynamics_workflows.R
```

## Optional advanced workflow

```bash
cd ~/Downloads/systems-thinking-code/articles/jay-forrester-and-the-origins-of-system-dynamics
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-advanced.txt
python python/advanced_pandas_system_dynamics_dashboard.py
```

## Responsible use

These workflows use synthetic data for learning, methods demonstration, and reproducible modeling. They are not substitutes for local evidence, stakeholder participation, engineering review, community knowledge, historical analysis, ethical review, or public accountability.
