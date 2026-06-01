# Institutional Memory and System Learning

This scaffold supports the Systems Thinking article **“Institutional Memory and System Learning.”** It provides synthetic data, reproducible examples, and multi-language starting points for studying institutional memory as a systems capacity.

## Purpose

The repository is designed for systems-thinking education, organizational learning analysis, knowledge architecture, public administration research, and reproducible modeling demonstrations. It uses synthetic data only and focuses on institutional memory, feedback preservation, learning retention, turnover-related knowledge loss, documentation quality, decision records, repeated mistakes, knowledge networks, and memory-based structural redesign.

## Structure

- `python/` — memory stock-flow modeling, turnover knowledge loss, documentation quality scoring, feedback loop closure, repeated mistake risk, knowledge network analysis, and redesign scenarios.
- `r/` — base R summaries and visual-ready tables for institutional memory and learning-retention patterns.
- `julia/` — nonlinear memory decay, learning retention, and memory-authority feedback examples.
- `sql/` — schemas for memory assets, decision records, feedback signals, learning events, turnover events, documentation quality, repeated errors, redesign actions, model runs, and outputs.
- `rust/`, `go`, `cpp`, `fortran`, `c` — lightweight systems-language scaffolds for diagnostics and simulation.
- `docs/` — modeling principles, article notes, institutional memory framework, feedback preservation framework, documentation quality guide, diagnostic questions, ethics notes, assumptions, and responsible use.
- `data/` — synthetic datasets.
- `outputs/` — generated tables and figures.
- `notebooks/` — notebook placeholders.

## Article thesis

Institutional memory turns experience into durable learning by preserving feedback, decisions, assumptions, context, and lessons so systems do not repeat the same mistakes under new conditions. Memory becomes system learning only when it is usable, connected to authority, and embedded into future routines, tools, rules, and governance.

## Suggested workflows

```bash
python3 python/institutional_memory_baseline.py
python3 python/memory_stock_flow_model.py
python3 python/turnover_knowledge_loss.py
python3 python/documentation_quality_score.py
python3 python/feedback_loop_closure.py
python3 python/memory_redesign_scenarios.py
```

The scripts write lightweight outputs to `outputs/tables/` using only standard-library Python.

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/institutional-memory-and-system-learning/python/run_advanced_pandas_workflow.py
```
