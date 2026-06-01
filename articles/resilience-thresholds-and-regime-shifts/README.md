# Resilience, Thresholds, and Regime Shifts

Professional companion workflows for modeling resilience, threshold risk, early warning signals, and regime-shift scenarios.

## Run Python workflows

```bash
cd ~/Downloads/systems-thinking-code/articles/resilience-thresholds-and-regime-shifts
python3 python/run_all_resilience_workflows.py
```

## Run R workflows

```bash
cd ~/Downloads/systems-thinking-code/articles/resilience-thresholds-and-regime-shifts
Rscript r/run_all_resilience_workflows.R
```

The Python scripts require only the standard library. The R scripts use base R only.

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/resilience-thresholds-and-regime-shifts/python/run_advanced_pandas_workflow.py
```
