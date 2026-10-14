# SCREENING LOG: Wed Oct 14, 12:35pm ET (MIDDAY)

10 names moved: 4 queue re-tests + 6 new names from a fresh under-$15 scanner pass. 6 killed, 4 parked. No web searches.

## Part 1: queue re-tests (live quotes ~16:35 UTC)

| Ticker | Contract | Direction | Stock | Bid / Ask | BE at ask | Needs | R6 cap | R7 (OI / spread) | Result |
|---|---|---|---|---|---|---|---|---|---|
| TTWO | Dec18 $190C (paper) | CALLS | $202.92 (+1.3%) | 24.20 / 26.00 | $216.00 | +6.45% | 7.35% | 849 / 7.2% | PASS R1/R3/R6/R7; R4 dating still open. EVENING 1 paper doc |
| ALGM | Nov20 $35C (paper) | CALLS | $32.23 (-4.2%) | 1.90 / 2.05 | $37.05 | +14.95% | 10.5% | 6,812 / 7.6% | PARK, R6 |
| BTBT | Jan15 $1C (real) | CALLS | $1.105 (-8.7%) | 0.24 / 0.30 | $1.30 | +17.6% | 8.23% | 2,261 / 22% | PARK, R6 |
| ONDS | Dec18 $8C (real) | CALLS | $6.335 (-5.6%) | 0.34 / 0.36 | $8.36 | +32.0% | 20.89% | 38,059 / 5.7% | PARK, R6 |

## Part 2: fresh scanner pass

Preview scan (not saved): market cap >= $300M, earnings Oct 20 - Dec 11, price $0.50-15, 52-week range pct < 0.25. Three price bands so each came in under the 200-row cap: $0.50-15 (391 total, top 200 shown, $8.18-14.985), $0.50-8.20 (259 total, top 200, $2.305-8.20), $0.50-2.32 (62, complete). Every row diffed against tickers named in week-08/09 research, research_queue.md, passes.md, paper_book.md and the Oct 10-14 journals. The universe was swept on Oct 12-13, so only names that fell into the bottom quartile since then (small-cap selloff Oct 13-14) are new: **12 new**. Diff caveat: it matches any capitalized 1-5 letter word, so a ticker that happens to be a common word (OPEN, LOT) counts as "seen" even if it was never screened. Those two were screened before anyway (OPEN in the Oct 12 pass).

Screened this run (the 6 cheapest, most relevant to real money at the $0.676 line):

| Ticker | Direction | Price | Range pct | Print | Ratings (B/H/S), low tgt | Result |
|---|---|---|---|---|---|---|
| SLDB | CALLS | $5.52 (-5.1%) | 0.226 | Nov 2 PM (f), LY Nov 3 PM | 13/0/0, low $11 | **KILLED, R7** (and R6). Dec18 chain (Nov20 fails R2's 21-day test): OI 0-1 on $4/$5/$6, quotes 0.10 / 4.90 or no bid. R6: 6-print median 4.04% (1.6, 10.6, 15.3, 1.3, 4.4, 3.7), cap 6.06%, BE must be <= ~$5.86 |
| GTN.A | CALLS | $4.84 (-9.5%) | 0.013 | none in tool | 4/1/1, low $3 | **KILLED, no listed options** (empty chain) |
| EDIT | CALLS | $2.275 (-7.0%) | 0.230 | Nov 10 | 8/2/2 | **KILLED, R3** (2 Sells) |
| ACDC | CALLS | $4.265 (-6.5%) | 0.231 | Nov 10 | none | **KILLED, no coverage** |
| NUAI | CALLS | $3.57 (-16.8%) | 0.209 | Nov 30 | none | **KILLED, no coverage** |
| SES | CALLS | $0.945 (-5.5%) | 0.140 | Nov 5 | none | **KILLED, no coverage** |

Queued for the next run (not screened, batch cap): **RGC** $7.94 (Nov 20 scan date, range 0.053), **RPC** $7.94 (Nov 6, 0.245), **BOBS** $13.13 (Nov 30, 0.247), **ALM** $10.14 (Nov 3, 0.248), **CEPF** $10.26 and **ATII** $9.92 (both SPACs, expect no coverage).

## GLOSSARY
- **R1-R7**: Iron Rules, binder Tab 1. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor, R5 affordability, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven = strike + ask.
- **(f)**: earnings date `verified: false` (estimated). **LY**: last year's same-quarter date.
- **Range pct**: (price - 52w low) / (52w high - 52w low).
- **Paper / real**: paper-book candidate vs. a contract the real fund could afford.
