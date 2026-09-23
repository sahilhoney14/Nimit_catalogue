import os
try:
    from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance  # type: ignore
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pillow'])
    from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance  # type: ignore

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR) if os.path.basename(SCRIPT_DIR) == 'tools' else SCRIPT_DIR

def generate_engaging_hospitality_composite(output_path=None):
    w, h = 1200, 896
    
    # 1. Base Canvas
    canvas = Image.new('RGB', (w, h), color=(10, 14, 26))
    
    # Load User Reference Image
    user_img_path = r'C:\Users\sahil\.gemini\antigravity-ide\brain\7c8d0df1-550f-4b35-bfeb-3d73301648c4\.user_uploaded\media_1789979802067.png'
    raw_ref = Image.open(user_img_path).convert('RGB')
    
    # Background: Upscaled Luxury Hotel Reception Desk
    # Crop clean lower half (reception desk, smiling receptionist, businessman, hotel signage)
    reception_crop = raw_ref.crop((0, 95, raw_ref.width, raw_ref.height - 20))
    # Resize to fill background with high-quality Lanczos
    bg_w = w
    bg_h = int(w * (reception_crop.height / reception_crop.width))
    bg_resized = reception_crop.resize((bg_w, bg_h), Image.Resampling.LANCZOS)
    
    # Enhance warmth, sharpness and contrast of hotel background
    enh_sharp = ImageEnhance.Sharpness(bg_resized).enhance(1.4)
    enh_color = ImageEnhance.Color(enh_sharp).enhance(1.15)
    enh_contrast = ImageEnhance.Contrast(enh_color).enhance(1.08)
    
    # Paste background at lower position
    paste_y = h - bg_resized.height + 20
    canvas.paste(enh_contrast, (0, paste_y))
    
    # Add dark cinematic gradient overlay at the top (to make floating cards stand out with deep contrast)
    overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    o_draw = ImageDraw.Draw(overlay)
    for y in range(h):
        # Dark at top (alpha 245), fading smoothly downwards over the hotel scene (alpha 30 at bottom)
        if y < 450:
            alpha = int(245 - (y / 450.0) * 110)
        else:
            alpha = int(135 - ((y - 450) / (h - 450.0)) * 115)
        o_draw.line([(0, y), (w, y)], fill=(8, 12, 24, alpha))
        
    canvas.paste(overlay, (0, 0), overlay)
    
    # Subtle cyber grid across top background
    grid_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    g_draw = ImageDraw.Draw(grid_layer)
    for gx in range(0, w, 40):
        g_draw.line([(gx, 0), (gx, 480)], fill=(0, 210, 255, 18), width=1)
    for gy in range(0, 480, 40):
        g_draw.line([(0, gy), (w, gy)], fill=(0, 210, 255, 18), width=1)
    canvas.paste(grid_layer, (0, 0), grid_layer)
    
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
            
    f_master = get_font('title', 19)
    f_card_h = get_font('title', 16)
    f_badge = get_font('title', 11)
    f_bold = get_font('bold', 13)
    f_reg = get_font('regular', 12)
    f_sm = get_font('regular', 11)
    f_mono = get_font('mono', 11)
    f_mono_lg = get_font('mono', 14)

    # 2. Master Top Header Bar
    top_bar = Image.new('RGBA', (w, 52), (8, 14, 28, 230))
    t_draw = ImageDraw.Draw(top_bar)
    t_draw.line([(0, 51), (w, 51)], fill=(0, 210, 255, 90), width=1)
    
    t_draw.ellipse([24, 18, 38, 32], fill=(0, 240, 255))
    t_draw.text((48, 15), "NIMIT AI // SMART HOSPITALITY & HOTEL OPERATIONS", fill=(255, 255, 255), font=f_master)
    
    # Status badges on right
    t_draw.rounded_rectangle([860, 10, 1005, 42], radius=6, fill=(15, 38, 60, 210), outline=(0, 210, 255, 140))
    t_draw.ellipse([872, 22, 880, 30], fill=(0, 255, 140))
    t_draw.text((888, 18), "HOTEL IoT: ONLINE", fill=(0, 255, 170), font=f_badge)
    
    t_draw.rounded_rectangle([1015, 10, 1165, 42], radius=6, fill=(35, 15, 25, 210), outline=(255, 80, 100, 140))
    t_draw.ellipse([1028, 22, 1036, 30], fill=(255, 75, 90))
    t_draw.text((1044, 18), "SMART SUITES: ACTIVE", fill=(255, 130, 145), font=f_badge)
    
    canvas.paste(top_bar, (0, 0), top_bar)
    
    # -------------------------------------------------------------------------
    # 3. THREE HERO CARDS: TOP-LEFT, TOP-CENTER, TOP-RIGHT
    # -------------------------------------------------------------------------
    
    # Helper to crop circular photo vignette
    def make_circular_photo(source_crop_box, target_size=(110, 110), border_color=(0, 220, 255)):
        raw_crop = raw_ref.crop(source_crop_box)
        resized = raw_crop.resize(target_size, Image.Resampling.LANCZOS)
        
        # Circular mask
        mask = Image.new('L', target_size, 0)
        m_draw = ImageDraw.Draw(mask)
        m_draw.ellipse([0, 0, target_size[0], target_size[1]], fill=255)
        
        out = Image.new('RGBA', target_size, (0, 0, 0, 0))
        out.paste(resized, (0, 0), mask)
        
        # Draw crisp circular border
        o_draw = ImageDraw.Draw(out)
        o_draw.ellipse([1, 1, target_size[0]-2, target_size[1]-2], outline=border_color, width=3)
        return out

    # PHOTO 1: Nurse Call Button in bedroom (from raw_ref ~ 10, 45 to 175, 170)
    nurse_photo = make_circular_photo((15, 50, 170, 165), target_size=(116, 116), border_color=(255, 80, 95))
    
    # PHOTO 2: IP-PBX VoIP Desk Phone (from raw_ref ~ 180, 80 to 345, 195)
    phone_photo = make_circular_photo((180, 85, 340, 190), target_size=(116, 116), border_color=(180, 100, 255))
    
    # PHOTO 3: Biometric Fingerprint Smart Lock (from raw_ref ~ 360, 35 to 475, 180)
    # Let's crop clean lock avoiding the top right bookmark area
    lock_photo = make_circular_photo((365, 45, 470, 175), target_size=(116, 116), border_color=(0, 230, 170))

    # Helper to draw glass card
    def draw_hero_card(x1, y1, x2, y2, photo_img, border_rgb, title_text, sub_text, badge_text, badge_rgb, telemetry_items=[]):
        # Soft Outer Glow
        glow = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        g_d = ImageDraw.Draw(glow)
        g_d.rounded_rectangle([x1-4, y1-4, x2+4, y2+4], radius=16, fill=(border_rgb[0], border_rgb[1], border_rgb[2], 30))
        glow = glow.filter(ImageFilter.GaussianBlur(12))
        canvas.paste(glow, (0, 0), glow)
        
        # Card Body
        card = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        c_d = ImageDraw.Draw(card)
        
        # Dark glass fill & neon border
        c_d.rounded_rectangle([x1, y1, x2, y2], radius=14, fill=(12, 18, 36, 230), outline=(border_rgb[0], border_rgb[1], border_rgb[2], 210), width=2)
        # Top metallic reflection line
        c_d.line([(x1+16, y1+2), (x2-16, y1+2)], fill=(255, 255, 255, 75), width=1)
        
        # Paste Circular Photo on Left side of card
        photo_x = x1 + 14
        photo_y = y1 + 16
        card.paste(photo_img, (photo_x, photo_y), photo_img)
        
        # Text & Details on Right side of card
        text_x = photo_x + photo_img.width + 16
        
        # Badge Pill
        badge_w = len(badge_text) * 8 + 18
        c_d.rounded_rectangle([text_x, y1+16, text_x+badge_w, y1+34], radius=4, fill=(badge_rgb[0], badge_rgb[1], badge_rgb[2], 45), outline=badge_rgb)
        c_d.text((text_x+9, y1+18), badge_text, fill=badge_rgb, font=f_badge)
        
        # Title
        c_d.text((text_x, y1+40), title_text, fill=(255, 255, 255), font=f_card_h)
        # Subtitle
        c_d.text((text_x, y1+62), sub_text, fill=(175, 195, 225), font=f_sm)
        
        # Telemetry pills below
        for ti, (t_label, t_val, t_col) in enumerate(telemetry_items):
            ty = y1 + 86 + ti * 22
            c_d.ellipse([text_x, ty+4, text_x+6, ty+10], fill=t_col)
            c_d.text((text_x+12, ty), f"{t_label}: ", fill=(160, 185, 215), font=f_mono)
            c_d.text((text_x+12 + len(t_label)*7 + 10, ty), t_val, fill=t_col, font=f_mono)
            
        canvas.paste(card, (0, 0), card)

    # -------------------------------------------------------------------------
    # CARD 1: NURSE / ATTENDANT CALLING SYSTEM (Left: 30, 68 to 395, 245)
    # -------------------------------------------------------------------------
    draw_hero_card(
        x1=30, y1=68, x2=395, y2=235,
        photo_img=nurse_photo,
        border_rgb=(255, 75, 90),
        title_text="Nurse / Attendant Call",
        sub_text="Bedside Touch SOS Panel",
        badge_text="EMERGENCY DISPATCH",
        badge_rgb=(255, 90, 105),
        telemetry_items=[
            ("STATUS", "SOS ACTIVE (BED 402)", (255, 80, 95)),
            ("RESPONSE", "< 00:01.2s", (0, 255, 180)),
            ("WARD HUB", "STATION 3A EN ROUTE", (0, 220, 255))
        ]
    )

    # -------------------------------------------------------------------------
    # CARD 2: UNIFIED COMMUNICATIONS PLATFORM (Center: 415, 68 to 785, 235)
    # -------------------------------------------------------------------------
    draw_hero_card(
        x1=415, y1=68, x2=785, y2=235,
        photo_img=phone_photo,
        border_rgb=(170, 95, 255),
        title_text="Unified Communications",
        sub_text="IP-PBX VoIP Master Desk",
        badge_text="HD VOICE MESH",
        badge_rgb=(190, 120, 255),
        telemetry_items=[
            ("TRUNKS", "64 / 64 ACTIVE SIP", (0, 255, 180)),
            ("ROUTING", "CONCIERGE -> SUITE 402", (255, 255, 255)),
            ("CODEC", "G.722 HD • 0.0% LOSS", (0, 220, 255))
        ]
    )

    # -------------------------------------------------------------------------
    # CARD 3: FINGER / CARD LOCK SYSTEM (Right: 805, 68 to 1170, 235)
    # -------------------------------------------------------------------------
    draw_hero_card(
        x1=805, y1=68, x2=1170, y2=235,
        photo_img=lock_photo,
        border_rgb=(0, 230, 170),
        title_text="Finger / Card Lock System",
        sub_text="Biometric Optical & RFID",
        badge_text="AES-256 ENCRYPTED",
        badge_rgb=(0, 240, 180),
        telemetry_items=[
            ("BIOMETRIC", "MATCH 99.8% (GUEST)", (0, 255, 150)),
            ("KEYCARD", "VIP NFC 13.56 MHz TAP", (0, 220, 255)),
            ("ENERGY", "AUTO-POWER ON INSERT", (255, 190, 40))
        ]
    )

    # -------------------------------------------------------------------------
    # 4. TRACER LINES & HUD CALLOUT CONNECTORS (Connecting Cards to Reception Scene)
    # -------------------------------------------------------------------------
    trace_layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    tr_d = ImageDraw.Draw(trace_layer)
    
    # Connecting line from Nurse Call (left card) down to guest/concierge
    tr_d.line([(210, 235), (210, 380), (320, 440)], fill=(255, 80, 95, 160), width=2)
    tr_d.ellipse([317, 437, 323, 443], fill=(255, 90, 105))
    
    # Connecting line from IP-PBX (center card) down to front desk
    tr_d.line([(600, 235), (600, 420), (660, 470)], fill=(180, 100, 255, 160), width=2)
    tr_d.ellipse([657, 467, 663, 473], fill=(190, 110, 255))
    
    # Connecting line from Biometric Lock (right card) down to guest keycard in hand
    tr_d.line([(990, 235), (990, 460), (480, 680)], fill=(0, 230, 170, 160), width=2)
    tr_d.ellipse([477, 677, 483, 683], fill=(0, 255, 180))
    
    # Floating Reception Telemetry HUD Box (Over Reception Desk)
    rec_box = (680, 360, 1150, 480)
    tr_d.rounded_rectangle(rec_box, radius=10, fill=(10, 18, 36, 210), outline=(0, 210, 255, 180), width=2)
    tr_d.text((695, 372), "SMART RECEPTION & GUEST CHECK-IN GATEWAY", fill=(0, 230, 255), font=f_badge)
    tr_d.text((695, 394), "Live Check-in • Digital Keycard Issuance • IoT Suite Automation", fill=(255, 255, 255), font=f_bold)
    tr_d.text((695, 418), "• Automated Keycard Encoding & RFID Room Assignment", fill=(180, 210, 240), font=f_sm)
    tr_d.text((695, 438), "• Instant PBX Guest Intercom Sync & Concierge Dispatch", fill=(180, 210, 240), font=f_sm)
    tr_d.text((695, 458), "• Smart Energy & Climate Welcome Scene (22°C Active)", fill=(0, 255, 180), font=f_mono)

    canvas.paste(trace_layer, (0, 0), trace_layer)

    # 5. Master Outer Frame & Tech Corner Brackets
    border_draw = ImageDraw.Draw(canvas)
    border_draw.rectangle([0, 0, w-1, h-1], outline=(0, 210, 255, 180), width=2)
    corner_len = 36
    corners = [(0, 0, 1, 1), (w-1, 0, -1, 1), (0, h-1, 1, -1), (w-1, h-1, -1, -1)]
    for cx, cy, dx, dy in corners:
        border_draw.line([(cx, cy), (cx + dx * corner_len, cy)], fill=(0, 255, 255), width=4)
        border_draw.line([(cx, cy), (cx, cy + dy * corner_len)], fill=(0, 255, 255), width=4)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    canvas.save(output_path, quality=96)
    print(f"Successfully generated engaging composite at {output_path} ({w}x{h})")

if __name__ == '__main__':
    generate_engaging_hospitality_composite()
