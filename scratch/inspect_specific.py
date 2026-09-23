import os
from PIL import Image

# Let's inspect the specific logo images
check_list = [
    ('logo_06.png', 'Agni'),
    ('logo_07.png', 'Ajanta Pharma'),
    ('logo_13.png', 'Apollo'),
    ('logo_18.png', 'Atul'),
    ('logo_22.png', 'Borosil'),
    ('logo_26.png', 'CHARUSAT'),
    ('logo_43.png', 'GGRC'),
    ('logo_44.png', 'GNFC'),
    ('logo_60.png', 'MGVCL'),
    ('logo_91.png', 'Utopia'),
]

for fn, name in check_list:
    im = Image.open(f"c:/nimit/assets/client_logos/{fn}")
    print(f"{fn} ({name}): size={im.size}")
