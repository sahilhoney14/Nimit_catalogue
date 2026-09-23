from PIL import Image

im1 = Image.open('c:/nimit/assets/clients_prestigious_part1.png').convert('RGB')
w, h = im1.size

# Let's inspect horizontal lines between row 0 and row 1
# Row height approx 140
for y in range(130, 150):
    # check how many pixels across x are pure white
    white_count = sum(1 for x in range(w) if im1.getpixel((x, y)) == (255, 255, 255))
    print(f"y={y}: white_count={white_count}/{w} ({white_count/w*100:.1f}%)")
