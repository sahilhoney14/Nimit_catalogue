from PIL import Image

def inspect_card_crop(path):
    im = Image.open(path).convert('RGB')
    w, h = im.size
    print(f"=== {path} ({w}x{h}) ===")
    
    # Check bounding box of non-white content
    min_x, max_x, min_y, max_y = w, 0, h, 0
    for y in range(h):
        for x in range(w):
            p = im.getpixel((x, y))
            if not (p[0] > 245 and p[1] > 245 and p[2] > 245):
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
    print(f"Content box: x=[{min_x}..{max_x}] ({max_x - min_x}px), y=[{min_y}..{max_y}] ({max_y - min_y}px)")

inspect_card_crop('c:/nimit/scratch/precise_crops/card_07_p1_r0_c7.png') # Apollo
inspect_card_crop('c:/nimit/scratch/precise_crops/card_17_p1_r1_c8.png') # Borosil
inspect_card_crop('c:/nimit/scratch/precise_crops/card_62_p2_r0_c8.png') # MGVCL
inspect_card_crop('c:/nimit/scratch/precise_crops/card_86_p2_r3_c5.png') # Utopia
