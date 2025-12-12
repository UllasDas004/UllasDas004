from PIL import Image, ImageDraw, ImageFont
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# --- 🌱🔥💧 UPDATE SOCIALS HERE 💧🔥🌱 ---
SOCIALS = {
    "social_grass.png": ("Grass Type", "EMAIL", "ullasdas004@gmail.com", "#7AC74C", "#4E8234"),
    "social_fire.png": ("Fire Type", "LINKEDIN", "linkedin.com/in/ullas-das", "#EE8130", "#9C531F"),
    "social_water.png": ("Water Type", "INSTAGRAM", "instagram.com/ullasdas", "#6390F0", "#445E9C")
}

HEADER_TEXT = "CHOOSE YOUR STARTER"
HEADER_FILE = "header_socials.png"

# Config
FONT_TEXT = os.path.join(ASSETS_DIR, "PokemonGb-RAeo.ttf")
FONT_HEADER = os.path.join(ASSETS_DIR, "Pokemon Solid.ttf")
COLOR_BG = "#383838"      
COLOR_TEXT = "#FFFFFF"    

def draw_social_card(filename, type_name, label, value, color_primary, color_dark):
    width = 250
    height = 100
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Main Box
    draw.rounded_rectangle([0, 0, width, height], radius=10, fill=COLOR_BG, outline=color_primary, width=4)

    try:
        font_type = ImageFont.truetype(FONT_TEXT, 10)
        font_label = ImageFont.truetype(FONT_TEXT, 16)
        font_val = ImageFont.truetype(FONT_TEXT, 8)
    except:
        font_type = ImageFont.load_default()
        font_label = ImageFont.load_default()
        font_val = ImageFont.load_default()

    # Decor: Pokeball simplified
    draw.ellipse([width-40, -10, width+10, 40], fill=color_dark)
    
    # Type Label (Top Left)
    draw.text((15, 10), type_name, font=font_type, fill=color_primary)

    # Main Label (Center)
    draw.text((15, 35), label, font=font_label, fill=COLOR_TEXT)

    # Value/Handle (Bottom)
    draw.text((15, 70), value, font=font_val, fill="#AAAAAA")

    # Type Icon (Simulated with simple shapes)
    cx, cy = width - 30, height - 30
    draw.ellipse([cx-15, cy-15, cx+15, cy+15], fill=color_primary) 
    # Just a colored dot to represent the type energy

    img.save(os.path.join(ASSETS_DIR, filename))
    print(f"Generated {filename}")

def generate_header():
    try:
        font = ImageFont.truetype(FONT_HEADER, 60)
    except: return

    dummy = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
    bbox = dummy.textbbox((0, 0), HEADER_TEXT, font=font)
    width = (bbox[2] - bbox[0]) + 40
    height = (bbox[3] - bbox[1]) + 40

    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.text((20, 20), HEADER_TEXT, font=font, fill="#FFCB05", stroke_width=4, stroke_fill="#3C5AA6")
    
    img.save(os.path.join(ASSETS_DIR, HEADER_FILE))
    print(f"Generated {HEADER_FILE}")

if __name__ == "__main__":
    for fname, data in SOCIALS.items():
        draw_social_card(fname, *data)
    generate_header()
