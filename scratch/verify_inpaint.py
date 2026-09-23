from PIL import Image

im_after = Image.open('c:/nimit/scratch/camera_after.png')
print("Inpainted crop size:", im_after.size)

# Check if any dark text remnants remain in the PTZ area (x=100..250 in im, which is 20..170 in crop)
# Let's count dark pixels in the area where PTZ-EXP-01 was
dark_in_ptz = sum(1 for y in range(15, 100) for x in range(20, 170) if im_after.getpixel((x, y))[0] < 85 and im_after.getpixel((x, y))[1] < 90)
print(f"Dark pixels in PTZ area: {dark_in_ptz} (was thousands before inpainting)")

# Check HAZ-LOC area (x=155..295 in crop, y=60..155)
dark_in_hazloc = sum(1 for y in range(60, 155) for x in range(155, 295) if im_after.getpixel((x, y))[0] < 95 and im_after.getpixel((x, y))[1] < 100)
print(f"Dark pixels in HAZ-LOC area: {dark_in_hazloc}")
