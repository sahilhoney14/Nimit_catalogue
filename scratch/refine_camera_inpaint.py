import os
import math
import random
from PIL import Image, ImageFilter

# Load original high-res image
orig = Image.open('c:/nimit/assets/process_analytics_visual.jpg').convert('RGB')
w, h = orig.size

# We want to inpaint the camera body text:
# 1. Main PTZ-EXP-01 text on top of camera casing
# 2. HAZ-LOC RATED and SWIR/EO on the side
# 3. Small text on the bottom bracket mount

# Let's create an accurate mask for each text area:
mask = Image.new('L', (w, h), 0)

# Region A: "PTZ-EXP-01"
# The letters are dark (RGB sum < 300) in the region x=[118..285], y=[138..230]
# But the casing background is bright metal (RGB sum > 450)
for y in range(135, 235):
    for x in range(118, 285):
        r, g, b = orig.getpixel((x, y))
        # Text detection: darker than surrounding metal
        # The metal in this area is around (160..210, 180..225, 195..240)
        # Text is (30..80, 40..90, 50..105)
        if (r + g + b) < 320 and r < 110 and g < 115 and b < 130:
            mask.putpixel((x, y), 255)

# Region B: "HAZ-LOC RATED" & "SWIR/EO"
for y in range(185, 275):
    for x in range(235, 375):
        r, g, b = orig.getpixel((x, y))
        if (r + g + b) < 360 and r < 125 and g < 130 and b < 145:
            mask.putpixel((x, y), 255)

# Region C: Mount bracket text
for y in range(345, 380):
    for x in range(155, 225):
        r, g, b = orig.getpixel((x, y))
        if (r + g + b) < 350 and r < 120 and g < 125 and b < 135:
            mask.putpixel((x, y), 255)

# Dilate mask by 5px to cover letter antialiasing
dilated_mask = mask.filter(ImageFilter.MaxFilter(5))

# Process bounding box x in [100..390], y in [125..390]
bx0, by0, bx1, by1 = 100, 125, 390, 390
bw = bx1 - bx0
bh = by1 - by0

r_grid = [[orig.getpixel((bx0 + x, by0 + y))[0] for x in range(bw)] for y in range(bh)]
g_grid = [[orig.getpixel((bx0 + x, by0 + y))[1] for x in range(bw)] for y in range(bh)]
b_grid = [[orig.getpixel((bx0 + x, by0 + y))[2] for x in range(bw)] for y in range(bh)]
m_grid = [[(1 if dilated_mask.getpixel((bx0 + x, by0 + y)) > 128 else 0) for x in range(bw)] for y in range(bh)]

# 1. Initial directional interpolation along cylindrical gradient
for y in range(bh):
    for x in range(bw):
        if m_grid[y][x]:
            samples_r, samples_g, samples_b = [], [], []
            for radius in range(1, 30):
                # Sample along cylinder axis (dx=2, dy=-1) and perpendicular (dx=1, dy=2)
                for dx, dy in [(2, -1), (-2, 1), (1, 2), (-1, -2), (1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx * radius, y + dy * radius
                    if 0 <= nx < bw and 0 <= ny < bh:
                        if not m_grid[ny][nx]:
                            samples_r.append(r_grid[ny][nx])
                            samples_g.append(g_grid[ny][nx])
                            samples_b.append(b_grid[ny][nx])
                if len(samples_r) >= 6:
                    break
            if samples_r:
                r_grid[y][x] = sum(samples_r) / len(samples_r)
                g_grid[y][x] = sum(samples_g) / len(samples_g)
                b_grid[y][x] = sum(samples_b) / len(samples_b)

# 2. 80 iterations of anisotropic Laplace smoothing
for iteration in range(80):
    next_r = [row[:] for row in r_grid]
    next_g = [row[:] for row in g_grid]
    next_b = [row[:] for row in b_grid]
    
    for y in range(1, bh - 1):
        for x in range(1, bw - 1):
            if m_grid[y][x]:
                # Weights: cylinder longitudinal direction gets higher weight
                avg_r = (r_grid[y][x-1] * 1.2 + r_grid[y][x+1] * 1.2 +
                         r_grid[y-1][x] * 1.0 + r_grid[y+1][x] * 1.0 +
                         r_grid[y-1][x+1] * 1.4 + r_grid[y+1][x-1] * 1.4 +
                         r_grid[y-1][x-1] * 0.6 + r_grid[y+1][x+1] * 0.6) / (2.4 + 2.0 + 2.8 + 1.2)
                         
                avg_g = (g_grid[y][x-1] * 1.2 + g_grid[y][x+1] * 1.2 +
                         g_grid[y-1][x] * 1.0 + g_grid[y+1][x] * 1.0 +
                         g_grid[y-1][x+1] * 1.4 + g_grid[y+1][x-1] * 1.4 +
                         g_grid[y-1][x-1] * 0.6 + g_grid[y+1][x+1] * 0.6) / (2.4 + 2.0 + 2.8 + 1.2)
                         
                avg_b = (b_grid[y][x-1] * 1.2 + b_grid[y][x+1] * 1.2 +
                         b_grid[y-1][x] * 1.0 + b_grid[y+1][x] * 1.0 +
                         b_grid[y-1][x+1] * 1.4 + b_grid[y+1][x-1] * 1.4 +
                         b_grid[y-1][x-1] * 0.6 + b_grid[y+1][x+1] * 0.6) / (2.4 + 2.0 + 2.8 + 1.2)
                         
                next_r[y][x] = avg_r
                next_g[y][x] = avg_g
                next_b[y][x] = avg_b
                
    r_grid, g_grid, b_grid = next_r, next_g, next_b

# 3. Add subtle natural metallic grain
random.seed(101)
final_im = orig.copy()
for y in range(bh):
    for x in range(bw):
        if m_grid[y][x]:
            grain = (random.random() - 0.5) * 2.0
            rv = max(0, min(255, int(round(r_grid[y][x] + grain))))
            gv = max(0, min(255, int(round(g_grid[y][x] + grain))))
            bv = max(0, min(255, int(round(b_grid[y][x] + grain))))
            final_im.putpixel((bx0 + x, by0 + y), (rv, gv, bv))

# Save comparison crop and updated assets
final_crop = final_im.crop((80, 120, 420, 390))
final_crop.save('c:/nimit/scratch/camera_clean_final.png')

final_im.save('c:/nimit/assets/process_analytics_visual.jpg', quality=98)
final_im.save('c:/nimit/assets/process_analytics_visual_clean.jpg', quality=98)
print("Saved clean camera graphic to assets/process_analytics_visual.jpg!")
