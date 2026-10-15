# SCREENING LOG: Thu Oct 15, 12:35pm ET (MIDDAY)

10 names moved: 5 queue re-tests + 5 new names from a fresh under-$5 scanner pass. 5 killed (all new), 0 advanced. No web searches.

## Part 1: queue re-tests (live quotes ~16:35 UTC)

| Ticker | Contract | Direction | Stock | Bid / Ask | BE at ask | Needs | R6 cap | R7 (OI / spread) | Result |
|---|---|---|---|---|---|---|---|---|---|
| PAAS | Jan15 $40C (paper) | CALLS | $43.15 (+1.9%) | 5.50 / 6.10 | $46.10 | n/a | BE <= $46.34 | 5,368 / 10.3% | PARK, R1: 0.273, 84 cents over the $42.31 line |
| TTWO | Dec18 $190C (paper) | CALLS | $209.06 (+3.9%) | 27.60 / 29.90 | $219.90 | +5.18% | 7.35% | 854 / 8.0% | PARK, Argus $192 gate (Fri WRAP re-vote) |
| ALGM | Nov20 $35C (paper) | CALLS | $31.67 (-1.7%) | 1.60 / 1.75 | $36.75 | +16.0% | 10.5% | 6,816 / 9.0% | PARK, R6 (Fri WRAP kill if >15% short) |
| BTBT | Jan15 $1C (real) | CALLS | $1.045 (-2.8%) | 0.20 / 0.23 | $1.23 | +17.7% | 8.23% | 3,275 / 14.0% | PARK, R6 |
| ONDS | Dec18 $8C (real) | CALLS | $6.20 (+1.0%) | 0.32 / 0.35 | $8.35 | +34.7% | 20.89% | 37,968 / 9.0% | PARK, R6 |

Ratings re-pulled: no change (PAAS 7/2/0 low $51, TTWO 29/1/1 low $270, ALGM 14/1/0 low $48, BTBT 6/0/0 low $3.50, ONDS 11/0/0 low $13).

## Part 2: fresh scanner pass

Preview scan (not saved): market cap >= $300M, earnings Oct 20 - Dec 11, price $0.50-5, 52-week range pct < 0.25. **151 rows** (complete, under the 200 cap). Diffed against every capitalized token in week-08/09 research, passes.md, paper_book.md, research_queue.md and the Oct 10-15 journals: **5 new**.

| Ticker | Direction | Price | Range pct | Print | Ratings (B/H/S), low tgt | Result |
|---|---|---|---|---|---|---|
| ANNX | CALLS | $3.555 (-3.1%) | 0.219 | Nov 9 PM (f), LY Nov 10 PM | 9/2/0, low $7 | **KILLED, R7 + R5.** Nov20 fails R2's 21-day test, so Dec18. $3C: no bid / 4.30 (OI 601). $4C: no bid / 3.40, OI 185. $5C: 0.85 / 1.15 (OI 6,979), spread 30% of mid (R7), ask over the $0.676 line (R5), BE $6.15 = +73% |
| LND | CALLS | $3.60 (-2.2%) | 0.213 | Nov 5 | none | **KILLED, no coverage** |
| HYLN | CALLS | $3.24 (-3.9%) | 0.242 | Nov 11 | none | **KILLED, no coverage** |
| VFF | CALLS | $2.575 (+0.6%) | 0.242 | Nov 10 | none | **KILLED, no coverage** |
| SID | CALLS | $1.165 (-3.7%) | 0.241 | Nov 10 | 0/7/4 | **KILLED, R3** (4 Sells, 0 Buys) |

The under-$5 bottom quartile with a print in window is otherwise all names already screened. Next new names come from the $5-15 band (EVENING 3) or from prices moving.

## GLOSSARY
- **R1-R7**: Iron Rules, binder Tab 1. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor, R5 affordability, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven = strike + ask.
- **(f)**: earnings date `verified: false` (estimated). **LY**: last year's same-quarter date.
- **Range pct**: (price - 52w low) / (52w high - 52w low).
- **Paper / real**: paper-book candidate vs. a contract the real fund could afford.
