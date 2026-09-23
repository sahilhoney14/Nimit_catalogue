import re

with open('builders/build_catalog.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to remove premise-card-arrow divs from topic cards
arrow_pattern = re.compile(
    r'[ \t]*<div class="premise-card-arrow">\s*<svg[^>]*>[\s\S]*?<\/svg>\s*<\/div>\s*\n'
)

new_content = arrow_pattern.sub('', content)

with open('builders/build_catalog.py', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Removed premise-card-arrow icons from builders/build_catalog.py.")
