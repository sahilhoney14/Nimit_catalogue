import re
import json

with open('build_catalog.py', 'r', encoding='utf-8') as f:
    text = f.read()

tags = re.findall(r"'tag':\s*'([^']+)'", text)
titles = re.findall(r"'title':\s*'([^']+)'", text)
for i, (tag, title) in enumerate(zip(tags, titles)):
    print(f"Slide {i+1}: tag='{tag}', title='{title}'")

print(f"Total slides in build_catalog.py: {len(tags)}")

with open('slides_data.json', 'r', encoding='utf-8') as f:
    sd = json.load(f)

print(f"\nTotal slides in slides_data.json: {len(sd)}")
for s in sd[:6]:
    print(f"Slide {s.get('slide_num')}: paragraphs={s.get('paragraphs', [])[:3]}, media={s.get('media', [])}")
