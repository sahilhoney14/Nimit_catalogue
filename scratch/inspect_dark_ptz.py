from PIL import Image

im_before = Image.open('c:/nimit/scratch/camera_before.png')
im_after = Image.open('c:/nimit/scratch/camera_after.png')
w, h = im_before.size

# Let's check where the dark pixels in PTZ area are:
# The crop is from (80, 120, 420, 390)
# So image coord x = crop_x + 80, y = crop_y + 120
dark_pts = []
for y in range(15, 100):
    for x in range(20, 170):
        r, g, b = im_after.getpixel((x, y))
        if r < 85 and g < 90:
            dark_pts.append((x, y, r, g, b))

print("Sample dark points in PTZ area after inpainting:")
for p in dark_pts[:15]:
    print(f"crop_x={p[0]} (img_x={p[0]+80}), crop_y={p[1]} (img_y={p[1]+120}): RGB=({p[2]},{p[3]},{p[4]})")
