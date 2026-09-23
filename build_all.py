# -*- coding: utf-8 -*-
"""
NIMIT AI Vision Presentation & Web Portal - Master Build Runner
Compiles all 3 core presentation portals into standalone HTML deliverables:
  1. index.html       (NIMIT Company Hub & Overview)
  2. solutions.html   (Intelligent Industry Solutions Ecosystem - 18 Slides)
  3. modules.html     (Art of Intelligence AI Analytics Catalog - 18 Slides)
"""

import os
import sys
import time
import subprocess

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
BUILDERS_DIR = os.path.join(ROOT_DIR, "builders")

BUILD_SCRIPTS = [
    ("Company Hub (index.html)", "build_company_hub.py"),
    ("Solutions Ecosystem (solutions.html)", "build_solutions.py"),
    ("AI Modules Catalog (modules.html)", "build_catalog.py"),
]

def run_builds():
    print("=" * 70)
    print("  NIMIT AI VISION — MASTER BUILD COMPILER")
    print("=" * 70)
    start_time = time.time()
    errors = 0

    for name, script_name in BUILD_SCRIPTS:
        script_path = os.path.join(BUILDERS_DIR, script_name)
        if not os.path.exists(script_path):
            print(f"[-] ERROR: Script not found: {script_path}")
            errors += 1
            continue

        print(f"[*] Building {name}...")
        t0 = time.time()
        res = subprocess.run([sys.executable, script_path], cwd=ROOT_DIR, capture_output=True, text=True)
        elapsed = time.time() - t0

        if res.returncode == 0:
            print(f"    [+] SUCCESS ({elapsed:.2f}s): {res.stdout.strip()}")
        else:
            print(f"    [-] FAILED ({elapsed:.2f}s)")
            print(f"    STDERR: {res.stderr.strip()}")
            errors += 1

    total_time = time.time() - start_time
    print("-" * 70)
    if errors == 0:
        print(f"[SUCCESS] All 3 portals compiled successfully in {total_time:.2f}s!")
        print(f"  • Entry Portal : file:///{os.path.join(ROOT_DIR, 'index.html').replace(chr(92), '/')}")
        print(f"  • Solutions    : file:///{os.path.join(ROOT_DIR, 'solutions.html').replace(chr(92), '/')}")
        print(f"  • AI Modules   : file:///{os.path.join(ROOT_DIR, 'modules.html').replace(chr(92), '/')}")
    else:
        print(f"[WARNING] Build completed with {errors} error(s) in {total_time:.2f}s.")
    print("=" * 70)

if __name__ == "__main__":
    run_builds()
