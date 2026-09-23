import re

with open('builders/build_catalog.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove <span class="topic-category-badge">MODULE \d+ &bull; [^<]+</span>\n\s*
new_content = re.sub(
    r'[ \t]*<span class="topic-category-badge">MODULE \d+ &bull; [^<]+</span>\s*\n',
    '',
    content
)

# 2. Remove the overlay badge from the visual frames in modules:
# <div class="usecases-image-overlay-badge">\s*<span class="matrix-live-dot"></span>\s*<span>[^<]+</span>\s*</div>\s*\n
new_content = re.sub(
    r'[ \t]*<div class="usecases-image-overlay-badge">\s*<span class="matrix-live-dot"></span>\s*<span>[^<]+</span>\s*</div>\s*\n',
    '',
    new_content
)

with open('builders/build_catalog.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated builders/build_catalog.py successfully.")
