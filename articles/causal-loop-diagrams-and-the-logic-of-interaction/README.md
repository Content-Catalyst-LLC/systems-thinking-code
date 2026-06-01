# Causal Loop Diagrams and the Logic of Interaction

This repository folder supports the article **“Causal Loop Diagrams and the Logic of Interaction.”** It provides synthetic datasets, code examples, and documentation for constructing causal loop diagrams, representing signed causal graphs, detecting feedback loops, classifying loop polarity, annotating delays, comparing stakeholder mental models, and connecting causal structure to behavior-over-time patterns.

## Purpose

The scaffold is designed for systems-thinking education, applied policy analysis, institutional learning, and reproducible demonstrations. It treats causal loop diagrams as structured hypotheses: every variable, arrow, sign, delay, and boundary is a claim that should be made explicit, documented, and tested against evidence.

## Repository structure

- `python/` — causal-loop diagram builder, signed graph loop detection, polarity analysis, delay annotation, stakeholder map comparison, and behavior-over-time linkage.
- `r/` — causal edge tables, signed graph summaries, loop-polarity tables, visualization, and stakeholder map comparison.
- `julia/` — signed feedback-network and loop-dynamics examples.
- `sql/` — schemas for variables, edges, feedback loops, loop polarity, delays, and model runs.
- `rust/` — command-line causal-loop diagnostics scaffold.
- `go/` — causal-pathway utility scaffold.
- `cpp/` — efficient loop detection and signed graph diagnostics examples.
- `fortran/` — recurrence-based loop dynamics example.
- `c/` — low-level loop scan utility.
- `docs/` — modeling principles, article notes, style guide, assumptions, and responsible-use documentation.
- `data/` — synthetic variables, causal edges, feedback loops, delay annotations, stakeholder maps, and behavior-over-time examples.
- `outputs/` — generated outputs placeholder.
- `notebooks/` — notebook placeholders.

## Suggested workflow

1. Inspect the synthetic variables and causal edges in `data/`.
2. Run the Python or R examples to classify loop polarity and summarize diagram structure.
3. Compare stakeholder map assumptions and delay annotations.
4. Use the documentation files to evaluate variable naming, boundary choices, evidence, and responsible interpretation.

## Responsible use

These examples are for synthetic-data modeling, systems education, institutional learning, and reproducible analysis. They should not be used as deterministic decision tools or as substitutes for stakeholder participation, domain expertise, historical analysis, ethics review, or affected-community knowledge.

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/causal-loop-diagrams-and-the-logic-of-interaction/python/run_advanced_pandas_workflow.py
```
