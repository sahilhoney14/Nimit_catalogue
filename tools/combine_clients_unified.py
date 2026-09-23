# -*- coding: utf-8 -*-
"""
Tool to combine Part 1 & Part 2 client logo grids into a seamless high-res master image.
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

def process_unified():
    p1 = os.path.join(ROOT_DIR, 'assets', 'clients_prestigious_part1.png')
    p2 = os.path.join(ROOT_DIR, 'assets', 'clients_prestigious_part2.png')
    
    if not os.path.exists(p1) or not os.path.exists(p2):
        print("[-] Client source images not found. Skipping.")
        return

    im1 = Image.open(p1).convert('RGBA')
    im2 = Image.open(p2).convert('RGBA')
    
    # 1. Clean bottom-left blue arrow in im1
    draw1 = ImageDraw.Draw(im1)
    draw1.rectangle([0, 740, 75, im1.height], fill=(255, 255, 255, 255))
    
    # 2. Crop excess white margins on the junction edges
    im1_cropped = im1.crop((0, 0, 1692, im1.height))
    im2_cropped = im2.crop((30, 0, im2.width, im2.height))
    
    # 3. Match heights
    target_h = im1_cropped.height
    im2_scaled_w = int(im2_cropped.width * (target_h / im2_cropped.height))
    im2_scaled = im2_cropped.resize((im2_scaled_w, target_h), Image.Resampling.LANCZOS)
    
    # 4. Join seamlessly with tight 8px gap
    middle_gap = 8
    total_w = im1_cropped.width + middle_gap + im2_scaled_w
    unified = Image.new('RGB', (total_w, target_h), color=(255, 255, 255))
    
    unified.paste(im1_cropped.convert('RGB'), (0, 0))
    unified.paste(im2_scaled.convert('RGB'), (im1_cropped.width + middle_gap, 0))
    
    # 5. Save crystal sharp high-res master
    out_w = 2800
    out_h = int(out_w * (unified.height / unified.width))
    unified_final = unified.resize((out_w, out_h), Image.Resampling.LANCZOS)
    
    unified_path = os.path.join(ROOT_DIR, 'assets', 'clients_prestigious_unified.png')
    unified_final.save(unified_path, quality=98)
    print(f"Successfully generated seamless unified client logo wall: {unified_path} {unified_final.size}")

if __name__ == '__main__':
    process_unified()
