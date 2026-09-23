from PIL import Image

def inspect_box(fn, label):
    im = Image.open(f'c:/nimit/scratch/robust_crops/{fn}').convert('RGB')
    w, h = im.size
    
    # 1. Trim 6px outer boundary to avoid gutter edges
    inner = im.crop((6, 6, w - 6, h - 6))
    iw, ih = inner.size
    
    # Find bounding box of content
    min_x, max_x, min_y, max_y = iw, 0, ih, 0
    for y in range(ih):
        for x in range(iw):
            p = inner.getpixel((x, y))
            if not (p[0] > 245 and p[1] > 245 and p[2] > 245):
                if x < min_x: min_x = x
                if x > max_x: max_x = x
                if y < min_y: min_y = y
                if y > max_y: max_y = y
                
    content_w = max_x - min_x
    content_h = max_y - min_y
    print(f"{label} ({fn}): size={w}x{h}, content box=[{min_x}..{max_x}] ({content_w}px) x [{min_y}..{max_y}] ({content_h}px)")

inspect_box('robust_06_p1_r0_c6.png', 'Anoopam Mission')
inspect_box('robust_07_p1_r0_c7.png', 'Apollo Hospitals')
inspect_box('robust_16_p1_r1_c7.png', 'Atul')
inspect_box('robust_17_p1_r1_c8.png', 'Borosil Renewables')
inspect_box('robust_22_p1_r2_c4.png', 'CHARUSAT')
inspect_box('robust_35_p1_r3_c8.png', 'GGRC')
inspect_box('robust_59_p2_r0_c5.png', 'GNFC')
inspect_box('robust_62_p2_r0_c8.png', 'MGVCL')
inspect_box('robust_86_p2_r3_c5.png', 'Utopia')
