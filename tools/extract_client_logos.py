# -*- coding: utf-8 -*-
"""
Production Client Logo Extraction & Processing Pipeline.
Extracts all 99 client brand logos using exact sub-pixel bounding boxes,
eliminates all divider lines, borders, and shadows,
sorts them alphabetically A-to-Z, and exports high-definition assets to assets/client_logos/.
"""

import os
import sys
import json
from typing import Dict, List, Any

try:
    from PIL import Image, ImageDraw  # type: ignore
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow'])
    from PIL import Image, ImageDraw  # type: ignore

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from tools.generate_perfect_logos import run_generate_perfect_logos

if __name__ == '__main__':
    run_generate_perfect_logos()
