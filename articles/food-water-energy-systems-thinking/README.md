# Food-Water-Energy Systems Thinking

This professional scaffold supports systems analysis of the food-water-energy nexus using synthetic but realistic data and reproducible workflows.

The repository is designed for practitioners, analysts, educators, sustainability teams, public agencies, infrastructure planners, and researchers who need a transparent starting point for modeling cross-sector trade-offs among food production, water security, energy demand, climate stress, vulnerability, and resilience.

## What this scaffold contains

- Dependency-light Python workflows that run with the Python standard library.
- Base R workflows that run without tidyverse, readr, dplyr, or ggplot2.
- Optional advanced Python workflow using pandas, matplotlib, and openpyxl when installed.
- SQL schemas and quality checks for nexus indicators.
- Compact Julia, Go, Rust, C, C++, and Fortran examples for reproducibility, validation, scenario execution, and numerical kernels.
- Documentation for method notes, validation, assumptions, limitations, and responsible use.

## Default smoke-tested workflow

```bash
cd ~/Downloads/systems-thinking-code/articles/food-water-energy-systems-thinking
python3 python/run_all_nexus_workflows.py
Rscript r/run_all_nexus_workflows.R
```

## Optional advanced workflow

```bash
cd ~/Downloads/systems-thinking-code/articles/food-water-energy-systems-thinking
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements-advanced.txt
python python/run_advanced_pandas_workflow.py
```

## Responsible use

The workflows use synthetic data for methods demonstration and decision-support prototyping. They are not a substitute for hydrological, agricultural, energy-system, climate, ecological, legal, or community-specific analysis. For real planning, replace synthetic values with validated local data, document assumptions, and include affected communities in model review.
