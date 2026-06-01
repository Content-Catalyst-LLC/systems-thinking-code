"""Run all Python public-policy workflow scripts."""
from pathlib import Path
import subprocess
import sys
ROOT = Path(__file__).resolve().parents[1]
for folder in [ROOT / "outputs" / "tables", ROOT / "outputs" / "figures"]:
    folder.mkdir(parents=True, exist_ok=True)
for script in [
    "public_policy_feedback_model.py", "administrative_burden_index.py", "public_trust_stock_flow.py",
    "implementation_capacity_model.py", "distributional_policy_impact.py", "policy_delay_simulation.py",
    "feedback_closure_diagnostics.py"]:
    subprocess.run([sys.executable, str(ROOT / "python" / script)], check=True)
print("Python public policy workflow complete.")
