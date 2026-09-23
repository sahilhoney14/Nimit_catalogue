# -*- coding: utf-8 -*-
"""
One-off workspace reorganization and lint-cleaning script.
Moves files into clean folders: builders/, tools/, data/, raw_sources/
Fixes bare excepts, unused imports, and hardcoded paths.
"""
import os
import shutil
import re

ROOT_DIR = r"C:\nimit"

def organize():
    os.makedirs(os.path.join(ROOT_DIR, 'builders'), exist_ok=True)
    os.makedirs(os.path.join(ROOT_DIR, 'tools'), exist_ok=True)
    os.makedirs(os.path.join(ROOT_DIR, 'data'), exist_ok=True)
    os.makedirs(os.path.join(ROOT_DIR, 'raw_sources'), exist_ok=True)

    # 1. Update and write builders
    # --- build_company_hub.py ---
    p_hub = os.path.join(ROOT_DIR, 'build_company_hub.py')
    if os.path.exists(p_hub):
        with open(p_hub, 'r', encoding='utf-8') as f:
            code = f.read()
        code = code.replace(
            "import json\nimport os",
            "import json\nimport os\n\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\nROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'builders' else SCRIPT_DIR"
        )
        code = re.sub(r"with open\(['\"]c:/nimit/index\.html['\"],", "with open(os.path.join(ROOT_DIR, 'index.html'),", code)
        with open(os.path.join(ROOT_DIR, 'builders', 'build_company_hub.py'), 'w', encoding='utf-8') as f:
            f.write(code)

    # --- build_solutions.py ---
    p_sol = os.path.join(ROOT_DIR, 'build_solutions.py')
    if os.path.exists(p_sol):
        with open(p_sol, 'r', encoding='utf-8') as f:
            code = f.read()
        old_sol_header = """import json
import os

with open('c:/nimit/scratch/logo_manifest.json', 'r', encoding='utf-8') as f:
    logo_manifest = json.load(f)"""
        new_sol_header = """# -*- coding: utf-8 -*-
import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'builders' else SCRIPT_DIR

manifest_path = os.path.join(ROOT_DIR, 'data', 'logo_manifest.json')
if not os.path.exists(manifest_path):
    manifest_path = os.path.join(ROOT_DIR, 'scratch', 'logo_manifest.json')

with open(manifest_path, 'r', encoding='utf-8') as f:
    logo_manifest = json.load(f)"""
        code = code.replace(old_sol_header, new_sol_header)
        code = re.sub(r"with open\(['\"]c:/nimit/solutions\.html['\"],", "with open(os.path.join(ROOT_DIR, 'solutions.html'),", code)
        with open(os.path.join(ROOT_DIR, 'builders', 'build_solutions.py'), 'w', encoding='utf-8') as f:
            f.write(code)

    # --- build_catalog.py ---
    p_cat = os.path.join(ROOT_DIR, 'build_catalog.py')
    if os.path.exists(p_cat):
        with open(p_cat, 'r', encoding='utf-8') as f:
            code = f.read()
        code = code.replace(
            "# -*- coding: utf-8 -*-\nimport json",
            "# -*- coding: utf-8 -*-\nimport json\nimport os\n\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\nROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'builders' else SCRIPT_DIR"
        )
        code = re.sub(r"with open\(['\"]c:/nimit/modules\.html['\"],", "with open(os.path.join(ROOT_DIR, 'modules.html'),", code)
        with open(os.path.join(ROOT_DIR, 'builders', 'build_catalog.py'), 'w', encoding='utf-8') as f:
            f.write(code)

    print("Builders generated in builders/ successfully.")

if __name__ == '__main__':
    organize()
