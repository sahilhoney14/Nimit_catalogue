import os
from PIL import Image, ImageDraw

os.makedirs('c:/nimit/scratch/precise_crops', exist_ok=True)

im1 = Image.open('c:/nimit/assets/clients_prestigious_part1.png').convert('RGB')
im2 = Image.open('c:/nimit/assets/clients_prestigious_part2.png').convert('RGB')

# Clean bottom-left arrow on im1
draw1 = ImageDraw.Draw(im1)
draw1.rectangle([0, 740, 75, im1.height], fill=(255, 255, 255))

# Part 1 exact row and col dividers
p1_rows = [0, 139, 265, 408, 573, 708, 842]
p1_cols = [
    [0, 190, 400, 563, 762, 955, 1182, 1341, 1562, 1710],
    [0, 198, 381, 564, 787, 967, 1146, 1341, 1545, 1710],
    [0, 209, 377, 563, 788, 965, 1149, 1341, 1564, 1710],
    [0, 194, 370, 603, 782, 984, 1150, 1367, 1536, 1710],
    [0, 209, 368, 565, 779, 981, 1151, 1342, 1535, 1710],
    [0, 174, 377, 599, 779, 984, 1146, 1341, 1540, 1710]
]

# Part 2 exact row and col dividers
p2_rows = [0, 162, 311, 446, 590, 735]
p2_cols = [
    [24, 203, 377, 564, 781, 969, 1146, 1363, 1543, 1715],
    [24, 189, 390, 600, 759, 964, 1181, 1359, 1557, 1715],
    [24, 203, 374, 576, 774, 969, 1146, 1358, 1535, 1715],
    [24, 190, 370, 599, 795, 960, 1152, 1359, 1535, 1715],
    [24, 191, 376, 599, 769, 962, 1146, 1341, 1572, 1715]
]

precise_cards = []

# Crop P1
for r in range(6):
    y0 = p1_rows[r]
    y1 = p1_rows[r+1]
    for c in range(9):
        x0 = p1_cols[r][c]
        x1 = p1_cols[r][c+1]
        crop = im1.crop((x0, y0, x1, y1))
        idx = len(precise_cards)
        precise_cards.append({
            'index': idx,
            'source': f'p1_r{r}_c{c}',
            'crop': crop
        })
        crop.save(f'c:/nimit/scratch/precise_crops/card_{idx:02d}_p1_r{r}_c{c}.png')

# Crop P2
for r in range(5):
    y0 = p2_rows[r]
    y1 = p2_rows[r+1]
    for c in range(9):
        x0 = p2_cols[r][c]
        x1 = p2_cols[r][c+1]
        crop = im2.crop((x0, y0, x1, y1))
        idx = len(precise_cards)
        precise_cards.append({
            'index': idx,
            'source': f'p2_r{r}_c{c}',
            'crop': crop
        })
        crop.save(f'c:/nimit/scratch/precise_crops/card_{idx:02d}_p2_r{r}_c{c}.png')

print(f"Saved {len(precise_cards)} precisely cropped cards.")
