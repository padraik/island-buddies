# Screening log: Wed Nov 25, EVENING 1 (6:00pm ET)

**Job:** queue item 1 (FORM re-quote, Apr16 and the Jul16 fallback), then queue item 2 (band C parks, median-first). Nothing held. R5 line: 10% x $715.96 / 100 = **$0.716/share** (3.5/5), so everything below is paper-book size.

**Source:** Robinhood tools, run ~23:00-23:40 UTC Nov 25 on Wednesday's close (market closed Thu Nov 26 for Thanksgiving). 0 web searches.

## 1. FORM re-quote

Stock **$72.25** (-1.4% vs $73.30). Print Feb 3 PM (f).

| Contract | Bid / Ask | Spread | OI | BE at ask | R6 (cap 26.0%) | Verdict |
|---|---|---|---|---|---|---|
| $70C Apr16 `70ed8add` | 15.40 / 18.70 | 19.4% | 6 | $88.70 (+22.8%) | pass | **R7 (OI)** |
| $75C Apr16 `fba780c3` | 13.30 / 15.40 | 14.6% | 15 | $90.40 (+25.1%) | pass | **R7 (OI)** |
| $70C Jul16 `ba73bc5b` | 19.20 / 22.40 | 15.4% | 0 | $92.40 (+27.9%) | fail | R6 + R7 |
| $75C Jul16 `241a55ba` | 16.80 / 20.10 | 17.9% | 0 | $95.10 | fail | R6 + R7 |
| $80C Jul16 `ce2bc12d` | 14.90 / 18.90 | 23.7% | 0 | $98.90 | fail | R6 + R7 |

**FORM stays dead on R7.** The Apr16 chain doesn't trade and the Jul16 chain has no open interest at all. Moved off the active queue to a weekly re-quote line.

## 2. Band C parks, median-first (24 names)

Moves from daily closes (Oct 1 2025 - Nov 24 2026; PM = print day to next day, AM = prior close to print day), the last 5 prints. R1 = closing-range percentile over the last 52 weeks.

| Ticker | Next print (f) | Moves (oldest first) | Median | R1 | Verdict |
|---|---|---|---|---|---|
| OMCL | Feb 4 AM | +13.6 / -16.3 / +20.9 / -10.4 / +2.6 | **13.56%** | 0.129 | to the chain |
| NSSC | Feb 1 AM | -7.7 / +11.2 / -15.2 / -1.3 / -18.4 | **11.20%** | 0.065 | to the chain |
| FLEX | Feb 3 AM | +2.9 / -10.9 / +39.7 / -9.1 / +11.6 | **10.85%** | 0.094 | to the chain |
| NOW | Jan 27 PM | +2.5 / -9.9 / -17.7 / -3.7 / -26.9 | **9.94%** | 0.097 | to the chain |
| BROS | Feb 11 PM | -4.2 / +4.7 / -9.3 / -18.8 / -21.4 | **9.35%** | 0.046 | to the chain |
| IPGP | Feb 11 AM | -2.2 / +35.5 / -25.7 / +7.9 / +2.1 | 7.88% | 0.013 | **KILLED R6 structural** |
| ROAD | Feb 4 AM | -3.6 / +11.2 / +6.9 / +19.5 / -7.4 | 7.44% | 0.013 | **KILLED R6 structural** |
| BKR | Jan 25 PM | -3.3 / +6.9 / -7.4 (2 dates fell on weekends) | 6.90% | 0.056 | **KILLED R6 structural** |
| APTV | Feb 1 AM | -4.3 / +2.9 / -7.9 / -16.6 / -6.5 | 6.53% | 0.050 | **KILLED R6 structural** |
| AGIO | Feb 11 AM | +2.9 / +1.3 / +13.1 / -6.5 / -9.9 | 6.46% | 0.339 | **MID-OUT (R1)** |
| UBER | Feb 3 AM | -5.1 / -5.1 / +8.5 / -5.3 / +4.9 | 5.15% | 0.042 | **KILLED R6 structural** |
| GLW | Jan 27 AM | -3.3 / -5.0 / -8.9 / -12.1 / -1.1 | 4.98% | 0.110 | **KILLED R6 structural** |
| BWA | Feb 10 AM | +3.1 / +22.5 / +3.8 / +5.9 / -4.7 | 4.70% | 0.224 | **KILLED R6 structural** |
| TPG | Feb 4 AM | -2.6 / -4.5 / +1.4 / +5.7 / +7.5 | 4.55% | 0.282 | **MID-OUT (R1)** |
| WFRD | Feb 2 PM | +0.6 / +4.1 / +1.4 / +4.5 / +7.8 | 4.15% | 0.058 | **KILLED R6 structural** |
| HLNE | Feb 2 AM | +6.4 / -3.7 / +4.1 / +7.1 / +0.9 | 4.09% | 0.130 | **KILLED R6 structural** |
| GGG | Jan 25 PM | +0.1 / +1.0 / -3.9 / +5.2 / -15.3 | 3.94% | 0.210 | **KILLED R6 structural** |
| TRMB | Feb 9 AM | +2.5 / +2.9 / -7.2 / -2.8 / -17.3 | 2.91% | 0.166 | **KILLED R6 structural** |
| ALLY | Jan 20 AM | +3.6 / +0.0 / +8.1 / -2.4 / +1.0 | 2.39% | 0.124 | **KILLED R6 structural** |
| WAL | Jan 25 PM | +3.2 / +1.2 / +0.7 / +3.6 / +2.3 | 2.27% | 0.127 | **KILLED R6 structural** |
| ESAB | Feb 19 AM | -5.6 / -1.5 / +0.8 / +2.2 / +3.0 | 2.21% | 0.186 | **KILLED R6 structural** |
| KKR | Feb 4 AM | +1.7 / -5.3 / -1.3 / +1.7 / +1.7 | 1.68% | 0.156 | **KILLED R6 structural** |
| CARR | Feb 4 AM | +0.8 / -0.7 / +8.8 / -8.9 / -1.3 | 1.30% | 0.106 | **KILLED R6 structural** |
| SYF | Jan 26 AM | -0.7 / -5.8 / -1.2 / -1.6 / -1.2 | 1.21% | 0.167 | **KILLED R6 structural** |

### Ratings on the five chain names

| Ticker | Close Nov 25 | B/H/S | Low target | Stamp | R3 | Floor vs stock | R6 cap (1.5x) |
|---|---|---|---|---|---|---|---|
| OMCL | 34.59 | 7/1/0 | 50 | none | pass | +44.6% | 20.3% |
| NSSC | 30.46 | 6/0/0 | 42 | none | pass | +37.9% | 16.8% |
| FLEX | 67.34 | 16/0/0 | 84 | none | pass | +24.7% | 16.3% |
| NOW | 92.16 | 45/4/1 | 100 | Oct 29 (session after the Oct 28 print) | pass (1 Sell) | +8.5% | 14.9% |
| BROS | 36.09 | 27/2/0 | 38 | Nov 5 (session after the Nov 4 print) | pass | +5.3% | 14.0% |

### R2 expiries

Rule 2: expiry at least 21 days after the later of (tool date, last year's date), and the 10-Q/10-K deadline at least 5 trading days before expiry.
- **NOW** (Dec FY, large accelerated): Jan 27 / LY Jan 28 -> Feb 18. Feb19 fails (b): 10-K deadline Mar 1 is after it. **Mar19** passes (10-K Mar 1, 14 trading days before).
- **NSSC** (FQ2 ends Dec 31, 10-Q): Feb 1 / LY Feb 2 -> Feb 23, 10-Q Feb 9. **Mar19.**
- **FLEX** (FQ3 ends Dec 31, 10-Q): Feb 3 / LY Feb 4 -> Feb 25; no Mar19 listed. **Apr16.**
- **OMCL** (Dec FY): Feb 4 / LY Feb 5 -> Feb 26; chain lists Feb19 then May21. **May21.**
- **BROS** (Dec FY): Feb 11 / LY Feb 12 -> Mar 5; no Mar19 listed. **Apr16.**

### Chains (closing quotes, 3:59pm Nov 25)

| Contract | Bid / Ask | Spread | OI | BE at ask | Move to BE | R4 (BE < low) | R6 | R7 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| OMCL $35C May21 | 3.90 / 6.70 | 53% | 2 | $41.70 | +20.6% vs 20.3% | pass | fail (0.3 pt) | fail | **KILLED R6 + R7** |
| OMCL $40C May21 | 2.30 / 4.70 | 69% | 2 | $44.70 | +29.2% | pass | fail | fail | KILLED R6 + R7 |
| NSSC $30C Mar19 | 2.15 / 5.10 | 81% | 1 | $35.10 | +15.2% vs 16.8% | pass | pass | fail | **KILLED R7** |
| NSSC $35C Mar19 | 0.00 / 3.50 | -- | 3 | $38.50 | +26.4% | pass | fail | fail | KILLED R6 + R7 |
| FLEX $70C Apr16 | 10.60 / 12.80 | 18.8% | 41 | $82.80 | +23.0% vs 16.3% | pass | fail | fail (OI) | **KILLED R6 + R7** |
| BROS $35C Apr16 | 5.30 / 6.60 | 21.8% | 93 | $41.60 | +15.3% vs 14.0% | fail ($38) | fail | fail (OI) | **KILLED R4 + R6 + R7** |
| NOW $90C Mar19 | 13.40 / 14.10 | 5.1% | 771 | $104.10 | +13.0% | **fail ($100)** | pass | pass | R4 |
| NOW $85C Mar19 | 15.90 / 16.95 | 6.4% | 403 | $101.95 | +10.6% | fail | pass | pass | R4 |
| NOW $80C Mar19 `cf99017d` | 18.95 / 20.25 | 6.6% | 363 | $100.25 | +8.8% | fail by $0.25 | pass | pass | R4 (passes at mid, $99.60) |
| **NOW $75C Mar19** `16d51634` | 22.30 / 23.70 | 6.1% | 251 | **$98.70** | +7.1% | pass ($1.30) | pass | pass (OI by 1) | **ADVANCE (paper)** |
| **NOW $70C Mar19** `deca0cea` | 25.90 / 27.40 | 5.6% | 376 | **$97.40** | +5.7% | pass ($2.60) | pass | pass | **ADVANCE (paper)** |

**NOW advances to the paper book.** It's the first liquid name since GOOGL to pass R1, R2, R3, R4, R6 and R7 on one contract: 9.9% median print, 0.097 on its range after a -26.9% Oct 28 print, 45 Buys. Things the doc has to deal with:
- **Deep ITM.** The $70C is $22.16 intrinsic + $5.24 time value at the ask (delta 0.83), the same shape as AVGO $280C and GOOGL $200C. Bearxter argued against that shape on AVGO; the doc has to answer it again.
- **R4 room is thin.** $100 is only 8.5% over the stock. The $70C has $2.60 of room; the $75C has $1.30 and OI of 251, one contract over the floor.
- **One Sell.** NOW is 45/4/1. That passes R3 (max 1), and it's the first one-Sell name that's gotten this far, which makes it a data point for the sweep's Rule 3 agenda item.
- **Correlation:** GOOGL $200C Mar19 is already open in the paper book. Both are large-cap AI/software. Macxter's take.
- **Floor owner and date:** the tool's Oct 29 stamp is when the aggregate last changed, not necessarily when the $100 was published. One search would settle whose $100 it is and when it was set.

## Tally

25 moved (FORM + 24 band C). 1 advanced (NOW, paper). Killed: FORM R7; OMCL R6+R7; NSSC R7; FLEX R6+R7; BROS R4+R6+R7; AGIO, TPG R1; 17 R6 structural. 0 searches.

## GLOSSARY

- **R1-R7:** the Iron Rules, binder Tab 1. R1 range (bottom 25%), R2 earnings before expiry, R3 analyst consensus, R4 lowest Buy target above breakeven, R5 price cap on reserve, R6 move to breakeven no more than 1.5x the median earnings move, R7 liquidity (OI >= 250, spread <= 25% of mid).
- **Median print / median move:** the middle of the absolute one-day stock moves on recent earnings reports.
- **R6 structural:** the median is so small that no affordable strike could fit inside 1.5x of it, so the name dies before any chain check.
- **MID-OUT:** the stock sits in the middle of its 52-week range (25-74%), so it isn't a calls or puts candidate.
- **BE (breakeven):** strike + premium paid. At the ask = using the price you'd actually pay.
- **OI (open interest):** contracts currently outstanding on that strike. Low OI means a thin market.
- **Spread:** ask minus bid, as a percent of the midpoint.
- **Deep ITM:** in the money by a lot. Most of the price is intrinsic value, and the option moves almost like the stock (delta near 1).
- **Delta:** how much the option moves per $1 move in the stock.
- **Large accelerated filer (LA):** a big SEC filer with a 60-day 10-K deadline (Mar 1 for a December year-end).
- **(f):** the earnings date is estimated, not announced (`verified: false`).
- **Paper book:** `Baxter/paper_book.md`, entries with no money, used to test the rules on names the real fund can't afford.
- **Stamp:** the `updated_at` date on the analyst-ratings aggregate.
