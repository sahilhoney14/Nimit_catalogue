# -*- coding: utf-8 -*-
"""
NIMIT Asset Optimization & Dead Weight Cleaner
1. Backs up original PNG/JPG images into scratch/original_images_backup/
2. Converts all visual images & client logos to high-efficiency WebP format
3. Cleans up uncompressed originals from assets/ to shrink deployment
4. Updates all builder scripts and data manifest
5. Adds preload="metadata" to all video tags in build_catalog.py
"""

import os
import shutil
import json
import re
from PIL import Image

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(ROOT_DIR, 'assets')
SCRATCH_BACKUP = os.path.join(ROOT_DIR, 'scratch', 'original_images_backup')

os.makedirs(SCRATCH_BACKUP, exist_ok=True)

# 1. Collect all images in assets/
conversion_map = {} # old_rel_path -> new_rel_path
total_orig_size = 0
total_new_size = 0

print("=" * 60)
print("  STEP 1: Converting images to WebP...")
print("=" * 60)

for dirpath, _, filenames in os.walk(ASSETS_DIR):
    # Skip any leftover Main_Clients if any
    if 'Main_Clients' in dirpath:
        continue
    for fn in filenames:
        ext = os.path.splitext(fn)[1].lower()
        if ext in ['.png', '.jpg', '.jpeg']:
            fp = os.path.join(dirpath, fn)
            orig_sz = os.path.getsize(fp)
            total_orig_size += orig_sz
            
            # Backup original
            rel_from_assets = os.path.relpath(fp, ASSETS_DIR)
            backup_fp = os.path.join(SCRATCH_BACKUP, rel_from_assets)
            os.makedirs(os.path.dirname(backup_fp), exist_ok=True)
            shutil.copy2(fp, backup_fp)
            
            # Target webp file
            base_name = os.path.splitext(fn)[0]
            webp_fn = base_name + '.webp'
            webp_fp = os.path.join(dirpath, webp_fn)
            
            # Convert
            try:
                with Image.open(fp) as im:
                    # If RGBA, save as RGBA WebP
                    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
                        im = im.convert('RGBA')
                        im.save(webp_fp, 'WEBP', quality=88, method=6)
                    else:
                        im = im.convert('RGB')
                        im.save(webp_fp, 'WEBP', quality=85, method=6)
                
                new_sz = os.path.getsize(webp_fp)
                total_new_size += new_sz
                
                old_rel = os.path.relpath(fp, ROOT_DIR).replace(os.sep, '/')
                new_rel = os.path.relpath(webp_fp, ROOT_DIR).replace(os.sep, '/')
                conversion_map[old_rel] = new_rel
                
                # Also record basename mapping
                conversion_map[fn] = webp_fn
                
                # Delete original from assets (keep nimit_logo.png as a safety fallback)
                if fn != 'nimit_logo.png':
                    os.remove(fp)
            except Exception as e:
                print(f"[-] Error converting {fn}: {e}")

print(f"[+] Total original image size: {total_orig_size / (1024*1024):.2f} MB")
print(f"[+] Total optimized WebP size: {total_new_size / (1024*1024):.2f} MB")
print(f"[+] Space saved on images:     {(total_orig_size - total_new_size) / (1024*1024):.2f} MB ({(1 - total_new_size/total_orig_size)*100:.1f}%)")

# 2. Update data/logo_manifest.json
manifest_path = os.path.join(ROOT_DIR, 'data', 'logo_manifest.json')
if os.path.exists(manifest_path):
    print("\n" + "=" * 60)
    print("  STEP 2: Updating data/logo_manifest.json...")
    print("=" * 60)
    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)
    
    for item in manifest:
        old_fn = item.get('filename', '')
        if old_fn.lower().endswith('.png'):
            base = os.path.splitext(old_fn)[0]
            item['filename'] = base + '.webp'
            item['path'] = f"assets/client_logos/{base}.webp"
            
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)
    print(f"[+] Updated {len(manifest)} logo records to .webp in {manifest_path}")

# 3. Update builders scripts
print("\n" + "=" * 60)
print("  STEP 3: Updating Builder Scripts...")
print("=" * 60)

builder_files = [
    os.path.join(ROOT_DIR, 'builders', 'build_company_hub.py'),
    os.path.join(ROOT_DIR, 'builders', 'build_solutions.py'),
    os.path.join(ROOT_DIR, 'builders', 'build_catalog.py')
]

for bf in builder_files:
    with open(bf, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace image references
    for old_rel, new_rel in conversion_map.items():
        if '/' in old_rel: # full relative path like assets/image18.png
            content = content.replace(old_rel, new_rel)
    
    # For build_catalog.py, also add preload="metadata" to video tags
    if 'build_catalog.py' in bf:
        # replace <video class="brochure-video-player" src="..." ...> with preload="metadata"
        def add_preload(match):
            tag = match.group(0)
            if 'preload=' not in tag:
                # insert preload="metadata" after <video
                tag = tag.replace('<video ', '<video preload="metadata" ')
            return tag
        
        content = re.sub(r'<video[^>]+>', add_preload, content)
        print("[+] Added preload='metadata' to video elements in build_catalog.py")

    with open(bf, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[+] Updated asset references in {os.path.basename(bf)}")

print("\n[SUCCESS] Optimization complete!")
