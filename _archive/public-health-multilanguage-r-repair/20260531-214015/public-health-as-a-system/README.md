# Public Health as a System

Professional companion repository for the article **Public Health as a System**.

This folder contains dependency-light and optional advanced workflows for modeling public health as an interacting system of disease dynamics, care capacity, public trust, prevention, social determinants, environmental exposure, vulnerability, and intervention timing.

## Default workflows

These workflows are designed to run without fragile package dependencies.

```bash
cd ~/Downloads/systems-thinking-code/articles/public-health-as-a-system
python3 python/run_all_public_health_workflows.py
Rscript r/run_all_public_health_workflows.R
```

The Python workflow uses only the Python standard library. The R workflow uses base R only.

## Optional advanced workflow

An optional pandas/matplotlib/openpyxl workflow is included for richer outputs. It is intentionally separate from the default smoke test.

```bash
cd ~/Downloads/systems-thinking-code/articles/public-health-as-a-system
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-advanced.txt
python python/run_advanced_pandas_workflow.py
```

## Outputs

Generated files are written to:

- `outputs/tables/` — CSV summaries, diagnostics, validation reports, and optional workbook exports
- `outputs/figures/` — base R and optional matplotlib figures

## Professional use

These scripts are synthetic by design, but they are structured as reusable professional scaffolds. Replace the assumptions with local public-health surveillance data, social determinant indicators, care-capacity data, environmental exposure metrics, community trust measures, or intervention scenarios before using them for applied decisions.
