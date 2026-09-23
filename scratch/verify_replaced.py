import json
from PIL import Image

with open('c:/nimit/scratch/logo_manifest.json', 'r', encoding='utf-8') as f:
    manifest = json.load(f)

for item in manifest:
    if 'Adani' in item['name'] or 'Meghmani' in item['name']:
        print(f"#{item['order']:02d}: {item['filename']} -> {item['name']}")
        im = Image.open(f"c:/nimit/{item['path']}")
        print(f"   Size: {im.size}, Mode: {im.mode}")
