# Screening log: Tue Oct 13, OPEN (9:35am ET)

**Source:** the research queue's 10 names (BTBT, ONDS, GGAL, ALGM, SE, HII, ALNY, FN, AVAV, LEU), worked per PREMARKET's plan. Live quotes pulled 9:35am ET (13:35 UTC), the first minute of trading, so option spreads are wide on the thinner names; every kill/park below holds even at a generous read of the quote.

## Queue re-tests (R6 on the live ask)

| # | Name | Direction | Contract | Live quote | Stock | Test | Result |
|---|---|---|---|---|---|---|---|
| 1 | **BTBT** | CALLS (real money) | Jan15 $1C `25ebc8de` | 0.27 / 0.34, OI 2,252 | $1.195 (-3.6%) | R6: BE at ask $1.34 vs max $1.293 (stock x 1.0823): needs +12.1% vs cap 8.23%. | **PARK, R6.** Further away than Monday's close. Passes at stock >= ~$1.24 with a $0.34 ask. |
| 2 | **ONDS** | CALLS (real money) | Dec18 $8C `cfbc25b7` | 0.37 / 0.42, OI 37,782 | $6.52 (-2.2%) | R6: BE at ask $8.42 vs max $7.885 (stock x 1.2089): needs +29.1% vs cap 20.89%. | **PARK, R6.** Needs stock ~$6.97 at a $0.42 ask. |
| 3 | **ALGM** | CALLS (paper) | Nov20 $35C `832a1519` | 1.90 / 2.45, OI 6,793 | $32.77 (-3.0%) | R6: BE at ask $37.45 vs max $36.21 (stock x 1.105): needs +14.3% vs cap 10.5%. | **PARK, R6.** Third straight down day; gap widening. |

## GGAL: R2 and R6 (the open checks from Monday)

| Check | Data | Result |
|---|---|---|
| R1 | $36.86 vs 52w closing range $32.09 - $60.79 | 16.6%, passes |
| R3 / R4 | 5/3/0, **low now $45** (was $50 on Monday's pull) | R3 passes; R4 still clears a $40C BE (~$42-44), with less room |
| R2 (6-K filer, needs both dates) | Tool: no upcoming Q3 2026 row (labels scrambled, latest row 2026-08-25 reported). LY Q3: Nov 25, 2025. One web search: aggregator lists Q3 2026 results **Nov 25, 2026**, call Nov 26. | Tool date (1) missing; aggregator only. Would need date + 21 <= Jan 15 (Nov 25 + 21 = Dec 16, ok) but the tool leg is absent. Moot, see R6. |
| R6 | Print-day moves (reports after the close; reaction = next session), the four tool-dated prints: Nov 26 2025 **+4.48%**, Mar 5 2026 **-1.91%**, May 14 2026 **+0.14%**, Aug 26 2026 **-0.66%**. Median abs **1.29%**; even using the bigger of print day / next day for each, median 1.82%. Cap 1.5x = **1.9% - 2.7%**. | Jan15 $40C at any ask needs > +8.5% just to the strike ($40 vs $36.86). **KILLED, R6.** Argentina macro moves GGAL; its own prints barely do. |
| R7 (live) | Jan15 $40C 0.95 / 4.00, OI 736 | opening quote, spread 123%; not needed after R6. |

## R7 open-interest re-checks (OI updates overnight)

| # | Name | Contract | Live quote | OI | Stock | Result |
|---|---|---|---|---|---|---|
| 5 | **SE** | Dec18 $95C `4fe7f5f7` | 8.90 / 9.90 | **163** (was 162) | $95.59 (-0.3%) | **PARK, R7.** OI flat for 3 sessions. |
| 6 | **HII** | Nov20 $270C `ad19b167` | 10.60 / 12.90 | **230** (was 232) | $262.11 (-0.7%) | **PARK, R7.** OI drifting down. |
| 7 | **ALNY** | Nov20 $230C `736ea6c9` | 14.50 / 18.50 | **203** (was 199) | $228.41 (+0.6%) | **PARK, R7.** |
| 8 | **FN** | Dec18 $460C `73da42ea` | 36.90 / 45.40 | **69** (was 67) | $431.92 (**-5.4%**) | **PARK, R7** (watch list). Down 5% at the open; R6 gap now wider too. |
| 9 | **AVAV** | Jan15 $135C `423fe2f0` | 13.10 / 14.10 | **93** (was 91) | $128.01 (-2.7%) | **PARK, R7** (watch list). |
| 10 | **LEU** | Dec18 $140C `be8103f5` | 12.40 / 15.10 | **154** (was 136) | $132.48 (-2.1%) | **PARK, R7** (watch list). Only one of the six actually growing OI. |

**Moved:** 10 names. 1 kill (GGAL, R6), 9 parked (3 on R6, 6 on R7). 0 entries.

**Real-money entry:** none. BTBT and ONDS, the only contracts under the $0.676 line, both fail R6 by more than they did at Monday's close.

**Pattern worth writing down:** the six R7 names have now been checked on three consecutive mornings and OI moved by single digits on five of them. December/January mid-cap strikes don't grow open interest a week at a time; they grow it in the last month before expiry. Re-checking them every morning is spending a run on a number that isn't going to move. Next re-check: Saturday Oct 17, not before.

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry (21-day cushion on the later of tool date and last year's date; 6-K filers need both dates), R3 analyst consensus (calls: at most 1 Sell, at least 3 Buys, Buys >= Holds), R4 lowest Buy target above breakeven, R5 affordability, R6 reachability (breakeven move <= 1.5x median earnings move), R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **BE (breakeven):** strike + premium paid.
- **OI (open interest):** contracts outstanding on that strike.
- **Spread % of mid:** (ask - bid) / mid.
- **Print-day move:** close-to-close change on the first session after the earnings release.
- **LY:** last year's same-quarter report date.
- **6-K filer:** foreign company; no 10-Q deadline backstop, so R2 needs both dates.
- **PARK:** alive, waiting on one specific check or price; stays on the queue.
- **Watch list:** passes R1-R6 but not R7; re-checked weekly, not every run.
