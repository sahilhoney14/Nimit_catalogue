from PIL import Image

def find_gutters(img_path, num_rows, num_cols):
    img = Image.open(img_path).convert('RGB')
    w, h = img.size
    print(f"=== Finding gutters for {img_path} ({w}x{h}) ===")
    
    # 1. Row boundaries:
    # Expected approximate step: h / num_rows
    row_step = h / num_rows
    row_dividers = [0]
    for r in range(1, num_rows):
        center_y = int(r * row_step)
        # search around center_y +/- 15 for max white pixels
        best_y = center_y
        max_white = -1
        for y in range(center_y - 15, center_y + 16):
            if 0 <= y < h:
                white_count = sum(1 for x in range(w) if img.getpixel((x, y)) == (255, 255, 255))
                if white_count > max_white:
                    max_white = white_count
                    best_y = y
        row_dividers.append(best_y)
    row_dividers.append(h)
    print("Row dividers:", row_dividers)
    
    # 2. For each row slice, find column dividers:
    col_step = w / num_cols
    all_row_col_dividers = []
    for r in range(num_rows):
        y0, y1 = row_dividers[r], row_dividers[r+1]
        row_cols = [0]
        for c in range(1, num_cols):
            center_x = int(c * col_step)
            best_x = center_x
            max_white = -1
            for x in range(center_x - 20, center_x + 21):
                if 0 <= x < w:
                    white_count = sum(1 for y in range(y0, y1) if img.getpixel((x, y)) == (255, 255, 255))
                    if white_count > max_white:
                        max_white = white_count
                        best_x = x
            row_cols.append(best_x)
        row_cols.append(w)
        all_row_col_dividers.append(row_cols)
        print(f"Row {r} col dividers:", row_cols)
        
    return row_dividers, all_row_col_dividers

p1_rows, p1_cols = find_gutters('c:/nimit/assets/clients_prestigious_part1.png', 6, 9)
p2_rows, p2_cols = find_gutters('c:/nimit/assets/clients_prestigious_part2.png', 5, 9)
