from PIL import Image

im = Image.open('c:/nimit/assets/process_analytics_visual.jpg').convert('RGB')

# Area 1: PTZ-EXP-01
im.crop((95, 130, 260, 255)).save('c:/nimit/scratch/text_ptz.png')

# Area 2: HAZ-LOC RATED / SWIR/EO
im.crop((230, 180, 380, 275)).save('c:/nimit/scratch/text_hazloc.png')

# Area 3: Mount text
im.crop((150, 335, 230, 385)).save('c:/nimit/scratch/text_mount.png')

print("Saved text close-up crops.")
