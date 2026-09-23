import os
from PIL import Image

def find_logo_islands_in_image(img_path, num_rows, expected_cols_per_row=9):
    img = Image.open(img_path).convert('RGB')
    w, h = img.size
    print(f"=== Finding exact logo islands for {img_path} ({w}x{h}) ===")
    
    # 1. Find the horizontal row bands:
    # A row band is a vertical interval [y_start, y_end] where dark pixels exist,
    # separated by horizontal lines where dark pixels are 0 or minimal.
    row_step = h / num_rows
    row_bands = []
    for r in range(num_rows):
        approx_mid = int((r + 0.5) * row_step)
        
        # Scan upwards to find top of this row's logos
        top_y = approx_mid
        for y in range(approx_mid, max(0, approx_mid - int(row_step * 0.6)), -1):
            dark_count = sum(1 for x in range(w) if any(c < 200 for c in img.getpixel((x, y))))
            if dark_count == 0:
                top_y = y
                break
        else:
            top_y = max(0, int(r * row_step))
            
        # Scan downwards to find bottom of this row's logos
        bottom_y = approx_mid
        for y in range(approx_mid, min(h, approx_mid + int(row_step * 0.6))):
            dark_count = sum(1 for x in range(w) if any(c < 200 for c in img.getpixel((x, y))))
            if dark_count == 0:
                bottom_y = y
                break
        else:
            bottom_y = min(h, int((r + 1) * row_step))
            
        row_bands.append((top_y, bottom_y))
        print(f"Row {r} vertical band: y=[{top_y}..{bottom_y}] (h={bottom_y - top_y}px)")
        
    # 2. For each row band, find the 9 contiguous dark-pixel islands along x:
    all_islands = []
    for r, (y0, y1) in enumerate(row_bands):
        # Scan across x from 0 to w
        dark_per_col = [sum(1 for y in range(y0, y1) if any(c < 200 for c in img.getpixel((x, y)))) for x in range(w)]
        
        # Find contiguous spans where dark_per_col > 0
        islands = []
        in_island = False
        start_x = 0
        
        for x in range(w):
            if dark_per_col[x] > 0:
                if not in_island:
                    in_island = True
                    start_x = x
            else:
                if in_island:
                    in_island = False
                    # Only accept islands that are at least 15px wide (filters out tiny single-pixel specks)
                    if (x - start_x) >= 15:
                        islands.append((start_x, x))
                        
        if in_island and (w - start_x) >= 15:
            islands.append((start_x, w))
            
        print(f"Row {r}: found {len(islands)} islands: {islands}")
        all_islands.append((row_bands[r], islands))
        
    return all_islands

islands1 = find_logo_islands_in_image('c:/nimit/assets/clients_prestigious_part1.png', 6)
islands2 = find_logo_islands_in_image('c:/nimit/assets/clients_prestigious_part2.png', 5)
