# Sensitivity Analysis for System Interventions

This scaffold supports reproducible sensitivity analysis for systems-thinking interventions using synthetic data. It includes parameter sweeps, Monte Carlo examples, threshold searches, robustness comparisons, distributional sensitivity, and structural sensitivity notes.

## Purpose

Use this repository for methods demonstration, learning, and transparent systems analysis. Replace synthetic data with validated domain data before using the workflow for applied research or decision support.

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/sensitivity-analysis-for-system-interventions/python/run_advanced_pandas_workflow.py
```
