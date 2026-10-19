# Screening log: Mon Oct 19, 2026, 9:35am ET OPEN (VM, LIVE)

**Session job:** DO, 10 names off the top of the queue (PREMARKET's plan), plus the Monday passes.md un-staling. Live quotes 13:35 UTC, the first minute of the session, so option spreads are opening-wide; every test is on the live ask anyway, and spread fails at the open get a mid-day re-test before they kill anything. Reserve (spendable) $676.28: Rule 5 3.5/5 line $0.676. Ratings re-pulled for all 12 queue names: no count or low target moved since Saturday.

| # | Name | Direction | Contract | Live quote | Stock | Test | Result |
|---|---|---|---|---|---|---|---|
| 1 | **MSTR** | CALLS (paper) | Nov20 $120C `da3b54fb` | 23.75 / 25.70, OI 1,764 | $139.94 (+2.3%) | R1: line $137.90, stock over it. R6 at the ask: BE $145.70, +4.1% vs 7.82% (passes) | **PARK, R1.** Not killed: a red day brings it back under the line. Floor-dating gate ($165 undated) still open behind it. |
| 2 | **CIFR** | CALLS (paper) | Dec18 $10C `f9efed33` | 1.25 / 1.45, OI 3,469, spread 14.8% | $9.08 (+1.1%) | R6: BE $11.45, +26.1% vs 28.27% (passes, 2.2 pt margin). R7 pass | **PARK, floor gate.** $18 low still needs a date after the Oct 14 convert. Kill Fri Oct 30. |
| 3 | **UEC** | CALLS (paper) | Jan15 $7C `60caab3b` | 1.47 / 1.72, OI 1,812, spread 15.7% | $7.95 (+0.5%) | R6: BE $8.72, +9.7% vs 10.67% (passes; margin narrowed from 2.4 to 1.0 pt on the opening ask) | **PARK, floor gate** ($10 traces to 2025-era targets). |
| 4 | **RIOT** | CALLS (paper) | Nov20 $13C `e6e7ea4c` | 1.95 / 2.40, OI 669, spread 20.7% | $14.00 (+2.0%) | R6: BE $15.40, +10.0% vs 10.69% (passes). R7 pass | **PARK, floor gate.** JPM $22 (Aug 17) aged past 60 days today: no dated floor at all now. Kill Tue Oct 27. |
| 5 | **FLUT** | CALLS (paper) | Jan15 $75C `a5b4198b` | 8.50 / 10.00, OI **772**, spread 16.2% | $75.23 (-0.5%) | R7: **OI 772, passes** (was 235). R4 at the ask: BE $85.00 vs low $85 = zero margin, fails (the low must be above BE). At mid ($9.25) BE $84.25 would pass by $0.75. R6 +13.0% vs 18.96% | **PARK, R4** (opening spread). Mid-day re-quote: ask <= $9.95 with the stock flat clears R4 by a nickel, still undated owner. |
| 6 | **NRG** | CALLS (paper) | Dec18 $105C `6fa30201` | 7.90 / 10.60 (bid size 9), OI 517 | $104.04 (+0.3%) | R6: BE $115.60, +11.1% vs 13.42% (passes). R7: spread 29.2% at the open (fails, re-test mid-day) | **PARK, floor gate** ($159, record Oct 3). Kill Mon Nov 2. |
| 7 | **NXT** | CALLS (paper) | Nov20 $80C `c1c39e5f` | 7.80 / 9.70, OI 275, spread 21.7% | $80.89 (+1.1%) | R6: BE $89.70, +10.9% vs 13.14% (passes). R7 pass (OI 275) | **PARK, floor gate** ($101, record Oct 13). Kill Mon Oct 26. |
| 8 | **APTV** | CALLS (paper) | Dec18 $45C `6f545918` | 2.40 / 3.80, OI **2** | $44.58 (-0.6%) | R7: OI 2 on today's open (OI is set overnight, a mid-day re-pull won't change it) | **KILLED, R7.** Friday's plan: "still < 250 = kill." |
| 9 | **INSM** | CALLS (paper) | Nov20 $105C `dc6214c4` | 3.30 / 4.90 (ask size 2), OI 5,116, spread 39% | $97.49 (+1.3%) | R6: BE $109.90, +12.7% vs 17.1% (passes). R7 spread fails on the opening quote | **PARK, floor gate + R7 re-test mid-day.** Kill Mon Oct 26. |
| 10 | **PL** | CALLS (paper) | Jan15 $10C `bb9b3f83` | 4.00 / 4.70, OI 4,181, spread 16.1% | $13.67 (+0.8%) | R6 at the ask: BE $14.70, +7.5%. Q4 Dec 9 PM (f) per PREMARKET | **PARK, floor gate** ($17 undated; 8/5/0). |

**Watch line (free re-quote):** ONDS $6.205 (revive >= ~$6.90: no), BTBT $0.958 (revive >= ~$1.10: no), CLSK $8.65 (revive > ~$9.20: no). PAAS $44.46 vs the $42.31 R1 line: no. TTWO $205.62, ratings stamp still Aug 7: parked.

**Monday passes.md un-staling:** ONDS $6.205, neither trigger ($4-5 or above $15): Keep Watching. **JFB:** Robinhood now returns `inactive_instruments: ["JFB"]` (was "no quote" on Oct 5 and Oct 12): no tradeable instrument, Stop Watching. No new pitches.

**Moved this run:** 10 names. 1 killed (APTV, R7), 9 parked (MSTR R1; FLUT R4 at the opening ask with R7 now passing; CIFR, UEC, RIOT, NRG, NXT, INSM, PL on floor gates). 0 advanced, 0 paper entries.

**Real-money entry:** none. No real-money doc exists, and nothing under the $0.676 line passes R6 (watch line all short of their revive prices).

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 lowest Buy target above breakeven, R5 affordability, R6 reachability (breakeven move <= 1.5x median earnings move), R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **BE (breakeven):** strike + ask.
- **OI (open interest):** contracts outstanding on that strike, set once a day before the open.
- **Spread % of mid:** (ask - bid) / mid.
- **Floor gate:** the low target exists but isn't dated within 60 days and after the decline (binder Tab 6), so R4 can't pass yet.
- **(f):** earnings date not company-verified.
- **PARK:** alive, waiting on one specific check or price; stays on the queue.
- **Opening spread:** quotes in the first minutes after 9:30 run wide; spread fails then are re-tested later in the day.
- **Paper / real:** paper-book candidate vs. a contract the real fund could afford.
