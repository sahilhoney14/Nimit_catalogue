import os
from PIL import Image

im1 = Image.open('c:/nimit/assets/clients_prestigious_part1.png').convert('RGB')
im2 = Image.open('c:/nimit/assets/clients_prestigious_part2.png').convert('RGB')

# Let's inspect the exact layout of Row 1 in Part 1 (where Borosil is at column 8)
# Let's print out what is at x = 1450 to 1750 in Row 1 (y = 140 to 265)
# In Row 1: Col 7 is Atul, Col 8 is Borosil
# Let's find the boundary between Atul and Borosil:
for x in range(1450, 1560):
    white_in_col = sum(1 for y in range(145, 260) if im1.getpixel((x, y)) == (255, 255, 255))
    if white_in_col > 90: # mostly white column
        print(f"Row 1 (Atul / Borosil boundary) x={x}: white={white_in_col}/115")

# Let's check Part 2 Row 0 Col 8 (MGVCL) (y = 0 to 160, x = 1450 to 1560):
for x in range(1450, 1560):
    white_in_col = sum(1 for y in range(10, 155) if im2.getpixel((x, y)) == (255, 255, 255))
    if white_in_col > 120:
        print(f"P2 Row 0 (GSP / MGVCL boundary) x={x}: white={white_in_col}/145")
