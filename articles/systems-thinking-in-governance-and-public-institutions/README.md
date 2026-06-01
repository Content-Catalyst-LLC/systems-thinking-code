# Systems Thinking in Governance and Public Institutions

This scaffold supports the Systems Thinking article **“Systems Thinking in Governance and Public Institutions.”** It provides synthetic data, reproducible examples, and multi-language starting points for studying governance as a public system of feedback, capacity, trust, accountability, administrative burden, coordination, memory, and public value.

## Purpose

The repository is designed for systems-thinking education, public administration analysis, institutional learning, civic governance research, and reproducible modeling demonstrations. It uses synthetic data only and focuses on governance systems, public institutions, policy feedback, administrative burden, public trust, coordination networks, institutional capacity, public value, and structural redesign.

## Structure

- `python/` — governance baseline, administrative burden index, public trust stock-flow, coordination networks, policy feedback closure, institutional capacity, public value scoring, and redesign scenarios.
- `r/` — base R summaries and visual-ready tables for governance systems analysis.
- `julia/` — nonlinear governance, trust-capacity feedback, and policy-learning examples.
- `sql/` — schemas for public institutions, policy interventions, feedback signals, administrative burden, trust indicators, coordination edges, capacity stocks, public value metrics, redesign scenarios, model runs, and outputs.
- `rust/`, `go/`, `cpp/`, `fortran/`, `c/` — lightweight systems-language scaffolds for diagnostics and simulation.
- `docs/` — governance frameworks, administrative burden notes, public trust and legitimacy, coordination and public value, diagnostic questions, ethics, assumptions, and responsible use.
- `data/` — synthetic datasets.
- `outputs/` — generated tables and figures.
- `notebooks/` — notebook placeholders.

## Article thesis

Governance systems depend on feedback, trust, capacity, coordination, legitimacy, memory, and accountability. When these structures weaken, public institutions can repeat failure despite good intentions. Systems thinking helps public institutions diagnose burden, public trust, policy resistance, coordination gaps, power, learning decay, and public-value trade-offs.

## Suggested workflows

```bash
python3 python/governance_system_baseline.py
python3 python/administrative_burden_index.py
python3 python/public_trust_stock_flow.py
python3 python/coordination_network_analysis.py
python3 python/policy_feedback_closure.py
python3 python/governance_redesign_scenarios.py
```

The scripts write lightweight outputs to `outputs/tables/` using only standard-library Python.

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/systems-thinking-in-governance-and-public-institutions/python/run_advanced_pandas_workflow.py
```
