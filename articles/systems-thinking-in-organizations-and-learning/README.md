# Systems Thinking in Organizations and Learning

This article scaffold supports the Systems Thinking article **“Systems Thinking in Organizations and Learning.”** It provides synthetic data, reproducible examples, and multi-language starting points for studying organizations as learning systems shaped by feedback, routines, incentives, mental models, institutional memory, burnout dynamics, information flows, and structural redesign.

## Purpose

The repository is designed for systems-thinking education, organizational learning analysis, public-interest management research, and reproducible modeling demonstrations. It uses synthetic data only and focuses on patterns such as workload-capacity mismatch, feedback distortion, local optimization, learning decay, defensive routines, and organizational burnout.

## Structure

- `python/` — workload-capacity models, organizational-learning simulations, institutional memory decay, signal distortion, local optimization, and redesign scenarios.
- `r/` — base R scripts for plotting and summarizing organizational learning patterns.
- `julia/` — nonlinear learning dynamics and adaptation examples.
- `sql/` — schemas for teams, workload events, capacity stocks, feedback signals, learning events, memory assets, burnout indicators, scenarios, and outputs.
- `rust/` — command-line diagnostics scaffold.
- `go` — learning scenario runner scaffold.
- `cpp/` — efficient capacity and feedback-delay examples.
- `fortran/` — recurrence model for learning and memory.
- `c/` — low-level organizational feedback simulation utility.
- `docs/` — modeling principles, article notes, learning framework, feedback and memory framework, ethics and power notes, assumptions, and responsible-use notes.
- `data/` — synthetic datasets.
- `outputs/` — generated tables and figures.
- `notebooks/` — notebook placeholders.

## Article thesis

Organizations learn through structure. Feedback, memory, incentives, capacity, authority, voice, and power determine whether recurring problems become evidence for redesign or whether they are normalized as individual failure, communication breakdown, or lack of resilience.

## Suggested workflows

```bash
python3 python/workload_capacity_model.py
python3 python/institutional_memory_decay.py
python3 python/feedback_signal_distortion.py
python3 python/local_optimization_model.py
python3 python/learning_redesign_scenarios.py
```

The scripts write lightweight outputs to `outputs/tables/` using only standard-library Python.
