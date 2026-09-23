# -*- coding: utf-8 -*-
"""
Tool to sort and render alphabetical client walls for desktop and mobile.
"""
import sys
import os
try:
    from PIL import Image, ImageDraw  # type: ignore
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow'])
    from PIL import Image, ImageDraw  # type: ignore

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'tools' else SCRIPT_DIR
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

try:
    from scratch.crop_cards import cards
    from scratch.assign_names import names
except ImportError:
    cards = []
    names = {}

# 1. Clean bottom-left arrow on card 45 (Nesman Group)
for c in cards:
    if c.get('index') == 45:
        im = c['image'].copy()
        draw = ImageDraw.Draw(im)
        draw.rectangle([0, im.height - 40, 50, im.height], fill=(255, 255, 255))
        c['image'] = im

# 2. Sort cards strictly alphabetically A to Z
sorted_cards = sorted(cards, key=lambda c: names.get(c.get('index', 0), '').lower())

def extract_logo_content(card_img):
    """
    Extracts the tight bounding box of the logo from a card crop.
    """
    rgb_img = card_img.convert('RGB')
    w, h = rgb_img.size
    
    min_x, max_x, min_y, max_y = w, 0, h, 0
    pad = 6
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
        min_x = max(0, min_x - 3)
        min_y = max(0, min_y - 3)
        max_x = min(w, max_x + 3)
        max_y = min(h, max_y + 3)
        
    return rgb_img.crop((min_x, min_y, max_x, max_y))

def create_card_tile(logo_crop, tile_w=240, tile_h=160):
    """
    Creates a card tile with light border.
    """
    tile = Image.new('RGB', (tile_w, tile_h), color=(255, 255, 255))
    draw = ImageDraw.Draw(tile)
    
    # Subtle card border
    draw.rounded_rectangle([0, 0, tile_w - 1, tile_h - 1], radius=10, outline=(226, 232, 240), width=1)
    
    # Scale logo into tile inner box
    inner_w = tile_w - 36
    inner_h = tile_h - 30
    
    lw, lh = logo_crop.size
    scale = min(inner_w / lw, inner_h / lh, 1.25)
    
    new_w = max(1, int(round(lw * scale)))
    new_h = max(1, int(round(lh * scale)))
    
    scaled_logo = logo_crop.resize((new_w, new_h), Image.Resampling.LANCZOS)
    
    ox = (tile_w - new_w) // 2
    oy = (tile_h - new_h) // 2
    tile.paste(scaled_logo, (ox, oy))
    
    return tile

def build_desktop_grid():
    if not sorted_cards:
        print("[-] No cards available to build desktop grid.")
        return
    cols = 11
    rows = 9
    card_w = 240
    card_h = 160
    gap = 14
    margin = 20
    
    total_w = margin * 2 + cols * card_w + (cols - 1) * gap
    total_h = margin * 2 + rows * card_h + (rows - 1) * gap
    
    canvas = Image.new('RGB', (total_w, total_h), color=(255, 255, 255))
    
    for i, item in enumerate(sorted_cards):
        r = i // cols
        c = i % cols
        
        logo_content = extract_logo_content(item['image'])
        tile = create_card_tile(logo_content, card_w, card_h)
        
        x = margin + c * (card_w + gap)
        y = margin + r * (card_h + gap)
        canvas.paste(tile, (x, y))
        
    out_master = os.path.join(ROOT_DIR, 'assets', 'clients_prestigious_unified.png')
    out_alpha = os.path.join(ROOT_DIR, 'assets', 'clients_prestigious_alphabetical.png')
    canvas.save(out_master, quality=98)
    canvas.save(out_alpha, quality=98)
    print(f"Generated Desktop A-Z Client Wall: {out_master} ({total_w}x{total_h})")

def build_mobile_grid():
    if not sorted_cards:
        print("[-] No cards available to build mobile grid.")
        return
    cols = 5
    rows = 20
    card_w = 200
    card_h = 136
    gap = 10
    margin = 12
    
    total_w = margin * 2 + cols * card_w + (cols - 1) * gap
    total_h = margin * 2 + rows * card_h + (rows - 1) * gap
    
    canvas = Image.new('RGB', (total_w, total_h), color=(255, 255, 255))
    
    for i, item in enumerate(sorted_cards):
        r = i // cols
        c = i % cols
        
        logo_content = extract_logo_content(item['image'])
        tile = create_card_tile(logo_content, card_w, card_h)
        
        x = margin + c * (card_w + gap)
        y = margin + r * (card_h + gap)
        canvas.paste(tile, (x, y))
        
    out_mobile = os.path.join(ROOT_DIR, 'assets', 'clients_prestigious_mobile.png')
    canvas.save(out_mobile, quality=98)
    print(f"Generated Mobile A-Z Client Wall: {out_mobile} ({total_w}x{total_h})")

if __name__ == '__main__':
    build_desktop_grid()
    build_mobile_grid()
