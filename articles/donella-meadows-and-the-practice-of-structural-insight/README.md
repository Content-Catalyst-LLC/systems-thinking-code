# Donella Meadows and the Practice of Structural Insight

Professional companion repository scaffold for the article **“Donella Meadows and the Practice of Structural Insight.”**

This folder supports reproducible systems analysis inspired by Donella Meadows’s work on structural insight, stocks, flows, feedback, overshoot, limits, leverage points, resilience, information flows, rules, goals, paradigms, self-organization, equity, and public responsibility.

## Purpose

The scaffold is designed for synthetic-data methods demonstration, sustainability systems analysis, public policy learning, institutional diagnostics, resilience planning, leverage-point analysis, and reproducible workflow development. Default workflows run without external Python or R packages. Optional advanced workflows use pandas, matplotlib, and openpyxl when installed.

## Folder structure

- `python/` — dependency-light Python workflows and optional advanced pandas/matplotlib workflow
- `r/` — base R diagnostics and visualization scripts
- `julia/` — nonlinear overshoot, leverage, and resilience examples
- `sql/` — relational schemas for structural-insight data
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
cd ~/Downloads/systems-thinking-code/articles/donella-meadows-and-the-practice-of-structural-insight
python3 python/run_all_meadows_structural_insight_workflows.py
Rscript r/run_all_meadows_structural_insight_workflows.R
```

## Optional advanced workflow

```bash
cd ~/Downloads/systems-thinking-code/articles/donella-meadows-and-the-practice-of-structural-insight
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-advanced.txt
python python/advanced_pandas_meadows_dashboard.py
```

## Responsible use

These workflows use synthetic data for learning, methods demonstration, and reproducible modeling. They are not substitutes for local evidence, ecological expertise, public accountability, affected-community participation, historical analysis, legal review, or ethical review.
