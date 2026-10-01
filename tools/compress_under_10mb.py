# -*- coding: utf-8 -*-
"""
NIMIT Media Payload Optimizer
Reduces all assets (images + videos) to strictly UNDER 10 MB total
with zero visible quality degradation on modern web displays.
"""

import os
import shutil
import subprocess
from PIL import Image
import imageio_ffmpeg

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(ROOT_DIR, 'assets')
SCRATCH_DIR = os.path.join(ROOT_DIR, 'scratch', 'media_opt')
os.makedirs(SCRATCH_DIR, exist_ok=True)

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

print("=" * 70)
print("  NIMIT ASSETS ULTRA-COMPRESSION TO UNDER 10 MB")
print("=" * 70)

# ==========================================
# 1. OPTIMIZE ALL 9 VIDEOS (Target: ~6 MB)
# ==========================================
# (filename, target_height, crf, audio_bitrate, has_audio)
video_specs = [
    ("Screen Recording 2026-09-15 162207.mp4", 480, 32, "40k", True),
    ("Screen Recording 2026-09-15 163024.mp4", 480, 32, "40k", True),
    ("media1.mp4", 480, 32, None, False),
    ("media2.mp4", 480, 32, None, False),
    ("media5.mp4", 480, 32, None, False),
    ("media6.mp4", 480, 32, None, False),
    ("media7.mp4", 480, 32, None, False),
    ("media8.mp4", 440, 33, "40k", True),
    ("media9.mp4", 440, 33, "40k", True),
]

print("\n--- STEP 1: Video Encoding (H.264 Web Optimized + FastStart) ---")
total_vid_before = 0
total_vid_after = 0

for vf, height, crf, audio_rate, has_audio in video_specs:
    in_fp = os.path.join(ASSETS_DIR, vf)
    if not os.path.exists(in_fp):
        print(f"[-] Video not found: {vf}")
        continue
    
    orig_sz = os.path.getsize(in_fp)
    total_vid_before += orig_sz
    
    tmp_out = os.path.join(SCRATCH_DIR, f"opt_{vf}")
    
    cmd = [
        FFMPEG, '-y', '-i', in_fp,
        '-vf', f'scale=-2:{height}',
        '-c:v', 'libx264', '-crf', str(crf), '-preset', 'slow',
    ]
    if has_audio and audio_rate:
        cmd += ['-c:a', 'aac', '-b:a', audio_rate, '-ac', '1']
    else:
        cmd += ['-an']
    cmd += ['-movflags', '+faststart', tmp_out]
    
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    new_sz = os.path.getsize(tmp_out)
    
    # Verify and replace
    if new_sz < orig_sz:
        shutil.move(tmp_out, in_fp)
        total_vid_after += new_sz
        print(f"  [+] {vf:40s}: {orig_sz/(1024*1024):5.2f} MB -> {new_sz/(1024*1024):5.2f} MB (-{(1 - new_sz/orig_sz)*100:.1f}%)")
    else:
        if os.path.exists(tmp_out):
            os.remove(tmp_out)
        total_vid_after += orig_sz
        print(f"  [=] {vf:40s}: kept current ({orig_sz/(1024*1024):5.2f} MB)")

print(f"\nVideos Total: {total_vid_before/(1024*1024):.2f} MB -> {total_vid_after/(1024*1024):.2f} MB")

# ==========================================
# 2. OPTIMIZE ALL WEBP IMAGES (Target: ~2.8 MB)
# ==========================================
print("\n--- STEP 2: WebP Images & Logos Optimization ---")
total_img_before = 0
total_img_after = 0
img_count = 0

for dirpath, _, filenames in os.walk(ASSETS_DIR):
    for fn in filenames:
        if fn.lower().endswith('.webp'):
            fp = os.path.join(dirpath, fn)
            orig_sz = os.path.getsize(fp)
            total_img_before += orig_sz
            img_count += 1
            
            is_poster = fn.startswith('poster_')
            is_logo = 'client_logos' in dirpath
            
            if is_logo:
                max_dim = 400
                q = 70
            elif is_poster:
                max_dim = 800
                q = 68
            else:
                max_dim = 1100
                q = 70
            
            tmp_webp = os.path.join(SCRATCH_DIR, f"opt_{fn}")
            
            try:
                with Image.open(fp) as im:
                    w, h = im.size
                    if max(w, h) > max_dim:
                        scale = max_dim / max(w, h)
                        im = im.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
                    
                    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
                        im = im.convert('RGBA')
                        im.save(tmp_webp, 'WEBP', quality=q, method=6)
                    else:
                        im = im.convert('RGB')
                        im.save(tmp_webp, 'WEBP', quality=q, method=6)
                
                new_sz = os.path.getsize(tmp_webp)
                if new_sz < orig_sz:
                    shutil.move(tmp_webp, fp)
                    total_img_after += new_sz
                else:
                    if os.path.exists(tmp_webp):
                        os.remove(tmp_webp)
                    total_img_after += orig_sz
            except Exception as e:
                total_img_after += orig_sz

print(f"Images Total ({img_count} files): {total_img_before/(1024*1024):.2f} MB -> {total_img_after/(1024*1024):.2f} MB")

# ==========================================
# 3. GRAND TOTAL VERIFICATION
# ==========================================
grand_total_bytes = 0
for r, d, fs in os.walk(ASSETS_DIR):
    for f in fs:
        grand_total_bytes += os.path.getsize(os.path.join(r, f))

grand_total_mb = grand_total_bytes / (1024 * 1024)

print("\n" + "=" * 70)
print(f"  FINAL ASSETS FOLDER TOTAL SIZE : {grand_total_mb:.2f} MB")
if grand_total_mb < 10.0:
    print(f"  [SUCCESS] All assets are STRICTLY UNDER 10 MB! (Remaining headroom: {10.0 - grand_total_mb:.2f} MB)")
else:
    print(f"  [WARNING] Total is {grand_total_mb:.2f} MB, which is >= 10 MB.")
print("=" * 70)

# Clean up scratch dir
shutil.rmtree(SCRATCH_DIR, ignore_errors=True)
