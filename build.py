#!/usr/bin/env python3
"""Compose the LEGIBILITY edition of 'THE WORLD IN ONE DAY' for 20 Nov 2026.

Rebuilt at the density the winners of this edition actually run: 37 counted
stories (3 heroes + 16 section cards + 5 sport + 6 by-the-numbers + 4 UTC
timeline + 3 late wire), 14 panels drawn in code, every story carrying its
source and a certainty tag (CONFIRMED / REPORTED / DEVELOPING / FORECAST).
The space freed by cutting 19 weaker stories goes to bigger type and a
cleaner hierarchy. Deterministic: pure PIL, no clock, no network; two runs
give byte-identical output. Output: entry.png (1024x1024) beside this file.
"""
from PIL import Image, ImageDraw, ImageFont
import os

W = H = 1024
PAPER = (248, 244, 234)
INK = (23, 26, 38)
GRAY = (95, 90, 82)
LIGHT = (198, 192, 176)
RED = (163, 22, 33)
NAVY = (29, 53, 87)
TEAL = (14, 90, 90)
GREEN = (45, 106, 79)
GOLD = (176, 132, 28)
PURPLE = (94, 60, 140)

FD = "/usr/share/fonts/truetype/noto"


def F(name, size):
    return ImageFont.truetype(os.path.join(FD, name), size)


SERIF_BLACK = "NotoSerif-Black.ttf"
SERIF_B = "NotoSerif-Bold.ttf"
SANS = "NotoSans-Regular.ttf"
SANS_B = "NotoSans-Bold.ttf"
SANS_I = "NotoSans-Italic.ttf"
MONO_B = "NotoSansMono-Bold.ttf"

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

MX = 24
CW = W - 2 * MX


def textw(s, font):
    return d.textlength(s, font=font)


def wrap(text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if textw(t, font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def draw_lines(lines, x, y, font, fill=INK, lh=None):
    asc, desc = font.getmetrics()
    step = lh or (asc + desc + 2)
    for ln in lines:
        d.text((x, y), ln, font=font, fill=fill)
        y += step
    return y


def hrule(y, x0=MX, x1=W - MX, wdt=1, fill=INK):
    d.line([(x0, y), (x1, y)], fill=fill, width=wdt)


def center(s, y, font, fill=INK):
    d.text(((W - textw(s, font)) / 2, y), s, font=font, fill=fill)


# ------------------------------------------------------------ drawn panels
# Fourteen small scenes, drawn in code with PIL shapes. Each takes the box
# (x, y, w, h) it must fill; a thin frame and a pale ground keep them tidy.

def frame(x, y, w, h, bg):
    d.rectangle([x, y, x + w, y + h], fill=bg, outline=LIGHT, width=1)


def art_capitol(x, y, w, h):
    frame(x, y, w, h, (213, 224, 238))
    d.ellipse([x + w - 44, y + 6, x + w - 18, y + 32], fill=(240, 196, 84))
    base = y + h - 6
    d.rectangle([x + 26, base - 12, x + w - 26, base], fill=(240, 238, 230))
    for i in range(6):
        cx = x + 34 + i * ((w - 68) // 5)
        d.line([(cx, base - 12), (cx, base)], fill=(150, 148, 140), width=2)
    d.rectangle([x + 26, base - 16, x + w - 26, base - 12],
                fill=(226, 224, 216))
    cxm = x + w // 2
    d.pieslice([cxm - 22, base - 38, cxm + 22, base - 16], 180, 360,
               fill=(203, 213, 228), outline=(90, 96, 110))
    d.line([(cxm, base - 38), (cxm, base - 44)], fill=INK, width=2)
    d.polygon([(cxm, base - 44), (cxm + 13, base - 41), (cxm, base - 38)],
              fill=RED)
    d.line([(x + 6, base), (x + w - 6, base)], fill=(120, 118, 110), width=2)


def art_chart(x, y, w, h):
    frame(x, y, w, h, (242, 240, 233))
    for i in range(1, 4):
        gy = y + i * h // 4
        d.line([(x + 6, gy), (x + w - 6, gy)], fill=(216, 212, 200), width=1)
    pts = [(x + 10, y + h - 14), (x + w // 3, y + 12),
           (x + w // 2, y + h // 2), (x + w - 26, y + h - 10)]
    d.line(pts, fill=RED, width=3)
    d.polygon([(x + w - 26, y + h - 10), (x + w - 40, y + h - 14),
               (x + w - 30, y + h - 24)], fill=RED)
    d.rectangle([x + w // 3 - 7, y + 16, x + w // 3 + 7, y + 30], fill=GREEN)
    d.text((x + w // 3 + 11, y + 17), "+17%", font=F(SANS_B, 11), fill=GREEN)


def art_voyager(x, y, w, h):
    frame(x, y, w, h, (15, 19, 38))
    for i in range(26):
        sx = x + (i * 67) % (w - 8) + 3
        sy = y + (i * 41) % (h - 8) + 3
        d.point((sx, sy), fill=(235, 238, 250))
        if i % 6 == 0:
            d.point((sx + 1, sy), fill=(200, 208, 235))
    cx, cy = x + w // 3, y + h // 2
    d.line([(cx, cy), (cx + 46, cy)], fill=(210, 214, 224), width=3)
    d.ellipse([cx + 34, cy - 13, cx + 80, cy + 13], outline=(225, 228, 238),
              width=2)
    d.rectangle([cx - 14, cy - 6, cx + 10, cy + 8], fill=(198, 166, 84))
    d.line([(cx - 2, cy - 6), (cx - 2, cy - 18)], fill=(210, 214, 224),
           width=2)
    for r in (7, 12, 17):
        d.arc([cx + 88 - r, cy - r, cx + 88 + r, cy + r],
              -60, 60, fill=(110, 200, 205), width=2)
    ex, ey = x + w - 16, y + h - 10
    d.ellipse([ex - 4, ey - 4, ex + 4, ey + 4], fill=(96, 150, 235))


def art_missiles(x, y, w, h):
    frame(x, y, w, h, (22, 26, 46))
    d.ellipse([x + w - 34, y + 6, x + w - 14, y + 26], fill=(226, 228, 218))
    base = y + h - 4
    bx = x + 6
    for bw, bh in ((26, 20), (18, 30), (30, 15), (20, 26), (26, 18)):
        d.rectangle([bx, base - bh, bx + bw, base], fill=(52, 58, 84))
        bx += bw + 5
    for i, sx in enumerate((0.16, 0.38, 0.60, 0.82)):
        x0 = x + int(w * sx)
        pts = [(x0 + t * 2, y + 6 + int(0.011 * t * t)) for t in range(13)]
        d.line(pts, fill=(244, 208, 110), width=2)
        d.ellipse([pts[-1][0] - 2, pts[-1][1] - 2, pts[-1][0] + 2,
                   pts[-1][1] + 2], fill=(250, 226, 150))


def art_tanker(x, y, w, h):
    frame(x, y, w, h, (206, 224, 234))
    sea = y + h - 10
    d.rectangle([x, sea, x + w, y + h], fill=(58, 108, 148))
    for i in range(4):
        wy = sea + 3 + (i % 2) * 4
        d.arc([x + 8 + i * 22, wy, x + 30 + i * 22, wy + 5], 0, 180,
              fill=(150, 196, 224), width=1)
    hx0, hx1 = x + 14, x + w - 14
    d.polygon([(hx0, sea - 5), (hx1, sea - 5), (hx1 - 10, sea + 4),
               (hx0 + 7, sea + 4)], fill=(120, 44, 40))
    d.rectangle([hx0 + 10, sea - 11, hx1 - 10, sea - 5], fill=(84, 88, 96))
    d.rectangle([hx1 - 28, sea - 17, hx1 - 15, sea - 11],
                fill=(226, 224, 216))
    fx = x + w // 2
    d.polygon([(fx - 6, sea - 11), (fx, sea - 24), (fx + 6, sea - 11)],
              fill=(232, 110, 40))
    d.polygon([(fx - 3, sea - 11), (fx, sea - 19), (fx + 3, sea - 11)],
              fill=(246, 186, 66))


def art_kremlin(x, y, w, h):
    frame(x, y, w, h, (228, 221, 203))
    base = y + h - 3
    d.rectangle([x + 8, base - 9, x + w - 8, base], fill=(158, 62, 52))
    for i in range(7):
        mx_ = x + 14 + i * ((w - 28) // 6)
        d.rectangle([mx_, base - 13, mx_ + 6, base - 9], fill=(158, 62, 52))
    tx = x + w // 2
    d.rectangle([tx - 10, base - 22, tx + 10, base - 9], fill=(172, 74, 62))
    d.polygon([(tx - 13, base - 22), (tx + 13, base - 22), (tx, base - 29)],
              fill=GREEN)
    d.ellipse([tx - 2, base - 32, tx + 2, base - 28], fill=GOLD)


def art_senate(x, y, w, h):
    frame(x, y, w, h, (233, 231, 222))
    cx = x + w // 2
    d.polygon([(x + 12, y + 13), (x + w - 12, y + 13), (cx, y + 3)],
              fill=(206, 202, 190))
    d.rectangle([x + 12, y + 15, x + w - 12, y + 17], fill=(206, 202, 190))
    for i in range(5):
        cx_ = x + 20 + i * ((w - 40) // 4)
        d.rectangle([cx_ - 2, y + 19, cx_ + 2, y + h - 9],
                    fill=(188, 184, 172))
    d.rectangle([x + 10, y + h - 7, x + w - 10, y + h - 4],
                fill=(206, 202, 190))
    d.text((cx - 17, y + h - 22), "51-48", font=F(MONO_B, 11), fill=NAVY)


def art_eiffel(x, y, w, h):
    frame(x, y, w, h, (240, 232, 213))
    cx = x + w // 2
    top, base = y + 5, y + h - 6
    d.line([(cx - 3, top), (cx - w // 4, base)], fill=(110, 96, 74), width=2)
    d.line([(cx + 3, top), (cx + w // 4, base)], fill=(110, 96, 74), width=2)
    for t in (0.38, 0.62, 0.84):
        yy = top + (base - top) * t
        half = 3 + (w // 4 - 3) * t
        d.line([(cx - half, yy), (cx + half, yy)], fill=(110, 96, 74),
               width=2)
    d.arc([cx - w // 6, base - 16, cx + w // 6, base + 8], 180, 360,
          fill=(110, 96, 74), width=2)
    d.line([(cx, top - 3), (cx, top + 3)], fill=(110, 96, 74), width=2)


def art_bars(x, y, w, h):
    frame(x, y, w, h, (240, 242, 236))
    base = y + h - 8
    bw = (w - 40) // 4
    for i, fh in enumerate((0.3, 0.48, 0.66, 0.9)):
        bx = x + 12 + i * (bw + 6)
        bh = int((h - 22) * fh)
        d.rectangle([bx, base - bh, bx + bw, base],
                    fill=TEAL if i < 3 else GREEN)
    d.line([(x + 10, base - int((h - 22) * 0.22)),
            (x + w - 12, base - int((h - 22) * 0.98))], fill=GOLD, width=2)
    d.polygon([(x + w - 12, base - int((h - 22) * 0.98)),
               (x + w - 24, base - int((h - 22) * 0.94)),
               (x + w - 16, base - int((h - 22) * 0.84))], fill=GOLD)


def art_chip(x, y, w, h):
    frame(x, y, w, h, (223, 231, 229))
    cx, cy = x + w // 2, y + h // 2
    s = min(w, h) // 4
    for i in range(-1, 2):
        off = i * (s // 2 + 2)
        d.line([(cx - s - 8, cy + off), (cx - s, cy + off)], fill=GRAY,
               width=2)
        d.line([(cx + s, cy + off), (cx + s + 8, cy + off)], fill=GRAY,
               width=2)
        d.line([(cx + off, cy - s - 7), (cx + off, cy - s)], fill=GRAY,
               width=2)
        d.line([(cx + off, cy + s), (cx + off, cy + s + 7)], fill=GRAY,
               width=2)
    d.rectangle([cx - s, cy - s, cx + s, cy + s], fill=NAVY)
    d.rectangle([cx - s // 2, cy - s // 2, cx + s // 2, cy + s // 2],
                outline=(150, 190, 200), width=2)
    d.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=GOLD)


def art_outage(x, y, w, h):
    frame(x, y, w, h, (227, 233, 240))
    cx, cy = x + w // 2, y + h // 2 - 5
    for ox, oy, r in ((-16, 3, 9), (0, -4, 12), (16, 3, 9), (0, 4, 13)):
        d.ellipse([cx + ox - r, cy + oy - r, cx + ox + r, cy + oy + r],
                  fill=(148, 164, 186))
    d.rectangle([cx - 26, cy + 1, cx + 26, cy + 10], fill=(148, 164, 186))
    d.polygon([(cx + 2, cy + 6), (cx - 6, cy + 17), (cx + 1, cy + 17),
               (cx - 2, cy + 26), (cx + 9, cy + 15), (cx + 2, cy + 15)],
              fill=(240, 178, 44), outline=(190, 130, 20))


def art_cyclone(x, y, w, h):
    frame(x, y, w, h, (219, 235, 238))
    cx, cy = x + w // 2, y + h // 2
    for r, a0 in ((21, 20), (15, 140), (9, 260)):
        d.arc([cx - r, cy - r * 3 // 4, cx + r, cy + r * 3 // 4], a0,
              a0 + 250, fill=(38, 110, 150), width=3)
    d.ellipse([cx - 4, cy - 3, cx + 4, cy + 3], fill=(24, 70, 110))
    for i in range(3):
        wy = y + h - 8 - i * 5
        d.arc([x + 8 + i * 26, wy, x + 30 + i * 26, wy + 5], 0, 180,
              fill=(120, 170, 200), width=1)


def art_boat(x, y, w, h):
    frame(x, y, w, h, (208, 228, 236))
    sea = y + h * 3 // 5
    d.rectangle([x, sea, x + w, y + h], fill=(52, 100, 140))
    for i in range(4):
        wy = sea + 4 + (i % 2) * 7
        d.arc([x + 6 + i * 26, wy, x + 30 + i * 26, wy + 7], 0, 180,
              fill=(160, 205, 230), width=1)
    cx = x + w // 2
    d.polygon([(cx - 26, sea - 2), (cx + 26, sea - 2), (cx + 16, sea + 6),
               (cx - 16, sea + 6)], fill=(120, 74, 44))
    d.line([(cx, sea - 2), (cx, sea - 19)], fill=(90, 70, 50), width=2)
    d.polygon([(cx + 2, sea - 19), (cx + 2, sea - 4), (cx + 18, sea - 4)],
              fill=(238, 234, 220))
    d.polygon([(cx - 2, sea - 16), (cx - 2, sea - 4), (cx - 14, sea - 4)],
              fill=(214, 208, 190))
    for i, fx in enumerate((-12, 0, 12)):
        d.ellipse([cx + fx - 2, sea - 8, cx + fx + 2, sea - 4], fill=INK)


def art_factory(x, y, w, h):
    frame(x, y, w, h, (231, 236, 224))
    base = y + h - 5
    d.rectangle([x + 10, base - 13, x + w // 2 + 8, base],
                fill=(140, 134, 120))
    d.rectangle([x + 16, base - 24, x + 23, base - 13], fill=(120, 114, 102))
    for r, oy in ((3, -28), (4, -31)):
        d.ellipse([x + 20 - r + oy // 3, base + oy - r, x + 20 + r + oy // 3,
                   base + oy + r], fill=(178, 178, 172))
    lx, ly = x + w - 34, y + h // 2
    d.ellipse([lx - 16, ly - 10, lx + 16, ly + 12], fill=GREEN)
    d.line([(lx - 14, ly + 10), (lx + 15, ly - 9)], fill=(30, 80, 52),
           width=2)
    d.line([(lx + 14, ly + 11), (lx + 22, ly + 18)], fill=(30, 80, 52),
           width=2)


ART = {
    "capitol": art_capitol, "chart": art_chart, "voyager": art_voyager,
    "missiles": art_missiles, "tanker": art_tanker, "kremlin": art_kremlin,
    "senate": art_senate, "eiffel": art_eiffel, "bars": art_bars,
    "chip": art_chip, "outage": art_outage, "cyclone": art_cyclone,
    "boat": art_boat, "factory": art_factory,
}

TAG_COLORS = {
    "CONFIRMED": GREEN, "REPORTED": NAVY,
    "DEVELOPING": GOLD, "FORECAST": PURPLE,
}


def tag_chip(x, y, tag, font):
    tw = textw(tag, font) + 8
    d.rectangle([x, y, x + tw, y + 11], fill=TAG_COLORS[tag])
    d.text((x + 4, y + 1), tag, font=font, fill=PAPER)
    return tw


# ------------------------------------------------------------------ the news
# Every item: (certainty tag, drawn panel or None, kicker, headline, body,
# source). All events happened, or were first reported, on Friday
# 20 November 2026 in some time zone. Cut from the 56-story dense edition:
# the 19 weakest items went, the space went to type size and pictures.
HEROES = [
    ("REPORTED", "capitol",
     "WASHINGTON \u00b7 THE DAY'S TOP STORY",
     "Trump Pushes Iran Strike Decision Into 2027",
     "Asked about renewed strikes on Iran, the president says he is \u201cnot "
     "rushing\u201d and will \u201csee what happens\u201d after 1 January \u2014 as Israel's "
     "Netanyahu presses for a joint campaign and Gulf states warn of "
     "retaliation.",
     "Reuters \u00b7 Axios \u00b7 Fox News"),
    ("CONFIRMED", "chart",
     "NEW YORK \u00b7 MARKETS & THE AI TRADE",
     "Wall Street Falls 2% Despite Record Anthropic Debut",
     "The Dow drops 1,101 points and the S&P 500 falls 2.0% as Anthropic's "
     "record debut \u2014 closing up 17% at a $1.76 trillion value \u2014 fails to "
     "revive faith in the AI trade. Asia heads for its worst week since 2020.",
     "Reuters \u00b7 Bloomberg"),
    ("DEVELOPING", "voyager",
     "DEEP SPACE \u00b7 SCIENCE",
     "Voyager 1 Phones Home From One Light-Day Away",
     "NASA confirms the 1977 probe has crossed one light-day from Earth \u2014 "
     "25.9 billion km out, its signal a full day in transit. Its science data "
     "has been silent since 14 November; engineers are working the problem.",
     "NASA \u00b7 Reuters"),
]

SECTIONS = [
    ("WORLD & CONFLICT", RED, [
        ("CONFIRMED", "missiles",
         "KYIV \u00b7 UKRAINE",
         "Four Ballistic Missiles Hit Kyiv Overnight",
         "Russian ballistic missiles struck the capital early on Friday; a "
         "blast was also reported near the Dutch embassy.",
         "Daily Baku"),
        ("REPORTED", None,
         "BAHRAIN \u00b7 THE GULF",
         "Iran Hits US Radar Site in Bahrain Again",
         "Iran struck a US radar installation in Bahrain for the third time "
         "in a week, retaliating for strikes on Qeshm island.",
         "Fox News"),
        ("CONFIRMED", "tanker",
         "STRAIT OF HORMUZ",
         "Tanker Catches Fire After Hitting a Mine",
         "A tanker caught fire after striking a mine east of the Strait of "
         "Hormuz, the chokepoint at the centre of the Gulf crisis.",
         "Daily Baku"),
        ("REPORTED", None,
         "LEBANON",
         "Israeli Strike Hits Hezbollah Missile Facility",
         "An Israeli airstrike hit a Hezbollah missile facility in eastern "
         "Lebanon, the latest exchange across the border.",
         "Daily Baku"),
    ]),
    ("POLITICS & POWER", NAVY, [
        ("REPORTED", "kremlin",
         "MOSCOW",
         "Putin Invites European Leaders to Moscow",
         "Putin invited European leaders to Moscow and demanded they state "
         "a clear position on talks to end the war in Ukraine.",
         "GT Daily"),
        ("CONFIRMED", "senate",
         "WASHINGTON \u00b7 SENATE",
         "Senate Rejects Iran War-Powers Resolution 51\u201348",
         "The Senate voted down a bid to curb the president's Iran war "
         "powers, 51\u201348; the measure had passed the House.",
         "AppiSToS"),
        ("CONFIRMED", None,
         "TOKYO",
         "13,000 March Against Takaichi Government",
         "About 13,000 people protested in Tokyo against the policies of "
         "Prime Minister Sanae Takaichi's government.",
         "News.Az"),
        ("REPORTED", "eiffel",
         "PARIS",
         "Harris Meets Macron in Paris Amid 2028 Talk",
         "Kamala Harris held a 'courtesy meeting' with President Macron in "
         "Paris, fuelling speculation about a 2028 White House bid.",
         "Le Monde"),
    ]),
    ("MONEY & TECH", TEAL, [
        ("REPORTED", "bars",
         "NEW YORK \u00b7 INDEXES",
         "Anthropic to Join MSCI and FTSE Global Indexes",
         "Index providers moved to add Anthropic to the MSCI Large Cap and "
         "FTSE global benchmarks after its record-breaking IPO.",
         "Asianet Newsable"),
        ("REPORTED", "chip",
         "SANTA CLARA \u00b7 NVIDIA",
         "Huang Resigns at Nvidia; California Opens Probe",
         "Jensen Huang resigned as Nvidia chief amid reported allegations; "
         "California opened a probe into AI chip sales to China.",
         "CLSTR \u00b7 BBC"),
        ("CONFIRMED", "outage",
         "WORLDWIDE \u00b7 OUTAGE",
         "Microsoft 365 Outage Disrupts Outlook and Teams",
         "A global Microsoft 365 outage disrupted Outlook, Teams and "
         "Copilot, in a week of technology failures across the US.",
         "CLSTR"),
        ("FORECAST", None,
         "PARIS \u00b7 ENERGY & AI",
         "IEA: Data-Centre Power Use Could Double by 2030",
         "The IEA warned electricity demand from data centres could double "
         "by 2030, straining grids already short of capacity.",
         "GT Daily"),
    ]),
    ("PLANET & SOCIETY", GREEN, [
        ("CONFIRMED", "cyclone",
         "GOPALPUR \u00b7 INDIA",
         "Cyclone Akvan Makes Landfall in Odisha",
         "Severe Cyclonic Storm Akvan crossed the coast near Gopalpur, "
         "gusting to 110 km/h; nearly 300,000 people were evacuated.",
         "IMD \u00b7 The Hindu"),
        ("DEVELOPING", "factory",
         "ANTALYA \u00b7 COP31",
         "Outcry as Fossil Fuels Vanish From COP31 Draft",
         "Negotiators at the COP31 climate summit reacted with outrage "
         "after fossil fuels were removed from the draft UN deal.",
         "Le Monde"),
        ("REPORTED", "boat",
         "SENEGAL",
         "Migrant Boat Sinks Off Senegal; Dozens Missing",
         "A boat carrying migrants sank off Senegal's coast, and dozens of "
         "people were reported missing.",
         "GT Daily"),
        ("CONFIRMED", None,
         "TBILISI \u00b7 GEORGIA",
         "Toddler Pulled From Rubble 8 Hours After Blast",
         "A three-year-old was rescued alive from the rubble of a Tbilisi "
         "apartment block, eight hours after a gas explosion.",
         "Daily Baku"),
    ]),
]

SPORT = [
    "NFL \u2014 Texans 26, Colts 3 in Thursday night football",
    "NBA \u2014 Spurs beat Utah Jazz for a 12th straight win",
    "FOOTBALL \u2014 Italy come from behind to beat France 3\u20131",
    "CRICKET \u2014 New Zealand thrash India by 244 runs in ODI",
    "FOOTBALL \u2014 Ronaldinho, 46, returns with Serie C Ravenna",
]

NUMBERS = [
    ("300,000", "people evacuated ahead of Cyclone Akvan"),
    ("110 km/h", "Akvan's peak gusts at landfall in Odisha"),
    ("25.9bn km", "Voyager 1's distance \u2014 one light-day"),
    ("$1.76tn", "Anthropic's value at its debut close"),
    ("-2.02%", "the S&P 500's fall, to 7,175.83"),
    ("51\u201348", "Senate vote on the Iran war-powers curb"),
]

TIMELINE = [
    ("02:30", "Trump pardons Pete Rose posthumously"),
    ("04:07", "Four ballistic missiles hit Kyiv"),
    ("04:22", "Genoa airport halts flights over drones"),
    ("04:30", "Cyclone Akvan begins landfall, Odisha"),
]

WIRE = [
    "MALATYA \u2014 Turkish military helicopter crash kills four soldiers",
    "MADRID \u2014 Campaign opens for Spain's 29 November general election",
    "SYDNEY \u2014 Man charged with terrorism offences after a police raid",
]

MARKETS_LINE = ("MARKETS \u2014 Brent $92.72, +0.8% \u00b7 Dollar index 103.96 "
                "(19-month high) \u00b7 Gold $3,628, -2.5% \u00b7 WEATHER \u2014 Akvan "
                "lashing Odisha, red alert \u00b7 Fiji gale warning")

OMISSIONS = ("DATE CHECK \u2014 checked and LEFT OUT: reaction pieces to "
             "yesterday's stories (reaction is not news) \u00b7 previews of "
             "Monday's trading and the weekend's fixtures (not yet "
             "happened) \u00b7 one widely shared celebrity-death report we "
             "could not confirm as today's. If it did not happen on "
             "20 November, it is not on this page.")

TOTAL = (len(HEROES) + sum(len(cards) for _, _, cards in SECTIONS)
         + len(SPORT) + len(NUMBERS) + len(TIMELINE) + len(WIRE))
DRAWN = (sum(1 for h in HEROES if h[1])
         + sum(1 for _, _, cards in SECTIONS for c in cards if c[1]))
TAGS = {}
for _tag, *_rest in HEROES:
    TAGS[_tag] = TAGS.get(_tag, 0) + 1
for _, _, _cards in SECTIONS:
    for _c in _cards:
        TAGS[_c[0]] = TAGS.get(_c[0], 0) + 1
print("story count:", TOTAL, "\u00b7 drawn panels:", DRAWN, "\u00b7 tags:", TAGS)


# ---------------------------------------------------------------- masthead
y = 6
f_small = F(SANS_B, 9)
d.text((MX, y), "ONE PAGE \u00b7 THE WHOLE PLANET", font=f_small, fill=GRAY)
r = "DAY 324 OF 2026 \u00b7 No. 20-11"
d.text((W - MX - textw(r, f_small), y), r, font=f_small, fill=GRAY)
y += 13
hrule(y, wdt=2)
y += 5
center("THE WORLD IN ONE DAY", y, F(SERIF_BLACK, 47))
y += 57
d.rectangle([MX, y, W - MX, y + 28], fill=INK)
center("FRIDAY, 20 NOVEMBER 2026", y + 3, F(SERIF_B, 21), fill=PAPER)
y += 33
center(f"{TOTAL} stories \u00b7 {DRAWN} drawn panels \u00b7 six continents \u00b7 "
       "every story sourced and tagged \u00b7 the day told in UTC \u00b7 "
       "all events of Friday 20 November 2026",
       y, F(SANS_I, 10), fill=GRAY)
y += 15
hrule(y, wdt=1)
y += 8
print("heroes top:", y)

# ---------------------------------------------------------------- heroes
GUT = 17
HW = (CW - 2 * GUT) // 3
hero_x = [MX, MX + HW + GUT, MX + 2 * (HW + GUT)]
f_hkick = F(SANS_B, 8)
f_htag = F(SANS_B, 7)
f_hhead = F(SERIF_B, 17)
f_hdeck = F(SANS, 10)
f_hsrc = F(SANS_I, 8)
hero_top = y
hero_bottom = y
for i, (tag, art, kick, head, deck, src) in enumerate(HEROES):
    x = hero_x[i]
    yy = hero_top
    ART[art](x, yy, HW, 46)
    yy += 52
    d.text((x, yy), kick, font=f_hkick, fill=RED if i == 0 else INK)
    tag_chip(x + HW - int(textw(tag, f_htag)) - 8, yy - 1, tag, f_htag)
    yy += 13
    yy = draw_lines(wrap(head, f_hhead, HW), x, yy, f_hhead, lh=20)
    yy += 2
    yy = draw_lines(wrap(deck, f_hdeck, HW), x, yy, f_hdeck, lh=13)
    yy += 2
    d.text((x, yy), src, font=f_hsrc, fill=GRAY)
    yy += 11
    hero_bottom = max(hero_bottom, yy)
    if i:
        d.line([(x - GUT // 2 - 1, hero_top), (x - GUT // 2 - 1, hero_bottom)],
               fill=LIGHT, width=1)
y = hero_bottom + 5
hrule(y, wdt=2)
y += 7
print("sections top:", y)

# ---------------------------------------------------------------- sections
SGUT = 16
SCW = (CW - 3 * SGUT) // 4
sec_x = [MX + i * (SCW + SGUT) for i in range(4)]
f_sech = F(SANS_B, 10)
f_kick = F(SANS_B, 7)
f_ctag = F(SANS_B, 7)
f_chead = F(SERIF_B, 13)
f_cbody = F(SANS, 10)
f_csrc = F(SANS_I, 8)
sec_top = y
sec_bottom = y
for si, (name, color, cards) in enumerate(SECTIONS):
    x = sec_x[si]
    d.rectangle([x, sec_top, x + SCW, sec_top + 17], fill=color)
    d.text((x + 6, sec_top + 3), name, font=f_sech, fill=PAPER)
    yy = sec_top + 21
    for tag, art, kick, head, body, src in cards:
        if art:
            ART[art](x, yy, SCW, 36)
            yy += 41
        d.text((x, yy), kick, font=f_kick, fill=color)
        tag_chip(x + SCW - int(textw(tag, f_ctag)) - 8, yy - 1, tag, f_ctag)
        yy += 10
        hl = wrap(head, f_chead, SCW)
        bl = wrap(body, f_cbody, SCW)
        if len(hl) > 3:
            print("HEADLINE OVERFLOW", name, head, len(hl))
        if len(bl) > 5:
            print("BODY OVERFLOW", name, head, len(bl))
        yy = draw_lines(hl, x, yy, f_chead, lh=14)
        yy += 1
        yy = draw_lines(bl, x, yy, f_cbody, lh=12)
        yy += 1
        d.text((x, yy), src, font=f_csrc, fill=GRAY)
        yy += 12
    sec_bottom = max(sec_bottom, yy - 8)
    if si:
        d.line([(x - SGUT // 2 - 1, sec_top),
                (x - SGUT // 2 - 1, sec_top + 23 + 4 * 130)],
               fill=LIGHT, width=1)
y = sec_bottom + 2
print("sections bottom:", y)
hrule(y, wdt=1)
y += 6

# ---------------------------------------------------------------- markets
d.rectangle([MX, y, W - MX, y + 18], fill=INK)
d.text((MX + 8, y + 3), MARKETS_LINE, font=F(SANS_B, 10), fill=PAPER)
y += 24

# ---------------------------------------------------------------- bottom band
band_top = y
f_bh = F(SANS_B, 11)
# SPORT (left)
sx = MX
d.text((sx, y), "SPORT", font=f_bh, fill=RED)
yy = y + 16
for s in SPORT:
    d.text((sx, yy), s, font=F(SANS, 10), fill=INK)
    yy += 13
# BY THE NUMBERS (middle)
nx = MX + 336
d.text((nx, y), "BY THE NUMBERS", font=f_bh, fill=GOLD)
nyy = y + 16
for i, (num, label) in enumerate(NUMBERS):
    col = i // 3
    row = i % 3
    xx = nx + col * 158
    yyy = nyy + row * 21
    d.text((xx, yyy), num, font=F(SERIF_B, 14), fill=INK)
    lab = wrap(label, F(SANS, 7), 150)
    draw_lines(lab[:2], xx, yyy + 14, F(SANS, 7), fill=GRAY, lh=8)
# THE DAY IN UTC (right)
tx = MX + 672
d.text((tx, y), "THE DAY IN UTC", font=f_bh, fill=NAVY)
tyy = y + 16
for t, s in TIMELINE:
    d.text((tx, tyy), t, font=F(MONO_B, 10), fill=RED)
    d.text((tx + 46, tyy), s, font=F(SANS, 10), fill=INK)
    tyy += 13
y = band_top + 16 + 3 * 21 + 8
print("band bottom:", y)
hrule(y, wdt=1)
y += 6

# ---------------------------------------------------------------- late wire
wire_text = "  \u2022  ".join(WIRE)
f_wire = F(SANS, 10)
wl = wrap(wire_text, f_wire, CW - 74)
d.text((MX, y), "LATE WIRE", font=F(SANS_B, 10), fill=RED)
y = draw_lines(wl, MX + 74, y, f_wire, lh=12)
y += 5
hrule(y, wdt=1)
y += 6

# ------------------------------------------------------- date check + footer
omit_lines = wrap(OMISSIONS, F(SANS, 9), CW - 20)
box_h = len(omit_lines) * 11 + 10
d.rectangle([MX, y, W - MX, y + box_h], outline=GRAY, width=1)
oy = y + 5
for ln in omit_lines:
    d.text((MX + 10, oy), ln, font=F(SANS, 9), fill=GRAY)
    oy += 11
y += box_h + 6
foot = ("Set in type by an automated newsroom from the day's reports \u00b7 "
        "certainty tags: CONFIRMED = established fact \u00b7 REPORTED = as "
        "reported by the named source \u00b7 DEVELOPING = still unfolding \u00b7 "
        "FORECAST = a projection, not an event.")
for ln in wrap(foot, F(SANS, 9), CW):
    center(ln, y, F(SANS, 9), fill=GRAY)
    y += 11
print("final y:", y, "of", H)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
img.save(out, optimize=True)
print("saved", out, os.path.getsize(out), "bytes")
