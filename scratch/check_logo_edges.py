import os
from PIL import Image

# Let's inspect each of the 99 logos to see if any has unwanted pixels or clipping
# We can check left, right, top, bottom edges of each logo
problem_logos = []
for i in range(1, 100):
    fn = f"logo_{i:02d}.png"
    im = Image.open(f"c:/nimit/assets/client_logos/{fn}").convert('RGB')
    w, h = im.size
    
    # Check if left edge (x=0 to 10) or right edge (x=w-10 to w) has non-white pixels
    left_non_white = sum(1 for y in range(h) for x in range(8) if im.getpixel((x, y)) != (255, 255, 255))
    right_non_white = sum(1 for y in range(h) for x in range(w-8, w) if im.getpixel((x, y)) != (255, 255, 255))
    top_non_white = sum(1 for y in range(6) for x in range(w) if im.getpixel((x, y)) != (255, 255, 255))
    bottom_non_white = sum(1 for y in range(h-6, h) for x in range(w) if im.getpixel((x, y)) != (255, 255, 255))
    
    if left_non_white > 0 or right_non_white > 0 or top_non_white > 0 or bottom_non_white > 0:
        problem_logos.append((i, fn, left_non_white, right_non_white, top_non_white, bottom_non_white))

print(f"Logos with border noise: {len(problem_logos)}")
for p in problem_logos:
    print(p)
