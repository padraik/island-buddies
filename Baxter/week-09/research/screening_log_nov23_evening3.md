# Screening log: Mon Nov 23, EVENING 3 (10:00pm ET)

**Job (from EVENING 2's plan):** (1) TAL floor dating; (2) the Feb 13 - Mar 31 re-sweep (last swept Nov 13-14); (3) Tuesday's PREMARKET plan. Nothing held. R5 line: 10% x $715.96 / 100 = **$0.716/share** (3.5/5).

**Source:** Robinhood tools, run ~03:00-03:40 UTC Nov 24 on Monday's close. 2 web searches (both TAL floor dating).

## 1. TAL floor dating: gate MET

Full write-up: `research_TAL_feb19.md`, addendum A. Short version: the tool's $11.50 low (record refreshed Nov 1, three days after the Oct 29 print) clears BE $10.70 even if it's a Buy target. The lowest named Buy target, Morgan Stanley $12 Overweight, is event-dated after the Oct 29 EPS miss (the only miss in the last four quarters). Citi $11.54 and Macquarie $10.90 are Neutrals. BofA $12.50 and JPM $17 are not relied on. **Remaining gate: R7 OI 177 (needs 250).**

## 2. Re-sweep, prints Feb 13 - Mar 31 2027, bands A + B

| Scan | ID | Last | Rows |
|---|---|---|---|
| Band A (Nov 13 scan, re-run live) | `01ce0035-28a6-49c0-aed8-0ee1b83da395` | $1-8.19, prints Feb 13 - Mar 20 | 165 |
| Band B (Nov 14 scan, re-run live) | `fccfd39a-e704-451e-8e48-72719f90258a` | $8.19-25, prints Feb 13 - Mar 20 | 198 |
| Bands A+B, new | `a7226397-cbb5-4ff4-b12d-01f39cd0455a` | $1-25, prints Mar 21 - Mar 31 | 40 (5 closed-end funds dropped: SDHY, HPI, HPS, GHY, PPT) |

403 rows. Diffed against every week-08 / week-09 log, passes.md and paper_book.md: **16 never worked.** Everything else has been worked in an earlier session (parked or killed under its current quarter). Bands C/D not re-run tonight (paper size at this reserve; 131 parks still in the Nov 21 log).

### Rule 3 + Rule 4 proxy (R3 calls: at most 1 Sell, at least 3 Buys, Buys >= Holds; low target > Last)

| Ticker | Last | Print (f) | B/H/S | Low target | Verdict |
|---|---|---|---|---|---|
| HPP | 7.96 | Feb 26 | 4/6/2 | 9.00 | **KILLED R3** (2 Sells, Holds > Buys) |
| AGRO | 7.93 | Mar 16 | 2/5/0 | 10.50 | **KILLED R3** |
| NVAX | 7.89 | Feb 26 | 4/1/3 | 7.00 | **KILLED R3 + R4** |
| AIIR | 6.50 | Feb 26 | none | -- | **KILLED R3** (no coverage) |
| GENI | 5.61 | Mar 3 | 19/3/0 | 6.00 | park (thin, +7%) |
| CIG.C | 2.57 | Mar 19 | 4/3/1 | none | **KILLED R4** (no targets) |
| NESR | 18.70 | Feb 16 | 9/0/0 | 25.00 | park |
| CCEC | 17.89 | Mar 4 | 5/3/0 | 22.00 | park |
| PBR.A | 13.96 | Mar 4 | 9/1/0 | 20.70 | park |
| KYIV | 11.40 | Mar 12 | 7/1/0 | 15.00 | park |
| GDOT | 11.05 | Mar 12 | none | -- | **KILLED R3** |
| AAUC | 18.80 | Mar 31 | none | -- | **KILLED R3** |
| CMCL | 17.44 | Mar 24 | 5/1/0 | 23.11 | park |
| MGTX | 8.54 | Mar 25 | 6/1/0 | 16.00 | park |
| PGEN | 4.36 | Mar 25 | none | -- | **KILLED R3** |
| KOPN | 2.72 | Mar 29 | 7/0/0 | 6.50 | park |

### R6 structural: median earnings move, last 5 prints (daily closes; AM = prior close to print day, PM = print day to next day)

| Ticker | Moves | Median | Verdict |
|---|---|---|---|
| GENI | +1.6 / -6.6 / +8.6 / -6.0 / -15.5 | 6.6% | **KILLED R6** |
| NESR | +7.2 / +16.0 / +10.1 / +23.3 / -2.1 | **10.1%** | to the chain |
| CCEC | -4.6 / -5.0 / +0.9 / +0.3 / +10.0 | 4.6% | **KILLED R6** |
| PBR.A | +4.2 / +4.2 / -1.5 / -2.5 / -3.1 | 3.1% | **KILLED R6** |
| KYIV | +7.1 / +8.5 / +4.2 / -3.3 / -1.4 | 4.2% | **KILLED R6** |
| CMCL | +5.0 / +3.9 / +1.5 / +4.5 / +0.8 | 3.9% | **KILLED R6** |
| MGTX | -4.6 / -1.2 / -0.2 / -2.2 / -9.2 | 2.2% | **KILLED R6** |
| KOPN | -0.4 / -5.7 / +7.6 / +23.5 / +12.0 | 7.6% | **KILLED R6** (closest) |

### NESR chain (Mar19; print Feb 16 AM (f), LY Feb 17 + 21 = Mar 10, clears Mar19)

Stock $18.73 close. Cap 1.5 x 10.1% = 15.2%.
| Strike | Bid / Ask | OI | IV | BE at ask | Needs | Verdict |
|---|---|---|---|---|---|---|
| $17.5C | 2.40 / 4.70 | 0 | 69% | 22.20 | +18.5% | R6, R7 |
| $20C | 1.85 / 2.45 | 546 | 61% | 22.45 | +19.9% (+18.3% at mid) | R6; spread 27.9% fails R7 |
| $22.5C | 0.45 / 2.85 | 64 | 68% | 25.35 | +35.3% | R6, R7 |

**NESR KILLED R6** (and R5: no contract near $0.716). Same story as every 60%+ IV name: time value eats the room.

## 3. Queue item 3 leftovers

| Ticker | Print (f) | B/H/S, low, stamp | Median (5 prints) | Verdict |
|---|---|---|---|---|
| OWL | Feb 4 AM | 12/8/0, $10 on $8.80, Nov 21 | 6.4% (-4.2 / -3.6 / +9.8 / +6.4 / +7.7) | **KILLED R6** |
| LADR | Feb 4 AM | 5/1/0, $10 on $8.21, no stamp | 2.2% | **KILLED R6** |
| LBRT | Jan 27 PM | 9/5/0, $16, stamp **Nov 2024** | not run | **SKIPPED: stale stamp** (floor gate can't pass) |
| CX | Feb 18 | 17/2/0, $12, stamp **Aug 2020** | not run | **SKIPPED: stale stamp** |

## Tally

21 names moved: TAL (floor gate met), 16 re-sweep names (all killed), OWL, LADR (killed), LBRT, CX (skipped, stale). 0 advanced to a doc. Real-money candidate count: still 1 (TAL, OI gate).

**The finding, again:** the only names that clear R6 at our price are low-IV names with medium-size prints (TAL: 37.5% IV, 9.3% median). Tonight's best median (NESR 10.1%) came with 61% IV. The low-IV hunt (queue item 4) is the right next screen.

## GLOSSARY

- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry, R3 ratings mix, R4 bear floor, R5 price cap on reserve, R6 reachability (needed move <= 1.5x median earnings move), R7 liquidity (OI >= 250, spread <= 25% of mid).
- **Park:** passed R3 and the R4 proxy; waits for the next check.
- **R6 structural:** the median print move is too small (under ~8%) for any spring contract's time value to fit inside 1.5x of it.
- **(f):** earnings date estimated from cadence (`verified: false`).
- **Stale stamp:** the ratings record's `updated_at` is far older than 60 days, so the floor can't be dated.
- **Event-dated:** a target pinned to a date by the event it reacted to (an earnings print).
- **BE:** breakeven, strike + premium.
- **IV:** implied volatility.
