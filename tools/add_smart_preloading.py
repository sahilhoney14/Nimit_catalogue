# -*- coding: utf-8 -*-
"""
Inject Smart Preloading Engine into Builder Scripts:
1. build_company_hub.py
2. build_solutions.py
3. build_catalog.py
"""

import os
import re

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILDERS_DIR = os.path.join(ROOT_DIR, 'builders')

# 1. build_company_hub.py
hub_path = os.path.join(BUILDERS_DIR, 'build_company_hub.py')
with open(hub_path, 'r', encoding='utf-8') as f:
    hub_code = f.read()

hub_preload_fn = '''
    const preloadedImages = new Set();
    function preloadAdjacentImages(currentIdx) {
      [currentIdx + 1, currentIdx + 2, currentIdx - 1].forEach(idx => {
        if (idx >= 0 && idx < slides.length) {
          const s = slides[idx];
          if (s && s.html) {
            const matches = [...s.html.matchAll(/src="(assets\/[^"]+\.webp)"/g)];
            matches.forEach(m => {
              if (!preloadedImages.has(m[1])) {
                preloadedImages.add(m[1]);
                const img = new Image();
                img.src = m[1];
              }
            });
          }
        }
      });
    }
'''

if 'function preloadAdjacentImages' not in hub_code:
    # insert call in renderSlide
    hub_code = hub_code.replace(
        'animateCounters();',
        'animateCounters();\n        preloadAdjacentImages(currentIndex);'
    )
    # insert function before renderSlide
    hub_code = hub_code.replace(
        'function renderSlide(idx) {',
        hub_preload_fn + '\n    function renderSlide(idx) {'
    )
    # insert initial trigger
    hub_code = hub_code.replace(
        "renderSlide(getInitialSlide());",
        "renderSlide(getInitialSlide());\n    preloadAdjacentImages(getInitialSlide());"
    )
    with open(hub_path, 'w', encoding='utf-8') as f:
        f.write(hub_code)
    print("[+] Added Smart Preloading to build_company_hub.py")

# 2. build_solutions.py
sol_path = os.path.join(BUILDERS_DIR, 'build_solutions.py')
with open(sol_path, 'r', encoding='utf-8') as f:
    sol_code = f.read()

sol_preload_fn = '''
    const preloadedImages = new Set();
    function preloadAdjacentImages(currentNum) {{
      [currentNum + 1, currentNum + 2, currentNum - 1].forEach(num => {{
        if (num >= 1 && num <= totalSlides) {{
          const s = slidesData.find(x => x.num === num);
          if (s && s.html) {{
            const matches = [...s.html.matchAll(/src="(assets\/[^"]+\.webp)"/g)];
            matches.forEach(m => {{
              if (!preloadedImages.has(m[1])) {{
                preloadedImages.add(m[1]);
                const img = new Image();
                img.src = m[1];
              }}
            }});
          }}
        }}
      }});
    }}
'''

if 'function preloadAdjacentImages' not in sol_code:
    sol_code = sol_code.replace(
        'isTransitioning = false;',
        'isTransitioning = false;\n        preloadAdjacentImages(pageNum);'
    )
    sol_code = sol_code.replace(
        'function renderSlide(pageNum) {',
        sol_preload_fn + '\n    function renderSlide(pageNum) {'
    )
    sol_code = sol_code.replace(
        'renderSlide(1);',
        'renderSlide(1);\n    preloadAdjacentImages(1);'
    )
    with open(sol_path, 'w', encoding='utf-8') as f:
        f.write(sol_code)
    print("[+] Added Smart Preloading to build_solutions.py")

# 3. build_catalog.py
cat_path = os.path.join(BUILDERS_DIR, 'build_catalog.py')
with open(cat_path, 'r', encoding='utf-8') as f:
    cat_code = f.read()

cat_preload_fn = '''
    const preloadedMedia = new Set();
    function preloadAdjacentMedia(currentNum) {{
      [currentNum + 1, currentNum + 2, currentNum - 1].forEach(num => {{
        if (num >= 1 && num <= totalSlides) {{
          const s = slidesData.find(x => x.num === num);
          if (s && s.html) {{
            const vMatches = [...s.html.matchAll(/src="(assets\/[^"]+\.mp4)"/g)];
            vMatches.forEach(m => {{
              if (!preloadedMedia.has(m[1])) {{
                preloadedMedia.add(m[1]);
                const v = document.createElement('video');
                v.preload = 'auto';
                v.src = m[1];
              }}
            }});
            const pMatches = [...s.html.matchAll(/(?:poster|src)="(assets\/[^"]+\.webp)"/g)];
            pMatches.forEach(m => {{
              if (!preloadedMedia.has(m[1])) {{
                preloadedMedia.add(m[1]);
                const img = new Image();
                img.src = m[1];
              }}
            }});
          }}
        }}
      }});
    }}
'''

if 'function preloadAdjacentMedia' not in cat_code:
    cat_code = cat_code.replace(
        'isTransitioning = false;\n      }, 140);',
        'isTransitioning = false;\n        preloadAdjacentMedia(pageNum);\n      }, 140);'
    )
    cat_code = cat_code.replace(
        'function renderSlide(pageNum, direction = \'next\') {',
        cat_preload_fn + '\n    function renderSlide(pageNum, direction = \'next\') {'
    )
    cat_code = cat_code.replace(
        'renderSlide(1, \'next\');',
        'renderSlide(1, \'next\');\n    preloadAdjacentMedia(1);'
    )
    with open(cat_path, 'w', encoding='utf-8') as f:
        f.write(cat_code)
    print("[+] Added Smart Preloading to build_catalog.py")

print("\nDone injecting smart preloading!")
