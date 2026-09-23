from PIL import Image

im = Image.open('c:/nimit/assets/process_analytics_visual.jpg')
# Let's save smaller crops around the camera body:
# x=[80..400], y=[120..380]

crop1 = im.crop((80, 120, 420, 380))
crop1.save('c:/nimit/scratch/camera_body.png')

# Let's find the exact coordinates of the text on the camera body
# The camera surface is smooth metallic brushed steel / aluminum with subtle gradient
print("Saved camera_body.png")
