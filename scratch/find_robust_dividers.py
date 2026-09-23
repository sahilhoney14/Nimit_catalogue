from PIL import Image

def find_robust_dividers(img_path, num_rows, num_cols):
    img = Image.open(img_path).convert('RGB')
    w, h = img.size
    print(f"=== Finding ROBUST dividers for {img_path} ({w}x{h}) ===")
    
    # 1. Find the 6 horizontal row dividers by scanning full width
    row_step = h / num_rows
    row_bounds = [0]
    for r in range(1, num_rows):
        approx_y = int(r * row_step)
        best_y = approx_y
        max_white = -1
        for y in range(approx_y - 25, approx_y + 26):
            if 0 <= y < h:
                # count white pixels across the full width
                white_count = sum(1 for x in range(w) if img.getpixel((x, y)) == (255, 255, 255))
                if white_count > max_white:
                    max_white = white_count
                    best_y = y
        row_bounds.append(best_y)
    row_bounds.append(h)
    print("Row bounds:", row_bounds)
    
    # 2. For EACH row independently, find the 9 column intervals:
    # Notice: the left margin is around 0-30px, right margin around 1700-1750px
    col_step = (w - 40) / num_cols
    all_rows_cols = []
    
    for r in range(num_rows):
        y0 = row_bounds[r] + 5
        y1 = row_bounds[r+1] - 5
        row_h = y1 - y0
        
        # Find left edge of row (first non-white from x=0..80)
        left_x = 0
        for x in range(0, 100):
            non_white = sum(1 for y in range(y0, y1) if img.getpixel((x, y)) != (255, 255, 255))
            if non_white > 5:
                left_x = max(0, x - 2)
                break
                
        # Find right edge of row (last non-white from x=1750..1600)
        right_x = w
        for x in range(w - 1, w - 150, -1):
            non_white = sum(1 for y in range(y0, y1) if img.getpixel((x, y)) != (255, 255, 255))
            if non_white > 5:
                right_x = min(w, x + 2)
                break
                
        cols = [left_x]
        effective_w = right_x - left_x
        row_col_step = effective_w / num_cols
        
        for c in range(1, num_cols):
            approx_x = int(left_x + c * row_col_step)
            best_x = approx_x
            max_white = -1
            # Search in a generous +/- 35px window around approx_x for the true gutter
            for x in range(approx_x - 35, approx_x + 36):
                if 0 <= x < w:
                    white_count = sum(1 for y in range(y0, y1) if img.getpixel((x, y)) == (255, 255, 255))
                    if white_count > max_white:
                        max_white = white_count
                        best_x = x
            cols.append(best_x)
        cols.append(right_x)
        all_rows_cols.append(cols)
        print(f"Row {r} (y={y0}..{y1}): cols={cols}")
        
    return row_bounds, all_rows_cols

p1_r, p1_c = find_robust_dividers('c:/nimit/assets/clients_prestigious_part1.png', 6, 9)
p2_r, p2_c = find_robust_dividers('c:/nimit/assets/clients_prestigious_part2.png', 5, 9)
