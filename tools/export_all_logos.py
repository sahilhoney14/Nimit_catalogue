import sys
import os
sys.path.insert(0, 'c:/nimit')

try:
    from PIL import Image, ImageDraw  # type: ignore
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow'])
    from PIL import Image, ImageDraw  # type: ignore
from scratch.crop_cards import cards
from scratch.assign_names import names

os.makedirs('c:/nimit/assets/client_logos', exist_ok=True)

# 1. Clean bottom-left arrow on card 45 (Nesman Group)
for c in cards:
    if c['index'] == 45:
        im = c['image'].copy()
        draw = ImageDraw.Draw(im)
        draw.rectangle([0, im.height - 40, 50, im.height], fill=(255, 255, 255))
        c['image'] = im

# 2. Sort cards strictly alphabetically A to Z
sorted_cards = sorted(cards, key=lambda c: names.get(c['index'], '').lower())

def extract_tight_logo(card_img):
    rgb_img = card_img.convert('RGB')
    w, h = rgb_img.size
    
    pad = 6
    min_x, max_x, min_y, max_y = w, 0, h, 0
    for y in range(pad, h - pad):
        for x in range(pad, w - pad):
            p = rgb_img.getpixel((x, y))
            if not (p[0] > 248 and p[1] > 248 and p[2] > 248):
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
                
    if min_x >= max_x or min_y >= max_y:
        min_x, min_y, max_x, max_y = pad, pad, w - pad, h - pad
    else:
        min_x = max(0, min_x - 4)
        min_y = max(0, min_y - 4)
        max_x = min(w, max_x + 4)
        max_y = min(h, max_y + 4)
        
    return rgb_img.crop((min_x, min_y, max_x, max_y))

logo_manifest = []

for i, item in enumerate(sorted_cards):
    idx = item['index']
    brand_name = names.get(idx, f"Client {i+1}")
    
    logo_content = extract_tight_logo(item['image'])
    
    # Save as clean high-res square/contain card
    # Normalized canvas: 220 x 140
    card_canvas = Image.new('RGBA', (220, 140), (255, 255, 255, 255))
    
    # Fit logo into max 180 x 105
    max_w, max_h = 180, 105
    lw, lh = logo_content.size
    scale = min(max_w / lw, max_h / lh, 1.4)
    new_w = max(1, int(round(lw * scale)))
    new_h = max(1, int(round(lh * scale)))
    
    logo_scaled = logo_content.resize((new_w, new_h), Image.Resampling.LANCZOS)
    ox = (220 - new_w) // 2
    oy = (140 - new_h) // 2
    card_canvas.paste(logo_scaled, (ox, oy))
    
    filename = f"logo_{i+1:02d}.png"
    filepath = os.path.join('c:/nimit/assets/client_logos', filename)
    card_canvas.convert('RGB').save(filepath, quality=95)
    
    logo_manifest.append({
        'order': i + 1,
        'filename': filename,
        'path': f'assets/client_logos/{filename}',
        'name': brand_name,
        'orig_idx': idx
    })

print(f"Exported {len(logo_manifest)} client logos to c:/nimit/assets/client_logos/")

import json
with open('c:/nimit/scratch/logo_manifest.json', 'w', encoding='utf-8') as f:
    json.dump(logo_manifest, f, indent=2)

print("Saved logo manifest JSON.")
