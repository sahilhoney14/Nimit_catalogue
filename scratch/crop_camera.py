from PIL import Image

im = Image.open('c:/nimit/assets/process_analytics_visual.jpg')
w, h = im.size

# The camera is in the upper-left quadrant: x ≈ [50..450], y ≈ [100..450]
crop = im.crop((50, 100, 450, 450))
crop.save('c:/nimit/scratch/camera_crop.png')
print("Saved camera_crop.png")
