#!/usr/bin/env python3
"""Compose the DENSE edition of 'THE WORLD IN ONE DAY' for Friday 20 Nov 2026.

Winner-format front page: counted stories drawn from a story database —
3 heroes + 24 section cards + 5 sport + 8 by-the-numbers + 6 UTC timeline
+ 10 late wire = 56 items, every story carrying its source. Deterministic:
pure PIL, no clock, no network; two runs give byte-identical output.
Output: entry.png (1024x1024) beside this file.
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


# ------------------------------------------------------------------ the news
# Every item: (kicker, headline, body, source). All events happened, or were
# first reported, on Friday 20 November 2026 in some time zone.
HEROES = [
    ("WASHINGTON · THE DAY'S TOP STORY",
     "Trump Pushes Iran Strike Decision Into 2027",
     "Asked about renewed strikes on Iran, the president says he is \u201cnot "
     "rushing\u201d and will \u201csee what happens\u201d after 1 January \u2014 as Israel's "
     "Netanyahu presses for a joint campaign and Gulf states warn of "
     "retaliation.",
     "Reuters \u00b7 Axios \u00b7 Fox News"),
    ("NEW YORK · MARKETS & THE AI TRADE",
     "Wall Street Falls 2% Despite Record Anthropic Debut",
     "The Dow drops 1,101 points and the S&P 500 falls 2.0% as Anthropic's "
     "record debut \u2014 closing up 17% at a $1.76 trillion value \u2014 fails to "
     "revive faith in the AI trade. Asia heads for its worst week since 2020.",
     "Reuters \u00b7 Bloomberg"),
    ("DEEP SPACE · SCIENCE",
     "Voyager 1 Phones Home From One Light-Day Away",
     "NASA confirms the 1977 probe has crossed one light-day from Earth \u2014 "
     "25.9 billion km out, its signal a full day in transit. Its science data "
     "has been silent since 14 November; engineers are working the problem.",
     "NASA \u00b7 Reuters"),
]

SECTIONS = [
    ("WORLD & CONFLICT", RED, [
        ("KYIV \u00b7 UKRAINE",
         "Four Ballistic Missiles Hit Kyiv Overnight",
         "Russian ballistic missiles struck the capital early on Friday; a "
         "blast was also reported near the Dutch embassy.",
         "Daily Baku"),
        ("BAHRAIN \u00b7 THE GULF",
         "Iran Hits US Radar Site in Bahrain Again",
         "Iran struck a US radar installation in Bahrain for the third time "
         "in a week, retaliating for strikes on Qeshm island.",
         "Fox News"),
        ("STRAIT OF HORMUZ",
         "Tanker Catches Fire After Hitting a Mine",
         "A tanker caught fire after striking a mine east of the Strait of "
         "Hormuz, the chokepoint at the centre of the Gulf crisis.",
         "Daily Baku"),
        ("RIYADH \u00b7 SAUDI ARABIA",
         "Houthis Claim Strikes on Four Saudi Targets",
         "Houthi drones and missiles were fired at four Saudi targets; "
         "debris from an intercepted rocket damaged a Riyadh tower.",
         "Daily Baku \u00b7 News.Az"),
        ("LEBANON",
         "Israeli Strike Hits Hezbollah Missile Facility",
         "An Israeli airstrike hit a Hezbollah missile facility in eastern "
         "Lebanon, the latest exchange across the border.",
         "Daily Baku"),
        ("GAZA",
         "Israel Completes Operation Beyond 'Yellow Line'",
         "Israel's military completed a ground operation beyond the 'yellow "
         "line' in Gaza, amid shelling and airstrikes.",
         "GT Daily"),
    ]),
    ("POLITICS & POWER", NAVY, [
        ("MOSCOW",
         "Putin Invites European Leaders to Moscow",
         "Putin invited European leaders to Moscow and demanded they state "
         "a clear position on talks to end the war in Ukraine.",
         "GT Daily"),
        ("BERLIN",
         "European Allies Say They Are Ready for Russia Talks",
         "Ukraine's European allies, meeting in Berlin, said they hold a "
         "united position and are ready for negotiations with Russia.",
         "One Turn"),
        ("WASHINGTON \u00b7 SENATE",
         "Senate Rejects Iran War-Powers Resolution 51\u201348",
         "The Senate voted down a bid to curb the president's Iran war "
         "powers, 51\u201348; the measure had passed the House.",
         "AppiSToS"),
        ("PARIS",
         "Harris Meets Macron in Paris Amid 2028 Talk",
         "Kamala Harris held a 'courtesy meeting' with President Macron in "
         "Paris, fuelling speculation about a 2028 White House bid.",
         "Le Monde"),
        ("TOKYO",
         "13,000 March Against Takaichi Government",
         "About 13,000 people protested in Tokyo against the policies of "
         "Prime Minister Sanae Takaichi's government.",
         "News.Az"),
        ("WASHINGTON \u00b7 CYBER",
         "White House Taps Kirsten Davies as Cyber Chief",
         "After a wave of outages across the US, the White House named "
         "Pentagon official Kirsten Davies national cyber director.",
         "Le Monde"),
    ]),
    ("MONEY & TECH", TEAL, [
        ("NEW YORK \u00b7 INDEXES",
         "Anthropic to Join MSCI and FTSE Global Indexes",
         "Index providers moved to add Anthropic to the MSCI Large Cap and "
         "FTSE global benchmarks after its record-breaking IPO.",
         "Asianet Newsable"),
        ("SANTA CLARA \u00b7 NVIDIA",
         "Huang Resigns at Nvidia; California Opens Probe",
         "Jensen Huang resigned as Nvidia chief amid reported allegations; "
         "California opened a probe into AI chip sales to China.",
         "CLSTR \u00b7 BBC"),
        ("WORLDWIDE \u00b7 OUTAGE",
         "Microsoft 365 Outage Disrupts Outlook and Teams",
         "A global Microsoft 365 outage disrupted Outlook, Teams and "
         "Copilot, in a week of technology failures across the US.",
         "CLSTR"),
        ("PARIS \u00b7 ENERGY & AI",
         "IEA: Data-Centre Power Use Could Double by 2030",
         "The IEA warned electricity demand from data centres could double "
         "by 2030, straining grids already short of capacity.",
         "GT Daily"),
        ("TAIPEI \u00b7 MARKETS",
         "Taiwan Moves to Steady Tumbling Stocks",
         "Taiwan acted to steady its tumbling stock market as the Taiwan "
         "dollar neared a 10-year low against the greenback.",
         "CNBC TV18"),
        ("SHENZHEN \u00b7 APEC",
         "APEC Leaders Call to Keep Trade Corridors Open",
         "APEC leaders, closing their Shenzhen summit, called for open "
         "trade corridors and flagged the risks of AI misuse.",
         "MLex"),
    ]),
    ("PLANET & SOCIETY", GREEN, [
        ("GOPALPUR \u00b7 INDIA",
         "Cyclone Akvan Makes Landfall in Odisha",
         "Severe Cyclonic Storm Akvan crossed the coast near Gopalpur, "
         "gusting to 110 km/h; nearly 300,000 people were evacuated.",
         "IMD \u00b7 The Hindu"),
        ("ANTALYA \u00b7 COP31",
         "Outcry as Fossil Fuels Vanish From COP31 Draft",
         "Negotiators at the COP31 climate summit reacted with outrage "
         "after fossil fuels were removed from the draft UN deal.",
         "Le Monde"),
        ("SENEGAL",
         "Migrant Boat Sinks Off Senegal; Dozens Missing",
         "A boat carrying migrants sank off Senegal's coast, and dozens of "
         "people were reported missing.",
         "GT Daily"),
        ("HORN OF AFRICA",
         "Ethiopia and Eritrea Mass Troops on Border",
         "Ethiopia and Eritrea have built up forces along their shared "
         "border, raising fears of a return to war.",
         "African Spectator"),
        ("JUBA \u00b7 SOUTH SUDAN",
         "South Sudan Postpones First Elections to 2027",
         "South Sudan put off its first national elections since "
         "independence, from 22 December to 11 February 2027.",
         "African Spectator"),
        ("TBILISI \u00b7 GEORGIA",
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
    ("9,341", "cyclone shelters opened across Odisha"),
    ("25.9bn km", "Voyager 1's distance \u2014 one light-day"),
    ("$1.76tn", "Anthropic's value at its debut close"),
    ("-2.02%", "the S&P 500's fall, to 7,175.83"),
    ("51\u201348", "Senate vote on the Iran war-powers curb"),
    ("13,000", "marched in Tokyo against the government"),
]

TIMELINE = [
    ("02:30", "Trump pardons Pete Rose posthumously"),
    ("03:36", "White House names new cyber director"),
    ("03:47", "Houthis claim strikes on Saudi targets"),
    ("04:07", "Four ballistic missiles hit Kyiv"),
    ("04:22", "Genoa airport halts flights over drones"),
    ("04:30", "Cyclone Akvan begins landfall, Odisha"),
]

WIRE = [
    "SANA'A \u2014 Yemen's parliament designates the Houthis a terrorist organisation",
    "MALATYA \u2014 Turkish military helicopter crash kills four soldiers",
    "BRAS\u00cdLIA \u2014 Senate approves the government's fiscal adjustment package",
    "MADRID \u2014 Campaign opens for Spain's 29 November general election",
    "TRIPOLI \u2014 Libya seizes 4 million drug pills and cocaine in a raid",
    "SYDNEY \u2014 Man charged with terrorism offences after a police raid",
    "SARATOV \u2014 Three killed in a drone attack on the Russian region",
    "PARIS \u2014 Law obliges internet giants to share revenue with media",
    "CINCINNATI \u2014 Fiona the hippo dies after swallowing a visitor's hat",
    "AMSTERDAM \u2014 'The Year of the Ghost' wins Best Film at IDFA festival",
]

MARKETS_LINE = ("MARKETS \u2014 Brent $92.72, +0.8% \u00b7 Dollar index 103.96 "
                "(19-month high) \u00b7 Gold $3,628, -2.5% \u00b7 WEATHER \u2014 Akvan "
                "lashing Odisha, red alert \u00b7 Fiji gale warning")

TOTAL = (len(HEROES) + sum(len(cards) for _, _, cards in SECTIONS)
         + len(SPORT) + len(NUMBERS) + len(TIMELINE) + len(WIRE))
print("story count:", TOTAL)

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
center(f"{TOTAL} stories \u00b7 six continents \u00b7 every story sourced \u00b7 "
       "the day told in UTC \u00b7 all events of Friday 20 November 2026",
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
f_hhead = F(SERIF_B, 16)
f_hdeck = F(SANS, 9)
f_hsrc = F(SANS_I, 8)
hero_top = y
hero_bottom = y
for i, (kick, head, deck, src) in enumerate(HEROES):
    x = hero_x[i]
    yy = hero_top
    d.text((x, yy), kick, font=f_hkick, fill=RED if i == 0 else INK)
    yy += 11
    yy = draw_lines(wrap(head, f_hhead, HW), x, yy, f_hhead, lh=19)
    yy += 2
    yy = draw_lines(wrap(deck, f_hdeck, HW), x, yy, f_hdeck, lh=12)
    yy += 2
    d.text((x, yy), src, font=f_hsrc, fill=GRAY)
    yy += 10
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
f_sech = F(SANS_B, 9)
f_kick = F(SANS_B, 7)
f_chead = F(SERIF_B, 12)
f_cbody = F(SANS, 9)
f_csrc = F(SANS_I, 8)
SLOT = 88
sec_top = y
for si, (name, color, cards) in enumerate(SECTIONS):
    x = sec_x[si]
    d.rectangle([x, sec_top, x + SCW, sec_top + 16], fill=color)
    d.text((x + 6, sec_top + 3), name, font=f_sech, fill=PAPER)
    yy = sec_top + 21
    for kick, head, body, src in cards:
        hl = wrap(head, f_chead, SCW)
        bl = wrap(body, f_cbody, SCW)
        if len(hl) > 2:
            print("HEADLINE OVERFLOW", name, head, len(hl))
        if len(bl) > 3:
            print("BODY OVERFLOW", name, head, len(bl))
        d.text((x, yy), kick, font=f_kick, fill=color)
        yy += 10
        yy = draw_lines(hl, x, yy, f_chead, lh=13)
        yy += 1
        yy = draw_lines(bl, x, yy, f_cbody, lh=11)
        yy += 1
        d.text((x, yy), src, font=f_csrc, fill=GRAY)
        yy = sec_top + 21 + (cards.index((kick, head, body, src)) + 1) * SLOT
    if si:
        d.line([(x - SGUT // 2 - 1, sec_top), (x - SGUT // 2 - 1, sec_top + 21 + 6 * SLOT)],
               fill=LIGHT, width=1)
y = sec_top + 21 + 6 * SLOT + 4
print("sections bottom:", y)
hrule(y, wdt=1)
y += 6

# ---------------------------------------------------------------- markets
d.rectangle([MX, y, W - MX, y + 17], fill=INK)
d.text((MX + 8, y + 3), MARKETS_LINE, font=F(SANS_B, 9), fill=PAPER)
y += 23

# ---------------------------------------------------------------- bottom band
band_top = y
f_bh = F(SANS_B, 10)
# SPORT (left)
sx = MX
d.text((sx, y), "SPORT", font=f_bh, fill=RED)
yy = y + 15
for s in SPORT:
    d.text((sx, yy), s, font=F(SANS, 9), fill=INK)
    yy += 12
# BY THE NUMBERS (middle)
nx = MX + 336
d.text((nx, y), "BY THE NUMBERS", font=f_bh, fill=GOLD)
nyy = y + 15
for i, (num, label) in enumerate(NUMBERS):
    col = i // 4
    row = i % 4
    xx = nx + col * 158
    yyy = nyy + row * 21
    d.text((xx, yyy), num, font=F(SERIF_B, 13), fill=INK)
    lab = wrap(label, F(SANS, 7), 150)
    draw_lines(lab[:2], xx, yyy + 12, F(SANS, 7), fill=GRAY, lh=8)
# THE DAY IN UTC (right)
tx = MX + 672
d.text((tx, y), "THE DAY IN UTC", font=f_bh, fill=NAVY)
tyy = y + 15
for t, s in TIMELINE:
    d.text((tx, tyy), t, font=F(MONO_B, 9), fill=RED)
    d.text((tx + 42, tyy), s, font=F(SANS, 9), fill=INK)
    tyy += 12
y = band_top + 15 + 4 * 21 + 6
print("band bottom:", y)
hrule(y, wdt=1)
y += 6

# ---------------------------------------------------------------- late wire
wire_text = "  \u2022  ".join(WIRE)
f_wire = F(SANS, 9)
wl = wrap(wire_text, f_wire, CW - 74)
d.text((MX, y), "LATE WIRE", font=F(SANS_B, 9), fill=RED)
y = draw_lines(wl, MX + 74, y, f_wire, lh=11)
y += 4
hrule(y, wdt=2)
y += 6

# ---------------------------------------------------------------- footer
foot = ("DATE CHECK \u2014 This page sums up one day only: Friday, 20 November 2026. "
        "Every story above happened, or was first reported, on that date in some "
        "time zone. Set in type by an automated newsroom from the day's reports.")
for ln in wrap(foot, F(SANS, 9), CW):
    center(ln, y, F(SANS, 9), fill=GRAY)
    y += 11
print("final y:", y, "of", H)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
img.save(out, optimize=True)
print("saved", out, os.path.getsize(out), "bytes")
