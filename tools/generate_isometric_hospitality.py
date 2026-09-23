import os
import math
try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter  # type: ignore
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow'])
    from PIL import Image, ImageDraw, ImageFont, ImageFilter  # type: ignore

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'tools' else SCRIPT_DIR

def generate_isometric_hospitality_visual(output_path=None):
    if output_path is None:
        output_path = os.path.join(ROOT_DIR, 'assets', 'hospitality_solution_visual.jpg')
    w, h = 1200, 896
    
    # 1. Base Canvas - Deep Luxury Slate / Architectural Isometric Background
    img = Image.new('RGB', (w, h), color=(14, 20, 36))
    draw = ImageDraw.Draw(img)
    
    # Gradient backdrop (architectural ambient lighting)
    for y in range(h):
        r = int(14 + (y/h) * 8 + math.sin(y/h * math.pi) * 6)
        g = int(22 + (y/h) * 12 + math.sin(y/h * math.pi) * 10)
        b = int(40 + (y/h) * 18 + math.sin(y/h * math.pi) * 16)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
        
    # Architectural background floor grid (Isometric ground plane)
    grid_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(grid_layer)
    for i in range(-20, 40):
        # Isometric grid lines at 30 degrees
        x1 = i * 60
        y1 = 0
        x2 = x1 + h * 1.732
        y2 = h
        g_draw.line([(x1, y1), (x2, y2)], fill=(35, 55, 90, 45), width=1)
        
        x3 = i * 60 + 600
        y3 = 0
        x4 = x3 - h * 1.732
        y4 = h
        g_draw.line([(x3, y3), (x4, y4)], fill=(35, 55, 90, 45), width=1)
        
    img.paste(grid_layer, (0, 0), grid_layer)
    
    # Typography
    def get_font(name, size):
        font_map = {
            'title': 'C:/Windows/Fonts/bahnschrift.ttf',
            'bold': 'C:/Windows/Fonts/segoeuib.ttf',
            'regular': 'C:/Windows/Fonts/segoeui.ttf',
            'mono': 'C:/Windows/Fonts/consola.ttf'
        }
        p = font_map.get(name, 'C:/Windows/Fonts/arial.ttf')
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            return ImageFont.load_default()
            
    f_title = get_font('title', 20)
    f_hud_h = get_font('title', 15)
    f_badge = get_font('title', 11)
    f_bold = get_font('bold', 13)
    f_bold_lg = get_font('bold', 17)
    f_reg = get_font('regular', 12)
    f_mono = get_font('mono', 12)
    
    # -------------------------------------------------------------------------
    # 2. RENDER 3D ISOMETRIC SMART HOTEL BUILDING ROOMS (Cross-Section Cutaway)
    # -------------------------------------------------------------------------
    bldg = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    b_draw = ImageDraw.Draw(bldg)
    
    # Helper to draw isometric box / room
    def draw_iso_floor(poly_points, fill_color, border_color=(70, 95, 140, 180)):
        b_draw.polygon(poly_points, fill=fill_color, outline=border_color)
        
    def draw_iso_wall(poly_points, fill_color, border_color=(80, 110, 160, 180)):
        b_draw.polygon(poly_points, fill=fill_color, outline=border_color)

    # -------------------------------------------------------------------------
    # ROOM 1: LUXURY GUEST SUITE & CALL STATION (Top-Left Section)
    # -------------------------------------------------------------------------
    # Floor: Luxury wood parquet (warm walnut)
    r1_floor = [(60, 260), (380, 140), (560, 240), (240, 360)]
    draw_iso_floor(r1_floor, (65, 48, 38, 255), (120, 90, 70, 200))
    # Parquet plank lines
    for pl in range(1, 8):
        t = pl / 8.0
        p1 = (int(60 + t * (380 - 60)), int(260 + t * (140 - 260)))
        p2 = (int(240 + t * (560 - 240)), int(360 + t * (240 - 360)))
        b_draw.line([p1, p2], fill=(85, 62, 50, 180), width=1)
        
    # Back Left Wall (Smart suite wall with bedside panel)
    r1_wall1 = [(60, 260), (380, 140), (380, 20), (60, 140)]
    draw_iso_wall(r1_wall1, (42, 52, 78, 240), (90, 120, 170, 200))
    
    # Back Right Wall
    r1_wall2 = [(380, 140), (560, 240), (560, 120), (380, 20)]
    draw_iso_wall(r1_wall2, (32, 42, 65, 240), (80, 110, 155, 200))
    
    # Luxury Hotel King Bed (3D Isometric Model)
    # Bed base
    bed_base = [(120, 260), (280, 200), (340, 235), (180, 295)]
    b_draw.polygon(bed_base, fill=(28, 36, 56, 255), outline=(90, 110, 150))
    # Bed mattress & white luxury duvet
    bed_top = [(120, 245), (280, 185), (340, 220), (180, 280)]
    b_draw.polygon(bed_top, fill=(230, 235, 245, 255), outline=(180, 195, 220))
    # Pillows
    b_draw.polygon([(140, 240), (190, 220), (210, 230), (160, 250)], fill=(245, 245, 255), outline=(180, 190, 210))
    b_draw.polygon([(200, 215), (250, 195), (270, 205), (220, 225)], fill=(245, 245, 255), outline=(180, 190, 210))
    # Nightstand
    b_draw.polygon([(290, 180), (340, 160), (360, 172), (310, 192)], fill=(50, 38, 30), outline=(100, 80, 65))
    
    # Wall-Mounted Bedside Nurse/Attendant Call Unit (Glowing Hardware)
    b_draw.polygon([(240, 100), (285, 82), (285, 115), (240, 133)], fill=(240, 245, 250), outline=(0, 210, 255), width=2)
    # Glowing Red SOS Emergency Button on unit
    b_draw.polygon([(252, 108), (273, 100), (273, 116), (252, 124)], fill=(235, 45, 60), outline=(255, 150, 160))
    b_draw.line([(240, 133), (240, 155)], fill=(0, 240, 255), width=2) # Cord

    # -------------------------------------------------------------------------
    # ROOM 2: HOTEL RECEPTION LOBBY & CONCIERGE (Top-Right Section)
    # -------------------------------------------------------------------------
    # Floor: Polished Italian White & Gold Marble
    r2_floor = [(580, 240), (900, 120), (1140, 240), (820, 360)]
    draw_iso_floor(r2_floor, (48, 56, 75, 255), (140, 165, 210, 200))
    # Marble floor tile grid
    for mx in range(1, 6):
        t = mx / 6.0
        p1 = (int(580 + t * (900 - 580)), int(240 + t * (120 - 240)))
        p2 = (int(820 + t * (1140 - 820)), int(360 + t * (240 - 360)))
        b_draw.line([p1, p2], fill=(70, 82, 110, 160), width=1)
        
    # Back Feature Wall: Luxury Vertical Wood Slat Wall
    r2_wall1 = [(580, 240), (900, 120), (900, 10), (580, 130)]
    draw_iso_wall(r2_wall1, (40, 28, 20, 240), (100, 75, 55, 200))
    # Wood slats
    for sl in range(0, 320, 16):
        sx1 = 580 + int(sl * 0.8)
        sy1 = 240 - int(sl * 0.3)
        b_draw.line([(sx1, sy1), (sx1, sy1 - 100)], fill=(75, 52, 38), width=2)
        
    # "HOTEL RESORT" Grand Gold Signage on wall
    b_draw.text((680, 45), "GRAND SMART HOTEL & RESORT", fill=(240, 210, 140), font=f_bold)
    
    # Back Right Glass Window Wall overlooking city skyline
    r2_wall2 = [(900, 120), (1140, 240), (1140, 120), (900, 10)]
    draw_iso_wall(r2_wall2, (20, 45, 75, 220), (0, 210, 255, 160))
    # Window mullions
    b_draw.line([(980, 80), (980, 200)], fill=(0, 200, 255, 120), width=2)
    b_draw.line([(1060, 140), (1060, 260)], fill=(0, 200, 255, 120), width=2)
    
    # Marble Reception Front Counter (3D Isometric Desk)
    desk_top = [(680, 260), (840, 200), (890, 225), (730, 285)]
    b_draw.polygon(desk_top, fill=(230, 225, 215), outline=(210, 180, 130), width=2)
    desk_front = [(730, 285), (890, 225), (890, 290), (730, 350)]
    b_draw.polygon(desk_front, fill=(35, 26, 20), outline=(140, 110, 80))
    desk_left = [(680, 260), (730, 285), (730, 350), (680, 325)]
    b_draw.polygon(desk_left, fill=(28, 20, 16), outline=(100, 75, 55))
    
    # Enterprise Unified Communications IP-PBX Console on Counter
    phone_base = [(760, 235), (800, 220), (820, 230), (780, 245)]
    b_draw.polygon(phone_base, fill=(25, 30, 45), outline=(0, 210, 255), width=2)
    # Phone screen (color LCD)
    b_draw.polygon([(770, 215), (805, 202), (815, 218), (780, 230)], fill=(0, 220, 255), outline=(255, 255, 255))
    
    # Receptionist & Guest Isometric Figures (Silhouettes with modern style)
    # Receptionist behind desk
    b_draw.ellipse([805, 160, 825, 180], fill=(220, 185, 150)) # Head
    b_draw.polygon([(795, 180), (835, 180), (845, 230), (785, 230)], fill=(28, 38, 65)) # Suit
    # Guest checking in in front of desk
    b_draw.ellipse([670, 270, 690, 290], fill=(215, 180, 145))
    b_draw.polygon([(660, 290), (700, 290), (705, 360), (655, 360)], fill=(35, 50, 85)) # Navy blazer
    
    # -------------------------------------------------------------------------
    # ROOM 3: GUEST SUITE ENTRYWAY & BIOMETRIC LOCK (Bottom-Left Section)
    # -------------------------------------------------------------------------
    # Floor
    r3_floor = [(60, 560), (380, 440), (560, 540), (240, 660)]
    draw_iso_floor(r3_floor, (38, 48, 70, 255), (90, 120, 170, 200))
    
    # Doorway Entry Wall (Cutaway)
    r3_wall = [(240, 660), (560, 540), (560, 400), (240, 520)]
    draw_iso_wall(r3_wall, (30, 40, 60, 240), (80, 110, 160, 200))
    
    # 3D Smart Suite Door (Modern Dark Oak with Metallic Frame)
    door_frame = [(340, 620), (450, 580), (450, 430), (340, 470)]
    b_draw.polygon(door_frame, fill=(45, 32, 25), outline=(0, 240, 180), width=2)
    # Door panel inset
    b_draw.polygon([(350, 610), (440, 575), (440, 445), (350, 480)], fill=(32, 22, 18), outline=(90, 70, 55))
    
    # Smart Fingerprint & RFID Lock Handle Unit on Door
    lock_box = [(365, 535), (385, 527), (385, 570), (365, 578)]
    b_draw.polygon(lock_box, fill=(15, 20, 30), outline=(0, 240, 180), width=2)
    # Glowing Biometric Scanner Ring (Green LED Access Granted)
    b_draw.ellipse([368, 542, 382, 556], fill=(0, 255, 160), outline=(255, 255, 255))
    # VIP RFID Keycard hovering near lock with NFC waves
    b_draw.polygon([(320, 550), (350, 538), (355, 558), (325, 570)], fill=(0, 210, 255), outline=(255, 255, 255), width=2)
    b_draw.arc([340, 530, 370, 560], start=-45, end=45, fill=(0, 255, 180), width=2)

    # -------------------------------------------------------------------------
    # ROOM 4: SMART ROOM IoT AUTOMATION & CLOUD GATEWAY (Bottom-Right Section)
    # -------------------------------------------------------------------------
    # Floor: Smart suite lounge
    r4_floor = [(580, 540), (900, 420), (1140, 540), (820, 660)]
    draw_iso_floor(r4_floor, (32, 42, 62, 255), (75, 105, 155, 200))
    
    # Smart Lounge Sofa & Coffee Table
    sofa_base = [(680, 550), (820, 495), (860, 515), (720, 570)]
    b_draw.polygon(sofa_base, fill=(40, 55, 88), outline=(100, 130, 190))
    table_top = [(760, 575), (830, 548), (860, 560), (790, 587)]
    b_draw.polygon(table_top, fill=(210, 185, 140), outline=(140, 115, 80))
    
    # Wall Smart Screen / Interactive Hospitality Display
    b_draw.polygon([(940, 440), (1070, 500), (1070, 410), (940, 350)], fill=(10, 18, 38), outline=(0, 220, 255), width=2)
    # Screen UI graph
    b_draw.text((955, 380), "IoT ROOM CONTROL // SUITE 402", fill=(0, 240, 255), font=f_badge)
    b_draw.text((955, 400), "HVAC: 22°C • LIGHTS: WELCOME", fill=(255, 255, 255), font=f_badge)
    b_draw.text((955, 420), "ENERGY SAVER: KEYCARD ACTIVE", fill=(0, 255, 180), font=f_badge)
    
    # Cyber Interconnect Traces (Glowing Cyan Network Bus connecting all 4 zones)
    bus_lines = [
        [(285, 115), (420, 180), (560, 240), (680, 260)], # Call unit to PBX
        [(385, 550), (560, 480), (760, 235)],              # Lock to PBX
        [(385, 550), (600, 640), (940, 440)],              # Lock to IoT Screen
    ]
    for bl in bus_lines:
        for bi in range(len(bl)-1):
            b_draw.line([bl[bi], bl[bi+1]], fill=(0, 240, 255, 160), width=2)
            # Glowing node dot
            b_draw.ellipse([bl[bi][0]-4, bl[bi][1]-4, bl[bi][0]+4, bl[bi][1]+4], fill=(0, 255, 255))
            
    img.paste(bldg, (0, 0), bldg)
    
    # -------------------------------------------------------------------------
    # 3. FLOATING DARK-GLASS HUD TELEMETRY CARDS (Style of Education Visual)
    # -------------------------------------------------------------------------
    hud_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    h_draw = ImageDraw.Draw(hud_layer)
    
    def draw_hud_box(x1, y1, x2, y2, tag_text, title_text, desc_text, target_pt, anchor_pos='bottom', badge_col=(0, 210, 255)):
        # Card shadow & glow
        glow_c = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        g_c_draw = ImageDraw.Draw(glow_c)
        g_c_draw.rounded_rectangle([x1-4, y1-4, x2+4, y2+4], radius=12, fill=(badge_col[0], badge_col[1], badge_col[2], 35))
        glow_c = glow_c.filter(ImageFilter.GaussianBlur(10))
        img.paste(glow_c, (0, 0), glow_c)
        
        # HUD Panel Body
        h_draw.rounded_rectangle([x1, y1, x2, y2], radius=10, fill=(10, 18, 34, 235), outline=(badge_col[0], badge_col[1], badge_col[2], 210), width=2)
        # Top accent highlight
        h_draw.line([(x1+12, y1+2), (x2-12, y1+2)], fill=(255, 255, 255, 80), width=1)
        
        # Tag Badge
        h_draw.rounded_rectangle([x1+12, y1+10, x1+12+len(tag_text)*8, y1+28], radius=4, fill=(badge_col[0], badge_col[1], badge_col[2], 50), outline=badge_col)
        h_draw.text((x1+18, y1+12), tag_text, fill=badge_col, font=f_badge)
        
        # Title
        h_draw.text((x1+12, y1+34), title_text, fill=(255, 255, 255), font=f_hud_h)
        # Description
        h_draw.text((x1+12, y1+56), desc_text, fill=(180, 205, 235), font=f_reg)
        
        # Pointer line & Target Dot
        if anchor_pos == 'bottom':
            px = (x1 + x2) // 2
            py = y2
        elif anchor_pos == 'right':
            px = x2
            py = (y1 + y2) // 2
        elif anchor_pos == 'left':
            px = x1
            py = (y1 + y2) // 2
        else:
            px = (x1 + x2) // 2
            py = y1
            
        h_draw.line([(px, py), target_pt], fill=badge_col, width=2)
        h_draw.ellipse([target_pt[0]-5, target_pt[1]-5, target_pt[0]+5, target_pt[1]+5], fill=badge_col, outline=(255, 255, 255), width=2)

    # HUD 1: Nurse/Attendant Calling System (Top-Left)
    draw_hud_box(
        x1=30, y1=60, x2=340, y2=145,
        tag_text="EMERGENCY CALL",
        title_text="NURSE / ATTENDANT CALL",
        desc_text="Bedside Touch SOS • Response: 00:01.2s",
        target_pt=(260, 115),
        anchor_pos='bottom',
        badge_col=(255, 75, 90)
    )
    
    # HUD 2: Unified Communications Platform (Top-Right)
    draw_hud_box(
        x1=820, y1=60, x2=1160, y2=145,
        tag_text="VoIP IP-PBX MASTER",
        title_text="UNIFIED COMMUNICATIONS",
        desc_text="64 SIP Trunks • HD Voice • Concierge Mesh",
        target_pt=(790, 230),
        anchor_pos='left',
        badge_col=(170, 95, 255)
    )
    
    # HUD 3: Finger/Card Lock System (Bottom-Left)
    draw_hud_box(
        x1=30, y1=720, x2=390, y2=805,
        tag_text="BIOMETRIC & RFID",
        title_text="FINGER / CARD LOCK SYSTEM",
        desc_text="Optical 508 DPI Scanner • Contactless NFC Card",
        target_pt=(365, 555),
        anchor_pos='top',
        badge_col=(0, 230, 170)
    )
    
    # HUD 4: Smart Room IoT Controls (Bottom-Right)
    draw_hud_box(
        x1=780, y1=720, x2=1160, y2=805,
        tag_text="AUTOMATION HUB",
        title_text="SMART ROOM IoT CONTROLS",
        desc_text="Auto-HVAC (22°C) • Keycard Energy Activation",
        target_pt=(980, 470),
        anchor_pos='top',
        badge_col=(0, 210, 255)
    )

    img.paste(hud_layer, (0, 0), hud_layer)
    
    # 4. Master Outer Bevel & Corner Tech Brackets
    border_draw = ImageDraw.Draw(img)
    border_draw.rectangle([0, 0, w-1, h-1], outline=(0, 210, 255, 180), width=2)
    corner_len = 36
    corners = [(0, 0, 1, 1), (w-1, 0, -1, 1), (0, h-1, 1, -1), (w-1, h-1, -1, -1)]
    for cx, cy, dx, dy in corners:
        border_draw.line([(cx, cy), (cx + dx * corner_len, cy)], fill=(0, 255, 255), width=4)
        border_draw.line([(cx, cy), (cx, cy + dy * corner_len)], fill=(0, 255, 255), width=4)
        
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, quality=96)
    print(f"Successfully generated 3D isometric smart hotel ecosystem visual at {output_path} ({w}x{h})")

if __name__ == '__main__':
    generate_isometric_hospitality_visual()
