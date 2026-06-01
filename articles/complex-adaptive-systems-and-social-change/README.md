# Complex Adaptive Systems and Social Change

Professional companion repository scaffold for the article **“Complex Adaptive Systems and Social Change.”**

This folder supports reproducible systems analysis of social change as a complex adaptive process, including adaptive agents, network diffusion, threshold dynamics, trust, legitimacy, resistance, backlash, institutional response, governance learning, coalition capacity, equity alignment, and transformation momentum.

## Purpose

The scaffold is designed for synthetic-data methods demonstration, social-change systems analysis, policy strategy, institutional learning, movement ecology, governance design, and reproducible workflow development. Default workflows run without external Python or R packages. Optional advanced workflows use pandas, matplotlib, and openpyxl when installed.

## Folder structure

- `python/` — dependency-light Python workflows and optional advanced pandas/matplotlib workflow
- `r/` — base R diagnostics and visualization scripts
- `julia/` — nonlinear social diffusion and threshold dynamics examples
- `sql/` — relational schemas for complex social-change data
- `c/`, `cpp/`, `fortran`, `go`, `rust` — compact systems-language examples for validation, diffusion, and fast scanning
- `data/raw/` — synthetic source data
- `data/processed/` — cleaned or exported derived datasets
- `outputs/tables/` — generated CSV tables and diagnostics
- `outputs/figures/` — generated plots
- `docs/` — methods, assumptions, ethics, validation, and workflow notes
- `notebooks/` — placeholder notebooks for future walkthroughs
- `scripts/` — setup and convenience scripts

## Default workflow

```bash
cd ~/Downloads/systems-thinking-code/articles/complex-adaptive-systems-and-social-change
python3 python/run_all_complex_adaptive_social_change_workflows.py
Rscript r/run_all_complex_adaptive_social_change_workflows.R
```

## Optional advanced workflow

```bash
cd ~/Downloads/systems-thinking-code/articles/complex-adaptive-systems-and-social-change
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-advanced.txt
python python/advanced_pandas_social_change_dashboard.py
```

## Responsible use

These workflows use synthetic data for learning, methods demonstration, and strategy modeling. They are not substitutes for community participation, historical analysis, legal review, institutional accountability, qualitative research, local data validation, or affected-community governance.
