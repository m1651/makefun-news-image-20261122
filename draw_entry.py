#!/usr/bin/env python3
"""Draw entry.png: one image summing up the world news of Sunday, 22 Nov 2026.

Build tool only (run locally with PIL). The graded program is main.py,
which copies the finished entry.png to /output/entry.png with stdlib only.
Layout: 1024x1024, navy header with the date, then a 2x3 grid of stories,
each with a hand-drawn pictogram, a headline and a short factual label.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BASE = os.path.dirname(os.path.abspath(__file__))

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def pic_tanker(d, x, y, s):
    d.rectangle([x, y + s * 0.62, x + s, y + s * 0.78], fill="#1F6FB2")
    d.rectangle([x, y + s * 0.78, x + s, y + s * 0.86], fill="#155A8A")
    d.polygon([(x + s * 0.08, y + s * 0.62), (x + s * 0.92, y + s * 0.62),
               (x + s * 0.84, y + s * 0.78), (x + s * 0.16, y + s * 0.78)],
              fill="#263238")
    for i, c in enumerate(("#E8B84B", "#C0392B", "#2E7D6B")):
        d.rectangle([x + s * (0.18 + i * 0.22), y + s * 0.38,
                     x + s * (0.36 + i * 0.22), y + s * 0.60], fill=c)
    d.rectangle([x + s * 0.70, y + s * 0.30, x + s * 0.86, y + s * 0.60],
                fill="#ECEFF1")
    d.polygon([(x + s * 0.22, y + s * 0.38), (x + s * 0.30, y + s * 0.10),
               (x + s * 0.38, y + s * 0.38)], fill="#F57C00")


def pic_bitcoin(d, x, y, s):
    d.ellipse([x + s * 0.08, y + s * 0.06, x + s * 0.92, y + s * 0.90],
              fill="#F7931A")
    f = font(SANS_B, int(s * 0.52))
    d.text((x + s * 0.5, y + s * 0.48), "B", font=f, fill="white",
           anchor="mm")
    d.line([(x + s * 0.06, y + s * 0.92), (x + s * 0.35, y + s * 0.72),
            (x + s * 0.55, y + s * 0.84), (x + s * 0.94, y + s * 0.62)],
           fill="#C0392B", width=6)
    d.polygon([(x + s * 0.94, y + s * 0.62), (x + s * 0.80, y + s * 0.60),
               (x + s * 0.94, y + s * 0.74)], fill="#C0392B")


def pic_badge(d, x, y, s):
    d.polygon([(x + s * 0.5, y + s * 0.04), (x + s * 0.92, y + s * 0.22),
               (x + s * 0.86, y + s * 0.72), (x + s * 0.5, y + s * 0.96),
               (x + s * 0.14, y + s * 0.72), (x + s * 0.08, y + s * 0.22)],
              fill="#B8860B")
    d.polygon([(x + s * 0.5, y + s * 0.14), (x + s * 0.82, y + s * 0.28),
               (x + s * 0.77, y + s * 0.68), (x + s * 0.5, y + s * 0.86),
               (x + s * 0.23, y + s * 0.68), (x + s * 0.18, y + s * 0.28)],
              fill="#F5D76E")
    f = font(SANS_B, int(s * 0.30))
    d.text((x + s * 0.5, y + s * 0.50), "*", font=f, fill="#7A5C00",
           anchor="mm")


def pic_globe(d, x, y, s):
    d.ellipse([x + s * 0.06, y + s * 0.06, x + s * 0.94, y + s * 0.94],
              fill="#2E7D6B")
    d.ellipse([x + s * 0.22, y + s * 0.20, x + s * 0.48, y + s * 0.42],
              fill="#7CB342")
    d.ellipse([x + s * 0.55, y + s * 0.52, x + s * 0.82, y + s * 0.78],
              fill="#7CB342")
    d.ellipse([x + s * 0.58, y + s * 0.16, x + s * 0.74, y + s * 0.30],
              fill="#7CB342")
    d.arc([x + s * 0.06, y + s * 0.06, x + s * 0.94, y + s * 0.94],
          200, 340, fill="#E8B84B", width=5)


def pic_card(d, x, y, s):
    d.rounded_rectangle([x + s * 0.04, y + s * 0.18, x + s * 0.96,
                         y + s * 0.82], radius=int(s * 0.08), fill="#283593")
    d.rectangle([x + s * 0.04, y + s * 0.30, x + s * 0.96, y + s * 0.44],
                fill="#1A237E")
    d.rectangle([x + s * 0.12, y + s * 0.52, x + s * 0.30, y + s * 0.68],
                fill="#E8B84B")
    f = font(SANS_B, int(s * 0.30))
    d.text((x + s * 0.62, y + s * 0.62), "10%", font=f, fill="white",
           anchor="mm")


def pic_storm(d, x, y, s):
    d.ellipse([x + s * 0.10, y + s * 0.22, x + s * 0.45, y + s * 0.52],
              fill="#607D8B")
    d.ellipse([x + s * 0.35, y + s * 0.12, x + s * 0.72, y + s * 0.48],
              fill="#78909C")
    d.ellipse([x + s * 0.60, y + s * 0.26, x + s * 0.90, y + s * 0.54],
              fill="#607D8B")
    for i, xx in enumerate((0.20, 0.45, 0.68)):
        d.line([(x + s * xx, y + s * 0.58), (x + s * (xx - 0.04),
               y + s * 0.74)], fill="#1F6FB2", width=5)
    d.polygon([(x + s * 0.52, y + s * 0.58), (x + s * 0.38, y + s * 0.82),
               (x + s * 0.50, y + s * 0.82), (x + s * 0.42, y + s * 0.98),
               (x + s * 0.62, y + s * 0.70), (x + s * 0.50, y + s * 0.70)],
              fill="#F9A825")


PANELS = [
    ("MIDDLE EAST  •  HORMUZ", "#C0392B",
     "Tankers hit in the Strait of Hormuz",
     "Two tankers struck by projectiles; a third caught fire after "
     "hitting a mine. Bahrain says an Iranian strike set a plant ablaze.",
     pic_tanker),
    ("MARKETS  •  CRYPTO", "#E67E22",
     "Bitcoin crashes to $55k, then rebounds",
     "BTC fell to its lowest since Sept 2024, wiping out $2.6bn of "
     "leveraged bets, before climbing back above $60,000.",
     pic_bitcoin),
    ("MEXICO  •  CRIME", "#7A5C00",
     "FBI most-wanted \u201cChapo Isidro\u201d captured",
     "Mexican special forces seized Fausto Isidro Meza in Sinaloa. "
     "The raid left 11 dead and sparked cartel roadblocks.",
     pic_badge),
    ("CLIMATE  •  COP31", "#2E7D6B",
     "Climate talks in overtime for a second day",
     "In Antalya, nations are deadlocked over fossil fuels after a "
     "draft deal dropped all mention of coal, oil and gas.",
     pic_globe),
    ("USA  •  POLITICS", "#283593",
     "Trump vows a 10% cap on credit-card rates",
     "The president said he would work with the incoming Democratic "
     "Congress to cap rates at 10%.",
     pic_card),
    ("BRAZIL  •  WEATHER", "#455A64",
     "Storm kills 3 and wrecks 5,000 homes",
     "Hurricane-force winds hit Tupancireta in Rio Grande do Sul, "
     "tearing roofs off, felling trees and cutting power.",
     pic_storm),
]


def main():
    img = Image.new("RGB", (W, H), "#F4F1EA")
    d = ImageDraw.Draw(img)

    # ---- header band
    d.rectangle([0, 0, W, 148], fill="#0F2A43")
    d.rectangle([0, 148, W, 154], fill="#E8B84B")
    d.text((32, 22), "THE WORLD IN ONE IMAGE", font=font(SANS_B, 26),
           fill="#E8B84B")
    d.text((32, 52), "Sunday, 22 November 2026", font=font(SERIF_B, 56),
           fill="white")
    d.text((32, 116), "Six stories that defined the day \u2014 from Hormuz to Wall Street",
           font=font(SANS, 24), fill="#B0C4D8")

    # ---- grid: 2 cols x 3 rows
    gx, gy = 16, 170
    gap = 12
    pw = (W - 2 * gx - gap) // 2
    ph = (H - gy - 44 - 2 * gap) // 3
    for i, (tag, colour, head, body, pic) in enumerate(PANELS):
        col, row = i % 2, i // 2
        x0 = gx + col * (pw + gap)
        y0 = gy + row * (ph + gap)
        d.rounded_rectangle([x0, y0, x0 + pw, y0 + ph], radius=14,
                            fill="white", outline="#D8D2C4", width=2)
        d.rectangle([x0, y0 + 12, x0 + 8, y0 + ph - 12], fill=colour)
        tx = x0 + 24
        d.text((tx, y0 + 16), tag, font=font(SANS_B, 20), fill=colour)
        lines = wrap(d, head, font(SANS_B, 26), pw - 24 - 118)
        yy = y0 + 48
        for ln in lines[:3]:
            d.text((tx, yy), ln, font=font(SANS_B, 26), fill="#1A1A1A")
            yy += 31
        blines = wrap(d, body, font(SANS, 20), pw - 24 - 118)
        yy += 6
        for ln in blines[:4]:
            d.text((tx, yy), ln, font=font(SANS, 20), fill="#37474F")
            yy += 26
        pic(d, x0 + pw - 118, y0 + 52, 96)

    # ---- footer
    d.text((32, H - 34),
           "Reported 22 Nov 2026  •  Sources: Reuters, AP, UKMTO, Coinglass, AFP",
           font=font(SANS, 18), fill="#78909C")

    out = os.path.join(BASE, "entry.png")
    img.save(out, "PNG", optimize=True)
    print(out, img.size, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
