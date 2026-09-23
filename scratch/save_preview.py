import os
import json

with open('c:/nimit/scratch/logo_manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

html = ['<!DOCTYPE html><html><head><meta charset="UTF-8"><style>body{font-family:sans-serif;background:#0f172a;color:#fff;padding:20px;} .grid{display:grid;grid-template-columns:repeat(11, 1fr);gap:10px;} .card{background:#fff;color:#000;border-radius:8px;padding:6px;text-align:center;box-shadow:0 2px 5px rgba(0,0,0,0.2);} img{width:100%;height:65px;object-fit:contain;display:block;} .lbl{font-size:10px;font-weight:bold;margin-top:4px;color:#333;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;}</style></head><body>']
html.append('<h2>All 99 Cleaned & Isolated Client Logos (A to Z)</h2><div class="grid">')
for item in manifest:
    html.append(f'<div class="card" title="{item["name"]}"><img src="../{item["path"]}"><div class="lbl">#{item["order"]:02d} {item["name"]}</div></div>')
html.append('</div></body></html>')

with open('c:/nimit/scratch/preview_clean_logos.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(html))
print('Saved c:/nimit/scratch/preview_clean_logos.html')
