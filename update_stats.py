from PIL import Image, ImageDraw, ImageFont
import os

# --- 🛠️ UPDATE YOUR STATS HERE 🛠️ ---
# Format: "Main Text (Number)" : "Subtext (Reference)"
STATS = {
    "stat_pokedex.png": ("Caught: 550+", "LeetCode Questions"),
    "stat_kanto.png":   ("Kanto: 1650 BP", "LeetCode Rating"),
    "stat_sinnoh.png":  ("Sinnoh: 1229 BP", "Codeforces Rating"),
    "stat_hoenn.png":   ("Hoenn: 1550+ BP", "CodeChef Rating")
}

# --- HEADER GENERATION (Single One) ---
HEADER_TEXT = "LEAGUE STATS"
HEADER_FILE = "header_league_stats.png"
# ----------------------------------------

# Configuration
FONT_STATS = "assets/PokemonGb-RAeo.ttf" # New Pokedex Font
FONT_HEADER = "assets/Pokemon Solid.ttf" # Standard Header Font

# Stats Config
STAT_FONT_SIZE_MAIN = 20
STAT_FONT_SIZE_SUB = 12
STAT_TEXT_COLOR = "#FFFFFF" # White for Pokedex style text
STAT_PADDING = 10

# Header Config
HEADER_FONT_SIZE = 80
HEADER_TEXT_COLOR = "#FFCB05" 
HEADER_STROKE_COLOR = "#3C5AA6"
HEADER_STROKE_WIDTH = 5

def generate_stat_image(filename, main_text, sub_text):
    try:
        font_main = ImageFont.truetype(FONT_STATS, STAT_FONT_SIZE_MAIN)
        font_sub = ImageFont.truetype(FONT_STATS, STAT_FONT_SIZE_SUB)
    except IOError:
        print(f"⚠️ Could not load stat font at {FONT_STATS}")
        return

    # Calculate sizes
    dummy = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
    bbox_main = dummy.textbbox((0, 0), main_text, font=font_main)
    bbox_sub = dummy.textbbox((0, 0), sub_text, font=font_sub)
    
    w_main = bbox_main[2] - bbox_main[0]
    h_main = bbox_main[3] - bbox_main[1]
    w_sub = bbox_sub[2] - bbox_sub[0]
    h_sub = bbox_sub[3] - bbox_sub[1]

    width = max(w_main, w_sub) + STAT_PADDING * 2
    height = h_main + h_sub + STAT_PADDING * 2 + 5 # 5px spacing

    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Draw Main Text (Black Pokedex style)
    draw.text((STAT_PADDING, STAT_PADDING), main_text, font=font_main, fill=STAT_TEXT_COLOR)
    
    # Draw Sub Text (Smaller)
    draw.text((STAT_PADDING, STAT_PADDING + h_main + 5), sub_text, font=font_sub, fill=STAT_TEXT_COLOR)

    img.save(f"assets/{filename}")
    print(f"✅ Updated Stat: {filename}")

def generate_header_image():
    try:
        font = ImageFont.truetype(FONT_HEADER, HEADER_FONT_SIZE)
    except IOError:
        print(f"⚠️ Could not load header font at {FONT_HEADER}")
        return

    dummy = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
    bbox = dummy.textbbox((0, 0), HEADER_TEXT, font=font)
    width = (bbox[2] - bbox[0]) + 40
    height = (bbox[3] - bbox[1]) + 40

    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    draw.text((20, 20), HEADER_TEXT, font=font, fill=HEADER_TEXT_COLOR, stroke_width=HEADER_STROKE_WIDTH, stroke_fill=HEADER_STROKE_COLOR)
    
    img.save(f"assets/{HEADER_FILE}")
    print(f"✅ Updated Header: {HEADER_FILE}")

if __name__ == "__main__":
    print("⚡ Updating League Stats...")
    # Generate Stats
    for fname, (main, sub) in STATS.items():
        generate_stat_image(fname, main, sub)
    
    # Generate Header
    generate_header_image()
    
    print("🎉 All assets updated!")
