#!/usr/bin/env python3
"""Run-gate: execute every pattern, fail loudly on any failure."""
import subprocess, sys, time
from pathlib import Path

root = Path(__file__).resolve().parent.parent
files = sorted((root / "patterns").rglob("*.py"))
failed = []
for f in files:
    t0 = time.time()
    try:
        p = subprocess.run([sys.executable, str(f)], capture_output=True, text=True, timeout=90)
        ok = p.returncode == 0
    except subprocess.TimeoutExpired:
        ok = False
    print(f"{'PASS' if ok else 'FAIL':4s} {time.time()-t0:6.1f}s  {f.relative_to(root)}")
    if not ok:
        failed.append(f)
print(f"\n{len(files)-len(failed)}/{len(files)} PASS")
sys.exit(1 if failed else 0)
