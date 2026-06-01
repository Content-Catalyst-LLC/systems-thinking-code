# Emergence, Adaptation, and Complexity

This professional companion scaffold supports the article **Emergence, Adaptation, and Complexity** in the Systems Thinking series.

The repository models how local interaction, adaptation, diversity, synchronization, feedback, shock response, and governance assumptions can produce system-level patterns. It is designed for reproducible teaching, scenario analysis, and practitioner-facing systems diagnostics.

## Default workflows

The default workflows are intentionally dependency-light:

- Python uses only the standard library.
- R uses base R only.
- Optional advanced Python uses pandas, matplotlib, and openpyxl only when an advanced environment is installed.

## Main outputs

Generated outputs are written to:

- `outputs/tables/emergence_adaptation_complexity_timeseries.csv`
- `outputs/tables/emergence_adaptation_complexity_summary.csv`
- `outputs/tables/validation_report.txt`
- `outputs/figures/*.png` when base R is available

## Run

```bash
cd ~/Downloads/systems-thinking-code/articles/emergence-adaptation-and-complexity
python3 python/run_all_complexity_workflows.py
Rscript r/run_all_complexity_workflows.R
```

## Scope

These scripts are synthetic, transparent systems-modeling scaffolds. They are not empirical claims about a specific city, platform, institution, ecosystem, or community. Replace synthetic assumptions with validated domain data before using the workflows for applied decisions.
