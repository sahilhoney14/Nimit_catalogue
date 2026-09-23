import sys
import os
sys.path.insert(0, 'c:/nimit')

from PIL import Image
from scratch.crop_cards import cards
from scratch.assign_names import names

sorted_cards = sorted(cards, key=lambda c: names.get(c['index'], '').lower())

print("=== Alphabetical Order (A to Z) ===")
for i, c in enumerate(sorted_cards):
    print(f"{i+1:02d}. {names.get(c['index'])} (orig #{c['index']})")
