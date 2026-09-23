import os
try:
    from PIL import Image  # type: ignore
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow'])
    from PIL import Image  # type: ignore

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'tools' else SCRIPT_DIR, ImageDraw

def generate_mobile_clients():
    p1 = 'assets/clients_prestigious_part1.png'
    p2 = 'assets/clients_prestigious_part2.png'

    im1 = Image.open(p1).convert('RGB')
    draw1 = ImageDraw.Draw(im1)
    # Clean tiny blue arrow artifact at the bottom-left corner of part 1
    draw1.rectangle([0, 720, 90, im1.height], fill=(255, 255, 255))

    im2 = Image.open(p2).convert('RGB')

    # Tight crop to logo content bounds
    c1 = im1.crop((35, 0, 1695, im1.height))
    c2 = im2.crop((25, 0, 1705, im2.height))

    # Match target width exactly
    w_target = 1660
    c1_scaled_h = int(c1.height * (w_target / c1.width))
    c1_resized = c1.resize((w_target, c1_scaled_h), Image.Resampling.LANCZOS)

    c2_scaled_h = int(c2.height * (w_target / c2.width))
    c2_resized = c2.resize((w_target, c2_scaled_h), Image.Resampling.LANCZOS)

    # Vertical gap matching the logo grid's internal row spacing
    row_gap = 14
    total_h = c1_resized.height + row_gap + c2_resized.height
    stacked = Image.new('RGB', (w_target, total_h), (255, 255, 255))
    stacked.paste(c1_resized, (0, 0))
    stacked.paste(c2_resized, (0, c1_resized.height + row_gap))

    # Save high-res master
    final_w = 2000
    final_h = int(final_w * (total_h / w_target))
    stacked_final = stacked.resize((final_w, final_h), Image.Resampling.LANCZOS)

    out_path = 'assets/clients_prestigious_mobile.png'
    stacked_final.save(out_path, quality=98)
    print(f"Successfully generated {out_path} with size {stacked_final.size}")

if __name__ == '__main__':
    generate_mobile_clients()
