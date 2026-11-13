#!/usr/bin/env python3
"""Draw the 128x128 console examples for docs/small-screens.md.

Uses the console theme from tokens/tokens.json and the real console font
(minimal_font from the 32blit SDK), so the pictures show true pixels.

Run: python3 tools/console_mockups.py path/to/32blit-sdk/32blit/graphics/font.cpp
Needs Pillow. Writes PNGs to docs/assets/console/.
"""
import json
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "assets" / "console"
SIZE = 128

tokens = json.loads((ROOT / "tokens" / "tokens.json").read_text())
COLOUR = {name: c["value"] for name, c in tokens["color"].items()}
C = {role: COLOUR[name] for role, name in tokens["theme"]["console"].items()}


def load_font(path):
    """minimal_font: 96 glyphs from ' ', 6 column bytes each, bit 0 is the top row."""
    src = Path(path).read_text()
    table = lambda name: re.search(name + r"\[96\](?:\[6\])? = \{(.*?)\};", src, re.S).group(1)
    data = [int(x, 16) for x in re.findall(r"0x[0-9a-f]{2}", table("minimal_font_data"))]
    widths = [int(x) for x in re.findall(r"\d+", table("minimal_font_width"))]
    return data, widths


def text_width(font, s):
    return sum(font[1][ord(ch) - 32] for ch in s)


def text(img, font, xy, s, colour):
    data, widths = font
    x, y = xy
    for ch in s:
        glyph = ord(ch) - 32
        for col in range(6):
            bits = data[glyph * 6 + col]
            for row in range(8):
                if bits >> row & 1 and 0 <= x + col < SIZE and 0 <= y + row < SIZE:
                    img.putpixel((x + col, y + row), colour)
        x += widths[glyph]


def logo(size):
    """The logo drawn with hard pixels: its paths are straight-edged polygons."""
    svg = (ROOT / "logo" / "chilichip-logo.svg").read_text()
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Crop to the artwork (about 29..235 of the 256 box) so small sizes use every pixel.
    lo, hi = 26.0, 238.0
    scale = size / (hi - lo)
    for d, fill in re.findall(r'<path d="([^"]+)" fill="(#[0-9a-f]{6})"', svg):
        for sub in d.split("M")[1:]:
            nums = [float(n) for n in re.findall(r"-?\d+\.?\d*", sub)]
            pts = [((x - lo) * scale, (y - lo) * scale) for x, y in zip(nums[0::2], nums[1::2])]
            draw.polygon(pts, fill=fill)
    return img


def screen():
    img = Image.new("RGB", (SIZE, SIZE), C["bg"])
    return img, ImageDraw.Draw(img)


def status_bar(img, draw, font, title):
    text(img, font, (4, 2), title, _rgb(C["muted"]))
    draw.rectangle((112, 3, 121, 8), outline=C["muted"])
    draw.rectangle((122, 5, 122, 6), fill=C["muted"])
    draw.rectangle((114, 5, 118, 6), fill=C["success"])
    draw.line((0, 12, SIZE, 12), fill=C["line"])


def _rgb(hex_colour):
    h = hex_colour.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


def menu(font):
    img, draw = screen()
    status_bar(img, draw, font, "GAMES")
    rows = ["Space Fighters", "Chili Snake", "Tetris", "Minesweeper", "Game of Life", "Chili City"]
    for i, name in enumerate(rows):
        y = 16 + i * 16
        if i == 1:
            # Selected row: chili fill, dark text, and a marker so it does not rely on colour alone.
            draw.rectangle((0, y, SIZE - 1, y + 15), fill=C["accent"])
            draw.polygon([(0, y + 13), (SIZE - 1, y + 13), (SIZE - 1, y + 15), (0, y + 15)], fill=C["accent-shade"])
            text(img, font, (4, y + 3), ">", _rgb(C["on-accent"]))
            text(img, font, (12, y + 3), name, _rgb(C["on-accent"]))
        else:
            text(img, font, (12, y + 4), name, _rgb(C["text"]))
    text(img, font, (4, 116), "A open", _rgb(C["muted"]))
    text(img, font, (SIZE - 4 - text_width(font, "B back"), 116), "B back", _rgb(C["muted"]))
    return img


def dialog(font):
    img, draw = screen()
    status_bar(img, draw, font, "SAVES")
    for i, name in enumerate(["Slot 1  12:40", "Slot 2  03:15", "Slot 3  empty"]):
        text(img, font, (12, 20 + i * 16), name, _rgb(C["muted"]))
    # Panel with a hard offset shadow and one cut corner, like the facets of the logo.
    draw.rectangle((16, 40, 115, 99), fill=COLOUR["chili-deep"])
    draw.polygon([(12, 36), (105, 36), (111, 42), (111, 95), (12, 95)], fill=C["surface"], outline=C["line"])
    text(img, font, (20, 44), "Delete save?", _rgb(C["text"]))
    text(img, font, (20, 56), "Slot 2 will be", _rgb(C["muted"]))
    text(img, font, (20, 65), "gone for good.", _rgb(C["muted"]))
    draw.rectangle((20, 78, 59, 89), fill=C["accent"])
    draw.rectangle((20, 88, 59, 89), fill=C["accent-shade"])
    label = "Delete"
    text(img, font, (20 + (40 - text_width(font, label)) // 2, 80), label, _rgb(C["on-accent"]))
    draw.rectangle((64, 78, 103, 89), outline=C["muted"])
    label = "Keep"
    text(img, font, (64 + (40 - text_width(font, label)) // 2, 80), label, _rgb(C["text"]))
    return img


def splash(font):
    img, _ = screen()
    mark = logo(64)
    img.paste(mark, (32, 20), mark)
    label = "chilichip"
    text(img, font, ((SIZE - text_width(font, label)) // 2, 94), label, _rgb(C["text"]))
    return img


def palette(font):
    img, draw = screen()
    names = ["bg", "surface", "line", "muted", "text", "accent", "accent-shade", "success", "warning"]
    for i, role in enumerate(names):
        y = 2 + i * 14
        draw.rectangle((4, y, 27, y + 11), fill=C[role], outline=C["line"])
        text(img, font, (34, y + 2), role, _rgb(C["text"]))
    return img


if __name__ == "__main__":
    font = load_font(sys.argv[1])
    OUT.mkdir(parents=True, exist_ok=True)
    for name, img in {"menu": menu(font), "dialog": dialog(font), "splash": splash(font), "palette": palette(font)}.items():
        img.save(OUT / f"{name}.png")
    for size in (16, 32, 64):
        logo(size).save(OUT / f"logo-{size}.png")
    print(f"wrote {OUT.relative_to(ROOT)}")
