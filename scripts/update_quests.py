from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# --- 🗺️ UPDATE YOUR QUESTS HERE 🗺️ ---
# Format: "Filename": ("Title", "Description", ["Tech"], "Level")
QUESTS_DSA = {
    "quest_cp_1.png": ("TLE Eliminator", "CP31 Sheet Solutions.", ["CP", "Math", "Logic"], "Lv. 40"),
    "quest_cp_2.png": ("DSA with C++", "Mastering Data Structures.", ["C++", "STL", "Algos"], "Lv. 30"),
    "quest_cp_3.png": ("CSES Problem Set", "Solving hard problems.", ["C++", "DP", "Graphs"], "Lv. 50")
}

QUESTS_BACKEND = {
    "quest_be_1.png": ("FastAPI Service", "High performance backend.", ["Python", "FastAPI"], "Lv. 20")
}

QUESTS_ML = {
    "quest_ml_1.png": ("ML Model Training", "Predictive analysis models.", ["Python", "Scikit-Learn"], "Lv. 15")
}

CATEGORIES = {
    "DSA & CP": (QUESTS_DSA, "header_cat_dsa.png"),
    "Backend Dev": (QUESTS_BACKEND, "header_cat_backend.png"),
    "Machine Learning": (QUESTS_ML, "header_cat_ml.png")
}

# Config
FONT_TEXT = os.path.join(ASSETS_DIR, "PokemonGb-RAeo.ttf")
FONT_HEADER = os.path.join(ASSETS_DIR, "Pokemon Solid.ttf")

# Colors
COLOR_BG = "#383838"      
COLOR_BORDER = "#A8A8A8"  
COLOR_TITLE = "#FFCB05"   
COLOR_TEXT = "#FFFFFF"    
COLOR_ACCENT = "#3C5AA6"  

def draw_quest_card(filename, title, desc, techs, level):
    width = 800  # Wide Banner
    height = 140
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Main Box
    draw.rounded_rectangle([0, 0, width, height], radius=10, fill=COLOR_BG, outline=COLOR_BORDER, width=4)

    try:
        font_title = ImageFont.truetype(FONT_TEXT, 24)
        font_desc = ImageFont.truetype(FONT_TEXT, 16)
        font_small = ImageFont.truetype(FONT_TEXT, 14)
    except:
        font_title = ImageFont.load_default()
        font_desc = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Title
    draw.text((20, 15), title, font=font_title, fill=COLOR_TITLE)

    # Level (Right aligned)
    bbox = draw.textbbox((0, 0), level, font=font_title)
    w = bbox[2] - bbox[0]
    draw.text((width - w - 20, 15), level, font=font_title, fill=COLOR_TEXT)

    # Description (Wrapped)
    # Simple wrap logic or just truncate if too long? 
    # Let's wrap manually
    lines = textwrap.wrap(desc, width=60) # Adjust char width based on font
    y_text = 55
    for line in lines[:2]: # Max 2 lines
        draw.text((20, y_text), line, font=font_desc, fill=COLOR_TEXT)
        y_text += 25

    # Tech Stack (Bottom)
    tech_str = "Loot: " + ", ".join(techs)
    draw.text((20, height - 30), tech_str, font=font_small, fill=COLOR_ACCENT)

    img.save(os.path.join(ASSETS_DIR, filename))
    print(f"Generated {filename}")

def generate_header(text, filename):
    try:
        font = ImageFont.truetype(FONT_HEADER, 60) # Smaller header for sub-sections
    except: return

    dummy = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
    bbox = dummy.textbbox((0, 0), text, font=font)
    width = (bbox[2] - bbox[0]) + 40
    height = (bbox[3] - bbox[1]) + 40

    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.text((20, 20), text, font=font, fill=COLOR_TITLE, stroke_width=4, stroke_fill=COLOR_ACCENT)
    
    img.save(os.path.join(ASSETS_DIR, filename))
    print(f"Generated {filename}")

if __name__ == "__main__":
    for cat_name, (quests, header_file) in CATEGORIES.items():
        print(f"Processing Category: {cat_name}")
        generate_header(cat_name, header_file)
        for fname, data in quests.items():
            draw_quest_card(fname, *data)
    generate_header("TRAINER LEAGUE CARD", "header_trainer_card.png")
    generate_header("TRAINER INFO", "header_trainer_info.png")
