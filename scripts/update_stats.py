from PIL import Image, ImageDraw, ImageFont
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# --- 📊 UPDATE YOUR STATS HERE 📊 ---
STATS = {
    "stat_pokedex.png": ("Caught", "550+", "LeetCode Questions"),
    "stat_kanto.png": ("Kanto BP", "1856", "LeetCode Rating"),
    "stat_sinnoh.png": ("Sinnoh BP", "1432", "Codeforces Rating"),
    "stat_hoenn.png": ("Hoenn BP", "1602", "CodeChef Rating")
}

HEADER_TEXT = "LEAGUE STATS"
HEADER_FILE = "header_league_stats.png"

# Config
FONT_PATH = os.path.join(ASSETS_DIR, "PokemonGb-RAeo.ttf")
FONT_HEADER = os.path.join(ASSETS_DIR, "Pokemon Solid.ttf")

# Colors
COLOR_BG = "#00000000"     # Transparent
COLOR_TEXT = "#FFFFFF"     # White
COLOR_SHADOW = "#000000"   # Black Drop Shadow

def draw_stat_badge(filename, label, value, subtext):
    # Width increased for subtext
    img = Image.new("RGBA", (250, 50), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    try:
        font_main = ImageFont.truetype(FONT_PATH, 20)
        font_sub = ImageFont.truetype(FONT_PATH, 10)
    except:
        font_main = ImageFont.load_default()
        font_sub = ImageFont.load_default()

    # Draw Main Stat (Value)
    text = f"{label}: {value}"
    draw.text((2, 2), text, font=font_main, fill=COLOR_SHADOW) # Shadow
    draw.text((0, 0), text, font=font_main, fill=COLOR_TEXT)   # Main

    # Draw Subtext (Platform)
    draw.text((2, 25), subtext, font=font_sub, fill="#DDDDDD")

    img.save(os.path.join(ASSETS_DIR, filename))
    print(f"Generated {filename}")

def generate_header():
    try:
        font = ImageFont.truetype(FONT_HEADER, 50)
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
    for fname, (label, val, sub) in STATS.items():
        draw_stat_badge(fname, label, val, sub)
    generate_header()
