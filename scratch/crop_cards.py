import os
from PIL import Image

im1 = Image.open('c:/nimit/scratch/p1_cleaned.png')
im2 = Image.open('c:/nimit/assets/clients_prestigious_part2.png')

col_w1 = 1690.0 / 9.0
row_h1 = 842.0 / 6.0

col_w2 = (1702.0 - 32.0) / 9.0
row_h2 = 725.0 / 5.0

os.makedirs('c:/nimit/scratch/clean_cards', exist_ok=True)

# Standard target card size: 240 x 180 (4:3 aspect ratio)
TARGET_W = 240
TARGET_H = 180

cards = []

# Part 1: 54 cards (0 to 53)
for r in range(6):
    for c in range(9):
        x0 = int(round(c * col_w1))
        x1 = int(round((c + 1) * col_w1))
        y0 = int(round(r * row_h1))
        y1 = int(round((r + 1) * row_h1))
        
        crop = im1.crop((x0, y0, x1, y1))
        idx = len(cards)
        cards.append({
            'index': idx,
            'source': f'p1_r{r}_c{c}',
            'image': crop
        })

# Part 2: 45 cards (54 to 98)
for r in range(5):
    for c in range(9):
        x0 = int(round(32 + c * col_w2))
        x1 = int(round(32 + (c + 1) * col_w2))
        y0 = int(round(r * row_h2))
        y1 = int(round((r + 1) * row_h2))
        
        crop = im2.crop((x0, y0, x1, y1))
        idx = len(cards)
        cards.append({
            'index': idx,
            'source': f'p2_r{r}_c{c}',
            'image': crop
        })

print(f'Cropped {len(cards)} cards successfully.')
