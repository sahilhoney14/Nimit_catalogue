from PIL import Image

im_before = Image.open('c:/nimit/scratch/camera_before.png')
im_after = Image.open('c:/nimit/scratch/camera_after.png')

# Let's side-by-side compare before and after
w, h = im_before.size
comp = Image.new('RGB', (w * 2 + 10, h), (255, 255, 255))
comp.paste(im_before, (0, 0))
comp.paste(im_after, (w + 10, 0))
comp.save('c:/nimit/scratch/comparison_camera.png')
print("Saved comparison_camera.png")
