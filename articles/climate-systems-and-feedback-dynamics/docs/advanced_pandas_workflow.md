# Optional Advanced Pandas Workflow

The advanced workflow adds pandas, matplotlib, and openpyxl exports for richer professional outputs. It is optional and fails gracefully if dependencies are not installed.

Install from the repository root:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r articles/climate-systems-and-feedback-dynamics/requirements-advanced.txt
python articles/climate-systems-and-feedback-dynamics/python/run_advanced_pandas_climate_workflow.py
```

Outputs include:

- advanced grouped summary CSV
- Excel workbook
- emissions, CO2 stock, temperature, and risk figures
