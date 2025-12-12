import os

# Config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

OUTPUT_FILE = os.path.join(ASSETS_DIR, "pokedex_bug.png")
FONT_PATH = os.path.join(ASSETS_DIR, "PokemonGb-RAeo.ttf")
TEXT = "There is\nsome bugs,\nGotta Solve\n'Em All!"

# Colors
COLOR_RED = "#DC0A2D"
COLOR_DARK_RED = "#8B0000"
COLOR_SCREEN_BG = "#51AD60" # Gameboy Green
COLOR_SCREEN_DARK = "#2B5C33"
COLOR_BLUE_LENS = "#28AAFD"

def draw_pokedex():
    width = 400  # Widen to 400
    height = 550
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 1. Main Body (Red) - Wider
    draw.rounded_rectangle([10, 60, 390, 540], radius=20, fill=COLOR_RED, outline=COLOR_DARK_RED, width=5)
    
    # Top part
    draw.polygon([(10, 60), (10, 10), (160, 10), (190, 40), (390, 40), (390, 60)], fill=COLOR_RED, outline=COLOR_DARK_RED)
    draw.line([(10, 60), (390, 60)], fill=COLOR_RED, width=4) 

    # 2. Blue Lens (Top Left)
    draw.ellipse([30, 15, 80, 65], fill=COLOR_BLUE_LENS, outline="white", width=3)
    draw.ellipse([40, 25, 55, 40], fill="white")

    # 3. Small LEDs - Shifted Right
    draw.ellipse([260, 20, 275, 35], fill="red", outline="black")
    draw.ellipse([290, 20, 305, 35], fill="yellow", outline="black")
    draw.ellipse([320, 20, 335, 35], fill="lime", outline="black")

    # 4. The Screen Area - Wider
    draw.rounded_rectangle([40, 100, 360, 350], radius=10, fill="#DEDEDE", outline="#555555", width=3)

    # 5. The Actual Screen - Wider
    screen_rect = [60, 120, 340, 310]
    draw.rectangle(screen_rect, fill=COLOR_SCREEN_BG, outline=COLOR_SCREEN_DARK, width=3)

    # 6. D-Pad and Buttons
    # D-Pad (Left aligned, same)
    dpad_x, dpad_y = 60, 420
    draw.rectangle([dpad_x + 30, dpad_y, dpad_x + 60, dpad_y + 90], fill="#222", outline="black")
    draw.rectangle([dpad_x, dpad_y + 30, dpad_x + 90, dpad_y + 60], fill="#222", outline="black")
    
    # A/B Buttons (Shifted Right)
    draw.ellipse([300, 430, 340, 470], fill="#222", outline="black")

    # 7. Text
    try:
        font = ImageFont.truetype(FONT_PATH, 25) # Reduced font size for better fit
    except:
        font = ImageFont.load_default()
        print("Default font loaded")

    # Draw text centered in the screen_rect
    dummy = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
    bbox = dummy.multiline_textbbox((0, 0), TEXT, font=font, align="center")
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    
    screen_center_x = (screen_rect[0] + screen_rect[2]) // 2
    screen_center_y = (screen_rect[1] + screen_rect[3]) // 2
    
    # Draw text
    draw.multiline_text((screen_center_x - text_w // 2, screen_center_y - text_h // 2), 
                        TEXT, font=font, fill=COLOR_SCREEN_DARK, align="center", spacing=4)

    img.save(OUTPUT_FILE)
    print(f"Generated {OUTPUT_FILE}")

if __name__ == "__main__":
    draw_pokedex()
