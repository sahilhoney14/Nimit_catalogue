# -*- coding: utf-8 -*-
"""
Tool to cleanly extract and generate perfect client logos into assets/client_logos/
and output logo_manifest.json into data/.
"""
import os
import json
try:
    from PIL import Image, ImageDraw  # type: ignore
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow'])
    from PIL import Image, ImageDraw  # type: ignore

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'tools' else SCRIPT_DIR

def run_generate_perfect_logos():
    p1_path = os.path.join(ROOT_DIR, 'assets', 'clients_prestigious_part1.png')
    p2_path = os.path.join(ROOT_DIR, 'assets', 'clients_prestigious_part2.png')
    
    if not os.path.exists(p1_path) or not os.path.exists(p2_path):
        print(f"[-] Source client images not found in assets. Skipping logo extraction.")
        return

    im1 = Image.open(p1_path).convert('RGB')
    im2 = Image.open(p2_path).convert('RGB')

    # Clean bottom-left arrow on im1
    draw1 = ImageDraw.Draw(im1)
    draw1.rectangle([0, 740, 75, im1.height], fill=(255, 255, 255))

    # Exact bounding boxes for all 54 logos in Part 1 (y_band, [x_start, x_end] for each of 9 logos)
    p1_logo_boxes = [
        # Row 0: y=[16..139]
        ((16, 139), [
            (60, 214), (232, 395), (427, 580), (613, 713), (769, 921), 
            (963, 1116), (1133, 1298), (1315, 1475), (1504, 1651)
        ]),
        # Row 1: y=[158..281]
        ((158, 281), [
            (52, 214), (231, 397), (424, 580), (596, 762), (777, 950), 
            (956, 1103), (1140, 1298), (1315, 1465), (1502, 1677)
        ]),
        # Row 2: y=[301..427]
        ((301, 427), [
            (50, 200), (230, 392), (427, 580), (602, 760), (777, 932), 
            (969, 1123), (1144, 1301), (1333, 1485), (1509, 1656)
        ]),
        # Row 3: y=[432..557]
        ((432, 557), [
            (49, 211), (230, 392), (410, 571), (604, 764), (782, 954), 
            (1001, 1079), (1140, 1301), (1331, 1485), (1510, 1649)
        ]),
        # Row 4: y=[566..694]
        ((566, 694), [
            (50, 199), (242, 393), (417, 580), (601, 767), (784, 954), 
            (988, 1111), (1148, 1287), (1321, 1486), (1497, 1668)
        ]),
        # Row 5: y=[702..833]
        ((702, 833), [
            (53, 215), (232, 393), (422, 572), (603, 764), (789, 954), 
            (981, 1105), (1147, 1294), (1340, 1499), (1501, 1667)
        ])
    ]

    # Exact bounding boxes for all 45 logos in Part 2
    p2_logo_boxes = [
        # Row 0: y=[13..146]
        ((13, 146), [
            (43, 182), (225, 393), (420, 580), (597, 753), (784, 940), 
            (978, 1089), (1143, 1307), (1338, 1504), (1533, 1689)
        ]),
        # Row 1: y=[158..283]
        ((158, 283), [
            (45, 185), (223, 391), (428, 563), (604, 759), (790, 946), 
            (968, 1115), (1154, 1307), (1330, 1504), (1521, 1679)
        ]),
        # Row 2: y=[298..430]
        ((298, 430), [
            (45, 189), (223, 394), (419, 576), (612, 755), (786, 946), 
            (963, 1112), (1143, 1313), (1336, 1499), (1521, 1680)
        ]),
        # Row 3: y=[435..568]
        ((435, 568), [
            (43, 187), (225, 391), (425, 567), (605, 755), (786, 936), 
            (960, 1112), (1149, 1310), (1348, 1490), (1520, 1680)
        ]),
        # Row 4: y=[575..707]
        ((575, 707), [
            (43, 187), (225, 393), (420, 580), (603, 760), (785, 939), 
            (970, 1112), (1145, 1310), (1340, 1504), (1520, 1680)
        ])
    ]

    all_crops = []
    # Crop Part 1
    idx = 1
    for (y_top, y_bot), x_pairs in p1_logo_boxes:
        for x_left, x_right in x_pairs:
            c = im1.crop((x_left, y_top, x_right, y_bot))
            all_crops.append((idx, c))
            idx += 1

    # Crop Part 2
    for (y_top, y_bot), x_pairs in p2_logo_boxes:
        for x_left, x_right in x_pairs:
            c = im2.crop((x_left, y_top, x_right, y_bot))
            all_crops.append((idx, c))
            idx += 1

    # Load brand names
    details_path = os.path.join(ROOT_DIR, 'scratch', 'client_details.json')
    if os.path.exists(details_path):
        with open(details_path, 'r', encoding='utf-8') as f:
            details = json.load(f)
    else:
        details = {}

    # Sort alphabetically
    named_crops = []
    for idx, crop in all_crops:
        brand = details.get(str(idx), f"Client {idx}")
        named_crops.append((idx, brand, crop))

    named_crops.sort(key=lambda x: x[1].lower())

    out_dir = os.path.join(ROOT_DIR, 'assets', 'client_logos')
    os.makedirs(out_dir, exist_ok=True)

    manifest = []
    for i, (idx, brand, raw_crop) in enumerate(named_crops):
        cw, ch = raw_crop.size
        # Find tight bounding box
        min_x, max_x, min_y, max_y = cw, 0, ch, 0
        pad = 2
        for y in range(pad, ch - pad):
            for x in range(pad, cw - pad):
                p = raw_crop.getpixel((x, y))
                if not (p[0] > 246 and p[1] > 246 and p[2] > 246):
                    if x < min_x: min_x = x
                    if x > max_x: max_x = x
                    if y < min_y: min_y = y
                    if y > max_y: max_y = y
                    
        if min_x >= max_x or min_y >= max_y:
            tight_logo = raw_crop
        else:
            min_x = max(0, min_x - 2)
            min_y = max(0, min_y - 2)
            max_x = min(cw, max_x + 2)
            max_y = min(ch, max_y + 2)
            tight_logo = raw_crop.crop((min_x, min_y, max_x, max_y))
            
        # Render onto clean white 220 x 140 card
        card_img = Image.new('RGB', (220, 140), (255, 255, 255))
        max_w, max_h = 184, 110
        lw, lh = tight_logo.size
        scale = min(max_w / lw, max_h / lh, 1.35)
        new_w = max(1, int(round(lw * scale)))
        new_h = max(1, int(round(lh * scale)))
        
        scaled_logo = tight_logo.resize((new_w, new_h), Image.Resampling.LANCZOS)
        ox = (220 - new_w) // 2
        oy = (140 - new_h) // 2
        card_img.paste(scaled_logo, (ox, oy))
        
        filename = f"logo_{i+1:02d}.png"
        filepath = os.path.join(out_dir, filename)
        card_img.save(filepath, quality=98)
        
        manifest.append({
            'order': i + 1,
            'filename': filename,
            'path': f'assets/client_logos/{filename}',
            'name': brand,
            'orig_idx': idx
        })

    manifest_path = os.path.join(ROOT_DIR, 'data', 'logo_manifest.json')
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)

    print(f"Generated {len(manifest)} client logo files into assets/client_logos/ and updated data/logo_manifest.json.")

if __name__ == '__main__':
    run_generate_perfect_logos()
