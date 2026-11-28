# Screening log: Fri Nov 27, EVENING 3 (10:00pm ET)

**Job:** EVENING 3 refills the queue and leaves PREMARKET a plan. Queue item 1 was fresh supply: band C ($25-100) and band D ($100+) scans with the print window moved to **Jan 15 - Mar 31**, diffed against every week-09 log. Then the CHRW R1 re-check, then the weekly re-quote line (pulled tonight instead of Saturday; Friday's 1pm quotes are the last ones until Monday, so Saturday would see the same numbers). Nothing held. R5 line: 10% x $715.96 / 100 = **$0.716/share** (3.5/5).

**Source:** Robinhood tools, run ~03:00-03:20 UTC Nov 28 on Friday's 1pm close. 0 web searches.

## 1. Fresh band C/D scans (Jan 15 - Mar 31 prints)

Same filters as every week-09 sweep: market cap $300M+, stock, `FILTER_TYPE_EARNINGS_DATE` 20270115-20270331, R1 expression < 0.25, split by `FILTER_TYPE_LAST`.

| Scan | ID | Rows | Never worked in week-09 |
|---|---|---|---|
| Band D $100+ | `52c79307-721c-4442-9bad-686be5a0f1c2` | 104 | SPCX, NOVT, AGM.A |
| Band C $25-100 (capped at 200, covers $34.39-100) | `b6dbd264-4f3b-4ba9-a816-fa326dc28075` | 270 | IMKTA |
| Band C-low $25-34.39 | `31f26969-4131-4f86-a4fb-4baf4a9dbd15` | 71 | CLMT |

Diff: whole-word match against all week-09 research files. Short tickers (Z, ZG, AD, AB, PUK, FORTY) checked by hand: all appear in earlier logs with a kill or a no-coverage line.

## 2. Never-worked names, rated

| Ticker | Name | Last | Print (scanner) | R1 | Ratings (B/H/S) | Low target | Result |
|---|---|---|---|---|---|---|---|
| SPCX | SpaceX | 132.63 | Feb 26 | 0.230 | 37/8/3 | 105 | **KILLED R3** (3 Sells, max is 1) |
| NOVT | Novanta | 116.72 | Feb 24 | 0.206 | no coverage | n/a | **KILLED R3** (no coverage) |
| AGM.A / AGM | Federal Agricultural Mortgage | 122.44 | Feb 19 | 0.107 | no coverage (either class) | n/a | **KILLED R3** (no coverage; AGM.A volume 0) |
| IMKTA | Ingles Markets | 73.69 | Feb 5 | 0.208 | no coverage | n/a | **KILLED R3** (no coverage) |
| CLMT | Calumet | 27.48 | Feb 26 | 0.224 | 2/4/0 | 37 | **KILLED R3** (2 Buys, needs 3 and Buys >= Holds) |

## 3. CHRW R1 re-check

Last regular trade **$147.00** (Fri 12:59pm), same as EVENING 1 and 2. R1 0.264, still over the line (needs a close under ~$145.80). Stays on the queue for Monday's close.

## 4. Weekly re-quote line (Fri 12:59pm quotes)

| Contract | Bid / ask | OI (last week) | Stock | BE at ask | Result |
|---|---|---|---|---|---|
| RRX May21 $150C `01c93b13` | 31.10 / 34.20 | 3 (3) | 161.52 | 184.20 (+14.0%) | **R7** |
| TER Mar19 $200C `87acbe81` | 49.40 / 55.90 | 28 (22) | 222.94 | 255.90 (+14.8%) | **R7** (only mover on OI) |
| IDCC Mar19 $260C `c45b486d` | 27.80 / 30.60 | 2 (2) | 260.29 | 290.60 (+11.6%) | **R7** |
| IDCC Mar19 $250C `c4525159` | 32.80 / 35.80 | 2 (2) | 260.29 | 285.80 (+9.8%) | **R7** (20 traded Friday, OI not yet updated) |
| SANM Apr16 $150C `c6f02583` | 23.30 / 25.80 | 60 (60) | 145.57 | 175.80 (+20.8%) | **R7** |
| FORM Apr16 $70C `70ed8add` | 16.30 / 18.80 | 6 (6) | 74.41 | 88.80 (+19.3%) | **R7** |
| NSSC Mar19 $30C `cb60c11a` | 2.60 / 4.30 | 1 (1) | 30.86 | 34.30 (+11.1%) | **R7** (spread 49%) |
| BFAM Mar19 $45C `d588a1a9` | 8.50 / 12.80 | 0 (0) | 53.36 | 57.80 (+8.3%) | **R7** (spread 40%) |
| WMS Mar19 $110C / $115C / $120C | 15.60/18.50, 12.70/15.50, 10.00/12.70 | 0 / 1 / 1 | 121.20 | 128.50 / 130.50 / 132.70 | **R7** |

No contract on the line is within reach of OI 250. Nobody's trading these between now and the January prints; next re-quote Sat Dec 5.

## Summary

14 names moved: 5 never-worked (all R3), CHRW R1 (unchanged), 8 re-quote names (all R7). 0 advanced, 0 docs, 0 buyable, 0 searches.

**The finding:** the Jan 15 - Mar 31 C/D universe is fully worked. 375 rows across the two bands, 5 names the week hadn't seen, and none of those has an analyst board that passes R3. With A/B re-run at 8pm (2 new, both dead), the whole bottom-quartile universe for the Q4 print season has now been through the funnel at least once. New supply comes from price movement (names crossing under 0.25) and from the post-Dec 1 A/B re-run, not from new scans.

## GLOSSARY

- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry, R3 ratings mix, R4 bear floor, R5 price cap on reserve, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **Never worked:** a ticker that doesn't appear in any week-09 screening log or research file.
- **No coverage:** the ratings tool has too few analysts to report; R3 can't pass without at least 3 Buys.
- **BE (breakeven):** strike + premium paid. The stock has to be above this at expiry for the call to make money.
- **OI (open interest):** contracts outstanding. Low OI means a thin market and a wide spread to get out.
- **Re-quote line:** contracts that pass every rule except R7; checked once a week, not every run, in case liquidity shows up.
- **Band A/B/C/D:** price bands for the scanner ($1-8.19 / $8.19-25 / $25-100 / $100+). A/B are real-money size; C/D are paper-book size.
