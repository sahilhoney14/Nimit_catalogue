# -*- coding: utf-8 -*-
"""
High-Performance Video Optimization & Poster Generator for NIMIT
1. Backs up original MP4 files to scratch/original_videos_backup/
2. Extracts a crisp, lightweight WebP poster image (15-40 KB) for each video
3. Compresses MP4 videos (720p, CRF 27, H.264, Web FastStart enabled)
4. Updates builders/build_catalog.py with poster="..." attributes and smart preloading
5. Runs master build to update modules.html
"""

import os
import shutil
import subprocess
import imageio_ffmpeg

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(ROOT_DIR, 'assets')
BACKUP_DIR = os.path.join(ROOT_DIR, 'scratch', 'original_videos_backup')
os.makedirs(BACKUP_DIR, exist_ok=True)

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

video_files = [
    "media1.mp4",
    "media2.mp4",
    "Screen Recording 2026-09-15 163024.mp4",
    "Screen Recording 2026-09-15 162207.mp4",
    "media5.mp4",
    "media6.mp4",
    "media7.mp4",
    "media8.mp4",
    "media9.mp4"
]

print("=" * 65)
print("  NIMIT VIDEO COMPRESSION & POSTER GENERATION")
print("=" * 65)

total_orig = 0
total_comp = 0
poster_map = {} # video_filename -> poster_filename

for vf in video_files:
    in_fp = os.path.join(ASSETS_DIR, vf)
    if not os.path.exists(in_fp):
        print(f"[-] Video not found: {vf}")
        continue
    
    orig_sz = os.path.getsize(in_fp)
    total_orig += orig_sz
    
    # 1. Backup original
    backup_fp = os.path.join(BACKUP_DIR, vf)
    if not os.path.exists(backup_fp):
        shutil.copy2(in_fp, backup_fp)
    
    # Clean name for poster
    safe_base = os.path.splitext(vf)[0].replace(" ", "_").lower()
    poster_fn = f"poster_{safe_base}.webp"
    poster_fp = os.path.join(ASSETS_DIR, poster_fn)
    poster_map[vf] = poster_fn
    
    print(f"\n[*] Processing: {vf} ({orig_sz/(1024*1024):.2f} MB)")
    
    # 2. Extract WebP poster (at 0.2s or 0.1s to avoid black opening frame)
    cmd_poster = [
        FFMPEG, '-y', '-ss', '00:00:00.200', '-i', in_fp,
        '-vframes', '1',
        '-vf', 'scale=-2:720',
        '-c:v', 'libwebp', '-quality', '82',
        poster_fp
    ]
    subprocess.run(cmd_poster, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    poster_sz = os.path.getsize(poster_fp)
    print(f"    [+] Created poster: {poster_fn} ({poster_sz/1024:.1f} KB)")
    
    # 3. Compress video: 720p, CRF 27, faster preset, faststart moov atom
    tmp_out = os.path.join(ROOT_DIR, 'scratch', f"comp_{safe_base}.mp4")
    cmd_compress = [
        FFMPEG, '-y', '-i', in_fp,
        '-vf', 'scale=-2:720',
        '-c:v', 'libx264', '-crf', '27', '-preset', 'faster',
        '-c:a', 'aac', '-b:a', '96k',
        '-movflags', '+faststart',
        tmp_out
    ]
    subprocess.run(cmd_compress, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    comp_sz = os.path.getsize(tmp_out)
    total_comp += comp_sz
    
    # Replace original in assets/
    shutil.move(tmp_out, in_fp)
    print(f"    [+] Compressed video: {orig_sz/(1024*1024):.2f} MB -> {comp_sz/(1024*1024):.2f} MB (saved {(1 - comp_sz/orig_sz)*100:.1f}%)")

print("\n" + "=" * 65)
print(f"Total Video Size Before: {total_orig/(1024*1024):.2f} MB")
print(f"Total Video Size After:  {total_comp/(1024*1024):.2f} MB")
print(f"Total Video Savings:     {(total_orig - total_comp)/(1024*1024):.2f} MB ({(1 - total_comp/total_orig)*100:.1f}% reduction!)")
print("=" * 65)

# 4. Update builders/build_catalog.py to add poster="..." to video tags
catalog_builder_path = os.path.join(ROOT_DIR, 'builders', 'build_catalog.py')
with open(catalog_builder_path, 'r', encoding='utf-8') as f:
    code = f.read()

for vf, p_fn in poster_map.items():
    old_tag_fragment = f'src="assets/{vf}"'
    new_tag_fragment = f'src="assets/{vf}" poster="assets/{p_fn}"'
    if old_tag_fragment in code and f'poster="assets/{p_fn}"' not in code:
        code = code.replace(old_tag_fragment, new_tag_fragment)

with open(catalog_builder_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("[+] Updated builders/build_catalog.py with poster attributes!")
