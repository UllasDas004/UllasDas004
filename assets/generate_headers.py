from PIL import Image, ImageDraw, ImageFont
import os

# Configuration
FONT_PATH = "Pokemon Solid.ttf"
FONT_SIZE = 80
TEXT_COLOR = "#FFCB05"
STROKE_COLOR = "#3C5AA6"
STROKE_WIDTH = 5
PADDING = 20

headers = {
    "header_badges.png": "GYM BADGES",
    "header_moveset.png": "MOVESET",
    "header_stats.png": "BATTLE STATS",
    "header_snake.png": "ADVENTURE LOG",
    "header_terminal.png": "POKEDEX TERMINAL"
}

def generate_header(filename, text):
    try:
        font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    except IOError:
        print(f"Could not load font at {FONT_PATH}")
        return

    # Calculate text size using textbbox (for newer Pillow versions)
    dummy_img = Image.new('RGBA', (1, 1))
    draw = ImageDraw.Draw(dummy_img)
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # image dimensions
    width = text_width + PADDING * 2
    height = text_height + PADDING * 2 + 20 # Extra height for safety

    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Position
    x = PADDING
    y = PADDING

    # Draw Stroke (Draw text at offsets)
    # Using pillow's builtin stroke_width feature if available, else manual offset
    draw.text((x, y), text, font=font, fill=TEXT_COLOR, stroke_width=STROKE_WIDTH, stroke_fill=STROKE_COLOR)

    print(f"Saving {filename}...")
    img.save(filename)

if __name__ == "__main__":
    for fname, text in headers.items():
        generate_header(fname, text)
