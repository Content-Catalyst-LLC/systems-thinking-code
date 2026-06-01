# System Archetypes and Recurring Patterns

This companion repository supports the article **“System Archetypes and Recurring Patterns.”** It provides synthetic datasets and reproducible examples for recognizing recurring system structures such as limits to growth, fixes that fail, shifting the burden, eroding goals, escalation, success to the successful, tragedy of the commons, growth and underinvestment, and policy resistance.

The examples are designed for systems-thinking education, research workflows, and transparent modeling practice. They are not decision engines and should not be used to automate public, institutional, employment, financial, health, or environmental decisions without domain expertise, stakeholder review, validation, and ethical governance.

## Repository structure

- `python/` — archetype diagnostics, recurring-pattern simulations, scenario comparison, delay tests, and distributional analysis
- `r/` — archetype plots, summary tables, and visualization workflows
- `julia/` — nonlinear and delayed-feedback archetype dynamics
- `sql/` — schemas for archetypes, variables, feedback loops, cases, scenarios, model runs, and outputs
- `rust/` — command-line diagnostics scaffold
- `go/` — archetype scenario runner scaffold
- `cpp/` — efficient archetype scans and delayed-feedback solver examples
- `fortran/` — recurrence-based archetype model
- `c/` — low-level archetype simulation engine
- `docs/` — modeling principles, diagnostic questions, ethics notes, assumptions, and limitations
- `data/` — synthetic datasets
- `outputs/` — generated figures and tables
- `notebooks/` — notebook placeholders

## Suggested workflow

1. Review the article and the `docs/` notes.
2. Inspect the synthetic datasets in `data/`.
3. Run the Python examples for archetype behavior over time.
4. Use the R scripts to create summaries and visualizations.
5. Extend the scenarios with your own assumptions, but document every change.

## Public GitHub article folder

https://github.com/Content-Catalyst-LLC/systems-thinking-code/tree/main/articles/system-archetypes-and-recurring-patterns/

<!-- ADVANCED_PANDAS_WORKFLOW -->
## Optional Advanced pandas Workflow

This article folder includes an optional advanced pandas/matplotlib workflow in `python/run_advanced_pandas_workflow.py`. The default workflows remain dependency-light. To enable advanced outputs, run the repository-level setup script:

```bash
cd ~/Downloads/systems-thinking-code
./scripts/setup_advanced_python_env.sh
. .venv/bin/activate
python articles/system-archetypes-and-recurring-patterns/python/run_advanced_pandas_workflow.py
```
