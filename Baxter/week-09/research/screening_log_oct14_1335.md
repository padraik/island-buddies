# SCREENING LOG: Wed Oct 14, 1:35pm ET (MIDDAY)

10 names moved: the 6 names queued from the 12:35 fresh scan, plus 4 queue re-tests. 6 killed, 4 parked. No web searches.

## Part 1: the 12:35 scan's leftovers (ratings screen, then date and chain for survivors)

| Ticker | Direction | Price | Ratings (B/H/S), low tgt | Print | Result |
|---|---|---|---|---|---|
| RGC | CALLS | $8.10 (-1.1%) | none | n/a | **KILLED, no coverage** |
| RPC | CALLS | $7.94 (-2.9%) | none | n/a | **KILLED, no coverage** |
| CEPF | CALLS | $10.28 (SPAC) | none | n/a | **KILLED, no coverage** |
| ATII | CALLS | $9.23 (-13.8%, SPAC) | none | n/a | **KILLED, no coverage** |
| ALM | CALLS | $10.10 (-8.0%) | 11/1/0, low $12.85 | Nov 2 AM (f), LY Nov 3 AM | **KILLED, R7.** Nov20 fails R2's 21-day test (Nov 3 + 21 = Nov 24), so Dec18. $2.50 strike grid. $10C 1.45 / 2.20 (OI 112, 41% of mid); $12.5C 0.65 / 1.05 (OI 39, 47%); $15C 0.30 / 0.60 (OI 398, 67%). No strike passes both halves of R7. |
| BOBS | CALLS | $13.165 (-8.1%) | 11/2/0, low $18 | Nov 6 PM (f), no LY (listed this year); scan said Nov 30 | **KILLED, R7.** Nov20 fails R2's 21-day test (Nov 6 + 21 = Nov 27); next expiry Feb19 2027. $12.5C 2.35 / 2.80 (OI 9), $15C 0.15 / 3.60 (OI 9), $17.5C 0.30 / 2.40 (OI 23). OI fails everywhere. |

ALM and BOBS were the two with a real Buy consensus (11 Buys each, 0 Sells) and floors well above the price. Both died on the same thing SLDB did at 12:35: nobody trades the chain.

## Part 2: queue re-tests (live quotes ~17:35 UTC)

| Ticker | Contract | Direction | Stock | Bid / Ask | BE at ask | Needs | R6 cap | R7 (OI / spread) | Result |
|---|---|---|---|---|---|---|---|---|---|
| TTWO | Dec18 $190C (paper) | CALLS | $202.45 (+1.1%) | 24.10 / 26.50 | $216.50 | +6.94% | 7.35% | 849 / 9.5% | PASS R1/R3/R6/R7; R4 dating still open. EVENING 1 paper doc |
| ALGM | Nov20 $35C (paper) | CALLS | $32.11 (-4.6%) | 1.75 / 2.05 | $37.05 | +15.4% | 10.5% | 6,812 / 15.8% | PARK, R6 |
| BTBT | Jan15 $1C (real) | CALLS | $1.09 (-9.9%) | 0.23 / 0.27 | $1.27 | +16.5% | 8.23% | 2,261 / 16% | PARK, R6 |
| ONDS | Dec18 $8C (real) | CALLS | $6.285 (-6.3%) | 0.32 / 0.34 | $8.34 | +32.7% | 20.89% | 38,059 / 6.1% | PARK, R6 |

TTWO's R6 margin shrank (+6.45% -> +6.94% vs 7.35%) because the ask widened to 26.50, not because the stock moved much.

## GLOSSARY
- **R1-R7**: Iron Rules, binder Tab 1. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor, R5 affordability, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven = strike + ask.
- **(f)**: earnings date `verified: false` (estimated). **LY**: last year's same-quarter date.
- **OI**: open interest, contracts outstanding.
- **Paper / real**: paper-book candidate vs. a contract the real fund could afford.
- **SPAC**: special purpose acquisition company, a listed cash shell; usually no analyst coverage.
