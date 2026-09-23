# -*- coding: utf-8 -*-
"""
Removes inner paragraph descriptions from capability cards in builders/build_catalog.py,
keeping only the clean icon + title + arrow structure matching build_solutions.py.
"""
import re

with open("builders/build_catalog.py", "r", encoding="utf-8") as f:
    code = f.read()

# Pattern to match:
# <div class="premise-card-content">\s*<h3 class="premise-card-title">(.*?)</h3>\s*<span class="analytics-desc-lead".*?</span>\s*</div>
pattern = re.compile(
    r'<div class="premise-card-content">\s*<h3 class="premise-card-title">(.*?)</h3>\s*<span class="analytics-desc-lead".*?</span>\s*</div>',
    re.DOTALL
)

def replacer(match):
    title = match.group(1).strip()
    return f'<h3 class="analytics-card-title">{title}</h3>'

new_code, count = pattern.subn(replacer, code)

print(f"Replaced {count} cards to heading-only style.")

with open("builders/build_catalog.py", "w", encoding="utf-8") as f:
    f.write(new_code)
