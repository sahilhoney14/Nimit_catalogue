# -*- coding: utf-8 -*-
"""
Script to clean linting errors, bare exceptions, unused imports,
and hardcoded paths in all tool scripts, and write them to tools/.
"""
import os
import re

ROOT_DIR = r"C:\nimit"
TOOLS_DIR = os.path.join(ROOT_DIR, "tools")
os.makedirs(TOOLS_DIR, exist_ok=True)

# 1. generate_isometric_hospitality.py
def clean_generate_isometric_hospitality():
    with open(os.path.join(ROOT_DIR, "generate_isometric_hospitality.py"), "r", encoding="utf-8") as f:
        code = f.read()

    # Clean imports
    code = code.replace(
        "import os\nimport math\nimport random\nfrom PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance",
        "import os\nimport math\nfrom PIL import Image, ImageDraw, ImageFont, ImageFilter\n\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\nROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'tools' else SCRIPT_DIR"
    )
    # Clean bare except
    code = code.replace("except:\n            return ImageFont.load_default()", "except Exception:\n            return ImageFont.load_default()")
    # Clean default output path
    code = code.replace("output_path='assets/hospitality_solution_visual.jpg'", "output_path=None")
    code = code.replace(
        "def generate_isometric_hospitality_visual(output_path=None):\n    w, h = 1200, 896",
        "def generate_isometric_hospitality_visual(output_path=None):\n    if output_path is None:\n        output_path = os.path.join(ROOT_DIR, 'assets', 'hospitality_solution_visual.jpg')\n    w, h = 1200, 896"
    )
    with open(os.path.join(TOOLS_DIR, "generate_isometric_hospitality.py"), "w", encoding="utf-8") as f:
        f.write(code)

# 2. generate_sectors_visual.py
def clean_generate_sectors_visual():
    with open(os.path.join(ROOT_DIR, "generate_sectors_visual.py"), "r", encoding="utf-8") as f:
        code = f.read()
    code = code.replace(
        "import os\nimport math\nfrom PIL import Image, ImageDraw, ImageFont, ImageFilter",
        "import os\nimport math\nfrom PIL import Image, ImageDraw, ImageFont\n\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\nROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'tools' else SCRIPT_DIR"
    )
    code = code.replace("except:\n            return ImageFont.load_default()", "except Exception:\n            return ImageFont.load_default()")
    code = code.replace("output_path='assets/sectors_matrix_visual.jpg'", "output_path=None")
    code = code.replace(
        "def generate_sectors_visual(output_path=None):\n    w, h = 1200, 896",
        "def generate_sectors_visual(output_path=None):\n    if output_path is None:\n        output_path = os.path.join(ROOT_DIR, 'assets', 'sectors_matrix_visual.jpg')\n    w, h = 1200, 896"
    )
    with open(os.path.join(TOOLS_DIR, "generate_sectors_visual.py"), "w", encoding="utf-8") as f:
        f.write(code)

# 3. generate_hospitality_visual.py
def clean_generate_hospitality_visual():
    with open(os.path.join(ROOT_DIR, "generate_hospitality_visual.py"), "r", encoding="utf-8") as f:
        code = f.read()
    code = code.replace(
        "import os\nimport math\nfrom PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance",
        "import os\nimport math\nfrom PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance\n\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\nROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'tools' else SCRIPT_DIR"
    )
    code = code.replace("except:\n            return ImageFont.load_default()", "except Exception:\n            return ImageFont.load_default()")
    code = code.replace("output_path='assets/hospitality_solution_visual.jpg'", "output_path=None")
    code = code.replace(
        "def generate_hospitality_visual(output_path=None):\n    w, h = 1200, 896",
        "def generate_hospitality_visual(output_path=None):\n    if output_path is None:\n        output_path = os.path.join(ROOT_DIR, 'assets', 'hospitality_solution_visual.jpg')\n    w, h = 1200, 896"
    )
    with open(os.path.join(TOOLS_DIR, "generate_hospitality_visual.py"), "w", encoding="utf-8") as f:
        f.write(code)

# 4. generate_luxury_hospitality.py
def clean_generate_luxury_hospitality():
    with open(os.path.join(ROOT_DIR, "generate_luxury_hospitality.py"), "r", encoding="utf-8") as f:
        code = f.read()
    code = code.replace(
        "import os\nimport math\nimport random\nfrom PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance",
        "import os\nimport math\nfrom PIL import Image, ImageDraw, ImageFont, ImageFilter\n\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\nROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'tools' else SCRIPT_DIR"
    )
    code = code.replace("except:\n            return ImageFont.load_default()", "except Exception:\n            return ImageFont.load_default()")
    code = code.replace("output_path='assets/hospitality_solution_visual.jpg'", "output_path=None")
    code = code.replace(
        "def generate_luxury_hospitality_visual(output_path=None):\n    w, h = 1200, 896",
        "def generate_luxury_hospitality_visual(output_path=None):\n    if output_path is None:\n        output_path = os.path.join(ROOT_DIR, 'assets', 'hospitality_solution_visual.jpg')\n    w, h = 1200, 896"
    )
    with open(os.path.join(TOOLS_DIR, "generate_luxury_hospitality.py"), "w", encoding="utf-8") as f:
        f.write(code)

# 5. generate_engaging_hospitality.py
def clean_generate_engaging_hospitality():
    with open(os.path.join(ROOT_DIR, "generate_engaging_hospitality.py"), "r", encoding="utf-8") as f:
        code = f.read()
    code = code.replace(
        "import os\nimport math\nfrom PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance",
        "import os\nfrom PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance\n\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\nROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'tools' else SCRIPT_DIR"
    )
    code = code.replace("except:\n            return ImageFont.load_default()", "except Exception:\n            return ImageFont.load_default()")
    code = code.replace("output_path='assets/hospitality_solution_visual.jpg'", "output_path=None")
    code = code.replace(
        "def generate_engaging_hospitality(output_path=None):\n    w, h = 1200, 896",
        "def generate_engaging_hospitality(output_path=None):\n    if output_path is None:\n        output_path = os.path.join(ROOT_DIR, 'assets', 'hospitality_solution_visual.jpg')\n    w, h = 1200, 896"
    )
    with open(os.path.join(TOOLS_DIR, "generate_engaging_hospitality.py"), "w", encoding="utf-8") as f:
        f.write(code)

# 6. generate_alphabetical_clients.py
def clean_generate_alphabetical_clients():
    with open(os.path.join(ROOT_DIR, "generate_alphabetical_clients.py"), "r", encoding="utf-8") as f:
        code = f.read()
    code = code.replace(
        "import os\nimport json\nfrom PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance",
        "import os\nimport json\nfrom PIL import Image, ImageDraw, ImageFont, ImageEnhance\n\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\nROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'tools' else SCRIPT_DIR"
    )
    code = re.sub(r"['\"]scratch/logo_manifest\.json['\"]", "os.path.join(ROOT_DIR, 'data', 'logo_manifest.json')", code)
    code = re.sub(r"['\"]scratch/client_details\.json['\"]", "os.path.join(ROOT_DIR, 'scratch', 'client_details.json')", code)
    code = re.sub(r"['\"]assets/client_logos/", "os.path.join(ROOT_DIR, 'assets', 'client_logos') + '/'", code)
    code = code.replace("'assets/our_clients_alphabetical.png'", "os.path.join(ROOT_DIR, 'assets', 'our_clients_alphabetical.png')")
    with open(os.path.join(TOOLS_DIR, "generate_alphabetical_clients.py"), "w", encoding="utf-8") as f:
        f.write(code)

# 7. generate_clients_mobile.py
def clean_generate_clients_mobile():
    with open(os.path.join(ROOT_DIR, "generate_clients_mobile.py"), "r", encoding="utf-8") as f:
        code = f.read()
    code = code.replace(
        "import os\nfrom PIL import Image",
        "import os\nfrom PIL import Image\n\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\nROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'tools' else SCRIPT_DIR"
    )
    code = code.replace("'assets/our_clients_alphabetical.png'", "os.path.join(ROOT_DIR, 'assets', 'our_clients_alphabetical.png')")
    code = code.replace("'assets/our_clients_mobile_part1.png'", "os.path.join(ROOT_DIR, 'assets', 'our_clients_mobile_part1.png')")
    code = code.replace("'assets/our_clients_mobile_part2.png'", "os.path.join(ROOT_DIR, 'assets', 'our_clients_mobile_part2.png')")
    with open(os.path.join(TOOLS_DIR, "generate_clients_mobile.py"), "w", encoding="utf-8") as f:
        f.write(code)

# 8. generate_perfect_logos.py
def clean_generate_perfect_logos():
    with open(os.path.join(ROOT_DIR, "generate_perfect_logos.py"), "r", encoding="utf-8") as f:
        code = f.read()
    code = code.replace(
        "import os\nimport json\nfrom PIL import Image, ImageDraw, ImageFont, ImageEnhance",
        "import os\nimport json\nfrom PIL import Image, ImageDraw, ImageFont, ImageEnhance\n\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\nROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'tools' else SCRIPT_DIR"
    )
    code = re.sub(r"['\"]scratch/logo_manifest\.json['\"]", "os.path.join(ROOT_DIR, 'data', 'logo_manifest.json')", code)
    code = re.sub(r"['\"]scratch/client_details\.json['\"]", "os.path.join(ROOT_DIR, 'scratch', 'client_details.json')", code)
    code = re.sub(r"['\"]assets/client_logos/", "os.path.join(ROOT_DIR, 'assets', 'client_logos') + '/'", code)
    code = code.replace("'assets/our_clients_perfect.png'", "os.path.join(ROOT_DIR, 'assets', 'our_clients_perfect.png')")
    with open(os.path.join(TOOLS_DIR, "generate_perfect_logos.py"), "w", encoding="utf-8") as f:
        f.write(code)

# 9. export_all_logos.py
def clean_export_all_logos():
    with open(os.path.join(ROOT_DIR, "export_all_logos.py"), "r", encoding="utf-8") as f:
        code = f.read()
    code = code.replace(
        "import os\nimport json\nfrom PIL import Image",
        "import os\nimport json\nfrom PIL import Image\n\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\nROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'tools' else SCRIPT_DIR"
    )
    code = re.sub(r"['\"]scratch/final_logo_manifest\.json['\"]", "os.path.join(ROOT_DIR, 'data', 'logo_manifest.json')", code)
    code = re.sub(r"['\"]assets/client_logos['\"]", "os.path.join(ROOT_DIR, 'assets', 'client_logos')", code)
    with open(os.path.join(TOOLS_DIR, "export_all_logos.py"), "w", encoding="utf-8") as f:
        f.write(code)

# 10. combine_clients_unified.py
def clean_combine_clients_unified():
    with open(os.path.join(ROOT_DIR, "combine_clients_unified.py"), "r", encoding="utf-8") as f:
        code = f.read()
    code = code.replace(
        "from PIL import Image\nimport os",
        "import os\nfrom PIL import Image\n\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\nROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'tools' else SCRIPT_DIR"
    )
    code = code.replace("'assets/our_clients_alphabetical.png'", "os.path.join(ROOT_DIR, 'assets', 'our_clients_alphabetical.png')")
    code = code.replace("'assets/our_clients_unified.png'", "os.path.join(ROOT_DIR, 'assets', 'our_clients_unified.png')")
    with open(os.path.join(TOOLS_DIR, "combine_clients_unified.py"), "w", encoding="utf-8") as f:
        f.write(code)

# 11. process_combined_clients.py
def clean_process_combined_clients():
    with open(os.path.join(ROOT_DIR, "process_combined_clients.py"), "r", encoding="utf-8") as f:
        code = f.read()
    code = code.replace(
        "from PIL import Image, ImageEnhance, ImageFilter\nimport os",
        "import os\nfrom PIL import Image\n\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\nROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'tools' else SCRIPT_DIR"
    )
    code = code.replace("'assets/our_clients_alphabetical.png'", "os.path.join(ROOT_DIR, 'assets', 'our_clients_alphabetical.png')")
    code = code.replace("'assets/our_clients_unified.png'", "os.path.join(ROOT_DIR, 'assets', 'our_clients_unified.png')")
    with open(os.path.join(TOOLS_DIR, "process_combined_clients.py"), "w", encoding="utf-8") as f:
        f.write(code)

# 12. rebuild_master_images.py
def clean_rebuild_master_images():
    with open(os.path.join(ROOT_DIR, "rebuild_master_images.py"), "r", encoding="utf-8") as f:
        code = f.read()
    code = code.replace(
        "import os\nimport subprocess",
        "import os\nimport subprocess\n\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\nROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'tools' else SCRIPT_DIR"
    )
    with open(os.path.join(TOOLS_DIR, "rebuild_master_images.py"), "w", encoding="utf-8") as f:
        f.write(code)

# 13. inspect_modules.py
def clean_inspect_modules():
    with open(os.path.join(ROOT_DIR, "inspect_modules.py"), "r", encoding="utf-8") as f:
        code = f.read()
    code = code.replace(
        "import json\nimport re",
        "import os\nimport json\nimport re\n\nSCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))\nROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'tools' else SCRIPT_DIR"
    )
    code = code.replace("'slides_extracted.json'", "os.path.join(ROOT_DIR, 'data', 'slides_extracted.json')")
    with open(os.path.join(TOOLS_DIR, "inspect_modules.py"), "w", encoding="utf-8") as f:
        f.write(code)

def main():
    clean_generate_isometric_hospitality()
    clean_generate_sectors_visual()
    clean_generate_hospitality_visual()
    clean_generate_luxury_hospitality()
    clean_generate_engaging_hospitality()
    clean_generate_alphabetical_clients()
    clean_generate_clients_mobile()
    clean_generate_perfect_logos()
    clean_export_all_logos()
    clean_combine_clients_unified()
    clean_process_combined_clients()
    clean_rebuild_master_images()
    clean_inspect_modules()
    print("All tools cleaned and created in tools/ successfully.")

if __name__ == '__main__':
    main()
