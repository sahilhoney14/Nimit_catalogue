from PIL import Image

im = Image.open('c:/nimit/scratch/robust_crops/robust_07_p1_r0_c7.png').convert('RGB')
w, h = im.size
print("Apollo crop size:", w, h)

# Let's inspect column averages or non-white pixel counts in Apollo crop
for x in range(0, w, 5):
    non_white = sum(1 for y in range(h) if im.getpixel((x, y)) != (255, 255, 255))
    dark_pixels = sum(1 for y in range(h) if any(c < 200 for c in im.getpixel((x, y))))
    print(f"x={x:3d}: non_white={non_white:3d}/{h}, dark={dark_pixels:3d}/{h}")
