# Screening log: Mon Oct 19, 2026, 10:35am ET MIDDAY (VM, LIVE)

**Session job:** DO, 10 names (OPEN's MIDDAY plan: FLUT R4 re-quote, INSM/NRG R7 re-test on a settled spread, MSTR R1, then free R6 re-quotes). Live quotes 14:35 UTC, one hour into the session. Reserve (spendable) $676.28: Rule 5 3.5/5 line $0.676. Ratings re-pulled for all 12 queue names: no count or low target moved since the OPEN run (FLUT stamp still Oct 16, NRG Oct 3, NXT Oct 13, TTWO Aug 7).

| # | Name | Direction | Contract | Live quote | Stock | Test | Result |
|---|---|---|---|---|---|---|---|
| 1 | **FLUT** | CALLS (paper) | Jan15 $75C `a5b4198b` | 8.30 / 10.00, OI 772, spread 18.6% | $76.32 (+1.0%) | R4 at the ask: BE $85.00 vs low $85, zero margin, **fails** (the ask didn't move off 10.00 even with the stock up $1). At mid ($9.15) BE $84.15 would pass by $0.85. R6 +11.4% vs 18.96% (passes). R7 pass | **PARK, R4 at the ask.** Paper fills at the ask, so the ask is the test. Needs ask <= $9.95. Owner/date of the $85 still unknown. |
| 2 | **INSM** | CALLS (paper) | Nov20 $105C `dc6214c4` | 3.50 / 4.30, OI 5,116, spread **20.5%** | $94.77 (-1.6%) | R7: **passes** on the settled spread (was 39% at the open). R6 at the ask: BE $109.30, +15.3% vs 17.1% (passes, margin narrowed by the stock's dip) | **PARK, floor gate** ($165 low, undated). R7 no longer a blocker. Kill Mon Oct 26. |
| 3 | **NRG** | CALLS (paper) | Dec18 $105C `6fa30201` | 5.80 / 6.40, OI 517, spread **9.8%** | **$98.60 (-5.0%)** | R7: **passes** (was 29% at the open). R6 at the ask: BE $111.40, +13.0% vs 13.42% (passes by 0.4 pt). R1 improves with the drop. One search for why NRG is -5% today: nothing dated today came back (old Aug 4 Q2 miss, generic "Strong Buy" pieces) | **PARK, floor gate** ($159 record Oct 3). Watch the drop: a deeper slide breaks R6 at this strike (stock under ~$98.2 at a $6.40 ask); next run re-tests the Dec18 $100C if so. Kill Mon Nov 2. |
| 4 | **MSTR** | CALLS (paper) | Nov20 $120C `da3b54fb` | 23.25 / 25.10, OI 1,764 | $139.15 (+1.7%) | R1: line $137.90, stock over it | **PARK, R1.** R6 at the ask passes (BE $145.10, +4.3% vs 7.82%). |
| 5 | **CIFR** | CALLS (paper) | Dec18 $10C `f9efed33` | 1.32 / 1.44, OI 3,469 | $9.245 (+3.0%) | R6: BE $11.44, +23.7% vs 28.27% (passes, margin up to 4.6 pt) | **PARK, floor gate** ($18 needs a date after Oct 14). Kill Fri Oct 30. |
| 6 | **UEC** | CALLS (paper) | Jan15 $7C `60caab3b` | 1.42 / 1.59, OI 1,812 | $7.835 (-1.0%) | R6: BE $8.59, +9.6% vs 10.67% (passes) | **PARK, floor gate** ($10, 2025-era). |
| 7 | **RIOT** | CALLS (paper) | Nov20 $13C `e6e7ea4c` | 2.13 / 2.33, OI 669, spread 9.0% | $14.21 (+3.6%) | R6: BE $15.33, +7.9% vs 10.69% (passes) | **PARK, floor gate** (no dated floor since JPM $22 aged out today). Kill Tue Oct 27. |
| 8 | **NXT** | CALLS (paper) | Nov20 $80C `c1c39e5f` | 6.90 / 7.70, OI 275, spread 11.0% | $79.47 (-0.7%) | R6: BE $87.70, +10.4% vs 13.14% (passes). R7 pass | **PARK, floor gate** ($101, record Oct 13). Kill Mon Oct 26. |
| 9 | **PL** | CALLS (paper) | Jan15 $10C `bb9b3f83` | 4.00 / 4.50, OI 4,181, spread 11.8% | $13.44 (-0.9%) | R6 at the ask: BE $14.50, +7.9% | **PARK, floor gate** ($17 undated; 8/5/0). |
| 10 | **PAAS / TTWO** | CALLS (paper) | Jan15 $40C / Dec18 $190C | (stock only) | PAAS $44.30, TTWO $205.14 | PAAS R1 line $42.31: over. TTWO ratings stamp still Aug 7 | **PARK** (R1; R4 dating). |

**Watch line (free re-quote):** ONDS $6.095 (revive >= ~$6.90: no), BTBT $0.947 (>= ~$1.10: no), CLSK $8.75 (> ~$9.20: no).

**Moved this run:** 10 names re-tested at a settled mid-morning quote. 0 killed, 0 advanced. Two R7 blockers cleared (INSM 39% -> 20.5%, NRG 29% -> 9.8%): the opening-spread re-test rule worked as designed, both were opening-book artifacts. Every live name now passes R1-R3, R6 and R7 except MSTR/PAAS (R1) and FLUT (R4 at the ask); all of the rest are held by Rule 4 floor dating only. 1 web search (NRG's -5%: no dated news found).

**Finding:** the queue's single common blocker is now Rule 4 floor dating (Tab 6: target dated within 60 days and after the decline). Seven names sit there. The tool doesn't expose target dates, so each one costs a search; floor searches stay limited to names whose tool numbers change, per the queue rule, unless EVENING decides to spend one search apiece on the three with the nearest kill dates (NXT and INSM Oct 26, RIOT Oct 27).

**Real-money entry:** none. No real-money doc exists, and nothing under the $0.676 line passes R6.

## GLOSSARY
- **R1-R7:** binder Tab 1 Iron Rules. R1 range percentile, R2 earnings before expiry, R3 analyst consensus, R4 lowest Buy target above breakeven, R5 affordability, R6 reachability (breakeven move <= 1.5x median earnings move), R7 liquidity floor (OI >= 250, spread <= 25% of mid).
- **BE (breakeven):** strike + ask.
- **OI (open interest):** contracts outstanding on that strike, set once a day before the open.
- **Spread % of mid:** (ask - bid) / mid.
- **Floor gate:** the low target exists but isn't dated within 60 days and after the decline (binder Tab 6), so R4 can't pass yet.
- **PARK:** alive, waiting on one specific check or price; stays on the queue.
- **Opening spread:** quotes in the first minutes after 9:30 run wide; spread fails then are re-tested later in the day.
- **Paper / real:** paper-book candidate vs. a contract the real fund could afford.
