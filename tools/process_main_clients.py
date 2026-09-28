# -*- coding: utf-8 -*-
"""
Process main_clients logos:
Reads all official logos from assets/client_logos/main_clients/,
normalizes each logo onto a clean white canvas with high-quality resampling,
sorts alphabetically A-to-Z, and saves to assets/client_logos/ and data/logo_manifest.json.
"""

import os
import sys
import json
from PIL import Image

ROOT_DIR = r"c:\nimit"
MAIN_DIR = os.path.join(ROOT_DIR, "assets", "client_logos", "main_clients")
OUT_DIR = os.path.join(ROOT_DIR, "assets", "client_logos")
DATA_DIR = os.path.join(ROOT_DIR, "data")

NAME_MAP = {
    "Aarti-Industries.jpg": "Aarti Industries",
    "ABB.png": "ABB",
    "Adani.png": "Adani Group",
    "Aditya Birla - Hindalco.png": "Aditya Birla (Hindalco)",
    "Ajanta-Pharma.jpg": "Ajanta Pharma",
    "Alembic_Pharmaceuticals_Ltd.png": "Alembic Pharmaceuticals",
    "Anoopam Mission.jpg": "Anoopam Mission",
    "Apollo tyre.png": "Apollo Tyres",
    "Apothecon.png": "Apothecon Pharmaceuticals",
    "Armein Pharma.png": "Armein Pharmaceuticals",
    "ATG_Yokohama.jpg": "ATG Yokohama",
    "Atul.png": "Atul Ltd",
    "Baroda Dairy.png": "Baroda Dairy",
    "Bhaikaka University.png": "Bhaikaka University",
    "Borosil.png": "Borosil",
    "Charotar Gas.png": "Charotar Gas",
    "Charusat.png": "CHARUSAT University",
    "Cipla.png": "Cipla",
    "Darshanam Group.png": "Darshanam Group",
    "Deepak Chem Tech.png": "Deepak Chem Tech",
    "Deepak Nitrite.jpeg": "Deepak Nitrite",
    "Deepak Phenolics.png": "Deepak Phenolics",
    "DLF.png": "DLF",
    "Duflon.png": "Duflon",
    "Elmex.png": "Elmex Controls",
    "Encube.png": "Encube Ethicals",
    "Epoxy.png": "Epoxy House",
    "ERDA.jpg": "ERDA",
    "Flint.png": "Flint Group",
    "FMC.png": "FMC Corporation",
    "GACL.png": "GACL (Gujarat Alkalies)",
    "Gala.png": "Gala Precision",
    "Gandhi Tubes.png": "Gandhi Special Tubes",
    "GCPL.png": "GCPL (Godrej / Gujarat Chemical Port)",
    "GIPCL.jpg": "GIPCL",
    "GSFC.png": "GSFC",
    "HNG.png": "HNG Float Glass",
    "Indian Railways.jpg": "Indian Railways",
    "INEOS.png": "INEOS Styrolution",
    "JSW.png": "JSW Steel",
    "Kaizen.png": "Kaizen",
    "KP Group.png": "KP Group",
    "KPGU.png": "KPGU Vadodara",
    "L&T.png": "Larsen & Toubro (L&T)",
    "Meghmani.png": "Meghmani Group",
    "MSU.png": "MS University Baroda",
    "National food.png": "National Foods",
    "NJ India.png": "NJ India Invest",
    "OPAL.png": "OPAL (ONGC Petro additions)",
    "Pakona.png": "Pakona Engineers",
    "PGP Glass.png": "PGP Glass",
    "Plasser India.png": "Plasser India",
    "Polycab.png": "Polycab India",
    "Reliance.png": "Reliance Industries",
    "Saint Gobain.png": "Saint-Gobain",
    "SEW Eurodrive.png": "SEW-Eurodrive",
    "Shiva Pharmachem.png": "Shiva Pharmachem",
    "Signify.png": "Signify (Philips Lighting)",
    "Sintex.png": "Sintex Industries",
    "Sisecam.png": "Sisecam Flat Glass",
    "Statue of Unity.png": "Statue of Unity",
    "Sumandeep.png": "Sumandeep Vidyapeeth",
    "Sun Pharma.png": "Sun Pharma",
    "Tarasuns.png": "Tara Suns",
    "Torrent Power.png": "Torrent Power",
    "TTK Prestige.png": "TTK Prestige",
    "UPL.png": "UPL Limited",
    "Vadtal Mandir.png": "Vadtal Mandir",
    "Vardhman Group.png": "Vardhman Group",
    "VCCI.png": "VCCI",
    "Welcare Hospital.png": "Welcare Hospital",
    "Welspun.png": "Welspun World",
    "Zydus.png": "Zydus Cadila"
}

def clean_and_trim(img):
    if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
        rgba = img.convert('RGBA')
        alpha = rgba.split()[-1]
        bbox = alpha.getbbox()
        if bbox:
            rgba = rgba.crop(bbox)
        bg = Image.new("RGB", rgba.size, (255, 255, 255))
        bg.paste(rgba, mask=rgba.split()[-1])
        rgb_img = bg
    else:
        rgb_img = img.convert('RGB')

    # Fast grayscale threshold bounding box
    gray = rgb_img.convert('L')
    mask = gray.point(lambda p: 255 if p < 248 else 0)
    bbox = mask.getbbox()
    if bbox:
        w, h = rgb_img.size
        x0 = max(0, bbox[0] - 4)
        y0 = max(0, bbox[1] - 4)
        x1 = min(w, bbox[2] + 4)
        y1 = min(h, bbox[3] + 4)
        return rgb_img.crop((x0, y0, x1, y1))
    return rgb_img

def process_all():
    files = [f for f in os.listdir(MAIN_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    print(f"[*] Found {len(files)} client logo files in {MAIN_DIR}")

    items = []
    for fn in files:
        brand_name = NAME_MAP.get(fn, os.path.splitext(fn)[0].replace('-', ' ').replace('_', ' '))
        items.append({
            'source_fn': fn,
            'name': brand_name
        })

    # Sort A to Z
    items.sort(key=lambda x: x['name'].lower())

    manifest = []
    for i, item in enumerate(items):
        src_path = os.path.join(MAIN_DIR, item['source_fn'])
        raw_img = Image.open(src_path)
        trimmed = clean_and_trim(raw_img)

        # Standard clean canvas: 220 x 140
        canvas = Image.new('RGB', (220, 140), (255, 255, 255))
        max_w, max_h = 184, 110
        lw, lh = trimmed.size
        scale = min(max_w / lw, max_h / lh, 1.25)
        new_w = max(1, int(round(lw * scale)))
        new_h = max(1, int(round(lh * scale)))

        scaled = trimmed.resize((new_w, new_h), Image.Resampling.LANCZOS)
        ox = (220 - new_w) // 2
        oy = (140 - new_h) // 2
        canvas.paste(scaled, (ox, oy))

        filename = f"logo_{i+1:02d}.png"
        out_filepath = os.path.join(OUT_DIR, filename)
        canvas.save(out_filepath, quality=98)

        manifest.append({
            'order': i + 1,
            'filename': filename,
            'path': f'assets/client_logos/{filename}',
            'name': item['name'],
            'orig_source': item['source_fn']
        })

    # Remove any extra old logo files (e.g. logo_74.png .. logo_99.png if only 73 exist)
    for old_i in range(len(items) + 1, 120):
        old_fn = f"logo_{old_i:02d}.png"
        old_path = os.path.join(OUT_DIR, old_fn)
        if os.path.exists(old_path):
            try:
                os.remove(old_path)
            except Exception:
                pass

    manifest_path = os.path.join(DATA_DIR, "logo_manifest.json")
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"[+] Successfully exported {len(manifest)} client logos to {OUT_DIR}")
    print(f"[+] Saved manifest to {manifest_path}")

if __name__ == '__main__':
    process_all()
