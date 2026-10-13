# Screening log, Tue Oct 13, 2:35pm ET (MIDDAY)

*Live data pulled 18:35-18:37 UTC. Reserve $676.28 (3.5/5 line $0.676). Re-tests first, then the two pieces the 1:35 run left: the $10-12 rows its $10-25 scan cut, and the $25-50 band of the Oct 20 - Nov 20 print window.*

## Re-tests (parked on R6)

| Name | Contract | Stock | Quote | BE at ask | Needs | R6 cap | Result |
|---|---|---|---|---|---|---|---|
| BTBT | Jan15 $1C | 1.2201 (-1.6%) | 0.32 / 0.38 (OI 2,252) | 1.38 | +13.1% | 8.23% | **PARK** (passes at stock >= ~$1.275 with a 0.38 ask) |
| ONDS | Dec18 $8C | 6.67 (0.0%) | 0.42 / 0.47 (OI 37,782) | 8.47 | +27.0% | 20.89% | **PARK** |
| ALGM | Nov20 $35C (paper) | 33.46 (-1.0%) | 2.45 / 2.60 (OI 6,793) | 37.60 | +12.4% | 10.5% | **PARK** |

## Scanner, prints Oct 20 - Nov 20, range pct < 0.25, cap >= $300M (preview, not saved)

| Band | Matches | Rows returned | Not in any week-09 log, passes.md or paper_book.md |
|---|---|---|---|
| $10-12 | 53 | 53 | 1 (BKD) |
| $25-50 | 154 | 154 | 8 (LTM, OZK, GSHD, GBCI, CRI, SIM, HUBG, AOSL) |

Diff method: whole-word ticker match against every week-09 file plus passes.md and paper_book.md, same as 1:35.

## Free screen (R3 / R4 proxy, one ratings call)

| Name | Last | Range pct | Print (scanner) | Buy / Hold / Sell | Low target | Result |
|---|---|---|---|---|---|---|
| BKD | 10.10 | 0.23 | Nov 6 | 6 / 0 / 0 | $17 | ADVANCE |
| LTM | 48.90 | 0.25 | Nov 6 | 12 / 0 / 0 | $62.90 | ADVANCE |
| OZK | 45.01 | 0.24 | Oct 20 | 3 / 5 / 2 | $40 | **KILL, R3** (2 Sells, Buys < Holds) |
| GSHD | 44.44 | 0.23 | Oct 22 | 6 / 7 / 2 | $42 | **KILL, R3** |
| GBCI | 42.96 | 0.21 | Oct 22 | 5 / 1 / 0 | $53 | ADVANCE |
| CRI | 31.85 | 0.25 | Oct 27 | 3 / 5 / 1 | $30 | **KILL, R3** |
| SIM | 27.49 | 0.17 | Oct 27 | none | | **KILL, no coverage** |
| HUBG | 26.35 | 0.03 | Oct 23 | 2 / 6 / 0 | $28 | **KILL, R3** |
| AOSL | 26.09 | 0.24 | Nov 5 | none | | **KILL, no coverage** |

## R2 and chain stage (3 advancers)

| Name | Tool date (LY) | First R2 expiry | Strike | Quote | OI | Spread % mid | Result |
|---|---|---|---|---|---|---|---|
| BKD | Nov 5 PM (f) (LY Nov 6) | Dec18 (Nov20 is 14 days past Nov 6) | $10C / $11C / $12C | 0.65 / 1.40, 0.20 / 0.95, 0.05 / 0.75 | 17 / 75 / 79 | 73% / 130% / 175% | **KILL, R7** |
| LTM | Nov 13 PM (f) (LY Nov 14); 6-K filer, both dates present | Dec18 (Nov20 is 6 days past Nov 14) | $50C / $55C | 2.15 / 4.10, 0.05 / 2.20 | 473 / 84 | 62% / 191% | **KILL, R7** ($50C clears OI, spread 62%) |
| GBCI | Oct 22 PM (**verified**) (LY Oct 16) | Nov20 (29 days; Nov 9 10-Q deadline is 9 trading days before) | $45C / $50C | 0.00 / 3.10, 0.00 / 2.65 | 20 / 14 | no bid | **KILL, R7** |

**Moved:** 12 (3 re-tests, 9 new names). 9 kills, 3 parked, 0 advances, 0 entries. No web searches.

**Pattern:** the Oct 20 - Nov 20 window is now re-fished in every band up to $50 since the three red sessions. What's new is regional banks, Latin American ADRs and a senior-living operator, and none of them has a Dec/Nov chain anyone trades. LTM was the best of it (12 Buys, 0 Holds, floor $62.90 against a $48.90 stock) and its one liquid strike quotes a $1.95-wide market.

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile (bottom quartile for calls), R2 earnings before expiry (21-day cushion on the later of tool date and last year's date; 10-Q deadline at least 5 trading days before expiry; 6-K filers need both dates), R3 analyst consensus (max 1 Sell, 3+ Buys, Buys >= Holds), R4 lowest Buy target above breakeven, R5 affordability (ask x 100 <= 10% of reserve at 3.5/5), R6 reachability (breakeven move <= 1.5x median earnings move), R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **(f):** the earnings tool's date is `verified: false`, estimated from cadence.
- **OI:** open interest, contracts outstanding on that exact strike and expiry.
- **Spread % mid:** (ask - bid) / ((ask + bid) / 2).
- **6-K filer:** a foreign private issuer; no 10-Q deadline exists, so R2 needs both the tool date and last year's date.
- **PARK:** the contract is liquid and passes the other screens but fails R6 at today's price; re-checked each run.
