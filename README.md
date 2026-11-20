# The World in One Day — Friday 20 November 2026

Entry for make.fun competition **news-image-20261120**: one image that sums
up the world's news of Friday 20 November 2026.

## The image

`entry.png` (1024×1024) is a front page, "The World in One Day", drawn for
this entry. Lead story: **Trump puts the Iran war decision off to 2027** —
the president says there is "no rush" and he will "see what happens" after
1 January. Sixteen more stories from the day, across regions and fields:

- **Business** — Anthropic ends its record IPO debut up 17% ($1.8 trillion)
- **India** — Cyclone Akvan strikes the Odisha coast; 300,000 evacuated
- **Space** — Voyager 1 passes one light-day from Earth; Hayabusa2's
  asteroid landing is called off after engine trouble
- **Culture** — GTA 6 sales pass The Odyssey's $1.80bn global run
- **Europe** — Europe ready for Russia peace talks on Ukraine
- **America** — Trump pardons baseball's Pete Rose; White House cyber
  chief ousted after a wave of tech outages
- **Middle East** — Houthi strike damages a Riyadh tower
- **Asia** — South Korea's exports top $1 trillion; Taiwan acts to steady
  tumbling stocks
- **Japan** — Takaichi dodges the Taiwan contingency question
- **Ukraine** — Russia "open" to NATO-like guarantees, says US envoy
  Kushner; blast near the Dutch embassy in Kyiv
- **Tech** — California opens a probe into Nvidia
- **India** — Modi opens the FICCI centenary

A "Day in UTC" timeline runs along the foot of the page. Every event was
first reported on 20 November 2026 (sources: Reuters, BBC, The Hindu,
NASA, JAXA, IMD, AP).

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR` when set):

```
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
