# -*- coding: utf-8 -*-
"""
Production Client Logo Extraction & Processing Pipeline.
Crops all 99 client cards from the source slide images, cleans background noise,
sorts them alphabetically A-to-Z based on data/client_names.json,
and generates crisp normalized assets in assets/client_logos/ along with data/logo_manifest.json.
"""

import os
import sys
import json
from typing import Dict, List, Any

try:
    from PIL import Image, ImageDraw  # type: ignore
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow'])
    from PIL import Image, ImageDraw  # type: ignore

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
ASSETS_DIR = os.path.join(ROOT_DIR, "assets")
OUTPUT_LOGOS_DIR = os.path.join(ASSETS_DIR, "client_logos")

# Part 1 exact row & column dividers (6 rows x 9 cols = 54 cards)
P1_ROWS = [0, 139, 265, 408, 573, 708, 842]
P1_COLS = [
    [0, 190, 400, 563, 762, 955, 1182, 1341, 1562, 1710],
    [0, 198, 381, 564, 787, 967, 1146, 1341, 1545, 1710],
    [0, 209, 377, 563, 788, 965, 1149, 1341, 1564, 1710],
    [0, 194, 370, 603, 782, 984, 1150, 1367, 1536, 1710],
    [0, 209, 368, 565, 779, 981, 1151, 1342, 1535, 1710],
    [0, 174, 377, 599, 779, 984, 1146, 1341, 1540, 1710]
]

# Part 2 exact row & column dividers (5 rows x 9 cols = 45 cards)
P2_ROWS = [0, 162, 311, 446, 590, 735]
P2_COLS = [
    [24, 203, 377, 564, 781, 969, 1146, 1363, 1543, 1715],
    [24, 189, 390, 600, 759, 964, 1181, 1359, 1557, 1715],
    [24, 203, 374, 576, 774, 969, 1146, 1358, 1535, 1715],
    [24, 190, 370, 599, 795, 960, 1152, 1359, 1535, 1715],
    [24, 191, 376, 599, 769, 962, 1146, 1341, 1572, 1715]
]

def load_client_names() -> Dict[int, str]:
    """Loads client brand names from data/client_names.json."""
    names_path = os.path.join(DATA_DIR, "client_names.json")
    if os.path.exists(names_path):
        with open(names_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return {int(k): str(v) for k, v in data.items()}
    # Fallback to scratch module if json not found
    try:
        from scratch.assign_names import names
        return names
    except ImportError:
        return {}

def extract_clean_logo_box(card_img: Image.Image) -> Image.Image:
    """Trims outer boundary artifacts and extracts clean logo bounding box."""
    rgb_img = card_img.convert('RGB')
    w, h = rgb_img.size
    
    # 1. Trim 8px border margin to eliminate boundary noise from gutters
    trim_x, trim_y = 8, 8
    if w > 2 * trim_x and h > 2 * trim_y:
        inner = rgb_img.crop((trim_x, trim_y, w - trim_x, h - trim_y))
    else:
        inner = rgb_img
        
    iw, ih = inner.size
    
    # 2. Find bounding box of non-white content
    min_x, max_x, min_y, max_y = iw, 0, ih, 0
    for y in range(ih):
        for x in range(iw):
            p = inner.getpixel((x, y))
            if not (p[0] > 245 and p[1] > 245 and p[2] > 245):
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
                
    if min_x >= max_x or min_y >= max_y:
        return inner
    
    # Add 4px breathing room around content
    min_x = max(0, min_x - 4)
    min_y = max(0, min_y - 4)
    max_x = min(iw, max_x + 4)
    max_y = min(ih, max_y + 4)
    
    return inner.crop((min_x, min_y, max_x, max_y))

def run_extraction():
    os.makedirs(OUTPUT_LOGOS_DIR, exist_ok=True)
    os.makedirs(DATA_DIR, exist_ok=True)

    p1_path = os.path.join(ASSETS_DIR, "clients_prestigious_part1.png")
    p2_path = os.path.join(ASSETS_DIR, "clients_prestigious_part2.png")

    if not os.path.exists(p1_path) or not os.path.exists(p2_path):
        print(f"[-] ERROR: Source client images not found in {ASSETS_DIR}")
        return

    im1 = Image.open(p1_path).convert('RGB')
    im2 = Image.open(p2_path).convert('RGB')

    # Clean bottom-left arrow on im1
    draw1 = ImageDraw.Draw(im1)
    draw1.rectangle([0, 740, 75, im1.height], fill=(255, 255, 255))

    raw_cards = []

    # Crop Part 1 (54 cards)
    for r in range(6):
        y0, y1 = P1_ROWS[r], P1_ROWS[r + 1]
        for c in range(9):
            x0, x1 = P1_COLS[r][c], P1_COLS[r][c + 1]
            crop = im1.crop((x0, y0, x1, y1))
            idx = len(raw_cards)
            raw_cards.append({'index': idx, 'crop': crop})

    # Crop Part 2 (45 cards)
    for r in range(5):
        y0, y1 = P2_ROWS[r], P2_ROWS[r + 1]
        for c in range(9):
            x0, x1 = P2_COLS[r][c], P2_COLS[r][c + 1]
            crop = im2.crop((x0, y0, x1, y1))
            idx = len(raw_cards)
            raw_cards.append({'index': idx, 'crop': crop})

    names = load_client_names()
    print(f"[*] Loaded {len(names)} brand names from data/client_names.json.")

    # Sort strictly alphabetically A-to-Z
    sorted_cards = sorted(raw_cards, key=lambda c: names.get(c['index'], f"Client {c['index']:02d}").lower())

    manifest: List[Dict[str, Any]] = []

    for i, item in enumerate(sorted_cards):
        idx = item['index']
        brand_name = names.get(idx, f"Client #{idx:02d}")
        clean_logo = extract_clean_logo_box(item['crop'])

        # Create standardized crisp canvas: 220 x 140
        canvas = Image.new('RGB', (220, 140), (255, 255, 255))
        max_w, max_h = 184, 110
        lw, lh = clean_logo.size
        scale = min(max_w / lw, max_h / lh, 1.35)
        new_w = max(1, int(round(lw * scale)))
        new_h = max(1, int(round(lh * scale)))

        scaled_logo = clean_logo.resize((new_w, new_h), Image.Resampling.LANCZOS)
        ox = (220 - new_w) // 2
        oy = (140 - new_h) // 2
        canvas.paste(scaled_logo, (ox, oy))

        filename = f"logo_{i + 1:02d}.png"
        filepath = os.path.join(OUTPUT_LOGOS_DIR, filename)
        canvas.save(filepath, quality=98)

        manifest.append({
            'order': i + 1,
            'filename': filename,
            'path': f'assets/client_logos/{filename}',
            'name': brand_name,
            'orig_idx': idx
        })

    manifest_path = os.path.join(DATA_DIR, "logo_manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"[+] Successfully exported {len(manifest)} client logos to {OUTPUT_LOGOS_DIR}")
    print(f"[+] Canonical manifest saved to {manifest_path}")

if __name__ == "__main__":
    run_extraction()
