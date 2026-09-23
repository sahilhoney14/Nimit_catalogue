import os
from PIL import Image

def analyze_image(path):
    img = Image.open(path).convert('RGB')
    w, h = img.size
    print(f"Analyzing {path}: {w}x{h}")
    
    # Check vertical lines (columns) where all pixels are white
    # Or count non-white pixels across each column x
    col_density = [sum(1 for y in range(h) if img.getpixel((x, y)) != (255, 255, 255)) for x in range(w)]
    row_density = [sum(1 for x in range(w) if img.getpixel((x, y)) != (255, 255, 255)) for y in range(h)]
    
    return col_density, row_density

cd1, rd1 = analyze_image('c:/nimit/assets/clients_prestigious_part1.png')
cd2, rd2 = analyze_image('c:/nimit/assets/clients_prestigious_part2.png')

# Print where row density drops to near zero
print("P1 row valleys (near 0):")
for y, d in enumerate(rd1):
    if d < 10:
        print(f"y={y}: density={d}")

print("P2 row valleys (near 0):")
for y, d in enumerate(rd2):
    if d < 10:
        print(f"y={y}: density={d}")
