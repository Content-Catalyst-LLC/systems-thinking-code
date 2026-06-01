# Optional Advanced Pandas Workflow

The default workflow does not require pandas. The optional workflow can create richer summaries, figures, and Excel exports after installing advanced dependencies:

```bash
python3 -m pip install pandas matplotlib openpyxl
python3 python/run_advanced_pandas_workflow.py
```

If dependencies are missing, the script exits gracefully and does not fail the default smoke test.
