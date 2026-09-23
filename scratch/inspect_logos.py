import os
from PIL import Image

# Build an html page to display all 99 logos with index numbers
files = sorted(os.listdir('c:/nimit/scratch/all_client_logos'))
html = ['<!DOCTYPE html><html><head><style>body{font-family:sans-serif;background:#0f172a;color:#fff;padding:20px;} .grid{display:grid;grid-template-columns:repeat(9, 1fr);gap:10px;} .card{background:#fff;color:#000;border-radius:6px;padding:6px;text-align:center;box-shadow:0 2px 5px rgba(0,0,0,0.2);} img{width:100%;height:65px;object-fit:contain;display:block;} .lbl{font-size:11px;font-weight:bold;margin-top:4px;color:#333;}</style></head><body>']
html.append('<h2>All 99 Cropped Logos (Indexed)</h2><div class="grid">')
for i, f in enumerate(files):
    html.append(f'<div class="card"><img src="all_client_logos/{f}"><div class="lbl">#{i:02d}</div></div>')
html.append('</div></body></html>')

with open('c:/nimit/scratch/preview_logos.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(html))
print('Saved c:/nimit/scratch/preview_logos.html')
