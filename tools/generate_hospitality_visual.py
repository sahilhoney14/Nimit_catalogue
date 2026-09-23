import os
import math
import random
try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter  # type: ignore
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow'])
    from PIL import Image, ImageDraw, ImageFont, ImageFilter  # type: ignore

def create_hospitality_visual(output_path=None):
    w, h = 1200, 900
    
    # Base Image
    img = Image.new('RGB', (w, h), color=(8, 12, 24))
    draw = ImageDraw.Draw(img)
    
    # 1. Background Gradient
    for y in range(h):
        ratio = y / h
        # Dark navy-slate to deep obsidian gradient with subtle cyan-blue tint in middle
        r = int(7 + 10 * math.sin(ratio * math.pi) * 0.5 + 4 * ratio)
        g = int(12 + 18 * math.sin(ratio * math.pi) * 0.8 + 6 * ratio)
        b = int(24 + 32 * math.sin(ratio * math.pi) * 1.0 + 12 * ratio)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
    
    # 2. Isometric / Perspective Cyber Grid in Background
    grid_img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    grid_draw = ImageDraw.Draw(grid_img)
    
    # Horizontal grid lines with perspective spacing
    for i in range(25):
        gy = 50 + int((i ** 1.35) * 28)
        if gy < h:
            alpha = int(20 + 35 * (gy / h))
            grid_draw.line([(0, gy), (w, gy)], fill=(30, 60, 110, alpha), width=1)
            
    # Vertical grid lines
    for gx in range(0, w, 50):
        grid_draw.line([(gx, 0), (gx, h)], fill=(25, 50, 95, 25), width=1)
        
    # Glowing Circuit Traces and Nodes
    random.seed(42)
    circuit_nodes = [
        (120, 80), (350, 80), (480, 140), (700, 80), (950, 80), (1100, 160),
        (80, 480), (220, 480), (600, 480), (820, 480), (1050, 480),
        (150, 850), (450, 850), (750, 850), (1020, 850)
    ]
    for i in range(len(circuit_nodes)-1):
        if random.random() > 0.3:
            p1 = circuit_nodes[i]
            p2 = circuit_nodes[i+1]
            grid_draw.line([p1, (p2[0], p1[1]), p2], fill=(0, 210, 255, 40), width=1)
            
    for pt in circuit_nodes:
        grid_draw.ellipse([pt[0]-3, pt[1]-3, pt[0]+3, pt[1]+3], fill=(0, 240, 255, 120))
        grid_draw.ellipse([pt[0]-6, pt[1]-6, pt[0]+6, pt[1]+6], outline=(0, 240, 255, 50), width=1)
        
    img.paste(grid_img, (0, 0), grid_img)
    
    # Fonts
    def get_font(name, size, bold=False):
        font_map = {
            'title': 'C:/Windows/Fonts/bahnschrift.ttf',
            'bold': 'C:/Windows/Fonts/segoeuib.ttf',
            'regular': 'C:/Windows/Fonts/segoeui.ttf',
            'mono': 'C:/Windows/Fonts/consola.ttf'
        }
        path = font_map.get(name, 'C:/Windows/Fonts/arial.ttf')
        try:
            return ImageFont.truetype(path, size)
        except Exception:
            return ImageFont.load_default()

    font_hdr = get_font('title', 20)
    font_subhdr = get_font('title', 15)
    font_badge = get_font('title', 11)
    font_bold = get_font('bold', 14)
    font_bold_lg = get_font('bold', 18)
    font_regular = get_font('regular', 13)
    font_sm = get_font('regular', 11)
    font_mono = get_font('mono', 12)
    font_mono_lg = get_font('mono', 18)
    
    # Helper to draw rounded glassmorphism card
    def draw_glass_card(box, border_color=(0, 200, 255, 160), bg_color=(12, 22, 42, 210), glow=True):
        x1, y1, x2, y2 = box
        card_w, card_h = x2 - x1, y2 - y1
        
        # Soft Glow
        if glow:
            glow_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
            glow_draw = ImageDraw.Draw(glow_layer)
            glow_draw.rounded_rectangle([x1-4, y1-4, x2+4, y2+4], radius=16, fill=(border_color[0], border_color[1], border_color[2], 25))
            glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(12))
            img.paste(glow_layer, (0, 0), glow_layer)
            
        # Card Body
        card_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        card_draw = ImageDraw.Draw(card_layer)
        
        # Fill
        card_draw.rounded_rectangle([x1, y1, x2, y2], radius=14, fill=bg_color)
        # Border
        card_draw.rounded_rectangle([x1, y1, x2, y2], radius=14, outline=border_color, width=2)
        # Inner top highlight
        card_draw.line([(x1+16, y1+2), (x2-16, y1+2)], fill=(255, 255, 255, 50), width=1)
        
        img.paste(card_layer, (0, 0), card_layer)

    # 3. Top Master Header Bar
    top_bar = Image.new('RGBA', (w, 54), (10, 18, 36, 230))
    top_draw = ImageDraw.Draw(top_bar)
    top_draw.line([(0, 53), (w, 53)], fill=(0, 210, 255, 80), width=1)
    
    # Top bar elements
    top_draw.ellipse([24, 20, 36, 32], fill=(0, 240, 255))
    top_draw.text((46, 17), "NIMIT AI // HOSPITALITY & SMART FACILITY PLATFORM", fill=(255, 255, 255), font=font_hdr)
    
    # Right Status Badges
    top_draw.rounded_rectangle([860, 12, 1010, 42], radius=8, fill=(15, 35, 60, 200), outline=(0, 210, 255, 120))
    top_draw.ellipse([872, 23, 880, 31], fill=(0, 255, 140))
    top_draw.text((888, 19), "SYSTEM: ONLINE", fill=(0, 255, 170), font=font_badge)
    
    top_draw.rounded_rectangle([1020, 12, 1170, 42], radius=8, fill=(35, 15, 25, 200), outline=(255, 70, 85, 120))
    top_draw.ellipse([1032, 23, 1040, 31], fill=(255, 75, 90))
    top_draw.text((1048, 19), "IoT NODES: ACTIVE", fill=(255, 120, 130), font=font_badge)
    
    img.paste(top_bar, (0, 0), top_bar)
    
    # -------------------------------------------------------------
    # PANEL 1: NURSE / ATTENDANT CALLING SYSTEM (Top Left: 30, 70 to 580, 480)
    # -------------------------------------------------------------
    p1_box = (30, 70, 580, 480)
    draw_glass_card(p1_box, border_color=(255, 90, 95, 180), bg_color=(15, 20, 38, 235))
    
    p1_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    p1_draw = ImageDraw.Draw(p1_layer)
    
    # Panel 1 Header
    p1_draw.rounded_rectangle([48, 86, 84, 122], radius=8, fill=(255, 60, 70, 40), outline=(255, 70, 85, 180), width=1)
    # Bell / SOS icon
    p1_draw.ellipse([58, 96, 74, 112], fill=(255, 70, 85))
    p1_draw.text((94, 88), "NURSE / ATTENDANT CALLING SYSTEM", fill=(255, 255, 255), font=font_hdr)
    p1_draw.text((94, 110), "Bedside SOS Console • Emergency Response • Ward Hub", fill=(170, 190, 220), font=font_sm)
    
    p1_draw.rounded_rectangle([460, 86, 562, 112], radius=6, fill=(255, 50, 70, 50), outline=(255, 80, 100, 160))
    p1_draw.text((472, 92), "LIVE DISPATCH", fill=(255, 100, 110), font=font_badge)
    
    # Divider
    p1_draw.line([(48, 132), (562, 132)], fill=(255, 255, 255, 30), width=1)
    
    # Sub-Visual 1: Bedside Call Station Hardware Mockup (Left side of panel)
    p1_draw.rounded_rectangle([50, 148, 270, 340], radius=12, fill=(20, 30, 52, 230), outline=(0, 210, 255, 140), width=2)
    # Screen header
    p1_draw.rounded_rectangle([60, 158, 260, 190], radius=6, fill=(10, 18, 35, 240), outline=(0, 180, 220, 80))
    p1_draw.ellipse([70, 170, 78, 178], fill=(0, 255, 140))
    p1_draw.text((86, 166), "BED STATION 402-A", fill=(0, 240, 255), font=font_bold)
    
    # Big glowing SOS Call Button
    sos_cx, sos_cy = 160, 250
    # Pulse rings
    p1_draw.ellipse([sos_cx-48, sos_cy-48, sos_cx+48, sos_cy+48], outline=(255, 60, 70, 70), width=2)
    p1_draw.ellipse([sos_cx-40, sos_cy-40, sos_cx+40, sos_cy+40], outline=(255, 70, 85, 130), width=2)
    # Button circle
    p1_draw.ellipse([sos_cx-32, sos_cy-32, sos_cx+32, sos_cy+32], fill=(235, 45, 60), outline=(255, 140, 150), width=3)
    p1_draw.text((sos_cx-17, sos_cy-10), "SOS", fill=(255, 255, 255), font=font_bold_lg)
    
    p1_draw.text((105, 308), "PULL CORD / TAP TO CALL", fill=(200, 220, 250), font=font_sm)
    
    # Sub-Visual 2: Ward Response Telemetry (Right side of panel)
    p1_draw.rounded_rectangle([285, 148, 562, 235], radius=10, fill=(12, 22, 42, 220), outline=(255, 80, 90, 120))
    p1_draw.text((300, 158), "ACTIVE ALARM TELEMETRY", fill=(255, 120, 130), font=font_subhdr)
    p1_draw.text((300, 182), "PRIORITY: EMERGENCY CALL", fill=(255, 255, 255), font=font_bold)
    p1_draw.text((300, 204), "RESPONSE TIME: 00:01.4s", fill=(0, 255, 180), font=font_mono)
    
    p1_draw.rounded_rectangle([450, 195, 550, 225], radius=6, fill=(0, 180, 100, 40), outline=(0, 255, 140, 140))
    p1_draw.text((460, 202), "NURSE ON WAY", fill=(0, 255, 150), font=font_badge)
    
    # Sub-Visual 3: Real-time Vital / Cardiac Wave Telemetry Strip
    p1_draw.rounded_rectangle([285, 248, 562, 340], radius=10, fill=(10, 18, 35, 240), outline=(0, 200, 255, 90))
    p1_draw.text((298, 256), "WARD VITAL & STATUS STREAM", fill=(0, 210, 255), font=font_sm)
    
    # Waveform line
    wave_pts = []
    base_y = 300
    for wx in range(298, 550, 4):
        phase = (wx - 298) / 250 * 4 * math.pi
        if 80 < (wx - 298) < 140:
            wy = base_y + int(24 * math.sin((wx-298)*0.2) * math.cos((wx-298)*0.08))
        else:
            wy = base_y + int(5 * math.sin(phase))
        wave_pts.append((wx, wy))
    for wi in range(len(wave_pts)-1):
        p1_draw.line([wave_pts[wi], wave_pts[wi+1]], fill=(0, 255, 170), width=2)
        
    p1_draw.text((298, 320), "BPM: 74  •  SPO2: 99%  •  TEMP: 36.8°C", fill=(180, 210, 240), font=font_mono)
    
    # Bottom Ward Room Matrix Indicators
    rooms = [("ROOM 401", "CLEAR", (0, 255, 140)), ("ROOM 402", "SOS ACTIVE", (255, 60, 70)), ("ROOM 403", "ATTENDING", (255, 180, 0)), ("ROOM 404", "IDLE", (100, 180, 255))]
    for idx, (rm, st, col) in enumerate(rooms):
        rx1 = 50 + idx * 130
        rx2 = rx1 + 120
        p1_draw.rounded_rectangle([rx1, 355, rx2, 460], radius=8, fill=(16, 26, 48, 220), outline=(col[0], col[1], col[2], 100), width=1)
        p1_draw.ellipse([rx1+10, 368, rx1+18, 376], fill=col)
        p1_draw.text((rx1+24, 364), rm, fill=(255, 255, 255), font=font_bold)
        p1_draw.text((rx1+12, 390), st, fill=col, font=font_badge)
        p1_draw.text((rx1+12, 412), "NODE: OK", fill=(140, 165, 195), font=font_sm)
        p1_draw.text((rx1+12, 432), f"LAT: {idx*0.2 + 0.8:.1f}ms", fill=(0, 210, 255), font=font_mono)

    img.paste(p1_layer, (0, 0), p1_layer)

    # -------------------------------------------------------------
    # PANEL 2: UNIFIED COMMUNICATIONS PLATFORM (Top Right: 600, 70 to 1170, 480)
    # -------------------------------------------------------------
    p2_box = (600, 70, 1170, 480)
    draw_glass_card(p2_box, border_color=(160, 90, 255, 180), bg_color=(16, 18, 42, 235))
    
    p2_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    p2_draw = ImageDraw.Draw(p2_layer)
    
    # Panel 2 Header
    p2_draw.rounded_rectangle([618, 86, 654, 122], radius=8, fill=(160, 70, 255, 40), outline=(170, 90, 255, 180), width=1)
    # Phone / PBX icon
    p2_draw.rounded_rectangle([628, 94, 644, 114], radius=3, fill=(180, 110, 255))
    p2_draw.ellipse([634, 102, 638, 106], fill=(255, 255, 255))
    p2_draw.text((664, 88), "UNIFIED COMMUNICATIONS PLATFORM", fill=(255, 255, 255), font=font_hdr)
    p2_draw.text((664, 110), "IP-PBX Master Trunk • SIP Intercom • Guest VoIP Mesh", fill=(190, 180, 230), font=font_sm)
    
    p2_draw.rounded_rectangle([1040, 86, 1152, 112], radius=6, fill=(140, 70, 255, 50), outline=(170, 100, 255, 160))
    p2_draw.text((1052, 92), "VoIP MASTER", fill=(200, 150, 255), font=font_badge)
    
    # Divider
    p2_draw.line([(618, 132), (1152, 132)], fill=(255, 255, 255, 30), width=1)
    
    # Sub-Visual 1: Enterprise IP-PBX Console Mockup (Left half of panel)
    p2_draw.rounded_rectangle([620, 148, 850, 340], radius=12, fill=(22, 26, 56, 230), outline=(160, 110, 255, 140), width=2)
    # Console Screen
    p2_draw.rounded_rectangle([632, 158, 838, 230], radius=8, fill=(10, 14, 32, 240), outline=(0, 210, 255, 100))
    p2_draw.text((642, 166), "IP-PBX HD TRUNK // CH-12", fill=(0, 240, 255), font=font_bold)
    p2_draw.text((642, 186), "CALL: RECEPTION -> SUITE 402", fill=(255, 255, 255), font=font_sm)
    p2_draw.text((642, 206), "DURATION: 02:45 • CODEC: G.722", fill=(0, 255, 170), font=font_mono)
    
    # Keypad & Speed Dial Grid
    for kr in range(3):
        for kc in range(4):
            kx1 = 636 + kc * 50
            ky1 = 242 + kr * 28
            p2_draw.rounded_rectangle([kx1, ky1, kx1+42, ky1+22], radius=4, fill=(30, 38, 76), outline=(100, 120, 190, 80))
            p2_draw.text((kx1+14, ky1+4), f"{kr*4+kc+1}", fill=(200, 220, 255), font=font_badge)
            
    # Sub-Visual 2: Multi-Band Audio Spectrum Visualizer (Top Right of panel)
    p2_draw.rounded_rectangle([865, 148, 1152, 240], radius=10, fill=(12, 18, 42, 220), outline=(160, 90, 255, 100))
    p2_draw.text((880, 158), "REAL-TIME VoIP AUDIO SPECTRUM", fill=(180, 150, 255), font=font_subhdr)
    
    # Equalizer bars
    eq_bars = [15, 28, 45, 62, 54, 70, 85, 92, 78, 65, 88, 50, 42, 68, 75, 58, 35, 20]
    for bi, bh in enumerate(eq_bars):
        bx = 880 + bi * 14
        by2 = 225
        by1 = by2 - int(bh * 0.45)
        # Bar color gradient from cyan to violet
        r_c = int(0 + (bi / len(eq_bars)) * 200)
        g_c = int(220 - (bi / len(eq_bars)) * 100)
        b_c = int(255)
        p2_draw.rounded_rectangle([bx, by1, bx+9, by2], radius=3, fill=(r_c, g_c, b_c))
        
    p2_draw.text((880, 228), "128 kbps STEREO • ZERO JITTER • 0.0% LOSS", fill=(0, 255, 200), font=font_mono)
    
    # Sub-Visual 3: SIP Mesh Routing Topology Diagram (Bottom Right of panel)
    p2_draw.rounded_rectangle([865, 252, 1152, 340], radius=10, fill=(10, 15, 36, 240), outline=(0, 200, 255, 90))
    p2_draw.text((880, 260), "SIP MULTI-POINT DISPATCH MESH", fill=(0, 210, 255), font=font_sm)
    
    mesh_nodes = [
        (900, 305, "PBX CORE"),
        (980, 290, "DESK IP"),
        (980, 320, "ROOM 402"),
        (1080, 305, "CONCIERGE")
    ]
    # Connect lines
    p2_draw.line([(900, 305), (980, 290)], fill=(0, 240, 255), width=2)
    p2_draw.line([(900, 305), (980, 320)], fill=(180, 100, 255), width=2)
    p2_draw.line([(980, 290), (1080, 305)], fill=(0, 255, 170), width=2)
    p2_draw.line([(980, 320), (1080, 305)], fill=(255, 190, 0), width=2)
    
    for nx, ny, nlabel in mesh_nodes:
        p2_draw.ellipse([nx-7, ny-7, nx+7, ny+7], fill=(0, 240, 255), outline=(255, 255, 255), width=1)
        p2_draw.text((nx-24, ny+9), nlabel, fill=(220, 235, 255), font=font_badge)
        
    # Bottom Communication Features Strip
    p2_features = [
        ("SIP TRUNKS", "64 / 64 ACTIVE", (0, 255, 180)),
        ("INTERCOM", "AUTO-ATTENDANT", (180, 120, 255)),
        ("CONFERENCING", "16 BRIDGES", (255, 180, 40)),
        ("PAGING/PA", "ALL ZONES OK", (0, 220, 255))
    ]
    for idx, (ft, val, col) in enumerate(p2_features):
        fx1 = 620 + idx * 135
        fx2 = fx1 + 125
        p2_draw.rounded_rectangle([fx1, 355, fx2, 460], radius=8, fill=(20, 26, 52, 220), outline=(col[0], col[1], col[2], 100), width=1)
        p2_draw.ellipse([fx1+10, 368, fx1+18, 376], fill=col)
        p2_draw.text((fx1+24, 364), ft, fill=(255, 255, 255), font=font_bold)
        p2_draw.text((fx1+12, 390), val, fill=col, font=font_badge)
        p2_draw.text((fx1+12, 412), "ENCRYPTION: ON", fill=(150, 175, 210), font=font_sm)
        p2_draw.text((fx1+12, 432), "UPTIME: 99.99%", fill=(0, 255, 170), font=font_mono)

    img.paste(p2_layer, (0, 0), p2_layer)

    # -------------------------------------------------------------
    # PANEL 3: FINGER / CARD LOCK SYSTEM (Bottom Full-Width: 30, 500 to 1170, 875)
    # -------------------------------------------------------------
    p3_box = (30, 500, 1170, 875)
    draw_glass_card(p3_box, border_color=(0, 230, 170, 180), bg_color=(12, 24, 38, 235))
    
    p3_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    p3_draw = ImageDraw.Draw(p3_layer)
    
    # Panel 3 Header
    p3_draw.rounded_rectangle([48, 516, 84, 552], radius=8, fill=(0, 220, 150, 40), outline=(0, 240, 170, 180), width=1)
    # Key / Lock icon
    p3_draw.rounded_rectangle([58, 528, 74, 544], radius=3, fill=(0, 240, 170))
    p3_draw.ellipse([63, 524, 69, 530], outline=(0, 240, 170), width=2)
    p3_draw.text((94, 518), "FINGER / CARD LOCK SYSTEM & ACCESS AUTOMATION", fill=(255, 255, 255), font=font_hdr)
    p3_draw.text((94, 540), "Optical Biometric Fingerprint • RFID/NFC Contactless Keycard • Room Energy Gateway", fill=(170, 210, 215), font=font_sm)
    
    p3_draw.rounded_rectangle([1020, 516, 1152, 542], radius=6, fill=(0, 200, 140, 50), outline=(0, 255, 170, 160))
    p3_draw.text((1032, 522), "SECURE AES-256", fill=(0, 255, 180), font=font_badge)
    
    # Divider
    p3_draw.line([(48, 560), (1152, 560)], fill=(255, 255, 255, 30), width=1)
    
    # Sub-Visual 1: Smart Biometric Handle & Optical Scanner (Left: 50 to 360)
    p3_draw.rounded_rectangle([50, 575, 370, 855], radius=12, fill=(16, 28, 46, 230), outline=(0, 230, 170, 140), width=2)
    p3_draw.text((66, 588), "BIOMETRIC FINGERPRINT SCANNER", fill=(0, 240, 180), font=font_subhdr)
    
    # Futuristic Biometric Fingerprint Graphic with glowing scan rings
    fp_cx, fp_cy = 135, 710
    # Scan rings
    p3_draw.ellipse([fp_cx-55, fp_cy-55, fp_cx+55, fp_cy+55], outline=(0, 230, 170, 50), width=2)
    p3_draw.ellipse([fp_cx-45, fp_cy-45, fp_cx+45, fp_cy+45], outline=(0, 240, 180, 110), width=2)
    p3_draw.ellipse([fp_cx-35, fp_cy-35, fp_cx+35, fp_cy+35], fill=(8, 32, 38), outline=(0, 255, 200), width=2)
    
    # Simulated fingerprint ridge curves
    for r_idx in range(10, 32, 4):
        p3_draw.arc([fp_cx-r_idx, fp_cy-r_idx, fp_cx+r_idx, fp_cy+r_idx], start=30, end=330, fill=(0, 255, 180), width=2)
    # Laser Scan line
    p3_draw.line([(fp_cx-40, fp_cy), (fp_cx+40, fp_cy)], fill=(255, 255, 255), width=2)
    
    # Scanner status indicators
    p3_draw.rounded_rectangle([210, 640, 355, 680], radius=6, fill=(0, 180, 120, 40), outline=(0, 255, 160, 140))
    p3_draw.text((220, 648), "MATCH: 99.8%", fill=(0, 255, 170), font=font_bold)
    p3_draw.text((220, 664), "USER: REGISTERED GUEST", fill=(200, 230, 240), font=font_badge)
    
    p3_draw.rounded_rectangle([210, 695, 355, 735], radius=6, fill=(0, 120, 200, 40), outline=(0, 200, 255, 140))
    p3_draw.text((220, 703), "LOCK: MOTORIZED", fill=(0, 220, 255), font=font_bold)
    p3_draw.text((220, 719), "STATE: UNLOCKED", fill=(0, 255, 180), font=font_badge)
    
    p3_draw.rounded_rectangle([210, 750, 355, 790], radius=6, fill=(180, 100, 255, 40), outline=(190, 120, 255, 140))
    p3_draw.text((220, 758), "SPEED: 0.28s", fill=(210, 160, 255), font=font_bold)
    p3_draw.text((220, 774), "ANTI-SPOOF: ACTIVE", fill=(220, 200, 255), font=font_badge)
    
    p3_draw.text((66, 818), "OPTICAL 508 DPI • CAPACITIVE LIVE SCAN", fill=(160, 200, 220), font=font_sm)
    
    # Sub-Visual 2: Contactless RFID / NFC Keycard & Energy Switch (Center: 390 to 760)
    p3_draw.rounded_rectangle([390, 575, 760, 855], radius=12, fill=(16, 28, 48, 230), outline=(0, 210, 255, 140), width=2)
    p3_draw.text((406, 588), "CONTACTLESS RFID / NFC SMART KEYCARD", fill=(0, 220, 255), font=font_subhdr)
    
    # Modern Keycard Mockup Graphic
    p3_draw.rounded_rectangle([415, 630, 610, 750], radius=10, fill=(20, 40, 75), outline=(0, 240, 255), width=2)
    # Card chip & branding
    p3_draw.rounded_rectangle([430, 645, 465, 672], radius=4, fill=(255, 190, 40), outline=(255, 220, 100))
    p3_draw.text((430, 688), "NIMIT AI VIP KEYCARD", fill=(255, 255, 255), font=font_bold)
    p3_draw.text((430, 708), "SUITE 402  •  PREMIUM", fill=(0, 230, 255), font=font_sm)
    p3_draw.text((430, 726), "NFC 13.56 MHz // MIFARE DESFire", fill=(170, 200, 230), font=font_badge)
    
    # NFC Waves radiating from card to Reader
    for arc_r in range(15, 65, 15):
        p3_draw.arc([600-arc_r, 680-arc_r, 600+arc_r, 680+arc_r], start=-60, end=60, fill=(0, 255, 180), width=2)
        
    # Reader Unit
    p3_draw.rounded_rectangle([660, 640, 745, 740], radius=8, fill=(10, 18, 35), outline=(0, 255, 180), width=2)
    p3_draw.ellipse([695, 665, 710, 680], fill=(0, 255, 180))
    p3_draw.text((672, 695), "TAP CARD", fill=(255, 255, 255), font=font_badge)
    p3_draw.text((672, 715), "HERE >>>", fill=(0, 240, 255), font=font_badge)
    
    # Energy Switch automation strip
    p3_draw.rounded_rectangle([415, 770, 745, 840], radius=8, fill=(10, 20, 38), outline=(0, 200, 255, 100))
    p3_draw.ellipse([430, 792, 442, 804], fill=(255, 190, 0))
    p3_draw.text((452, 782), "INTELLIGENT KEYCARD ENERGY SAVER", fill=(255, 255, 255), font=font_bold)
    p3_draw.text((452, 804), "AUTOMATED LIGHTING, HVAC (22°C) & POWER ON INSERTION", fill=(0, 255, 180), font=font_sm)

    # Sub-Visual 3: Real-Time Access Audit Logs & Cloud Synced Telemetry (Right: 780 to 1150)
    p3_draw.rounded_rectangle([780, 575, 1150, 855], radius=12, fill=(14, 22, 40, 230), outline=(0, 210, 255, 140), width=2)
    p3_draw.text((796, 588), "LIVE ACCESS AUDIT LOGS & CLOUD SYNC", fill=(0, 210, 255), font=font_subhdr)
    
    # Audit Log entries
    log_entries = [
        ("13:58:24", "SUITE 402", "BIOMETRIC AUTH", "ACCESS GRANTED", (0, 255, 150)),
        ("13:58:26", "SUITE 402", "ENERGY SWITCH", "POWER ACTIVE", (255, 190, 0)),
        ("13:42:10", "ROOM 305", "RFID VIP TAP", "ACCESS GRANTED", (0, 255, 150)),
        ("13:30:15", "ROOM 208", "CLEANING STAFF", "MAID MASTER CARD", (180, 130, 255)),
        ("13:15:02", "SUITE 501", "MOBILE NFC APP", "DIGITAL KEY OK", (0, 220, 255)),
        ("12:59:44", "ROOM 104", "DOOR SENSOR", "DOOR CLOSED & SECURED", (140, 220, 180))
    ]
    
    for li, (lt, lr, lm, ls, lc) in enumerate(log_entries):
        ly = 625 + li * 34
        # alternating background
        p3_draw.rounded_rectangle([796, ly, 1135, ly+28], radius=5, fill=(20, 30, 52, 180), outline=(lc[0], lc[1], lc[2], 60))
        p3_draw.text((806, ly+6), lt, fill=(160, 190, 220), font=font_mono)
        p3_draw.text((875, ly+6), lr, fill=(255, 255, 255), font=font_badge)
        p3_draw.text((955, ly+6), lm, fill=(200, 220, 245), font=font_badge)
        p3_draw.text((1045, ly+6), ls, fill=lc, font=font_badge)

    p3_draw.text((796, 832), "CLOUD SYNC: ENCRYPTED • ZERO-TOUCH CHECK-IN READY", fill=(0, 255, 200), font=font_mono)

    img.paste(p3_layer, (0, 0), p3_layer)

    # 4. Final Polish - Holographic Border Frame
    border_draw = ImageDraw.Draw(img)
    border_draw.rectangle([0, 0, w-1, h-1], outline=(0, 210, 255, 180), width=2)
    # Corner Accents
    corner_len = 30
    # Top Left
    border_draw.line([(0, 0), (corner_len, 0)], fill=(0, 255, 255), width=4)
    border_draw.line([(0, 0), (0, corner_len)], fill=(0, 255, 255), width=4)
    # Top Right
    border_draw.line([(w-1, 0), (w-1-corner_len, 0)], fill=(0, 255, 255), width=4)
    border_draw.line([(w-1, 0), (w-1, corner_len)], fill=(0, 255, 255), width=4)
    # Bottom Left
    border_draw.line([(0, h-1), (corner_len, h-1)], fill=(0, 255, 255), width=4)
    border_draw.line([(0, h-1), (0, h-1-corner_len)], fill=(0, 255, 255), width=4)
    # Bottom Right
    border_draw.line([(w-1, h-1), (w-1-corner_len, h-1)], fill=(0, 255, 255), width=4)
    border_draw.line([(w-1, h-1), (w-1, h-1-corner_len)], fill=(0, 255, 255), width=4)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, quality=95)
    print(f"Successfully generated high-fidelity visual at {output_path} ({w}x{h})")

if __name__ == '__main__':
    create_hospitality_visual()
