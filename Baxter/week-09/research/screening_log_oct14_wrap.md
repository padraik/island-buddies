# Screening log: Wed Oct 14, 4:15pm ET (WRAP)

**Source:** the 10-name research queue, re-tested at the regular-session close. WRAP is a PREPARE slot; free quote re-tests only, no chain pulls, no web searches. Closing quotes 3:59-4:00pm ET (pulled ~20:16 UTC). Reserve $676.28, 3.5/5 line $0.676.

**Moved this session:** 6 contracts re-quoted at the close (TTWO, ALGM, BTBT, ONDS, FN, LEU), 4 stock-only checks (ALNY, HII, SE, AVAV). 0 killed, 1 pass (TTWO, paper), 5 parked on R6, 4 parked on R7 (OI is a daily number, re-pull at OPEN).

## Part 1: R6 re-tests at the close

| Ticker | Contract | Direction | Stock (day) | Bid / Ask | BE at ask | Needs | R6 cap | R7 (OI / spread) | Result |
|---|---|---|---|---|---|---|---|---|---|
| TTWO | Dec18 $190C (paper) | CALLS | $201.21 (+0.4%) | 23.00 / 24.50 | $214.50 | +6.60% | 7.35% | 849 / 6.3% | PASS R1/R3/R6/R7; margin 0.75 pts (wider than 3:35's 0.33, the ask came in a dollar). R4 dating still open. EVENING 1 paper doc |
| ALGM | Nov20 $35C (paper) | CALLS | $32.20 (-4.3%) | 1.80 / 2.15 | $37.15 | +15.4% | 10.5% | 6,812 / 17.7% | PARK, R6 |
| BTBT | Jan15 $1C (real) | CALLS | $1.07 (-11.6%) | 0.18 / 0.36 | $1.36 | +27.1% | 8.23% | 2,261 / 66.7% | PARK, R6. Closing spread doubled (0.24 / 0.25 at 3:35); R7 would fail too at this quote, but it's end-of-day width. Re-quote at OPEN |
| ONDS | Dec18 $8C (real) | CALLS | $6.145 (-8.4%) | 0.29 / 0.32 | $8.32 | +35.4% | 20.89% | 38,059 / 9.8% | PARK, R6. Friday drop-to-bottom test per queue note |
| FN | Dec18 $460C (paper) | CALLS | $392.93 (-8.2%) | 23.40 / 28.10 | $488.10 | +24.2% | see `screening_log_oct14_1435.md` | 70 / 18.3% | PARK; R6 kill check at OPEN against the logged cap |
| LEU | Dec18 $140C (paper) | CALLS | $119.915 (-10.7%) | 7.20 / 9.60 | $149.60 | +24.8% | see `screening_log_oct14_1435.md` | 154 / 28.6% | PARK; R6 kill check at OPEN. Closing spread fails R7 as well |

## Part 2: stock checks on R7-parked names

| Ticker | Stock | Day | Note |
|---|---|---|---|
| ALNY | $224.42 | +0.3% | OI was 131 (falling). Re-pull OI at OPEN; kill if it fell again |
| HII | $264.53 | +2.6% | OI 227, needs 250. Stock moved toward the $270 strike |
| SE | $95.32 | -0.6% | OI 161; also needs a dated R4 floor |
| AVAV | $120.54 | -5.2% | OI 112. The stock is moving away from the $135 strike; check R6 before OI at OPEN |

Same tape as all afternoon: the small and mid caps on the list closed red (BTBT -11.6%, LEU -10.7%, ONDS -8.4%, FN -8.2%, AVAV -5.2%, ALGM -4.3%). TTWO is the only queue name that improved into the close.

## GLOSSARY
- **R1-R7**: Iron Rules, binder Tab 1. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 bear floor, R5 affordability, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **BE**: breakeven = strike + ask.
- **OI**: open interest, contracts outstanding; updates once a day.
- **Paper / real**: paper-book candidate vs. a contract the real fund could afford.
- **Park**: stays on the queue, re-tested later; not killed.
- **WRAP**: the 4:15pm ET run; no trading tools, marks the book, prepares the next day's list.
