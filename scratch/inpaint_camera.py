import os
import math
import random
from PIL import Image, ImageFilter

im = Image.open('c:/nimit/assets/process_analytics_visual.jpg').convert('RGB')
w, h = im.size

# Load dilated mask
mask = Image.new('L', (w, h), 0)

# Region 1: "PTZ-EXP-01"
for y in range(130, 240):
    for x in range(100, 255):
        if y > 182 and x < 160: # avoid cable socket
            continue
        r, g, b = im.getpixel((x, y))
        if r < 82 and g < 88 and b < 102:
            mask.putpixel((x, y), 255)

# Region 2: "HAZ-LOC RATED" and "SWIR/EO"
for y in range(180, 275):
    for x in range(235, 375):
        r, g, b = im.getpixel((x, y))
        if r < 98 and g < 104 and b < 118:
            mask.putpixel((x, y), 255)

# Region 3: mount text
for y in range(345, 380):
    for x in range(155, 220):
        r, g, b = im.getpixel((x, y))
        if r < 100 and g < 105 and b < 118:
            mask.putpixel((x, y), 255)

# Dilate mask by 5px (radius 2)
dilated = mask.filter(ImageFilter.MaxFilter(5))

# Convert image and mask to list of pixels for fast multi-pass Laplace inpainting
# We only need to process the bounding box around the camera: x in [80..400], y in [120..390]
bx0, by0, bx1, by1 = 80, 120, 400, 390
bw = bx1 - bx0
bh = by1 - by0

# Extract RGB arrays
r_arr = [[im.getpixel((bx0 + x, by0 + y))[0] for x in range(bw)] for y in range(bh)]
g_arr = [[im.getpixel((bx0 + x, by0 + y))[1] for x in range(bw)] for y in range(bh)]
b_arr = [[im.getpixel((bx0 + x, by0 + y))[2] for x in range(bw)] for y in range(bh)]
m_arr = [[(1 if dilated.getpixel((bx0 + x, by0 + y)) > 128 else 0) for x in range(bw)] for y in range(bh)]

# 1. Initial fill along cylindrical axis (angle approx -20 degrees: dy/dx ≈ -0.36)
# For each masked pixel, sample from left-bottom and right-top outside mask
for y in range(bh):
    for x in range(bw):
        if m_arr[y][x]:
            # Find closest unmasked pixel in 4 directions
            samples_r, samples_g, samples_b = [], [], []
            for radius in range(1, 25):
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (2, -1), (-2, 1), (1, 1), (-1, -1)]:
                    nx, ny = x + dx * radius, y + dy * radius
                    if 0 <= nx < bw and 0 <= ny < bh:
                        if not m_arr[ny][nx]:
                            samples_r.append(r_arr[ny][nx])
                            samples_g.append(g_arr[ny][nx])
                            samples_b.append(b_arr[ny][nx])
                if len(samples_r) >= 4:
                    break
            if samples_r:
                r_arr[y][x] = sum(samples_r) / len(samples_r)
                g_arr[y][x] = sum(samples_g) / len(samples_g)
                b_arr[y][x] = sum(samples_b) / len(samples_b)

# 2. Multi-pass Laplace diffusion iterations for smooth harmonic gradient
for iteration in range(60):
    new_r = [row[:] for row in r_arr]
    new_g = [row[:] for row in g_arr]
    new_b = [row[:] for row in b_arr]
    
    for y in range(1, bh - 1):
        for x in range(1, bw - 1):
            if m_arr[y][x]:
                # 8-neighbor weighted Laplace with cylindrical bias (horizontal/diagonal)
                # Weights: top-right and bottom-left get slightly higher weight along cylinder axis
                w_diag = 0.8
                avg_r = (r_arr[y-1][x] + r_arr[y+1][x] + r_arr[y][x-1] + r_arr[y][x+1] +
                         (r_arr[y-1][x+1] + r_arr[y+1][x-1]) * w_diag +
                         (r_arr[y-1][x-1] + r_arr[y+1][x+1]) * 0.5) / (4.0 + 2 * w_diag + 1.0)
                         
                avg_g = (g_arr[y-1][x] + g_arr[y+1][x] + g_arr[y][x-1] + g_arr[y][x+1] +
                         (g_arr[y-1][x+1] + g_arr[y+1][x-1]) * w_diag +
                         (g_arr[y-1][x-1] + g_arr[y+1][x+1]) * 0.5) / (4.0 + 2 * w_diag + 1.0)
                         
                avg_b = (b_arr[y-1][x] + b_arr[y+1][x] + b_arr[y][x-1] + b_arr[y][x+1] +
                         (b_arr[y-1][x+1] + b_arr[y+1][x-1]) * w_diag +
                         (b_arr[y-1][x-1] + b_arr[y+1][x+1]) * 0.5) / (4.0 + 2 * w_diag + 1.0)
                         
                new_r[y][x] = avg_r
                new_g[y][x] = avg_g
                new_b[y][x] = avg_b
                
    r_arr, g_arr, b_arr = new_r, new_g, new_b

# 3. Add subtle realistic brushed metal micro-texture (noise +-1.5)
random.seed(42)
result_im = im.copy()
for y in range(bh):
    for x in range(bw):
        if m_arr[y][x]:
            noise = (random.random() - 0.5) * 2.5
            r_val = max(0, min(255, int(round(r_arr[y][x] + noise))))
            g_val = max(0, min(255, int(round(g_arr[y][x] + noise))))
            b_val = max(0, min(255, int(round(b_arr[y][x] + noise))))
            result_im.putpixel((bx0 + x, by0 + y), (r_val, g_val, b_val))

# Save output comparison
crop_before = im.crop((80, 120, 420, 390))
crop_after = result_im.crop((80, 120, 420, 390))

crop_before.save('c:/nimit/scratch/camera_before.png')
crop_after.save('c:/nimit/scratch/camera_after.png')

# Save final inpainted image to assets
clean_out_path = 'c:/nimit/assets/process_analytics_visual_clean.jpg'
result_im.save(clean_out_path, quality=98)
result_im.save('c:/nimit/assets/process_analytics_visual.jpg', quality=98)
print("Inpainted camera successfully and saved to assets/process_analytics_visual.jpg!")
