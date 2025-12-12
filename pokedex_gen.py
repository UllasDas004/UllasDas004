from PIL import Image, ImageDraw, ImageFont

# Config
OUTPUT_FILE = "assets/pokedex_bug.png"
FONT_PATH = "assets/PokemonGb-RAeo.ttf"
TEXT = "There is a bug,\nGotta Solve 'Em All!!!"

# Colors
COLOR_RED = "#DC0A2D"
COLOR_DARK_RED = "#8B0000"
COLOR_SCREEN_BG = "#51AD60" # Gameboy Green
COLOR_SCREEN_DARK = "#2B5C33"
COLOR_BLUE_LENS = "#28AAFD"

def draw_pokedex():
    width = 400
    height = 300
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 1. Main Body (Red)
    # Shape: Polygon for the cut corner? Or just a rounded rect.
    # Let's do a simple rounded rect style
    draw.rounded_rectangle([10, 50, 390, 290], radius=20, fill=COLOR_RED, outline=COLOR_DARK_RED, width=5)
    
    # Top Top part (The camera/lens part)
    # This is usually a bit higher on the left
    draw.rounded_rectangle([10, 10, 390, 60], radius=10, fill=COLOR_RED, outline=COLOR_DARK_RED, width=5)

    # 2. Blue Lens (Top Left)
    draw.ellipse([30, 20, 80, 70], fill=COLOR_BLUE_LENS, outline="white", width=3)
    # Reflection
    draw.ellipse([45, 30, 60, 45], fill="white")

    # 3. Small LEDs (Red/Yellow/Green)
    draw.ellipse([100, 25, 115, 40], fill="red", outline="black")
    draw.ellipse([125, 25, 140, 40], fill="yellow", outline="black")
    draw.ellipse([150, 25, 165, 40], fill="lime", outline="black")

    # 4. The Screen Area (Grey/White Container)
    draw.rounded_rectangle([40, 90, 360, 250], radius=10, fill="#DEDEDE", outline="#555555", width=3)

    # 5. The Actual Screen (Green)
    draw.rectangle([60, 110, 340, 230], fill=COLOR_SCREEN_BG, outline=COLOR_SCREEN_DARK, width=3)

    # 6. Text
    try:
        font = ImageFont.truetype(FONT_PATH, 20)
    except:
        font = ImageFont.load_default()
        print("Default font loaded")

    # Center text
    dummy = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
    bbox = dummy.textbbox((0, 0), TEXT, font=font, align="center")
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    screen_center_x = 60 + (340 - 60) // 2
    screen_center_y = 110 + (230 - 110) // 2
    
    draw.text((screen_center_x - text_w // 2, screen_center_y - text_h // 2), TEXT, font=font, fill=COLOR_SCREEN_DARK, align="center")

    img.save(OUTPUT_FILE)
    print(f"Generated {OUTPUT_FILE}")

if __name__ == "__main__":
    draw_pokedex()
