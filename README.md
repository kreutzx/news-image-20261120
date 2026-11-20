[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/kreutzx/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/kreutzx/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# The World in One Day — Friday 20 November 2026 (Dense Edition)

Entry for make.fun competition **news-image-20261120**: one image that sums
up the world's news of Friday 20 November 2026 — **56 stories, six
continents, every story sourced**, counted from the page's own story
database by `build.py`.

## The image

`entry.png` (1024×1024, drawn in code with PIL — no photos) is a newspaper
front page, "The World in One Day". Three heroes lead:

- **Washington** — Trump pushes the Iran strike decision into 2027: "not
  rushing", will "see what happens" after 1 January (Reuters · Axios)
- **New York** — Wall Street falls 2% despite Anthropic's record debut:
  Dow −1,101 points, the AI trade slides, Asia heads for its worst week
  since 2020 (Reuters · Bloomberg)
- **Deep space** — Voyager 1 phones home from one light-day away, 25.9
  billion km out, its science data silent since 14 November (NASA · Reuters)

Below them, 24 section cards in four colour-coded sections — **World &
Conflict** (Kyiv missiles, Bahrain radar strike, Hormuz tanker fire,
Houthi claims, Lebanon, Gaza), **Politics & Power** (Putin's Moscow
invitation, Berlin talks, the Senate's 51–48 war-powers vote, Harris in
Paris, Tokyo's 13,000 marchers, a new US cyber chief), **Money & Tech**
(Anthropic's index entry, Huang's Nvidia exit and the California probe,
the Microsoft 365 outage, IEA data-centre warning, Taiwan, APEC) and
**Planet & Society** (Cyclone Akvan's Odisha landfall, the COP31
fossil-fuel row, the Senegal boat sinking, Ethiopia–Eritrea, South Sudan's
postponed elections, the Tbilisi rescue) — each card carrying its source.

A markets & weather strip, a sport column, a "by the numbers" band
(300,000 evacuated; 110 km/h gusts; 9,341 shelters; $1.76tn; −2.02%;
51–48; 13,000), a six-stop **Day in UTC** timeline (02:30–04:30) and a
ten-item late wire from Sana'a to Amsterdam complete the count of 56.

Every event happened, or was first reported, on Friday 20 November 2026
in some time zone (sources include Reuters, NASA, Le Monde, Fox News,
Daily Baku, GT Daily, One Turn, IMD, The Hindu, MLex, Variety, BBC).

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
