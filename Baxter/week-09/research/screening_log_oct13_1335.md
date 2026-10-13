# Screening log, Tue Oct 13, 1:35pm ET (MIDDAY)

*Live data pulled 17:35-17:38 UTC. Reserve $676.28 (3.5/5 line $0.676). Re-tests first, then a re-run of the Oct 20 - Nov 20 print window under $25, looking for names that fell into the bottom quartile after three red sessions and that no earlier log has touched.*

## Re-tests (parked on R6)

| Name | Contract | Stock | Quote | BE at ask | Needs | R6 cap | Result |
|---|---|---|---|---|---|---|---|
| BTBT | Jan15 $1C | 1.2201 (-1.6%) | 0.33 / 0.38 (OI 2,252) | 1.38 | +13.1% | 8.23% | **PARK** (passes at stock >= ~$1.275 with a 0.38 ask) |
| ONDS | Dec18 $8C | 6.615 (-0.8%) | 0.42 / 0.45 (OI 37,782) | 8.45 | +27.7% | 20.89% | **PARK** |
| ALGM | Nov20 $35C (paper) | 33.04 (-2.2%) | 2.25 / 2.40 (OI 6,793) | 37.40 | +13.2% | 10.5% | **PARK** |

## Scanner re-run: prints Oct 20 - Nov 20, range pct < 0.25, cap >= $300M (preview, not saved)

| Band | Matches | Rows returned | Not in any week-09 log or passes.md |
|---|---|---|---|
| $1-5 | 130 | 130 | 4 (RXRX, VFS, HKD, NNDM) |
| $5-10 | 138 | 138 | 1 (ISOU) |
| $10-25 | 223 | 200 (23 cut, sorted high to low, so the cut rows are roughly $10-11.7) | 11 |

The bottom quartile under $25 has barely changed since the Oct 5 sweep: 252 of the 268 sub-$10 names were already in a log.

## Free screen (R3 / R4 proxy, one ratings call)

| Name | Last | Range pct | Print (scanner) | Buy / Hold / Sell | Low target | Result |
|---|---|---|---|---|---|---|
| ISOU | 8.67 | 0.23 | Nov 6 | none | | **KILL, no coverage** |
| RXRX | 3.85 | 0.25 | Nov 5 | 3 / 4 / 0 | $4 | **KILL, R3** (Buys < Holds) |
| VFS | 3.05 | 0.11 | Nov 20 | none | | **KILL, no coverage** |
| HKD | 1.68 | 0.10 | Oct 20 | none | | **KILL, no coverage** |
| NNDM | 1.455 | 0.24 | Nov 19 | none | | **KILL, no coverage** |
| FHB | 24.45 | 0.23 | Oct 23 | 1 / 7 / 3 | $26 | **KILL, R3** |
| NGNE | 22.56 | 0.24 | Nov 13 | 11 / 0 / 0 | $46 | ADVANCE |
| AMX | 21.655 | 0.22 | Oct 20 | 15 / 6 / 0 | $20.88 | **KILL, R4 proxy** (low under the stock) |
| TECX | 21.12 | 0.24 | Nov 6 | 9 / 1 / 0 | $26 | ADVANCE |
| ALH | 20.90 | 0.24 | Nov 13 | 7 / 1 / 0 | $26 | ADVANCE |
| IMNM | 17.60 | 0.25 | Nov 6 | 15 / 1 / 0 | $24 | ADVANCE |
| JANX | 17.35 | 0.23 | Nov 6 | 15 / 2 / 1 | $14 | **KILL, R4 proxy** |
| SRPT | 16.66 | 0.20 | Nov 3 | 7 / 12 / 5 | $5 | **KILL, R3** |
| SMMT | 15.66 | 0.21 | Oct 20 | 12 / 6 / 0 | $11.90 | **KILL, R4 proxy** |
| MLP | 15.04 | 0.21 | Nov 13 | none | | **KILL, no coverage** |
| ENTA | 11.765 | 0.23 | Nov 17 | 6 / 0 / 0 | $19 | ADVANCE |

## R2 and chain stage (the 5 advancers, all paper-priced)

| Name | Tool date (LY) | First R2 expiry | Strike | Quote | OI | Spread % mid | Result |
|---|---|---|---|---|---|---|---|
| NGNE | Nov 12 PM (f) (LY Nov 13) | Dec18 | $22.5C / $25C | 2.00 / 5.50, 1.10 / 4.90 | 3 / 2 | 93% / 127% | **KILL, R7** |
| TECX | Nov 5 PM (f) (LY Nov 6) | Dec18 | $22.5C / $25C | 1.30 / 4.90, 0.85 / 4.90 | 1 / 34 | 116% / 141% | **KILL, R7** |
| IMNM | Nov 5 PM (f) (LY Nov 6) | Dec18 | $18C / $19C / $20C | 0.60 / 4.90, 0.20 / 4.90, 1.00 / 4.80 | 1 / 35 / 288 | 156% / 184% / 131% | **KILL, R7** ($20C clears OI, spread is 131%) |
| ALH | Nov 12 AM (f) (LY Nov 13) | Jan15 (Nov20 fails the 21-day cushion; no Dec listed) | $20C / $22.5C | 1.25 / 3.00, 0.40 / 1.70 | 0 / 1 | 82% / 124% | **KILL, R7** |
| ENTA | Nov 16 PM (f), fiscal Q4, a 10-K (LY Nov 17) | Jan15 (the Dec 14 10-K deadline is only 4 trading days before Dec18) | $12.5C / $15C | 0.00 / 3.60, 0.00 / 2.80 | 0 / 7 | no bid | **KILL, R7** |

**Moved:** 19 (3 re-tests, 16 new names). 16 kills, 3 parked, 0 advances, 0 entries. No web searches. Went past the 10-name batch because the ratings pull was one free call and the chain checks were 4 instrument lists and 2 quote calls.

**Pattern:** a re-run of the window turns up almost nothing new. The only new names are small-cap biotechs and one lab-services company, and every one of them has a Dec/Jan chain with single- or double-digit OI and spreads over 80% of mid.

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile (bottom quartile for calls), R2 earnings before expiry (21-day cushion on the later of tool date and last year's date; 10-Q/10-K deadline at least 5 trading days before expiry), R3 analyst consensus (max 1 Sell, 3+ Buys, Buys >= Holds), R4 lowest Buy target above breakeven, R5 affordability (ask x 100 <= 10% of reserve at 3.5/5), R6 reachability (breakeven move <= 1.5x median earnings move), R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **R4 proxy:** at the free screen, the lowest Buy target is already under the stock price, so no call's breakeven can clear it.
- **(f):** the earnings tool's date is `verified: false` (estimated from cadence).
- **BE (breakeven):** strike + premium paid (at the ask).
- **OI:** open interest, contracts outstanding.
- **Spread % mid:** (ask - bid) / mid.
- **PARK:** alive, waiting on one specific price; stays on the queue.
