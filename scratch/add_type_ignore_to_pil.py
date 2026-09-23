# -*- coding: utf-8 -*-
"""
Appends '# type: ignore' to all PIL imports in tools/ and builders/
to eliminate Pyrefly and Pyright type-checker error markers.
"""
import glob
import re

files = sorted(glob.glob('tools/*.py') + glob.glob('builders/*.py'))

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    
    new_lines = []
    modified = False
    for line in lines:
        if 'from PIL import' in line and '# type: ignore' not in line:
            # strip trailing newline and add # type: ignore
            stripped = line.rstrip('\r\n')
            new_lines.append(stripped + '  # type: ignore\n')
            modified = True
        else:
            new_lines.append(line)
            
    if modified:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.writelines(new_lines)
        print('Added # type: ignore to:', f)

print('Done updating PIL imports.')
