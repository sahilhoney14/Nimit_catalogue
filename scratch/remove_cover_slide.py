import re
import os

catalog_file = r"c:\nimit\builders\build_catalog.py"
with open(catalog_file, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Remove slide 1 (the cover dict) from slides_data
# Locate slides_data = [
# The cover slide starts with:
#     {
#         'num': 1,
#         'tag': '01 // COVER',
# ... up to:
#     },
#     {
#         'num': 2,
#         'tag': '02 // MANIFESTO',

pattern_cover = re.compile(r"slides_data\s*=\s*\[\s*\{\s*'num':\s*1,\s*'tag':\s*'01 // COVER'.*?\}\s*,\s*\{\s*'num':\s*2,", re.DOTALL)
match = pattern_cover.search(content)
if not match:
    print("Error: Cover slide pattern not found!")
    exit(1)

# Replace with slides_data = [\n    {\n        'num': 1,
replacement_start = "slides_data = [\n    {\n        'num': 1,"
content = content[:match.start()] + replacement_start + content[match.end() - len("{\n        'num': 2,") + len("{\n        'num': 2,"):]

# 2. Renumber slides from 2..18 to 1..17
# Slide 2 (Manifesto) -> 1, 'tag': '01 // MANIFESTO'
content = content.replace("'tag': '02 // MANIFESTO'", "'tag': '01 // MANIFESTO'")

# Slide 3 (Why AI) -> 2, 'tag': '02 // WHY AI?'
content = content.replace("{\n        'num': 3,\n        'tag': '03 // WHY AI?'", "{\n        'num': 2,\n        'tag': '02 // WHY AI?'")

# Slide 4 (Solution) -> 3, 'tag': '03 // SOLUTION'
content = content.replace("{\n        'num': 4,\n        'tag': '04 // SOLUTION'", "{\n        'num': 3,\n        'tag': '03 // SOLUTION'")

# Slide 5 (Features) -> 4, 'tag': '05 // FEATURES'
content = content.replace("{\n        'num': 5,\n        'tag': '05 // FEATURES'", "{\n        'num': 4,\n        'tag': '04 // FEATURES'")

# Slide 6 (Vision) -> 5, 'tag': '06 // VISION'
content = content.replace("{\n        'num': 6,\n        'tag': '06 // VISION'", "{\n        'num': 5,\n        'tag': '05 // VISION'")

# Slide 7 (Module 01) -> 6, 'tag': '06 // MODULE 01'
content = content.replace("{\n        'num': 7,\n        'tag': '07 // MODULE 01'", "{\n        'num': 6,\n        'tag': '06 // MODULE 01'")

# Slide 8 (Module 02) -> 7, 'tag': '07 // MODULE 02'
content = content.replace("{\n        'num': 8,\n        'tag': '08 // MODULE 02'", "{\n        'num': 7,\n        'tag': '07 // MODULE 02'")

# Slide 9 (Module 03) -> 8, 'tag': '08 // MODULE 03'
content = content.replace("{\n        'num': 9,\n        'tag': '09 // MODULE 03'", "{\n        'num': 8,\n        'tag': '08 // MODULE 03'")

# Slide 10 (Module 04) -> 9, 'tag': '09 // MODULE 04'
content = content.replace("{\n        'num': 10,\n        'tag': '10 // MODULE 04'", "{\n        'num': 9,\n        'tag': '09 // MODULE 04'")

# Slide 11 (Module 05) -> 10, 'tag': '10 // MODULE 05'
content = content.replace("{\n        'num': 11,\n        'tag': '11 // MODULE 05'", "{\n        'num': 10,\n        'tag': '10 // MODULE 05'")

# Slide 12 (Module 06) -> 11, 'tag': '11 // MODULE 06'
content = content.replace("{\n        'num': 12,\n        'tag': '12 // MODULE 06'", "{\n        'num': 11,\n        'tag': '11 // MODULE 06'")

# Slide 13 (Module 07) -> 12, 'tag': '12 // MODULE 07'
content = content.replace("{\n        'num': 13,\n        'tag': '13 // MODULE 07'", "{\n        'num': 12,\n        'tag': '12 // MODULE 07'")

# Slide 14 (Module 08) -> 13, 'tag': '13 // MODULE 08'
content = content.replace("{\n        'num': 14,\n        'tag': '14 // MODULE 08'", "{\n        'num': 13,\n        'tag': '13 // MODULE 08'")

# Slide 15 (Module 09) -> 14, 'tag': '14 // MODULE 09'
content = content.replace("{\n        'num': 15,\n        'tag': '15 // MODULE 09'", "{\n        'num': 14,\n        'tag': '14 // MODULE 09'")

# Slide 16 (Module 10) -> 15, 'tag': '15 // MODULE 10'
content = content.replace("{\n        'num': 16,\n        'tag': '16 // MODULE 10'", "{\n        'num': 15,\n        'tag': '15 // MODULE 10'")

# Slide 17 (Module 11) -> 16, 'tag': '16 // MODULE 11'
content = content.replace("{\n        'num': 17,\n        'tag': '17 // MODULE 11'", "{\n        'num': 16,\n        'tag': '16 // MODULE 11'")

# Slide 18 (Contact) -> 17, 'tag': '17 // CONTACT'
content = content.replace("{\n        'num': 18,\n        'tag': '18 // CONTACT'", "{\n        'num': 17,\n        'tag': '17 // CONTACT'")

# 3. Update canvas container initial class
content = content.replace('class="app-screen-canvas is-cover-slide"', 'class="app-screen-canvas is-content-slide"')

# 4. Update JS speed detection video index (now slide 9)
content = content.replace('pageNum === 10;', 'pageNum === 9;')
content = content.replace('currentSlide !== 10 &&', 'currentSlide !== 9 &&')

with open(catalog_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully updated build_catalog.py without cover slide!")
