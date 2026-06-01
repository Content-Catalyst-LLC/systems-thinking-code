# Peter Senge and the Learning Organization

Professional companion repository scaffold for the article **“Peter Senge and the Learning Organization.”**

This folder supports reproducible systems analysis inspired by Peter Senge’s learning organization framework, including the five disciplines, systems thinking, mental models, shared vision, team learning, personal mastery, defensive routines, feedback use, psychological safety, institutional memory, trust, and adaptive capacity.

## Purpose

The scaffold is designed for synthetic-data methods demonstration, organizational learning analysis, institutional diagnostics, leadership development, organizational psychology, knowledge-flow analysis, and reproducible workflow development. Default workflows run without external Python or R packages. Optional advanced workflows use pandas, matplotlib, and openpyxl when installed.

## Folder structure

- `python/` — dependency-light Python workflows and optional advanced pandas/matplotlib workflow
- `r/` — base R diagnostics and visualization scripts
- `julia/` — nonlinear learning-loop and defensive-routine examples
- `sql/` — relational schemas for organizational learning data
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
cd ~/Downloads/systems-thinking-code/articles/peter-senge-and-the-learning-organization
python3 python/run_all_senge_learning_organization_workflows.py
Rscript r/run_all_senge_learning_organization_workflows.R
```

## Optional advanced workflow

```bash
cd ~/Downloads/systems-thinking-code/articles/peter-senge-and-the-learning-organization
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-advanced.txt
python python/advanced_pandas_senge_dashboard.py
```

## Responsible use

These workflows use synthetic data for learning, methods demonstration, and reproducible modeling. They are not substitutes for worker voice, organizational diagnosis, qualitative research, labor protections, legal review, affected-community feedback, psychological safety assessment, or ethical leadership practice.
