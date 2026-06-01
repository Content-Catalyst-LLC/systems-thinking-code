# Causality in Systems Thinking

Companion materials for the article **“Causality in Systems Thinking.”**

This folder translates systems-causality concepts into reproducible examples:

- linear and circular causality
- causal-loop examples
- structural cause mapping
- delayed effects and accumulation
- counterfactual scenario comparison
- causal-network analysis
- threshold behavior
- responsible causal documentation

## Folder Structure

```text
python/    causal-loop, structural-cause, delay, counterfactual, network, and threshold examples
r/         causal pattern summaries, counterfactual comparison, delay visualization, threshold plots, and causal tables
julia/     dynamic causality and nonlinear feedback examples
sql/       schemas for causal variables, causal relationships, counterfactuals, scenarios, indicators, and model runs
rust/      command-line causality diagnostics scaffold
go/        causal-pathway utility scaffold
cpp/       efficient causal-network and feedback-causality examples
fortran/   recurrence and dynamic-causality examples
c/         low-level causal simulation utilities
docs/      modeling principles and article notes
data/      synthetic datasets
outputs/   generated outputs
notebooks/ notebook placeholders
```

## Purpose

The goal is to make systems causality concrete. The code and data are intentionally synthetic so readers can study causal structure, feedback, accumulation, delay, threshold behavior, and counterfactual intervention without relying on sensitive or proprietary data.

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/causality-in-systems-thinking/python/run_advanced_pandas_workflow.py
```
