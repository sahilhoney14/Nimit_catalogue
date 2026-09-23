import os
from PIL import Image, ImageDraw

os.makedirs('c:/nimit/scratch/robust_crops', exist_ok=True)

im1 = Image.open('c:/nimit/assets/clients_prestigious_part1.png').convert('RGB')
im2 = Image.open('c:/nimit/assets/clients_prestigious_part2.png').convert('RGB')

# Clean bottom-left arrow on im1
draw1 = ImageDraw.Draw(im1)
draw1.rectangle([0, 740, 75, im1.height], fill=(255, 255, 255))

p1_rows = [0, 164, 264, 408, 579, 708, 842]
p1_cols = [
    [32, 190, 416, 557, 755, 955, 1101, 1324, 1485, 1685],
    [32, 198, 418, 563, 787, 933, 1136, 1324, 1498, 1699],
    [36, 232, 418, 563, 745, 965, 1145, 1325, 1514, 1697],
    [32, 237, 370, 603, 782, 984, 1116, 1285, 1514, 1684],
    [36, 232, 369, 565, 779, 926, 1151, 1300, 1521, 1696],
    [0, 164, 377, 599, 748, 922, 1137, 1333, 1482, 1696]
]

p2_rows = [0, 162, 311, 446, 590, 743]
p2_cols = [
    [37, 227, 414, 564, 781, 969, 1130, 1333, 1526, 1713],
    [22, 234, 390, 600, 754, 964, 1181, 1359, 1557, 1713],
    [30, 252, 374, 576, 774, 969, 1142, 1309, 1516, 1713],
    [22, 219, 411, 599, 744, 960, 1152, 1359, 1532, 1715],
    [22, 191, 376, 599, 749, 962, 1130, 1317, 1528, 1712]
]

robust_cards = []

for r in range(6):
    y0 = p1_rows[r]
    y1 = p1_rows[r+1]
    for c in range(9):
        x0 = p1_cols[r][c]
        x1 = p1_cols[r][c+1]
        crop = im1.crop((x0, y0, x1, y1))
        idx = len(robust_cards)
        robust_cards.append({
            'index': idx,
            'source': f'p1_r{r}_c{c}',
            'crop': crop
        })
        crop.save(f'c:/nimit/scratch/robust_crops/robust_{idx:02d}_p1_r{r}_c{c}.png')

for r in range(5):
    y0 = p2_rows[r]
    y1 = p2_rows[r+1]
    for c in range(9):
        x0 = p2_cols[r][c]
        x1 = p2_cols[r][c+1]
        crop = im2.crop((x0, y0, x1, y1))
        idx = len(robust_cards)
        robust_cards.append({
            'index': idx,
            'source': f'p2_r{r}_c{c}',
            'crop': crop
        })
        crop.save(f'c:/nimit/scratch/robust_crops/robust_{idx:02d}_p2_r{r}_c{c}.png')

print(f"Saved {len(robust_cards)} robust crops.")
