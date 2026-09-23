import os
import math
import random
try:
    from PIL import Image, ImageDraw, ImageFont  # type: ignore
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow"])
    from PIL import Image, ImageDraw, ImageFont  # type: ignore

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'tools' else SCRIPT_DIR

def create_sectors_visual(output_path=None):
    if output_path is None:
        output_path = os.path.join(ROOT_DIR, 'assets', 'smart_sectors_visual.jpg')
    w, h = 1200, 900
    
    # Base Image with deep gradient
    img = Image.new('RGB', (w, h), color=(10, 15, 29))
    draw = ImageDraw.Draw(img)
    
    # 1. Background Gradient
    for y in range(h):
        ratio = y / h
        r = int(9 + 12 * math.sin(ratio * math.pi) * 0.4 + 5 * ratio)
        g = int(14 + 20 * math.sin(ratio * math.pi) * 0.7 + 8 * ratio)
        b = int(28 + 38 * math.sin(ratio * math.pi) * 0.9 + 14 * ratio)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
        
    # 2. Isometric Cyber Matrix Grid
    grid_img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    grid_draw = ImageDraw.Draw(grid_img)
    
    # Horizon line & isometric grid
    for i in range(26):
        gy = 60 + int((i ** 1.38) * 26)
        if gy < h:
            alpha = int(18 + 40 * (gy / h))
            grid_draw.line([(0, gy), (w, gy)], fill=(38, 70, 120, alpha), width=1)
            
    for gx in range(0, w, 45):
        grid_draw.line([(gx, 0), (gx, h)], fill=(30, 60, 105, 24), width=1)
        
    # Telemetry Neural Nodes
    random.seed(101)
    nodes = [
        (100, 100), (320, 120), (600, 90), (880, 120), (1100, 100),
        (180, 480), (450, 460), (750, 460), (1020, 480),
        (120, 820), (380, 840), (600, 810), (820, 840), (1080, 820)
    ]
    for i in range(len(nodes)-1):
        if random.random() > 0.25:
            p1 = nodes[i]
            p2 = nodes[i+1]
            grid_draw.line([p1, (p2[0], p1[1]), p2], fill=(229, 25, 36, 45), width=1)
            grid_draw.ellipse([p1[0]-3, p1[1]-3, p1[0]+3, p1[1]+3], fill=(229, 25, 36, 140))
            
    img.paste(grid_img, (0, 0), grid_img)
    
    # Fonts
    def get_font(size, bold=False):
        try:
            if bold:
                return ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', size)
            return ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', size)
        except Exception:
            return ImageFont.load_default()
            
    title_font = get_font(28, bold=True)
    card_title_font = get_font(18, bold=True)
    card_sub_font = get_font(13, bold=False)
    tag_font = get_font(11, bold=True)
    
    # 3. Top Banner Card
    banner_box = [40, 35, w - 40, 110]
    draw.rounded_rectangle(banner_box, radius=14, fill=(15, 23, 42), outline=(229, 25, 36), width=2)
    draw.rectangle([42, 37, 50, 108], fill=(229, 25, 36))
    
    draw.text((70, 48), 'INTELLIGENT SECTOR ECOSYSTEM // MULTI-INDUSTRY DEPLOYMENT', font=tag_font, fill=(229, 25, 36))
    draw.text((70, 68), '“Smart Solutions for Every Sector, Secure Lives Everywhere”', font=title_font, fill=(255, 255, 255))
    
    # 4. 9 Sector Cards arranged in 2 balanced rows (Row 1: 4 cards, Row 2: 5 cards)
    sectors = [
        # Row 1 (4 items)
        {"name": "Industries", "sub": "Smart Factory & Heavy Infra", "color": (229, 25, 36), "icon": "🏭", "tag": "INDUSTRIAL"},
        {"name": "Religious Place", "sub": "Heritage & Large Gatherings", "color": (245, 158, 11), "icon": "🛕", "tag": "LANDMARKS"},
        {"name": "Education", "sub": "Universities & Smart Campuses", "color": (59, 130, 246), "icon": "🎓", "tag": "ACADEMIC"},
        {"name": "Hotel & Restaurant", "sub": "Luxury Hospitality & Dining", "color": (168, 85, 247), "icon": "🏨", "tag": "HOSPITALITY"},
        
        # Row 2 (5 items)
        {"name": "Campus", "sub": "Tech Parks & Commercial Infra", "color": (6, 182, 212), "icon": "🏢", "tag": "ENTERPRISE"},
        {"name": "Showroom", "sub": "Automotive & Retail Display", "color": (16, 185, 129), "icon": "🏬", "tag": "RETAIL"},
        {"name": "Jewellers", "sub": "High-Security Vault Protection", "color": (236, 72, 153), "icon": "💎", "tag": "HIGH-SECURITY"},
        {"name": "Hospital", "sub": "Critical Care & Nurse Calling", "color": (239, 68, 68), "icon": "🏥", "tag": "HEALTHCARE"},
        {"name": "Government Sector", "sub": "Civic Infra & Public Defense", "color": (100, 116, 139), "icon": "🏛️", "tag": "GOVERNANCE"}
    ]
    
    # Row 1 Layout (4 cards)
    row1_y = 135
    row1_h = 340
    card_w1 = (w - 80 - 3 * 20) // 4
    
    for i in range(4):
        s = sectors[i]
        cx = 40 + i * (card_w1 + 20)
        card_box = [cx, row1_y, cx + card_w1, row1_y + row1_h]
        
        # Draw Card Container
        draw.rounded_rectangle(card_box, radius=16, fill=(18, 26, 47), outline=(45, 65, 100), width=1)
        # Top Accent Strip
        draw.rounded_rectangle([cx, row1_y, cx + card_w1, row1_y + 8], radius=8, fill=s["color"])
        
        # Icon Circle
        icon_circle = [cx + card_w1//2 - 40, row1_y + 40, cx + card_w1//2 + 40, row1_y + 120]
        draw.ellipse(icon_circle, fill=(26, 38, 68), outline=s["color"], width=2)
        
        # Category Tag Pill
        tag_w = len(s["tag"]) * 8 + 16
        tag_box = [cx + card_w1//2 - tag_w//2, row1_y + 145, cx + card_w1//2 + tag_w//2, row1_y + 168]
        draw.rounded_rectangle(tag_box, radius=6, fill=(s["color"][0]//4, s["color"][1]//4, s["color"][2]//4), outline=s["color"], width=1)
        draw.text((cx + card_w1//2 - tag_w//2 + 8, row1_y + 150), s["tag"], font=tag_font, fill=s["color"])
        
        # Sector Name
        name_bbox = draw.textbbox((0, 0), s["name"], font=card_title_font)
        nw = name_bbox[2] - name_bbox[0]
        draw.text((cx + card_w1//2 - nw//2, row1_y + 190), s["name"], font=card_title_font, fill=(255, 255, 255))
        
        # Subtitle
        sub_bbox = draw.textbbox((0, 0), s["sub"], font=card_sub_font)
        sw = sub_bbox[2] - sub_bbox[0]
        draw.text((cx + card_w1//2 - sw//2, row1_y + 225), s["sub"], font=card_sub_font, fill=(148, 163, 184))
        
        # Status Pill
        status_box = [cx + 20, row1_y + row1_h - 45, cx + card_w1 - 20, row1_y + row1_h - 18]
        draw.rounded_rectangle(status_box, radius=6, fill=(12, 19, 36), outline=(38, 55, 85), width=1)
        draw.ellipse([cx + 32, row1_y + row1_h - 35, cx + 40, row1_y + row1_h - 27], fill=(16, 185, 129))
        draw.text((cx + 48, row1_y + row1_h - 37), "AI Surveillance Active", font=tag_font, fill=(16, 185, 129))
        
    # Row 2 Layout (5 cards)
    row2_y = 500
    row2_h = 340
    card_w2 = (w - 80 - 4 * 16) // 5
    
    for i in range(5):
        s = sectors[4 + i]
        cx = 40 + i * (card_w2 + 16)
        card_box = [cx, row2_y, cx + card_w2, row2_y + row2_h]
        
        # Draw Card Container
        draw.rounded_rectangle(card_box, radius=16, fill=(18, 26, 47), outline=(45, 65, 100), width=1)
        # Top Accent Strip
        draw.rounded_rectangle([cx, row2_y, cx + card_w2, row2_y + 8], radius=8, fill=s["color"])
        
        # Icon Circle
        icon_circle = [cx + card_w2//2 - 36, row2_y + 36, cx + card_w2//2 + 36, row2_y + 108]
        draw.ellipse(icon_circle, fill=(26, 38, 68), outline=s["color"], width=2)
        
        # Category Tag Pill
        tag_w = len(s["tag"]) * 7 + 14
        tag_box = [cx + card_w2//2 - tag_w//2, row2_y + 135, cx + card_w2//2 + tag_w//2, row2_y + 158]
        draw.rounded_rectangle(tag_box, radius=6, fill=(s["color"][0]//4, s["color"][1]//4, s["color"][2]//4), outline=s["color"], width=1)
        draw.text((cx + card_w2//2 - tag_w//2 + 7, row2_y + 140), s["tag"], font=tag_font, fill=s["color"])
        
        # Sector Name
        name_bbox = draw.textbbox((0, 0), s["name"], font=card_title_font)
        nw = name_bbox[2] - name_bbox[0]
        # Wrap if too wide
        if nw > card_w2 - 16:
            words = s["name"].split()
            line1 = " ".join(words[:1])
            line2 = " ".join(words[1:])
            b1 = draw.textbbox((0, 0), line1, font=card_title_font)
            b2 = draw.textbbox((0, 0), line2, font=card_title_font)
            draw.text((cx + card_w2//2 - (b1[2]-b1[0])//2, row2_y + 175), line1, font=card_title_font, fill=(255, 255, 255))
            draw.text((cx + card_w2//2 - (b2[2]-b2[0])//2, row2_y + 198), line2, font=card_title_font, fill=(255, 255, 255))
        else:
            draw.text((cx + card_w2//2 - nw//2, row2_y + 185), s["name"], font=card_title_font, fill=(255, 255, 255))
            
        # Subtitle
        sub_bbox = draw.textbbox((0, 0), s["sub"], font=card_sub_font)
        sw = sub_bbox[2] - sub_bbox[0]
        draw.text((cx + card_w2//2 - sw//2, row2_y + 230), s["sub"], font=card_sub_font, fill=(148, 163, 184))
        
        # Status Pill
        status_box = [cx + 14, row2_y + row2_h - 45, cx + card_w2 - 14, row2_y + row2_h - 18]
        draw.rounded_rectangle(status_box, radius=6, fill=(12, 19, 36), outline=(38, 55, 85), width=1)
        draw.ellipse([cx + 22, row2_y + row2_h - 35, cx + 30, row2_y + row2_h - 27], fill=(16, 185, 129))
        draw.text((cx + 36, row2_y + row2_h - 37), "AI Live Protect", font=tag_font, fill=(16, 185, 129))

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, quality=95)
    print(f"Generated sectors visual saved to {output_path}")

if __name__ == '__main__':
    create_sectors_visual()
