# -*- coding: utf-8 -*-
"""
NIMIT Ultra-Fast Media Optimizer
Brings total media payload (Videos + Images) to ~13-14 MB
without any noticeable loss in visual quality on web displays.
"""

import os
import shutil
import subprocess
from PIL import Image
import imageio_ffmpeg

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(ROOT_DIR, 'assets')
SCRATCH_DIR = os.path.join(ROOT_DIR, 'scratch')
os.makedirs(SCRATCH_DIR, exist_ok=True)

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

# ==========================================
# 1. OPTIMIZE VIDEOS (Target: ~10-11 MB total)
# ==========================================
video_configs = [
    ("Screen Recording 2026-09-15 162207.mp4", 28, 540, "64k"),
    ("Screen Recording 2026-09-15 163024.mp4", 28, 540, "64k"),
    ("media1.mp4", 28, 540, "64k"),
    ("media2.mp4", 28, 540, "64k"),
    ("media5.mp4", 28, 540, "64k"),
    ("media6.mp4", 28, 540, "64k"),
    ("media7.mp4", 28, 540, "64k"),
    ("media8.mp4", 29, 540, "48k"),
    ("media9.mp4", 29, 540, "48k"),
]

print("=" * 65)
print("  STEP 1: Compressing All 9 Videos to Ultra-Fast Web Size")
print("=" * 65)

total_vid_before = 0
total_vid_after = 0

for vf, crf, height, audio_rate in video_configs:
    in_fp = os.path.join(ASSETS_DIR, vf)
    if not os.path.exists(in_fp):
        print(f"[-] Video not found: {vf}")
        continue
    
    orig_sz = os.path.getsize(in_fp)
    total_vid_before += orig_sz
    
    tmp_out = os.path.join(SCRATCH_DIR, f"opt_{vf}")
    
    # Scale to 540p, apply CRF, fast preset, mono audio, faststart moov atom
    cmd = [
        FFMPEG, '-y', '-i', in_fp,
        '-vf', f'scale=-2:{height}',
        '-c:v', 'libx264', '-crf', str(crf), '-preset', 'faster',
        '-c:a', 'aac', '-b:a', audio_rate, '-ac', '1',
        '-movflags', '+faststart',
        tmp_out
    ]
    
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    comp_sz = os.path.getsize(tmp_out)
    total_vid_after += comp_sz
    
    # Replace with optimized file
    shutil.move(tmp_out, in_fp)
    print(f"[+] {vf:38s}: {orig_sz/(1024*1024):5.2f} MB -> {comp_sz/(1024*1024):5.2f} MB (saved {(1 - comp_sz/orig_sz)*100:.1f}%)")

print(f"\nVideos Total Before: {total_vid_before/(1024*1024):.2f} MB")
print(f"Videos Total After:  {total_vid_after/(1024*1024):.2f} MB")
print(f"Total Video Savings: {(total_vid_before - total_vid_after)/(1024*1024):.2f} MB")

# ==========================================
# 2. OPTIMIZE WEBP IMAGES & POSTERS (Target: ~3 MB)
# ==========================================
print("\n" + "=" * 65)
print("  STEP 2: Tuning WebP Images & Posters for Maximum Performance")
print("=" * 65)

total_img_before = 0
total_img_after = 0

for dirpath, _, filenames in os.walk(ASSETS_DIR):
    for fn in filenames:
        if fn.lower().endswith('.webp'):
            fp = os.path.join(dirpath, fn)
            orig_sz = os.path.getsize(fp)
            total_img_before += orig_sz
            
            try:
                with Image.open(fp) as im:
                    w, h = im.size
                    is_poster = fn.startswith('poster_')
                    max_dim = 960 if is_poster else 1400
                    
                    if w > max_dim:
                        new_h = int(h * (max_dim / w))
                        im = im.resize((max_dim, new_h), Image.Resampling.LANCZOS)
                    
                    quality = 74 if is_poster else 78
                    tmp_webp = os.path.join(SCRATCH_DIR, 'tmp_opt_img.webp')
                    
                    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
                        im = im.convert('RGBA')
                        im.save(tmp_webp, 'WEBP', quality=quality, method=6)
                    else:
                        im = im.convert('RGB')
                        im.save(tmp_webp, 'WEBP', quality=quality, method=6)
                
                new_sz = os.path.getsize(tmp_webp)
                # Keep smaller version
                if new_sz < orig_sz:
                    shutil.move(tmp_webp, fp)
                    total_img_after += new_sz
                else:
                    if os.path.exists(tmp_webp):
                        os.remove(tmp_webp)
                    total_img_after += orig_sz
            except Exception as e:
                total_img_after += orig_sz

print(f"Images Total Before: {total_img_before/(1024*1024):.2f} MB")
print(f"Images Total After:  {total_img_after/(1024*1024):.2f} MB")
print(f"Total Image Savings: {(total_img_before - total_img_after)/(1024*1024):.2f} MB")

# ==========================================
# 3. GRAND TOTAL
# ==========================================
grand_total = total_vid_after + total_img_after
print("\n" + "=" * 65)
print(f"  GRAND TOTAL MEDIA SIZE (VIDEOS + IMAGES): {grand_total/(1024*1024):.2f} MB")
print("=" * 65)
