import json
from PIL import Image

with open('c:/nimit/scratch/logo_manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

for item in manifest:
    name = item['name']
    if any(k in name for k in ['Apollo', 'Agni', 'Ajanta', 'Atul', 'Borosil', 'CHARUSAT', 'GGRC', 'GNFC', 'MGVCL', 'Utopia', 'Zydus']):
        print(f"{item['order']:02d}. {item['filename']}: {name}")
