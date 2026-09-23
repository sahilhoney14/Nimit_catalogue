# -*- coding: utf-8 -*-
"""
Tool to combine client slides into side-by-side or stacked master grids.
"""
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

def create_combined_clients():
    p1 = os.path.join(ROOT_DIR, 'assets', 'clients_prestigious_part1.png')
    p2 = os.path.join(ROOT_DIR, 'assets', 'clients_prestigious_part2.png')
    
    if not os.path.exists(p1) or not os.path.exists(p2):
        print("[-] Client source images not found. Skipping.")
        return

    im1 = Image.open(p1).convert('RGBA')
    im2 = Image.open(p2).convert('RGBA')
    
    # 1. Option A: Side-by-Side (2 Columns) - Wide Landscape 16:7 format
    target_h = max(im1.height, im2.height)
    im2_scaled_w = int(im2.width * (target_h / im2.height))
    im2_scaled = im2.resize((im2_scaled_w, target_h), Image.Resampling.LANCZOS)
    
    side_w = im1.width + im2_scaled_w + 60
    side_img = Image.new('RGB', (side_w, target_h + 40), color=(255, 255, 255))
    side_draw = ImageDraw.Draw(side_img)
    
    # Paste im1 on left
    side_img.paste(im1.convert('RGB'), (20, 20))
    # Vertical divider line
    div_x = 20 + im1.width + 10
    side_draw.line([(div_x, 30), (div_x, target_h + 10)], fill=(226, 232, 240), width=2)
    # Paste im2 on right
    side_img.paste(im2_scaled.convert('RGB'), (div_x + 20, 20))
    
    out_w = 2400
    out_h = int(out_w * (side_img.height / side_img.width))
    side_final = side_img.resize((out_w, out_h), Image.Resampling.LANCZOS)
    side_path = os.path.join(ROOT_DIR, 'assets', 'clients_prestigious_side_by_side.png')
    side_final.save(side_path, quality=98)
    print('Saved side-by-side:', side_final.size)
    
    # 2. Option B: Stacked 2-Row Master Grid
    max_w = max(im1.width, im2.width)
    im2_w_scaled = int(im2.height * (max_w / im2.width))
    im2_resized = im2.resize((max_w, im2_w_scaled), Image.Resampling.LANCZOS)
    
    stack_h = im1.height + im2_resized.height + 40
    stack_img = Image.new('RGB', (max_w + 40, stack_h), color=(255, 255, 255))
    stack_draw = ImageDraw.Draw(stack_img)
    
    stack_img.paste(im1.convert('RGB'), (20, 15))
    h_div_y = 15 + im1.height + 10
    stack_draw.line([(40, h_div_y), (max_w, h_div_y)], fill=(226, 232, 240), width=2)
    stack_img.paste(im2_resized.convert('RGB'), (20, h_div_y + 15))
    
    s_out_w = 2000
    s_out_h = int(s_out_w * (stack_img.height / stack_img.width))
    stack_final = stack_img.resize((s_out_w, s_out_h), Image.Resampling.LANCZOS)
    stack_path = os.path.join(ROOT_DIR, 'assets', 'clients_prestigious_stacked.png')
    stack_final.save(stack_path, quality=98)
    print('Saved stacked:', stack_final.size)
    
    comb_path = os.path.join(ROOT_DIR, 'assets', 'clients_prestigious_combined.png')
    stack_final.save(comb_path, quality=98)

if __name__ == '__main__':
    create_combined_clients()
