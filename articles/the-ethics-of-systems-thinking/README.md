# The Ethics of Systems Thinking

Professional companion repository scaffold for the article **“The Ethics of Systems Thinking.”**

This folder supports reproducible systems analysis focused on ethical systems practice: boundary inclusion, affected voice, accountability, harm exposure, repair capacity, ecological responsibility, model humility, structural change, power redistribution, and responsible intervention.

## Purpose

The scaffold is designed for synthetic-data methods demonstration, systems ethics, institutional accountability, AI and platform governance, climate adaptation ethics, infrastructure equity, public health systems, organizational learning, and reproducible workflow development. Default workflows run without external Python or R packages. Optional advanced workflows use pandas, matplotlib, and openpyxl when installed.

## Folder structure

- `python/` — dependency-light Python workflows and optional advanced pandas/matplotlib workflow
- `r/` — base R diagnostics and visualization scripts
- `julia/` — ethical leverage, boundary harm, and repair capacity examples
- `sql/` — relational schemas for ethical systems data
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
cd ~/Downloads/systems-thinking-code/articles/the-ethics-of-systems-thinking
python3 python/run_all_ethical_systems_workflows.py
Rscript r/run_all_ethical_systems_workflows.R
```

## Optional advanced workflow

```bash
cd ~/Downloads/systems-thinking-code/articles/the-ethics-of-systems-thinking
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-advanced.txt
python python/advanced_pandas_ethics_dashboard.py
```

## Responsible use

These workflows use synthetic data for learning, methods demonstration, and reproducible modeling. They are not substitutes for affected-community participation, ecological review, labor protections, legal review, AI governance review, public accountability, or ethical oversight.
