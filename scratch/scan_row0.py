from PIL import Image

im1 = Image.open('c:/nimit/assets/clients_prestigious_part1.png').convert('RGB')
w, h = im1.size

# In Row 0 (y = 20 to 130):
# Let's inspect x = 1150 to 1550:
# Where are the dark pixels of Anoopam Mission vs Apollo vs Apothecon?
for x in range(1150, 1550, 5):
    dark_y = [y for y in range(20, 130) if any(c < 180 for c in im1.getpixel((x, y)))]
    print(f"x={x:4d}: dark_y_count={len(dark_y):2d}")
