from PIL import Image

im = Image.open('c:/nimit/assets/process_analytics_visual.jpg').convert('RGB')

# Let's inspect the bounding box of the camera body
# The camera body is roughly x in [100..380], y in [130..360]
# Inside this area, the surface is metallic gray/blue with RGB values around (120..180, 140..190, 160..210)
# The text is dark pixels (RGB < 70 or much darker than surrounding metal)

text_pixels = []
for y in range(120, 380):
    for x in range(90, 380):
        r, g, b = im.getpixel((x, y))
        # Detect dark text pixels against the bright metallic casing
        # Metallic casing has r > 110, g > 120, b > 140
        # Text has r < 80, g < 80, b < 90
        if r < 85 and g < 90 and b < 100:
            text_pixels.append((x, y))

print(f"Found {len(text_pixels)} candidate text pixels.")
if text_pixels:
    min_x = min(p[0] for p in text_pixels)
    max_x = max(p[0] for p in text_pixels)
    min_y = min(p[1] for p in text_pixels)
    max_y = max(p[1] for p in text_pixels)
    print(f"Text bounding box: x=[{min_x}..{max_x}], y=[{min_y}..{max_y}]")
