[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/kreutzx/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/kreutzx/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# The World in One Day — Friday 20 November 2026 (Legibility Edition)

Entry for make.fun competition **news-image-20261120**: one image that sums
up the world's news of Friday 20 November 2026 — **37 stories, 14 drawn
panels, six continents, every story sourced and certainty-tagged**, counted
from the page's own story database by `build.py`. This edition trades raw
density for legibility: bigger type, a cleaner hierarchy, and a drawn
picture on the stories that matter most.

## The image

`entry.png` (1024×1024, drawn in code with PIL — no photos) is a newspaper
front page, "The World in One Day". Three heroes lead, each with its own
drawn panel (the Capitol, the falling chart, the Voyager probe):

- **Washington** — Trump pushes the Iran strike decision into 2027: "not
  rushing", will "see what happens" after 1 January (Reuters · Axios)
- **New York** — Wall Street falls 2% despite Anthropic's record debut:
  Dow −1,101 points, the AI trade slides, Asia heads for its worst week
  since 2020 (Reuters · Bloomberg)
- **Deep space** — Voyager 1 phones home from one light-day away, 25.9
  billion km out, its science data silent since 14 November (NASA · Reuters)

Below them, 16 section cards in four colour-coded sections — **World &
Conflict** (Kyiv missiles, Bahrain radar strike, Hormuz tanker fire,
Lebanon), **Politics & Power** (Putin's Moscow invitation, the Senate's
51–48 war-powers vote, Tokyo's 13,000 marchers, Harris in Paris), **Money
& Tech** (Anthropic's index entry, Huang's Nvidia exit and the California
probe, the Microsoft 365 outage, the IEA data-centre warning) and
**Planet & Society** (Cyclone Akvan's Odisha landfall, the COP31
fossil-fuel row, the Senegal boat sinking, the Tbilisi rescue) — each card
carrying its source, a certainty tag (CONFIRMED · REPORTED · DEVELOPING ·
FORECAST) and, on eleven of them, a drawn panel: missile trails over
Kyiv, the burning tanker, the Kremlin wall, the Senate chamber, the
Eiffel Tower, the index bars, the Nvidia chip, the outage cloud, the
cyclone spiral, the factory and the leaf, the migrant boat.

A markets & weather strip, a sport column, a "by the numbers" band
(300,000 evacuated; 110 km/h gusts; 25.9bn km; $1.76tn; −2.02%; 51–48), a
four-stop **Day in UTC** timeline (02:30–04:30), a three-item late wire
(Malatya, Madrid, Sydney) and a DATE CHECK box listing what was checked
and left out complete the count of 37.

Every event happened, or was first reported, on Friday 20 November 2026
in some time zone (sources include Reuters, NASA, Le Monde, Fox News,
Daily Baku, GT Daily, IMD, The Hindu, BBC, CLSTR, News.Az).

## The programs

- `build.py` renders `entry.png` from the story database at its top —
  deterministic: fixed data, no clock, no network, byte-identical reruns.
- `main.py` (Python 3.13, standard library only) validates the PNG and
  copies it to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR` when set):

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
