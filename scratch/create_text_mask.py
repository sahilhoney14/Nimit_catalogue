import os
import math
import random
from PIL import Image, ImageFilter

im = Image.open('c:/nimit/assets/process_analytics_visual.jpg').convert('RGB')
w, h = im.size

# Let's create an inpainting function for metallic surfaces
# 1. We identify the text mask in the camera casing:
# The camera body surface is angled at roughly -22 degrees (along the cylinder axis)
# For each pixel that is text, we interpolate from surrounding non-mask pixels along the cylinder gradient direction.

mask = Image.new('L', (w, h), 0)

# Identify text pixels in Region 1: "PTZ-EXP-01"
# PTZ-EXP-01 is located at x ≈ [102..250], y ≈ [135..225]
# Note: The cable socket is around x=[100..165], y=[185..260] (we only want text above it)
for y in range(130, 240):
    for x in range(100, 255):
        # avoid cable socket (cable is dark black/gray below y=185 when x < 155)
        if y > 182 and x < 160:
            continue
        r, g, b = im.getpixel((x, y))
        # Text is dark letters (r < 75, g < 80, b < 95) on bright metal (r > 130, g > 150, b > 170)
        if r < 80 and g < 85 and b < 100:
            mask.putpixel((x, y), 255)

# Identify text pixels in Region 2: "HAZ-LOC RATED" and "SWIR/EO"
for y in range(180, 275):
    for x in range(235, 375):
        r, g, b = im.getpixel((x, y))
        if r < 95 and g < 100 and b < 115:
            mask.putpixel((x, y), 255)

# Identify text pixels in Region 3: mount text
for y in range(345, 380):
    for x in range(155, 220):
        r, g, b = im.getpixel((x, y))
        if r < 100 and g < 105 and b < 115:
            mask.putpixel((x, y), 255)

# Dilate mask by 2px to include anti-aliasing edges
dilated_mask = mask.filter(ImageFilter.MaxFilter(5))

# Save mask for inspection
dilated_mask.crop((80, 120, 420, 390)).save('c:/nimit/scratch/camera_text_mask.png')
print("Generated and saved text mask.")
