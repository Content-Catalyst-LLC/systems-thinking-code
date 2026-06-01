"""Run all Python sustainability workflow scripts."""
from pathlib import Path
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[1]
for folder in [ROOT / "outputs" / "tables", ROOT / "outputs" / "figures"]:
    folder.mkdir(parents=True, exist_ok=True)
for script in [
    "sustainability_stock_flow_model.py", "carbon_accumulation_scenarios.py", "resource_overshoot_diagnostics.py",
    "resilience_threshold_simulation.py", "rebound_effect_model.py", "distributional_sustainability_analysis.py",
    "sensitivity_analysis_sustainability.py"]:
    subprocess.run([sys.executable, str(ROOT / "python" / script)], check=True)
print("Python sustainability workflow complete.")
