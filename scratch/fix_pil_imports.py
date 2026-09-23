# -*- coding: utf-8 -*-
"""
Safely standardizes PIL imports across all tools in tools/
"""
import glob
import re

tools = sorted(glob.glob('tools/*.py'))
for t in tools:
    with open(t, 'r', encoding='utf-8') as f:
        src = f.read()

    if 'try:\n    from PIL import' in src:
        print('Already wrapped:', t)
        continue

    m = re.search(r'from PIL import ([^\n]+)', src)
    if m:
        orig = m.group(0)
        items = m.group(1).strip()
        replacement = (
            "try:\n"
            f"    from PIL import {items}\n"
            "except ImportError:\n"
            "    import subprocess\n"
            "    import sys\n"
            f"    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow'])\n"
            f"    from PIL import {items}"
        )
        src = src.replace(orig, replacement)
        with open(t, 'w', encoding='utf-8') as f:
            f.write(src)
        print('Updated PIL import in:', t)

print('Done standardizing PIL imports.')
