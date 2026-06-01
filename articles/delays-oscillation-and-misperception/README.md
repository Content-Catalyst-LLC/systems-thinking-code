# Delays, Oscillation, and Misperception

Companion materials for the Systems Thinking article **“Delays, Oscillation, and Misperception.”**

This folder supports reproducible demonstrations of:

- delayed feedback
- oscillation and overcorrection
- overshoot and collapse
- hidden accumulation
- perception gaps
- policy timing
- delay-sensitive scenario comparison

The examples use synthetic data so readers can examine system structure, timing, and feedback behavior without relying on sensitive or proprietary datasets.

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/delays-oscillation-and-misperception/python/run_advanced_pandas_workflow.py
```
