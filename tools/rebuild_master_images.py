# -*- coding: utf-8 -*-
"""
Tool to rebuild desktop and mobile unified client logo wall images from assets/client_logos/.
"""
import os
import json
try:
    from PIL import Image  # type: ignore
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow'])
    from PIL import Image  # type: ignore

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'tools' else SCRIPT_DIR

def rebuild_masters():
    manifest_path = os.path.join(ROOT_DIR, 'data', 'logo_manifest.json')
    if not os.path.exists(manifest_path):
        manifest_path = os.path.join(ROOT_DIR, 'scratch', 'logo_manifest.json')

    if not os.path.exists(manifest_path):
        print("[-] logo_manifest.json not found.")
        return

    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    # 1. Build 11 x 9 Desktop Master
    card_w = 220
    card_h = 140
    gap = 12
    margin = 16
    cols = 11
    rows = 9

    total_w = margin * 2 + cols * card_w + (cols - 1) * gap
    total_h = margin * 2 + rows * card_h + (rows - 1) * gap

    desktop_img = Image.new('RGB', (total_w, total_h), (255, 255, 255))

    for i, item in enumerate(manifest):
        r = i // cols
        c = i % cols
        img_path = os.path.join(ROOT_DIR, item['path'])
        if os.path.exists(img_path):
            img = Image.open(img_path)
            x = margin + c * (card_w + gap)
            y = margin + r * (card_h + gap)
            desktop_img.paste(img, (x, y))

    out_unified = os.path.join(ROOT_DIR, 'assets', 'clients_prestigious_unified.png')
    out_alpha = os.path.join(ROOT_DIR, 'assets', 'clients_prestigious_alphabetical.png')
    desktop_img.save(out_unified, quality=98)
    desktop_img.save(out_alpha, quality=98)
    print(f"Generated clean master image: {out_unified} ({total_w}x{total_h})")

    # 2. Build Mobile Master (4 cols x 25 rows)
    m_cols = 4
    m_rows = 25
    m_total_w = margin * 2 + m_cols * card_w + (m_cols - 1) * gap
    m_total_h = margin * 2 + m_rows * card_h + (m_rows - 1) * gap

    mobile_img = Image.new('RGB', (m_total_w, m_total_h), (255, 255, 255))
    for i, item in enumerate(manifest):
        r = i // m_cols
        c = i % m_cols
        img_path = os.path.join(ROOT_DIR, item['path'])
        if os.path.exists(img_path):
            img = Image.open(img_path)
            x = margin + c * (card_w + gap)
            y = margin + r * (card_h + gap)
            mobile_img.paste(img, (x, y))

    out_mobile = os.path.join(ROOT_DIR, 'assets', 'clients_prestigious_mobile.png')
    mobile_img.save(out_mobile, quality=98)
    print(f"Generated clean mobile master image: {out_mobile} ({m_total_w}x{m_total_h})")

if __name__ == '__main__':
    rebuild_masters()
