# Screening Log -- Aug 4, 2026 (Batch 1 of the overnight run)

Michael's ask (1:30 AM, going to bed): screen 200 names or until 3 land at 4/5 or extremely close, whichever comes first. Doc-and-push after every 50. This is batch 1 of that run.

**Sectors, deliberately untouched by any prior batch:** managed care/health insurers, animal health, dental/optical, farm equipment, regional banks, consumer finance/payments, trucking/logistics, tobacco, timeshare/leisure travel, gaming equipment.

## Stage 1 -- Range percentile (free, fetch_price.py --range)

50 attempted, 6 unavailable (bad/delisted tickers: CNHI, CMA, SNV, DFS, FI, IGT -- likely ticker changes or API gaps, not a research finding), 44 valid.

| Ticker | Price | 52wk Range | Pctile | Direction |
|---|---|---|---|---|
| UNH | $414.90 | 236.95-461.62 | 79th | PUTS (logged only) |
| CVS | $105.50 | 61.35-110.68 | 89th | PUTS (logged only) |
| CI | $282.06 | 239.51-315.47 | 56th | MID-OUT |
| HUM | $374.50 | 163.11-428.88 | 80th | PUTS (logged only) |
| MOH | $193.91 | 121.06-244.89 | 59th | MID-OUT |
| CNC | $64.13 | 25.07-69.36 | 88th | PUTS (logged only) |
| ELV | $382.77 | 273.71-436.24 | 67th | MID-OUT |
| GEHC | $69.91 | 58.75-89.77 | 36th | MID-OUT |
| **ZTS** | **$77.57** | **71.47-160.48** | **7th** | **CALLS -- advances to chain** |
| **IDXX** | **$574.00** | **518.55-769.98** | **22nd** | **CALLS -- advances to chain** |
| ELAN | $25.72 | 13.75-27.72 | 86th | PUTS (logged only) |
| XRAY | $13.61 | 9.40-14.86 | 77th | PUTS (logged only) |
| ALGN | $172.89 | 122.00-200.44 | 65th | MID-OUT |
| EYE | $22.42 | 14.75-30.02 | 50th | MID-OUT |
| DE | $605.06 | 433.00-674.19 | 71st | MID-OUT |
| **AGCO** | **$103.92** | **99.21-143.78** | **11th** | **CALLS -- advances to chain** |
| TITN | $18.14 | 13.21-25.00 | 42nd | MID-OUT |
| LNN | $113.19 | 97.27-148.00 | 31st | MID-OUT |
| ZION | $70.84 | 46.19-73.34 | 91st | PUTS (logged only) |
| KEY | $22.79 | 16.47-24.07 | 83rd | PUTS (logged only) |
| FITB | $56.90 | 40.05-59.50 | 87th | PUTS (logged only) |
| HBAN | $17.36 | 14.89-19.45 | 54th | MID-OUT |
| RF | $31.48 | 22.70-32.47 | 90th | PUTS (logged only) |
| MTB | $249.48 | 174.76-255.00 | 93rd | PUTS (logged only) |
| WAL | $83.00 | 65.81-97.23 | 55th | MID-OUT |
| CFG | $72.00 | 46.53-74.70 | 90th | PUTS (logged only) |
| SYF | $77.84 | 63.08-88.77 | 57th | MID-OUT |
| COF | $218.61 | 174.24-259.63 | 52nd | MID-OUT |
| ALLY | $44.07 | 35.92-47.29 | 72nd | MID-OUT |
| PYPL | $57.82 | 38.46-79.22 | 48th | MID-OUT |
| GPN | $86.19 | 61.16-90.64 | 85th | PUTS (logged only) |
| **WU** | **$6.56** | **6.27-10.35** | **7th** | **CALLS -- advances to chain** |
| OMF | $64.68 | 45.78-71.93 | 72nd | MID-OUT |
| JBHT | $266.91 | 130.12-299.76 | 81st | PUTS (logged only) |
| ODFL | $211.46 | 126.01-252.03 | 68th | MID-OUT |
| SAIA | $363.87 | 249.32-494.71 | 47th | MID-OUT |
| XPO | $197.01 | 116.68-232.05 | 70th | MID-OUT |
| KNX | $68.42 | 38.62-82.86 | 67th | MID-OUT |
| CHRW | $147.00 | 113.40-210.33 | 35th | MID-OUT |
| LSTR | $176.76 | 119.32-228.46 | 53rd | MID-OUT |
| MO | $68.33 | 54.70-77.06 | 61st | MID-OUT |
| PM | $189.30 | 142.11-207.76 | 72nd | MID-OUT |
| BTI | $59.56 | 49.88-67.30 | 56th | MID-OUT |
| WH | $75.27 | 69.21-91.44 | 27th | MID-OUT |
| HGV | $45.90 | 36.79-55.40 | 49th | MID-OUT |
| TNL | $77.04 | 57.78-81.00 | 83rd | PUTS (logged only) |
| VAC | $97.40 | 44.58-105.97 | 86th | PUTS (logged only) |

**Tally: 4 MID-OUT... ** (correction: 24 MID-OUT, 16 PUTS-zone logged/untouched, 4 CALLS-zone advance to chain: ZTS, IDXX, AGCO, WU.)

## Stage 2 -- Chain feasibility (free, fetch_options_chain.py)

- **IDXX ($574 stock): KILLED.** No calls anywhere in the $0.10-$2.00 tradeable range across five expirations out to Jan 2027. Stock price too high for the fund's chain filter to find an affordable, reachable strike. No instrument, no search needed.
- **AGCO: KILLED on calendar.** AGCO already reported Q2 2026 on Jul 30 (missed EPS by $0.04) -- that miss is *why* the stock sits at 11th percentile. Next print is Q3, ~late October, outside every affordable expiry shown (Aug 21 and Sep 18 chains both pre-date it). Post-earnings-entry trap, same shape as the Jun 5 DSGX lesson. No search needed.
- **WU: KILLED on calendar.** Western Union also already reported Q2 2026, on Jul 30. The cheap stock (7th percentile, $6.56) and cheap chain ($7C Aug21 at $0.20, needing only +9.8%) look tempting, but this is the reaction to news that already happened, not a pre-earnings dislocation. Next print is Q3, ~late October -- outside both listed expiries. Same post-earnings trap as AGCO. No search needed.
- **ZTS: ADVANCES.** Aug 6, 2026 earnings lands 2 days before the Aug 21 expiry -- a real, live catalyst inside the window. $90C Aug21 at $1.00 (Rule 5 exactly at the floor), breakeven $91.00, needs +17.3%. Full writeup below and in `research_ZTS.md`.

## Stage 3 -- Full DD (search-funded, ZTS only)

**ZTS (Zoetis) -- KILLED on decline category, despite clean Rule 3.**

- Rule 2: passes. Aug 6, 2026 earnings, inside the Aug 21 expiry.
- Rule 3: **clean.** 18 analysts: 9 Strong Buy, 1 Moderate Buy, 8 Hold, **zero Sell/Underperform.**
- Rule 4: passes, thin. Morgan Stanley (Overweight/Buy) cut target $115 -> $99 on Jul 22, 2026 -- fresh (within 60 days, published after the decline, per the binder's dating requirement). $99 clears the $91.00 breakeven by $8, roughly 8.8% cushion. UBS's $99 target is Neutral-rated (Hold), doesn't count for Rule 4.
- **Decline category: this is the kill.** ZTS is down ~42.9% YTD across **two consecutive bad quarters**, not one isolated miss: Q3 2025 (Nov) already triggered "a market rerating from high to low growth" on decelerating growth, and Q1 2026 (May 7) then dropped the stock 21.5% on a real organic decline (companion animal segment -11% organic, Librela -32% in Q4 US revenue) plus guidance cuts, pet-owner spending pullback, and rising competition. Analysts cut price targets in response to the second event, they didn't just get caught flat-footed by a surprise -- the fair-value resets (Morgan Stanley, UBS, both cut Jul 22) are following a real deterioration in the underlying business, not correcting an overreaction to a clean beat-driven business. **This is Category 2 (fundamental deterioration), not Category 1 (event overreaction).** The binder's own rule: only event-overreaction is tradeable. Two consecutive negative-reaction quarters tied to the same structural story (softening companion-animal demand, competitive pressure) is the definition of a decline category, not a one-off.
- Rule 6 not scored -- categorical kill makes it moot, and getting real per-quarter move data would have cost a second search for no decision-relevant payoff.

**Not queued.** Would need a specific reason to believe the companion-animal deceleration has stopped (a beat-and-reaccelerate quarter, not just a smaller miss) before this gets a second look.

## Batch 1 tally

**50 attempted, 44 valid, 4 CALLS-zone advances, 3 killed in DD/chain (IDXX no-instrument, AGCO and WU both post-earnings calendar traps), 1 killed on decline category (ZTS). 0 advances to pitch.**

16 PUTS-zone names logged, untouched, per the no-dedicated-puts-pools rule (back-test still gates live puts entries).

Next: Batch 2, fresh sectors (semiconductor equipment, cybersecurity, cloud/SaaS, metals miners, REIT subtypes).
