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

def generate_attractive_hospitality_visual(output_path=None):
    w, h = 1200, 896
    
    # 1. Base Canvas - Deep Luxury Hospitality Interior Atmosphere
    base = Image.new('RGB', (w, h), color=(10, 14, 26))
    draw = ImageDraw.Draw(base)
    
    # Luxury Hotel Lobby Lighting Gradient (Warm Amber Architectural Ambient Glow + Deep Indigo Slate)
    for y in range(h):
        for x in range(0, w, 4):
            # Radial distance from warm lobby chandeliers (top center and top right)
            d1 = math.sqrt((x - 600)**2 + (y - 120)**2) / 700
            d2 = math.sqrt((x - 1000)**2 + (y - 200)**2) / 600
            d3 = math.sqrt((x - 200)**2 + (y - 700)**2) / 800
            
            glow_warm = max(0.0, 1.0 - d1) * 0.45 + max(0.0, 1.0 - d2) * 0.35
            glow_cyan = max(0.0, 1.0 - d3) * 0.3
            
            # Base dark tones
            r = int(12 + 75 * glow_warm + 10 * glow_cyan)
            g = int(16 + 55 * glow_warm + 35 * glow_cyan)
            b = int(28 + 30 * glow_warm + 65 * glow_cyan)
            
            draw.rectangle([x, y, x+4, y+1], fill=(min(255, r), min(255, g), min(255, b)))
            
    # Add architectural backdrop geometry (Luxury Hotel Reception, Wood Paneling, Marble Pillars)
    arch_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    arch_draw = ImageDraw.Draw(arch_layer)
    
    # Vertical luxury wood slat feature wall on the right side
    for wx in range(680, w, 24):
        arch_draw.rectangle([wx, 0, wx+14, h], fill=(38, 26, 20, 140))
        arch_draw.line([(wx, 0), (wx, h)], fill=(75, 52, 38, 160), width=1)
        arch_draw.line([(wx+14, 0), (wx+14, h)], fill=(18, 12, 10, 180), width=1)
        
    # Luxury Hotel Reception Marble Counter across lower background
    arch_draw.polygon([(0, 480), (w, 440), (w, 620), (0, 680)], fill=(22, 28, 44, 180))
    arch_draw.line([(0, 480), (w, 440)], fill=(210, 175, 120, 140), width=3) # Golden marble trim
    
    # Soft Bokeh Orbs (Luxury Chandelier Glows)
    bokeh_centers = [
        (450, 140, 90, (255, 190, 100, 40)),
        (580, 180, 130, (255, 210, 120, 35)),
        (750, 120, 100, (255, 180, 90, 45)),
        (920, 160, 120, (255, 200, 110, 35)),
        (250, 300, 140, (0, 210, 255, 25)),
        (1050, 400, 160, (0, 255, 180, 20))
    ]
    for bx, by, br, bcol in bokeh_centers:
        arch_draw.ellipse([bx-br, by-br, bx+br, by+br], fill=bcol)
        
    arch_layer = arch_layer.filter(ImageFilter.GaussianBlur(18))
    base.paste(arch_layer, (0, 0), arch_layer)
    
    # Grid lines & Digital Overlay Matrix
    matrix_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    m_draw = ImageDraw.Draw(matrix_layer)
    for gx in range(0, w, 40):
        m_draw.line([(gx, 0), (gx, h)], fill=(0, 210, 255, 12), width=1)
    for gy in range(0, h, 40):
        m_draw.line([(0, gy), (w, gy)], fill=(0, 210, 255, 12), width=1)
    base.paste(matrix_layer, (0, 0), matrix_layer)
    
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
    f_sub = get_font('title', 15)
    f_card_h = get_font('title', 17)
    f_badge = get_font('title', 11)
    f_bold = get_font('bold', 14)
    f_bold_lg = get_font('bold', 18)
    f_reg = get_font('regular', 13)
    f_sm = get_font('regular', 11)
    f_mono = get_font('mono', 12)
    f_mono_lg = get_font('mono', 16)
    
    # Helper: Glassmorphism Card with Gradient Border & Soft Shadow
    def create_card(x1, y1, x2, y2, border_rgb=(0, 220, 255), fill_rgb=(14, 22, 40), alpha_border=200, alpha_bg=230):
        c_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        c_draw = ImageDraw.Draw(c_layer)
        
        # Outer Shadow & Glow
        glow = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        g_draw = ImageDraw.Draw(glow)
        g_draw.rounded_rectangle([x1-6, y1-6, x2+6, y2+6], radius=20, fill=(border_rgb[0], border_rgb[1], border_rgb[2], 40))
        glow = glow.filter(ImageFilter.GaussianBlur(14))
        base.paste(glow, (0, 0), glow)
        
        # Card Body
        c_draw.rounded_rectangle([x1, y1, x2, y2], radius=16, fill=(fill_rgb[0], fill_rgb[1], fill_rgb[2], alpha_bg))
        c_draw.rounded_rectangle([x1, y1, x2, y2], radius=16, outline=(border_rgb[0], border_rgb[1], border_rgb[2], alpha_border), width=2)
        # Top metallic reflection line
        c_draw.line([(x1+20, y1+2), (x2-20, y1+2)], fill=(255, 255, 255, 90), width=1)
        base.paste(c_layer, (0, 0), c_layer)

    # 2. Header Strip across top
    top_strip = Image.new('RGBA', (w, 56), (10, 16, 32, 235))
    t_draw = ImageDraw.Draw(top_strip)
    t_draw.line([(0, 55), (w, 55)], fill=(0, 220, 255, 100), width=1)
    
    # Logo & Title
    t_draw.ellipse([26, 18, 42, 34], fill=(0, 230, 255))
    t_draw.text((54, 16), "NIMIT AI // SMART HOSPITALITY & FACILITY ECOSYSTEM", fill=(255, 255, 255), font=f_title)
    
    # Right Status Chips
    t_draw.rounded_rectangle([860, 12, 1005, 44], radius=8, fill=(15, 38, 60, 220), outline=(0, 230, 255, 140))
    t_draw.ellipse([874, 24, 882, 32], fill=(0, 255, 150))
    t_draw.text((890, 19), "HOTEL IoT: 100%", fill=(0, 255, 170), font=f_badge)
    
    t_draw.rounded_rectangle([1015, 12, 1165, 44], radius=8, fill=(35, 15, 30, 220), outline=(255, 80, 120, 140))
    t_draw.ellipse([1028, 24, 1036, 32], fill=(255, 75, 95))
    t_draw.text((1044, 19), "GUEST SUITES: CONNECTED", fill=(255, 140, 160), font=f_badge)
    
    base.paste(top_strip, (0, 0), top_strip)
    
    # -------------------------------------------------------------------------
    # 3. THREE HERO CARDS: TOP-LEFT, TOP-RIGHT, AND BOTTOM SPAN
    # -------------------------------------------------------------------------
    
    # -------------------------------------------------------------------------
    # CARD 1: NURSE / ATTENDANT CALLING SYSTEM (Top Left: 35, 76 to 585, 460)
    # -------------------------------------------------------------------------
    c1_box = (35, 76, 585, 460)
    create_card(c1_box[0], c1_box[1], c1_box[2], c1_box[3], border_rgb=(255, 75, 90), fill_rgb=(16, 20, 38), alpha_border=210)
    
    c1_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    c1_d = ImageDraw.Draw(c1_layer)
    
    # Header
    c1_d.rounded_rectangle([52, 92, 92, 132], radius=10, fill=(255, 60, 75, 45), outline=(255, 90, 110, 200), width=1)
    c1_d.ellipse([64, 104, 80, 120], fill=(255, 70, 85))
    c1_d.text((104, 94), "NURSE / ATTENDANT CALLING SYSTEM", fill=(255, 255, 255), font=f_card_h)
    c1_d.text((104, 118), "Bedside SOS Console • Instant Responder • Ward Telemetry", fill=(175, 195, 225), font=f_sm)
    
    c1_d.rounded_rectangle([465, 92, 568, 122], radius=6, fill=(255, 50, 70, 50), outline=(255, 90, 110, 180))
    c1_d.text((478, 98), "EMERGENCY SOS", fill=(255, 120, 130), font=f_badge)
    
    c1_d.line([(52, 142), (568, 142)], fill=(255, 255, 255, 30), width=1)
    
    # Hero Hardware Visual: 3D Bedside Touch Terminal with Glowing Red SOS Ring
    c1_d.rounded_rectangle([55, 156, 265, 340], radius=14, fill=(20, 30, 54, 240), outline=(0, 210, 255, 150), width=2)
    # Beveled Terminal Screen
    c1_d.rounded_rectangle([68, 168, 252, 205], radius=6, fill=(8, 14, 28), outline=(0, 230, 255, 100))
    c1_d.ellipse([78, 182, 86, 190], fill=(0, 255, 140))
    c1_d.text((94, 178), "ROOM 402 // BED-A", fill=(0, 240, 255), font=f_bold)
    
    # Large 3D Glowing SOS Button
    sos_x, sos_y = 160, 260
    # Outer pulsating neon waves
    c1_d.ellipse([sos_x-46, sos_y-46, sos_x+46, sos_y+46], outline=(255, 60, 75, 60), width=2)
    c1_d.ellipse([sos_x-38, sos_y-38, sos_x+38, sos_y+38], outline=(255, 80, 95, 120), width=2)
    # 3D Red Button Body
    c1_d.ellipse([sos_x-30, sos_y-30, sos_x+30, sos_y+30], fill=(235, 40, 55), outline=(255, 160, 170), width=3)
    c1_d.text((sos_x-16, sos_y-10), "SOS", fill=(255, 255, 255), font=f_bold_lg)
    c1_d.text((106, 314), "PRESS FOR ATTENDANT", fill=(200, 225, 255), font=f_badge)
    
    # Telemetry & Vital Wave Stream (Right side of Card 1)
    c1_d.rounded_rectangle([280, 156, 568, 242], radius=10, fill=(12, 20, 38, 220), outline=(255, 80, 95, 130))
    c1_d.text((295, 166), "ATTENDANT DISPATCH STREAM", fill=(255, 130, 140), font=f_sub)
    c1_d.text((295, 190), "RESPONDER: NURSE STATION 3", fill=(255, 255, 255), font=f_bold)
    c1_d.text((295, 212), "RESPONSE TIME: 00:01.2s", fill=(0, 255, 180), font=f_mono)
    
    c1_d.rounded_rectangle([460, 202, 555, 232], radius=6, fill=(0, 180, 90, 45), outline=(0, 255, 140, 140))
    c1_d.text((472, 208), "EN ROUTE", fill=(0, 255, 150), font=f_badge)
    
    # Live Cardiac / Status Wave Strip
    c1_d.rounded_rectangle([280, 254, 568, 340], radius=10, fill=(10, 16, 32, 240), outline=(0, 210, 255, 90))
    c1_d.text((294, 262), "LIVE GUEST TELEMETRY & ROOM COMFORT", fill=(0, 210, 255), font=f_sm)
    
    wave_pts = []
    base_wy = 302
    for wx in range(294, 555, 4):
        p_rel = (wx - 294)
        if 60 < p_rel < 130:
            wy = base_wy + int(20 * math.sin(p_rel * 0.22) * math.cos(p_rel * 0.08))
        else:
            wy = base_wy + int(4 * math.sin(p_rel * 0.12))
        wave_pts.append((wx, wy))
    for wi in range(len(wave_pts)-1):
        c1_d.line([wave_pts[wi], wave_pts[wi+1]], fill=(0, 255, 170), width=2)
    c1_d.text((294, 322), "HEART RATE: 72 BPM  •  COMFORT: OPTIMAL  •  NOISE: 28 dB", fill=(170, 200, 230), font=f_mono)
    
    # 4-Ward Room Status Matrix Strip
    rooms_data = [
        ("RM 401", "NORMAL", (0, 255, 140)),
        ("RM 402", "SOS ACTIVE", (255, 60, 75)),
        ("RM 403", "ATTENDING", (255, 180, 20)),
        ("RM 404", "STANDBY", (80, 190, 255))
    ]
    for idx, (rm, st, col) in enumerate(rooms_data):
        rx1 = 55 + idx * 130
        rx2 = rx1 + 120
        c1_d.rounded_rectangle([rx1, 355, rx2, 445], radius=8, fill=(18, 26, 48, 220), outline=(col[0], col[1], col[2], 120))
        c1_d.ellipse([rx1+12, 368, rx1+20, 376], fill=col)
        c1_d.text((rx1+26, 364), rm, fill=(255, 255, 255), font=f_bold)
        c1_d.text((rx1+12, 390), st, fill=col, font=f_badge)
        c1_d.text((rx1+12, 412), "NODE: 100% OK", fill=(130, 160, 190), font=f_sm)
        c1_d.text((rx1+12, 428), f"PING: {idx*0.2 + 0.6:.1f}ms", fill=(0, 220, 255), font=f_mono)
        
    base.paste(c1_layer, (0, 0), c1_layer)

    # -------------------------------------------------------------------------
    # CARD 2: UNIFIED COMMUNICATIONS PLATFORM (Top Right: 615, 76 to 1165, 460)
    # -------------------------------------------------------------------------
    c2_box = (615, 76, 1165, 460)
    create_card(c2_box[0], c2_box[1], c2_box[2], c2_box[3], border_rgb=(170, 90, 255), fill_rgb=(18, 18, 42), alpha_border=210)
    
    c2_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    c2_d = ImageDraw.Draw(c2_layer)
    
    # Header
    c2_d.rounded_rectangle([632, 92, 672, 132], radius=10, fill=(170, 80, 255, 45), outline=(180, 100, 255, 200), width=1)
    c2_d.rounded_rectangle([642, 102, 662, 122], radius=4, fill=(190, 110, 255))
    c2_d.ellipse([649, 110, 655, 116], fill=(255, 255, 255))
    c2_d.text((684, 94), "UNIFIED COMMUNICATIONS PLATFORM", fill=(255, 255, 255), font=f_card_h)
    c2_d.text((684, 118), "IP-PBX VoIP Hub • Reception Master Terminal • Intercom Mesh", fill=(190, 180, 230), font=f_sm)
    
    c2_d.rounded_rectangle([1040, 92, 1148, 122], radius=6, fill=(150, 70, 255, 50), outline=(180, 100, 255, 180))
    c2_d.text((1052, 98), "HD VoIP MASTER", fill=(210, 160, 255), font=f_badge)
    
    c2_d.line([(632, 142), (1148, 142)], fill=(255, 255, 255, 30), width=1)
    
    # Hero Hardware Visual: Modern Enterprise IP Phone Console (Left half of Card 2)
    c2_d.rounded_rectangle([635, 156, 855, 340], radius=14, fill=(22, 28, 58, 240), outline=(170, 110, 255, 150), width=2)
    # Color LCD Screen on Phone
    c2_d.rounded_rectangle([648, 168, 842, 235], radius=8, fill=(10, 14, 32), outline=(0, 220, 255, 110))
    c2_d.text((658, 176), "IP-PBX HD TRUNK // LINE 1", fill=(0, 240, 255), font=f_bold)
    c2_d.text((658, 196), "CONCIERGE -> GUEST SUITE 402", fill=(255, 255, 255), font=f_sm)
    c2_d.text((658, 214), "CODEC: G.722 HD • 02:48 ACTIVE", fill=(0, 255, 170), font=f_mono)
    
    # Keypad matrix
    for kr in range(3):
        for kc in range(4):
            kx1 = 650 + kc * 48
            ky1 = 246 + kr * 27
            c2_d.rounded_rectangle([kx1, ky1, kx1+40, ky1+21], radius=4, fill=(32, 40, 80), outline=(120, 130, 200, 90))
            c2_d.text((kx1+14, ky1+3), f"{kr*4+kc+1}", fill=(210, 230, 255), font=f_badge)
            
    # Audio Equalizer Visualizer (Top Right of Card 2)
    c2_d.rounded_rectangle([870, 156, 1148, 242], radius=10, fill=(14, 18, 42, 220), outline=(170, 90, 255, 110))
    c2_d.text((885, 166), "HD VOICE EQUALIZER SPECTRUM", fill=(190, 160, 255), font=f_sub)
    
    eq_bars = [18, 30, 48, 65, 55, 75, 88, 95, 80, 68, 90, 52, 45, 70, 78, 60, 38, 22]
    for bi, bh in enumerate(eq_bars):
        bx = 885 + bi * 14
        by2 = 228
        by1 = by2 - int(bh * 0.44)
        r_c = int(0 + (bi / len(eq_bars)) * 200)
        g_c = int(220 - (bi / len(eq_bars)) * 90)
        b_c = 255
        c2_d.rounded_rectangle([bx, by1, bx+9, by2], radius=3, fill=(r_c, g_c, b_c))
    c2_d.text((885, 230), "STEREO 128 kbps • 0.0% PACKET LOSS", fill=(0, 255, 200), font=f_mono)
    
    # SIP Multi-Point Routing Mesh (Bottom Right of Card 2)
    c2_d.rounded_rectangle([870, 254, 1148, 340], radius=10, fill=(10, 16, 36, 240), outline=(0, 210, 255, 90))
    c2_d.text((885, 262), "SIP ROUTING DISPATCH NETWORK", fill=(0, 220, 255), font=f_sm)
    
    mesh_pts = [
        (905, 305, "PBX CORE"),
        (980, 290, "RECEPTION"),
        (980, 322, "ROOM 402"),
        (1080, 305, "GUEST SERVICES")
    ]
    c2_d.line([(905, 305), (980, 290)], fill=(0, 240, 255), width=2)
    c2_d.line([(905, 305), (980, 322)], fill=(180, 100, 255), width=2)
    c2_d.line([(980, 290), (1080, 305)], fill=(0, 255, 170), width=2)
    c2_d.line([(980, 322), (1080, 305)], fill=(255, 190, 0), width=2)
    
    for nx, ny, nlabel in mesh_pts:
        c2_d.ellipse([nx-7, ny-7, nx+7, ny+7], fill=(0, 240, 255), outline=(255, 255, 255), width=1)
        c2_d.text((nx-24, ny+9), nlabel, fill=(220, 235, 255), font=f_badge)
        
    # Bottom Communication Features Strip
    c2_features = [
        ("SIP TRUNKS", "64 / 64 ACTIVE", (0, 255, 180)),
        ("INTERCOM", "AUTO-ATTENDANT", (180, 120, 255)),
        ("CONFERENCING", "16 BRIDGES", (255, 180, 40)),
        ("PAGING / PA", "ALL ZONES OK", (0, 220, 255))
    ]
    for idx, (ft, val, col) in enumerate(c2_features):
        fx1 = 635 + idx * 130
        fx2 = fx1 + 120
        c2_d.rounded_rectangle([fx1, 355, fx2, 445], radius=8, fill=(20, 26, 52, 220), outline=(col[0], col[1], col[2], 120))
        c2_d.ellipse([fx1+12, 368, fx1+20, 376], fill=col)
        c2_d.text((fx1+26, 364), ft, fill=(255, 255, 255), font=f_bold)
        c2_d.text((fx1+12, 390), val, fill=col, font=f_badge)
        c2_d.text((fx1+12, 412), "ENCRYPTION: ON", fill=(140, 170, 200), font=f_sm)
        c2_d.text((fx1+12, 428), "UPTIME: 99.99%", fill=(0, 255, 170), font=f_mono)
        
    base.paste(c2_layer, (0, 0), c2_layer)

    # -------------------------------------------------------------------------
    # CARD 3: FINGER / CARD LOCK SYSTEM (Bottom Spanned: 35, 480 to 1165, 860)
    # -------------------------------------------------------------------------
    c3_box = (35, 480, 1165, 860)
    create_card(c3_box[0], c3_box[1], c3_box[2], c3_box[3], border_rgb=(0, 230, 170), fill_rgb=(12, 24, 40), alpha_border=220)
    
    c3_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    c3_d = ImageDraw.Draw(c3_layer)
    
    # Header
    c3_d.rounded_rectangle([52, 496, 92, 536], radius=10, fill=(0, 220, 150, 45), outline=(0, 240, 170, 200), width=1)
    c3_d.rounded_rectangle([62, 508, 82, 526], radius=4, fill=(0, 240, 170))
    c3_d.ellipse([68, 504, 76, 512], outline=(0, 240, 170), width=2)
    c3_d.text((104, 498), "FINGER / CARD LOCK SYSTEM & ROOM AUTOMATION", fill=(255, 255, 255), font=f_card_h)
    c3_d.text((104, 522), "Optical Biometric Fingerprint • RFID/NFC Contactless Keycard • Room Energy Gateway", fill=(170, 215, 220), font=f_sm)
    
    c3_d.rounded_rectangle([1015, 496, 1148, 526], radius=6, fill=(0, 200, 140, 50), outline=(0, 255, 170, 180))
    c3_d.text((1028, 502), "ENCRYPTED AES-256", fill=(0, 255, 180), font=f_badge)
    
    c3_d.line([(52, 546), (1148, 546)], fill=(255, 255, 255, 30), width=1)
    
    # Sub-Visual 1: Smart Biometric Handle & Optical Scanner (Left: 55 to 370)
    c3_d.rounded_rectangle([55, 560, 370, 840], radius=12, fill=(16, 28, 48, 240), outline=(0, 230, 170, 140), width=2)
    c3_d.text((70, 574), "BIOMETRIC FINGERPRINT SCANNER", fill=(0, 240, 180), font=f_sub)
    
    # Biometric Fingerprint Graphic with glowing scan rings
    fp_x, fp_y = 140, 695
    c3_d.ellipse([fp_x-52, fp_y-52, fp_x+52, fp_y+52], outline=(0, 230, 170, 50), width=2)
    c3_d.ellipse([fp_x-42, fp_y-42, fp_x+42, fp_y+42], outline=(0, 240, 180, 110), width=2)
    c3_d.ellipse([fp_x-32, fp_y-32, fp_x+32, fp_y+32], fill=(8, 32, 40), outline=(0, 255, 200), width=2)
    
    for r_idx in range(10, 30, 4):
        c3_d.arc([fp_x-r_idx, fp_y-r_idx, fp_x+r_idx, fp_y+r_idx], start=30, end=330, fill=(0, 255, 180), width=2)
    c3_d.line([(fp_x-36, fp_y), (fp_x+36, fp_y)], fill=(255, 255, 255), width=2)
    
    # Status badges on right side of fingerprint module
    c3_d.rounded_rectangle([215, 625, 355, 665], radius=6, fill=(0, 180, 120, 40), outline=(0, 255, 160, 140))
    c3_d.text((225, 633), "MATCH: 99.8%", fill=(0, 255, 170), font=f_bold)
    c3_d.text((225, 649), "VERIFIED GUEST", fill=(200, 230, 240), font=f_badge)
    
    c3_d.rounded_rectangle([215, 680, 355, 720], radius=6, fill=(0, 120, 200, 40), outline=(0, 200, 255, 140))
    c3_d.text((225, 688), "LOCK: MOTORIZED", fill=(0, 220, 255), font=f_bold)
    c3_d.text((225, 704), "STATE: UNLOCKED", fill=(0, 255, 180), font=f_badge)
    
    c3_d.rounded_rectangle([215, 735, 355, 775], radius=6, fill=(180, 100, 255, 40), outline=(190, 120, 255, 140))
    c3_d.text((225, 743), "SPEED: 0.28s", fill=(210, 160, 255), font=f_bold)
    c3_d.text((225, 759), "ANTI-SPOOF: ACTIVE", fill=(220, 200, 255), font=f_badge)
    
    c3_d.text((70, 804), "OPTICAL 508 DPI • CAPACITIVE LIVE SCAN", fill=(160, 200, 220), font=f_sm)
    
    # Sub-Visual 2: Contactless RFID / NFC Keycard & Energy Saver (Center: 390 to 760)
    c3_d.rounded_rectangle([390, 560, 760, 840], radius=12, fill=(16, 28, 50, 240), outline=(0, 210, 255, 140), width=2)
    c3_d.text((406, 574), "CONTACTLESS RFID / NFC SMART KEYCARD", fill=(0, 220, 255), font=f_sub)
    
    # Keycard Graphic Mockup
    c3_d.rounded_rectangle([415, 615, 605, 735], radius=10, fill=(20, 40, 78), outline=(0, 240, 255), width=2)
    c3_d.rounded_rectangle([430, 630, 465, 656], radius=4, fill=(255, 190, 40), outline=(255, 220, 100))
    c3_d.text((430, 672), "NIMIT AI VIP KEYCARD", fill=(255, 255, 255), font=f_bold)
    c3_d.text((430, 692), "SUITE 402  •  PREMIUM", fill=(0, 230, 255), font=f_sm)
    c3_d.text((430, 710), "NFC 13.56 MHz // MIFARE DESFire", fill=(170, 200, 230), font=f_badge)
    
    # NFC Waves
    for arc_r in range(15, 65, 15):
        c3_d.arc([595-arc_r, 670-arc_r, 595+arc_r, 670+arc_r], start=-60, end=60, fill=(0, 255, 180), width=2)
        
    # Reader Unit
    c3_d.rounded_rectangle([655, 625, 740, 725], radius=8, fill=(10, 18, 35), outline=(0, 255, 180), width=2)
    c3_d.ellipse([690, 648, 705, 663], fill=(0, 255, 180))
    c3_d.text((667, 680), "TAP CARD", fill=(255, 255, 255), font=f_badge)
    c3_d.text((667, 700), "HERE >>>", fill=(0, 240, 255), font=f_badge)
    
    # Energy Switch automation strip
    c3_d.rounded_rectangle([415, 755, 740, 825], radius=8, fill=(10, 20, 40), outline=(0, 200, 255, 100))
    c3_d.ellipse([430, 778, 442, 790], fill=(255, 190, 0))
    c3_d.text((452, 768), "INTELLIGENT KEYCARD ENERGY SAVER", fill=(255, 255, 255), font=f_bold)
    c3_d.text((452, 790), "AUTOMATED LIGHTING, HVAC (22°C) & POWER ON INSERTION", fill=(0, 255, 180), font=f_sm)

    # Sub-Visual 3: Real-Time Access Audit Logs & Cloud Sync (Right: 780 to 1148)
    c3_d.rounded_rectangle([780, 560, 1148, 840], radius=12, fill=(14, 22, 42, 240), outline=(0, 210, 255, 140), width=2)
    c3_d.text((796, 574), "LIVE ACCESS AUDIT LOGS & CLOUD SYNC", fill=(0, 210, 255), font=f_sub)
    
    log_rows = [
        ("14:12:04", "SUITE 402", "BIOMETRIC AUTH", "ACCESS GRANTED", (0, 255, 150)),
        ("14:12:06", "SUITE 402", "ENERGY SWITCH", "POWER ACTIVE", (255, 190, 0)),
        ("14:05:18", "ROOM 305", "RFID VIP TAP", "ACCESS GRANTED", (0, 255, 150)),
        ("13:50:22", "ROOM 208", "HOUSEKEEPING", "MAID MASTER KEY", (180, 130, 255)),
        ("13:35:10", "SUITE 501", "MOBILE NFC APP", "DIGITAL KEY OK", (0, 220, 255)),
        ("13:10:45", "ROOM 104", "DOOR SENSOR", "DOOR SECURED", (140, 220, 180))
    ]
    for li, (lt, lr, lm, ls, lc) in enumerate(log_rows):
        ly = 612 + li * 33
        c3_d.rounded_rectangle([796, ly, 1132, ly+27], radius=5, fill=(20, 30, 54, 180), outline=(lc[0], lc[1], lc[2], 70))
        c3_d.text((806, ly+6), lt, fill=(160, 190, 220), font=f_mono)
        c3_d.text((875, ly+6), lr, fill=(255, 255, 255), font=f_badge)
        c3_d.text((955, ly+6), lm, fill=(200, 220, 245), font=f_badge)
        c3_d.text((1045, ly+6), ls, fill=lc, font=f_badge)

    c3_d.text((796, 818), "CLOUD SYNC: ENCRYPTED • ZERO-TOUCH CHECK-IN READY", fill=(0, 255, 200), font=f_mono)

    base.paste(c3_layer, (0, 0), c3_layer)

    # 4. Master Outer Frame & Tech Corner Brackets
    border_draw = ImageDraw.Draw(base)
    border_draw.rectangle([0, 0, w-1, h-1], outline=(0, 210, 255, 190), width=2)
    corner_len = 36
    # Corners in bright cyan
    corners = [(0, 0, 1, 1), (w-1, 0, -1, 1), (0, h-1, 1, -1), (w-1, h-1, -1, -1)]
    for cx, cy, dx, dy in corners:
        border_draw.line([(cx, cy), (cx + dx * corner_len, cy)], fill=(0, 255, 255), width=4)
        border_draw.line([(cx, cy), (cx, cy + dy * corner_len)], fill=(0, 255, 255), width=4)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    base.save(output_path, quality=96)
    print(f"Successfully generated attractive hospitality visual at {output_path} ({w}x{h})")

if __name__ == '__main__':
    generate_attractive_hospitality_visual()
