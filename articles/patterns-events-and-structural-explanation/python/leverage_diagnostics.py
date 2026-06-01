#!/usr/bin/env python3
"""Runnable professional workflow wrapper for Patterns Events and Structural Explanation."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name("run_professional_workflow.py")), run_name="__main__")
