import sys
import os
sys.path.insert(0, 'c:/nimit')

from PIL import Image, ImageDraw
from scratch.crop_precise_cards import precise_cards
from scratch.assign_names import names

os.makedirs('c:/nimit/assets/client_logos', exist_ok=True)
os.makedirs('c:/nimit/scratch/clean_inspection', exist_ok=True)

# Sort cards strictly alphabetically A to Z
sorted_cards = sorted(precise_cards, key=lambda c: names.get(c['index'], '').lower())

def extract_clean_logo(card_img):
    """
    Extracts the clean logo from the precisely cropped card.
    Trims any outer boundary artifacts and finds the genuine logo content.
    """
    rgb_img = card_img.convert('RGB')
    w, h = rgb_img.size
    
    # 1. Trim 8px border margin to ensure zero boundary noise from gutters/shadows
    trim_x = 8
    trim_y = 8
    if w > 2 * trim_x and h > 2 * trim_y:
        inner = rgb_img.crop((trim_x, trim_y, w - trim_x, h - trim_y))
    else:
        inner = rgb_img
        
    iw, ih = inner.size
    
    # 2. Find bounding box of non-white pixels
    min_x, max_x, min_y, max_y = iw, 0, ih, 0
    for y in range(ih):
        for x in range(iw):
            p = inner.getpixel((x, y))
            # If not pure/near white (RGB < 246)
            if not (p[0] > 245 and p[1] > 245 and p[2] > 245):
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
                
    if min_x >= max_x or min_y >= max_y:
        # If blank/white, return full inner
        return inner
    
    # Add 4px breathing room around content
    min_x = max(0, min_x - 4)
    min_y = max(0, min_y - 4)
    max_x = min(iw, max_x + 4)
    max_y = min(ih, max_y + 4)
    
    return inner.crop((min_x, min_y, max_x, max_y))

logo_manifest = []

for i, item in enumerate(sorted_cards):
    idx = item['index']
    brand_name = names.get(idx, f"Client {i+1}")
    
    clean_logo = extract_clean_logo(item['crop'])
    
    # Standard crisp canvas: 220 x 140
    card_canvas = Image.new('RGB', (220, 140), (255, 255, 255))
    
    max_w, max_h = 184, 110
    lw, lh = clean_logo.size
    scale = min(max_w / lw, max_h / lh, 1.35)
    new_w = max(1, int(round(lw * scale)))
    new_h = max(1, int(round(lh * scale)))
    
    scaled_logo = clean_logo.resize((new_w, new_h), Image.Resampling.LANCZOS)
    ox = (220 - new_w) // 2
    oy = (140 - new_h) // 2
    card_canvas.paste(scaled_logo, (ox, oy))
    
    filename = f"logo_{i+1:02d}.png"
    filepath = os.path.join('c:/nimit/assets/client_logos', filename)
    card_canvas.save(filepath, quality=98)
    
    logo_manifest.append({
        'order': i + 1,
        'filename': filename,
        'path': f'assets/client_logos/{filename}',
        'name': brand_name,
        'orig_idx': idx
    })

print(f"Successfully generated {len(logo_manifest)} clean logo assets.")

import json
with open('c:/nimit/scratch/logo_manifest.json', 'w', encoding='utf-8') as f:
    json.dump(logo_manifest, f, indent=2)

# Also generate a contact sheet grid for quick visual verification
contact_w = 220 * 11
contact_h = 140 * 9
contact_sheet = Image.new('RGB', (contact_w, contact_h), (255, 255, 255))

for i, item in enumerate(logo_manifest):
    r = i // 11
    c = i % 11
    img = Image.open(f"c:/nimit/{item['path']}")
    x = c * 220
    y = r * 140
    contact_sheet.paste(img, (x, y))

contact_sheet.save('c:/nimit/scratch/clean_inspection/all_99_cleaned_grid.png', quality=95)
print("Saved clean inspection contact sheet.")
