import os
import json
from PIL import Image

# 1. Update assign_names.py with Meghmani Group
with open('c:/nimit/scratch/assign_names.py', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace('"Nesman Group"', '"Meghmani Group"')
with open('c:/nimit/scratch/assign_names.py', 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated assign_names.py with Meghmani Group.")

# 2. Check the uploaded files
adani_path = 'C:/Users/sahil/.gemini/antigravity-ide/brain/4940482b-45fa-4cec-9446-0363497dc1e0/.user_uploaded/media_1790059184442.png'
meghmani_path = 'C:/Users/sahil/.gemini/antigravity-ide/brain/4940482b-45fa-4cec-9446-0363497dc1e0/.user_uploaded/media_1790059207900.png'

im_adani = Image.open(adani_path).convert('RGBA')
im_meghmani = Image.open(meghmani_path).convert('RGBA')

print("Adani size:", im_adani.size, "Meghmani size:", im_meghmani.size)
