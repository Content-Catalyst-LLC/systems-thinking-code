# Systems Thinking in an Age of Complexity

Professional companion repository scaffold for the article **“Systems Thinking in an Age of Complexity.”**

This folder supports reproducible systems analysis focused on complexity pressure, feedback amplification, resilience capacity, learning, trust, accountability, boundary inclusion, harm exposure, transformation capacity, and responsible systems intervention.

## Purpose

The scaffold is designed for synthetic-data methods demonstration, complexity-aware systems analysis, public policy, AI governance, climate and ecological systems, institutional learning, infrastructure resilience, public health, urban systems, and reproducible workflow development. Default workflows run without external Python or R packages. Optional advanced workflows use pandas, matplotlib, and openpyxl when installed.

## Folder structure

- `python/` — dependency-light Python workflows and optional advanced pandas/matplotlib workflow
- `r/` — base R diagnostics and visualization scripts
- `julia/` — nonlinear complexity, resilience threshold, and transformation examples
- `sql/` — relational schemas for complexity and systems-readiness data
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
cd ~/Downloads/systems-thinking-code/articles/systems-thinking-in-an-age-of-complexity
python3 python/run_all_age_complexity_workflows.py
Rscript r/run_all_age_complexity_workflows.R
```

## Optional advanced workflow

```bash
cd ~/Downloads/systems-thinking-code/articles/systems-thinking-in-an-age-of-complexity
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-advanced.txt
python python/advanced_pandas_complexity_dashboard.py
```

## Responsible use

These workflows use synthetic data for learning, methods demonstration, and reproducible modeling. They are not substitutes for public participation, affected-community review, ecological assessment, legal review, AI governance review, infrastructure safety review, or institutional accountability.
