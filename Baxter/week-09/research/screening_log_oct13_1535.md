# Screening log, Tue Oct 13, 3:35pm ET (LASTCALL, PREPARE)

*Live data pulled 19:35-19:40 UTC. Reserve $676.28 (3.5/5 line $0.676). LASTCALL is a PREPARE slot: re-tests, then the free steps only (scanner, ratings, earnings dates) on the $50-100 band of the Oct 20 - Nov 20 print window, so EVENING 1 starts at the chain stage. No chain checks, no web searches.*

## Re-tests (parked on R6)

| Name | Contract | Stock | Quote | BE at ask | Needs | R6 cap | Result |
|---|---|---|---|---|---|---|---|
| BTBT | Jan15 $1C | 1.225 (-1.2%) | 0.32 / 0.38 (OI 2,252) | 1.38 | +12.7% | 8.23% | **PARK** (passes at stock >= ~$1.275 with a 0.38 ask) |
| ONDS | Dec18 $8C | 6.68 (+0.1%) | 0.44 / 0.46 (OI 37,782) | 8.46 | +26.6% | 20.89% | **PARK** |
| ALGM | Nov20 $35C (paper) | 33.455 (-1.0%) | 2.30 / 2.60 (OI 6,793) | 37.60 | +12.4% | 10.5% | **PARK** |

## Scanner, prints Oct 20 - Nov 20, range pct < 0.25, cap >= $300M, Last $50-100 (preview, not saved)

121 matches, 121 rows returned. Diff (whole-word ticker match against every week-09 file plus passes.md and paper_book.md, same as 1:35 and 2:35): **17 new**. The >$100 band is left for EVENING 1.

## Free screen (R3 / R4 proxy, one ratings call)

| Name | Last | Range pct | Print (scanner) | Buy / Hold / Sell | Low target | Result |
|---|---|---|---|---|---|---|
| RMBS | 98.13 | 0.21 | Oct 26 | 8 / 2 / 1 | $100 | **KILL, R4 proxy** (floor 1.9% over the stock; no strike's BE fits under $100) |
| OMAB | 90.00 | 0.04 | Oct 23 | 5 / 9 / 2 | $100.87 (stamped 2020) | **KILL, R3** |
| BNTX | 89.62 | 0.23 | Nov 3 | 14 / 9 / 0 | $83.78 | **KILL, R4 proxy** (floor below the stock) |
| VC | 86.98 | 0.08 | Oct 23 | 8 / 4 / 0 | $104 | ADVANCE |
| ITRI | 86.58 | 0.14 | Oct 27 | 12 / 2 / 0 | $115 | ADVANCE |
| LRN | 83.65 | 0.24 | Oct 20 | 4 / 2 / 0 | $90 | ADVANCE |
| ALGT | 72.58 | 0.23 | Nov 4 | 12 / 3 / 0 | $85 | ADVANCE |
| CASH | 71.93 | 0.17 | Oct 21 | none | | **KILL, no coverage** |
| BYD | 70.31 | 0.20 | Oct 22 | 8 / 12 / 0 | $78 | **KILL, R3** (Buys < Holds) |
| ADC | 65.56 | 0.06 | Oct 20 | 13 / 8 / 0 | $72 | ADVANCE |
| EEFT | 63.97 | 0.08 | Oct 23 | 6 / 3 / 2 | $64 | **KILL, R3** (2 Sells) |
| LKFN | 56.90 | 0.25 | Oct 27 | none | | **KILL, no coverage** |
| PKX | 56.06 | 0.19 | Oct 27 | 18 / 5 / 0 | $52.61 (stamped 2021) | **KILL, R4 proxy** (floor below the stock, and stale) |
| BMRN | 54.58 | 0.24 | Oct 27 | 23 / 7 / 0 | $60 | ADVANCE |
| PNR | 53.11 | 0.03 | Oct 21 | 9 / 7 / 3 | $50 | **KILL, R3** (3 Sells) |
| PII | 51.49 | 0.14 | Oct 27 | 5 / 14 / 2 | $46 | **KILL, R3** |
| STC | 51.01 | 0.08 | Oct 22 | none | | **KILL, no coverage** |

## R2 (free, `get_earnings_results`) for the 6 advancers

| Name | Tool date | LY same quarter | First R2 expiry | Note |
|---|---|---|---|---|
| VC | Oct 22 AM (**verified**) | Oct 23, 2025 AM | Nov20 (28 days past LY; Nov 9 10-Q deadline 9 trading days before) | ramp sell would be Wed Oct 21 3:35 |
| ITRI | Oct 27 AM (**verified**) | Oct 30, 2025 AM | Nov20 (exactly 21 days past LY) | ramp sell Mon Oct 26 3:35 |
| LRN | Oct 20 PM (**verified**, FQ1) | Oct 28, 2025 PM | Nov20 (23 days past LY) | print is **next Tuesday**; the ramp-sell deadline would be the entry week itself |
| ALGT | Nov 3 PM (f) | Nov 4, 2025 PM | **Dec18** (Nov20 is 16 days past LY) | |
| ADC | Oct 20 PM (**verified**) | Oct 21, 2025 PM | Nov20 (30 days past LY) | print is next Tuesday, same as LRN |
| BMRN | Oct 26 PM (f) | Oct 27, 2025 PM | Nov20 (24 days past LY) | |

**Moved:** 20 (3 re-tests, 17 new names). 11 kills, 3 parked, 6 advance to the chain stage for EVENING 1. No web searches, no chain checks.

**Pattern:** at $50-100 the Rule 3 / Rule 4 screen finally leaves names with real coverage and floors well over the stock (ITRI $115 vs $86.58, VC $104 vs $86.98). The question for all six is Rule 5: at a $0.676 line, a stock this price usually has nothing near the money under a dollar, so expect them to land in the paper book if they clear R6 and R7.

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile (bottom quartile for calls), R2 earnings before expiry (21-day cushion on the later of tool date and last year's date; 10-Q deadline at least 5 trading days before expiry; 6-K filers need both dates), R3 analyst consensus (max 1 Sell, 3+ Buys, Buys >= Holds), R4 lowest Buy target above breakeven, R5 affordability (ask x 100 <= 10% of reserve at 3.5/5), R6 reachability (breakeven move <= 1.5x median earnings move), R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **R4 proxy:** the free screen's version of Rule 4, before any chain: if the lowest Buy target isn't comfortably above the stock price, no call's breakeven can sit under it.
- **(f):** the earnings tool's date is `verified: false`, estimated from cadence.
- **LY:** last year's same-quarter report date.
- **BE:** breakeven, strike plus premium paid.
- **OI:** open interest, contracts outstanding on that exact strike and expiry.
- **PARK:** the contract is still alive but fails one rule today; re-checked every run.
- **PREPARE:** a run that doesn't spend chain checks or searches, only lines up the next run's names.
- **Ramp sell:** binder Tab 4 default exit: sell an OTM call 24-48h before the print instead of holding through it.
