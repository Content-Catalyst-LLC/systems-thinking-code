# Systems Thinking in Public Policy

Professional companion scaffold for the Systems Thinking article **Systems Thinking in Public Policy**.

This repository treats public policy as a dynamic system of rules, implementation capacity, administrative burden, public trust, feedback closure, institutional memory, coordination, and distributional effects. The scripts use synthetic data, but they are structured as reusable professional workflows for policy analysts, public administrators, civic researchers, public-value strategists, and systems practitioners.

## Primary runnable workflows

From this article folder, run:

```bash
python3 python/run_all_public_policy_workflows.py
Rscript r/run_all_public_policy_workflows.R
```

These commands create professional diagnostic outputs under:

```text
outputs/tables/
outputs/figures/
```

## Professional-use intent

The workflows are designed to be adapted into real policy work: burden analysis, implementation-capacity diagnostics, trust-stock monitoring, feedback-loop closure, distributional impact analysis, delay simulation, and policy scenario comparison.

## Responsible use

Synthetic data is included for reproducibility. Do not use this scaffold as an operational policy, legal, benefits, public-health, housing, climate, regulatory, or enforcement decision system without real data validation, community review, institutional authorization, domain expertise, privacy safeguards, and transparent assumptions.

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/systems-thinking-in-public-policy/python/run_advanced_pandas_workflow.py
```
