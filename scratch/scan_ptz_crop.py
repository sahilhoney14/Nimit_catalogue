from PIL import Image

im = Image.open('c:/nimit/assets/process_analytics_visual.jpg').convert('RGB')
crop_ptz = im.crop((95, 130, 260, 255))

# Let's find the exact letters in crop_ptz:
w, h = crop_ptz.size
print("PTZ crop size:", w, h)
for y in range(0, h, 8):
    dark_in_row = [x for x in range(w) if crop_ptz.getpixel((x, y))[0] < 80 and crop_ptz.getpixel((x, y))[1] < 85]
    if dark_in_row:
        print(f"crop_y={y:2d} (img_y={y+130:3d}): dark x spans [{min(dark_in_row)}..{max(dark_in_row)}] (count={len(dark_in_row)})")
